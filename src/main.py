import argparse
import os
import json
import pandas as pd
import matplotlib.pyplot as plt

import torch
from datetime import datetime

# ⭐ ADDED missing imports you needed for finetuning JSON saving
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

# ------------------------------------------------------------------
# Helper: save metrics JSON (BASELINE)
# ------------------------------------------------------------------
def save_metrics_json(val_dict, test_dict, results_dir):
    out = {
        "Validation": val_dict,
        "Test": test_dict,
        "metadata": {
            "model": "BioClinicalBERT + LogisticRegression",
            "timestamp": datetime.utcnow().isoformat(),
        },
    }
    # Ensure directory exists
    os.makedirs(results_dir, exist_ok=True)
    
    with open(os.path.join(results_dir, "baseline_metrics.json"), "w") as f:
        json.dump(out, f, indent=2)


# ------------------------------------------------------------------
# Helper: save ROC/PR curves
# ------------------------------------------------------------------
def save_figures(name, y_true, probas, results_dir):
    # Create figures subdirectory
    fig_dir = os.path.join(results_dir, "figures")
    os.makedirs(fig_dir, exist_ok=True)

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
    plt.savefig(os.path.join(fig_dir, f"{name}_roc_curve.png"))
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
    plt.savefig(os.path.join(fig_dir, f"{name}_pr_curve.png"))
    plt.close()


