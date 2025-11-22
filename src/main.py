import argparse
import os
import json
import pandas as pd
import matplotlib.pyplot as plt

import torch
from datetime import datetime
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    average_precision_score,
    roc_curve,
    precision_recall_curve,
)

from preprocessing import apply_cleaning, stratified_group_split
from tokenization import load_tokenizer, tokenize_overflow_fixed_pt
from baseline_model import (
    load_bioclinical_bert_encoder,
    chunk_embeddings,
    aggregate_docs,
    train_logistic_regression,
)
from baseline_evaluate import (
    evaluate_with_target_recall,
    report_metrics,
)
from finetune_model import finetune_classifier
from utilities import log  # your global logging function


# ------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------
RESULTS_DIR = "/project/results"
FIG_DIR = os.path.join(RESULTS_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)


# ------------------------------------------------------------------
# Helper: save metrics JSON (BASELINE)
# ------------------------------------------------------------------
def save_metrics_json(val_dict, test_dict):
    out = {
        "Validation": val_dict,
        "Test": test_dict,
        "metadata": {
            "model": "BioClinicalBERT + LogisticRegression",
            "timestamp": datetime.utcnow().isoformat(),
        },
    }
    with open(os.path.join(RESULTS_DIR, "baseline_metrics.json"), "w") as f:
        json.dump(out, f, indent=2)


# ------------------------------------------------------------------
# Helper: save ROC/PR curves
# ------------------------------------------------------------------
def save_figures(name, y_true, probas):
    roc_auc = roc_auc_score(y_true, probas)
    pr_auc = average_precision_score(y_true, probas)
    positive_rate = y_true.mean()

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_true, probas)
    plt.figure(figsize=(7, 6))
    plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.4f})")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Random Guess")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"ROC Curve ({name})")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(FIG_DIR, f"{name}_roc_curve.png"))
    plt.close()

    # Precision-Recall Curve
    precision, recall, _ = precision_recall_curve(y_true, probas)
    plt.figure(figsize=(7, 6))
    plt.plot(recall, precision, label=f"PR Curve (AUC = {pr_auc:.4f})")
    plt.axhline(
        positive_rate,
        linestyle="--",
        color="red",
        label=f"Baseline (Pos Rate = {positive_rate:.4f})",
    )
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(f"PR Curve ({name})")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.savefig(os.path.join(FIG_DIR, f"{name}_pr_curve.png"))
    plt.close()


# ------------------------------------------------------------------
# BASELINE PIPELINE
# ------------------------------------------------------------------
def run_baseline(df_train, df_val, df_test, tokenizer):
    # Encoding
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc   = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc  = tokenize_overflow_fixed_pt(df_test, tokenizer)

    # Save encoded splits for fine-tuning later
    torch.save(train_enc, "/project/data/tokenized/enc_train.pt")
    torch.save(val_enc,   "/project/data/tokenized/enc_val.pt")
    torch.save(test_enc,  "/project/data/tokenized/enc_test.pt")

    # BioClinicalBERT Encoder
    encoder = load_bioclinical_bert_encoder()

    # Chunk embeddings
    train_chunk_emb = chunk_embeddings(train_enc, encoder)
    val_chunk_emb   = chunk_embeddings(val_enc, encoder)
    test_chunk_emb  = chunk_embeddings(test_enc, encoder)

    # Aggregate to doc-level
    train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
    val_doc_emb   = aggregate_docs(val_chunk_emb,   val_enc["doc_mapping"])
    test_doc_emb  = aggregate_docs(test_chunk_emb,  test_enc["doc_mapping"])

    # Targets
    y_train = df_train["readmitted"].to_numpy()
    y_val   = df_val["readmitted"].to_numpy()
    y_test  = df_test["readmitted"].to_numpy()

    # Logistic Regression baseline
    clf = train_logistic_regression(train_doc_emb, y_train)

    # Probabilities
    val_p  = clf.predict_proba(val_doc_emb)[:, 1]
    test_p = clf.predict_proba(test_doc_emb)[:, 1]

    # Thresholded predictions
    best_t, val_pred  = evaluate_with_target_recall(
        y_val, val_p, target_recall=0.75
    )
    _,      test_pred = evaluate_with_target_recall(
        y_test, test_p, target_recall=0.75
    )

    # Print metrics
    report_metrics("Validation", y_val, val_pred, val_p, best_t)
    report_metrics("Test", y_test, test_pred, test_p, best_t)

    # Build JSON metrics
    val_results = {
        "threshold": float(best_t),
        "accuracy": float(accuracy_score(y_val, val_pred)),
        "precision": float(precision_score(y_val, val_pred, zero_division=0)),
        "recall": float(recall_score(y_val, val_pred, zero_division=0)),
        "f1": float(f1_score(y_val, val_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_val, val_p)),
        "pr_auc": float(average_precision_score(y_val, val_p)),
        "confusion_matrix": confusion_matrix(y_val, val_pred).tolist(),
    }

    test_results = {
        "threshold": float(best_t),
        "accuracy": float(accuracy_score(y_test, test_pred)),
        "precision": float(precision_score(y_test, test_pred, zero_division=0)),
        "recall": float(recall_score(y_test, test_pred, zero_division=0)),
        "f1": float(f1_score(y_test, test_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_test, test_p)),
        "pr_auc": float(average_precision_score(y_test, test_p)),
        "confusion_matrix": confusion_matrix(y_test, test_pred).tolist(),
    }

    return val_results, test_results, val_p, test_p, y_val, y_test


