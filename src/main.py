import argparse
import pandas as pd

from preprocessing import apply_cleaning, stratified_group_split
from tokenization import load_tokenizer, tokenize_overflow_fixed_pt

from baseline_model import (
    load_bioclincial_bert_encoder,
    chunk_embeddings,
    aggregate_docs,
    train_logistic_regression,
)

from baseline_evaluate import (
    evaluate_with_target_recall,
    report_metrics
)


def run_baseline(df_train, df_val, df_test, tokenizer):
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc   = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc  = tokenize_overflow_fixed_pt(df_test, tokenizer)

    encoder = load_bioclincial_bert_encoder()

    train_chunk_emb = chunk_embeddings(train_enc, encoder)
    val_chunk_emb   = chunk_embeddings(val_enc, encoder)
    test_chunk_emb  = chunk_embeddings(test_enc, encoder)

    train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
    val_doc_emb   = aggregate_docs(val_chunk_emb,   val_enc["doc_mapping"])
    test_doc_emb  = aggregate_docs(test_chunk_emb,  test_enc["doc_mapping"])

    y_train = df_train["readmitted"].to_numpy()
    y_val   = df_val["readmitted"].to_numpy()
    y_test  = df_test["readmitted"].to_numpy()

    clf = train_logistic_regression(train_doc_emb, y_train)

    val_p  = clf.predict_proba(val_doc_emb)[:, 1]
    test_p = clf.predict_proba(test_doc_emb)[:, 1]

    best_t, val_pred  = evaluate_with_target_recall(y_val,  val_p,  target_recall=0.75)
    _,      test_pred = evaluate_with_target_recall(y_test, test_p, target_recall=0.75)

    report_metrics("VAL",  y_val,  val_pred,  val_p,  best_t)
    report_metrics("TEST", y_test, test_pred, test_p, best_t)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="baseline", choices=["baseline"])
    args = parser.parse_args()

    df = pd.read_parquet("/project/data/df_merged_filtered.parquet")
    df = apply_cleaning(df)
    df_train, df_val, df_test = stratified_group_split(df)

    tokenizer = load_tokenizer()

    run_baseline(df_train, df_val, df_test, tokenizer)


if __name__ == "__main__":
    main()