# ------------------------------------------------------------------
# BASELINE PIPELINE
# ------------------------------------------------------------------
def run_baseline(df_train, df_val, df_test, tokenizer, data_path, results_path):

    print("Tokenizing train/val/test...", flush=True)
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc   = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc  = tokenize_overflow_fixed_pt(df_test, tokenizer)

    # Define tokenized storage path based on input data_path
    tokenized_dir = os.path.join(data_path, "tokenized")
    os.makedirs(tokenized_dir, exist_ok=True)

    # Save encoded splits for fine-tuning later
    print(f"Saving tokenized data to {tokenized_dir}...", flush=True)
    torch.save(train_enc, os.path.join(tokenized_dir, "enc_train.pt"))
    torch.save(val_enc,   os.path.join(tokenized_dir, "enc_val.pt"))
    torch.save(test_enc,  os.path.join(tokenized_dir, "enc_test.pt"))

    print("Loading BioClinicalBERT encoder...", flush=True)
    encoder = load_bioclinical_bert_encoder()

    print("Generating chunk embeddings...", flush=True)
    train_chunk_emb = chunk_embeddings(train_enc, encoder)
    val_chunk_emb   = chunk_embeddings(val_enc, encoder)
    test_chunk_emb  = chunk_embeddings(test_enc, encoder)

    print("Aggregating chunk -> document embeddings...", flush=True)
    train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
    val_doc_emb   = aggregate_docs(val_chunk_emb,   val_enc["doc_mapping"])
    test_doc_emb  = aggregate_docs(test_chunk_emb,  test_enc["doc_mapping"])

    # Targets
    y_train = df_train["readmitted"].to_numpy()
    y_val   = df_val["readmitted"].to_numpy()
    y_test  = df_test["readmitted"].to_numpy()

    print("Training Logistic Regression baseline...", flush=True)
    clf = train_logistic_regression(train_doc_emb, y_train)

    print("Generating predictions...", flush=True)
    val_p  = clf.predict_proba(val_doc_emb)[:, 1]
    test_p = clf.predict_proba(test_doc_emb)[:, 1]

    best_t, val_pred  = evaluate_with_target_recall(y_val,  val_p,  target_recall=0.75)
    _,      test_pred = evaluate_with_target_recall(y_test, test_p, target_recall=0.75)

    # Print metrics
    report_metrics("Validation", y_val, val_pred, val_p, best_t)
    report_metrics("Test",       y_test, test_pred, test_p, best_t)

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
def run_finetuning(enc_train, results_path):
    start = datetime.utcnow()
    print("Starting fine-tuning BioClinicalBERT classifier...", flush=True)

    print(f"TRAIN chunks: {enc_train['input_ids'].shape[0]}", flush=True)
    n_docs = int(enc_train["doc_mapping"].max()) + 1
    print(f"Document count (train): {n_docs}", flush=True)

    print("Initializing classifier...", flush=True)
    model = finetune_classifier(enc_train)

    out_dir = os.path.join(results_path, "finetuned_model")
    os.makedirs(out_dir, exist_ok=True)
    model.save_pretrained(out_dir)

    print(f"Fine-tuned model saved to {out_dir}.", flush=True)

    duration = (datetime.utcnow() - start).total_seconds() / 60
    print(f"Fine-tuning completed in {duration:.2f} minutes.", flush=True)


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
    parser.add_argument(
        "--data_path",
        default="/project/storage/data", 
        help="Path to the folder containing parquet files and tokenized data"
    )
    parser.add_argument(
        "--results_path",
        default="/project/storage/results",
        help="Path to save output figures, metrics, and models"
    )
    args = parser.parse_args()

    os.makedirs(args.results_path, exist_ok=True)

    # ----------------------------------------------------------
    # BASELINE MODE
    # ----------------------------------------------------------
    if args.mode == "baseline":
        start_time = datetime.utcnow()
        print("Starting baseline model job...", flush=True)

        print("Loading dataset...", flush=True)
        parquet_path = os.path.join(args.data_path, "df_merged_filtered.parquet")
        df = pd.read_parquet(parquet_path)

        print("Applying text cleaning...", flush=True)
        df = apply_cleaning(df)

        print("Creating stratified splits...", flush=True)
        df_train, df_val, df_test = stratified_group_split(df)

        print("Loading tokenizer...", flush=True)
        tokenizer = load_tokenizer()

        print("Running baseline pipeline...", flush=True)
        val_results, test_results, val_p, test_p, y_val, y_test = run_baseline(
            df_train, df_val, df_test, tokenizer, args.data_path, args.results_path
        )

        print("Saving eval results...", flush=True)
        save_metrics_json(val_results, test_results, args.results_path)

        print("Saving curves...", flush=True)
        save_figures("validation_baseline", y_val, val_p, args.results_path)
        save_figures("test_baseline",       y_test, test_p, args.results_path)

        duration = (datetime.utcnow() - start_time).total_seconds() / 60
        print(f"Baseline completed in {duration:.2f} minutes.", flush=True)
        return

    # ----------------------------------------------------------
    # FINETUNE MODE
    # ----------------------------------------------------------
    if args.mode == "finetune":
        print("Starting fine-tuning job...", flush=True)
    
        train_path = os.path.join(args.data_path, "tokenized", "enc_train.pt")
        print(f"Loading TRAIN tokens from {train_path}...", flush=True)
        enc_train = torch.load(train_path)
    
        print("Fine-tuning on TRAIN split...", flush=True)
        model = finetune_classifier(enc_train)
    
        model_dir = os.path.join(args.results_path, "finetuned_model")
        os.makedirs(model_dir, exist_ok=True)
        model.save_pretrained(model_dir)
        print(f"Fine-tuned model saved to {model_dir}", flush=True)
    
        val_path  = os.path.join(args.data_path, "tokenized", "enc_val.pt")
        test_path = os.path.join(args.data_path, "tokenized", "enc_test.pt")
    
        print(f"Loading VAL tokens from {val_path}...", flush=True)
        enc_val = torch.load(val_path)
    
        print(f"Loading TEST tokens from {test_path}...", flush=True)
        enc_test = torch.load(test_path)
    
        from finetune_model import infer_logits
        from finetune_evaluate import softmax_np, aggregate_mean, best_threshold_f1, report
    
        print("Running inference on VAL...", flush=True)
        val_logits = infer_logits(model, enc_val)
        val_docs   = aggregate_mean(val_logits, enc_val["doc_mapping"])
        val_probas = softmax_np(val_docs)[:, 1]
        
        D = enc_val["doc_mapping"].numpy()
        y_chunks = enc_val["labels"].numpy()
        n = int(D.max()) + 1
        y_val = np.zeros(n, dtype=np.int32)
        for d in range(n):
            y_val[d] = y_chunks[D == d][0]
    
        print("Running inference on TEST...", flush=True)
        test_logits = infer_logits(model, enc_test)
        test_docs   = aggregate_mean(test_logits, enc_test["doc_mapping"])
        test_probas = softmax_np(test_docs)[:, 1]
        
        D_test = enc_test["doc_mapping"].numpy()
        y_chunks_test = enc_test["labels"].numpy()
        n_docs_test = int(D_test.max()) + 1
        y_test = np.zeros(n_docs_test, dtype=np.int32)
        for d in range(n_docs_test):
            y_test[d] = y_chunks_test[D_test == d][0]

        thr = best_threshold_f1(y_val, val_probas)
        val_pred  = (val_probas  >= thr).astype(int)
        test_pred = (test_probas >= thr).astype(int)
    
        report("FINETUNED VALIDATION", y_val, val_pred, val_probas, thr)
        report("FINETUNED TEST",       y_test, test_pred, test_probas, thr)
    
        result_json = {
            "threshold": float(thr),
            "Validation": {
                "precision": float(precision_score(y_val, val_pred, zero_division=0)),
                "recall": float(recall_score(y_val, val_pred, zero_division=0)),
                "f1": float(f1_score(y_val, val_pred, zero_division=0)),
                "roc_auc": float(roc_auc_score(y_val, val_probas)),
            },
            "Test": {
                "precision": float(precision_score(y_test, test_pred, zero_division=0)),
                "recall": float(recall_score(y_test, test_pred, zero_division=0)),
                "f1": float(f1_score(y_test, test_pred, zero_division=0)),
                "roc_auc": float(roc_auc_score(y_test, test_probas)),
            }
        }
    
        with open(os.path.join(args.results_path, "finetuned_metrics.json"), "w") as f:
            json.dump(result_json, f, indent=2)
    
        print(f"Saved metrics to {args.results_path}/finetuned_metrics.json", flush=True)
    
        save_figures("finetuned_validation", y_val, val_probas, args.results_path)
        save_figures("finetuned_test",       y_test, test_probas, args.results_path)
    
        print("Fine-tuning evaluation completed.", flush=True)
        return



if __name__ == "__main__":
    main()