# ------------------------------------------------------------------
# FINE-TUNING PIPELINE
# ------------------------------------------------------------------
def run_finetuning(enc_train):
    start = datetime.utcnow()
    log("Starting fine-tuning BioClinicalBERT classifier...")

    log(f"Tokenized TRAIN dataset loaded: {enc_train['input_ids'].shape[0]} chunks.")
    n_docs = int(enc_train["doc_mapping"].max()) + 1
    log(f"Document count (train): {n_docs}")

    log("Initializing BioClinicalBERT classifier...")
    model = finetune_classifier(enc_train)

    out_dir = "/project/results/finetuned_model"
    os.makedirs(out_dir, exist_ok=True)
    model.save_pretrained(out_dir)

    log(f"Fine-tuned model saved to {out_dir}.")

    duration = (datetime.utcnow() - start).total_seconds() / 60
    log(f"Fine-tuning job completed successfully in {duration:.2f} minutes.")


# ------------------------------------------------------------------
# MAIN ORCHESTRATOR
# ------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        default="baseline",
        choices=["baseline", "finetune"],
        help="Which pipeline to run: 'baseline' or 'finetune'.",
    )
    args = parser.parse_args()

    # ----------------------------------------------------------
    # BASELINE MODE
    # ----------------------------------------------------------
    if args.mode == "baseline":
        start_time = datetime.utcnow()
        log("Starting baseline model (Logistic Regression) job...")

        log("Loading the dataset...")
        df = pd.read_parquet("/project/data/df_merged_filtered.parquet")

        log("Applying text cleaning...")
        df = apply_cleaning(df)

        log("Creating stratified splits (patient-level)...")
        df_train, df_val, df_test = stratified_group_split(df)

        log("Loading the tokenizer...")
        tokenizer = load_tokenizer()

        log("Running baseline pipeline...")
        val_results, test_results, val_p, test_p, y_val, y_test = run_baseline(
            df_train, df_val, df_test, tokenizer
        )

        log("Saving eval results...")
        save_metrics_json(val_results, test_results)

        log("Saving ROC/PR curve plots...")
        save_figures("validation_baseline", y_val, val_p)
        save_figures("test_baseline", y_test, test_p)

        duration = (datetime.utcnow() - start_time).total_seconds() / 60
        log(f"Baseline completed successfully in {duration:.2f} minutes.")
        return

    # ----------------------------------------------------------
    # FINETUNE MODE
    # ----------------------------------------------------------
    if args.mode == "finetune":
        log("Starting fine-tuning job...")

        # Load ONLY the train split (safe, no leakage)
        enc_train = torch.load("/project/data/tokenized/enc_train.pt")

        log("Fine-tuning on TRAIN split...")
        run_finetuning(enc_train)
        return


if __name__ == "__main__":
    main()
