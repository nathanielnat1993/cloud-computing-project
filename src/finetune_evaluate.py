import numpy as np
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
)
import torch
from transformers import AutoModelForSequenceClassification
from finetune_model import infer_logits  # <-- fixed import


def softmax_np(x):
    x = x - x.max(axis = 1, keepdims = True)
    e = np.exp(x)
    return e / e.sum(axis = 1, keepdims = True)


def aggregate_mean(logits_tensor, doc_map_tensor):
    L = logits_tensor.numpy()
    D = doc_map_tensor.numpy()
    n = int(D.max()) + 1 if D.size else 0

    sums = np.zeros((n, L.shape[1]), dtype = np.float32)
    np.add.at(sums, D, L)
    counts = np.bincount(D, minlength = n).astype(np.float32)[:, None]

    return sums / counts


def best_threshold_f1(y, p):
    ts = np.linspace(0.01, 0.99, 99)
    f1s = [f1_score(y, (p >= t).astype(int)) for t in ts]
    return ts[int(np.argmax(f1s))]


def report(split, y, pred, p, thr):
    print("\n=== {} Metrics (threshold = {:.3f}) ===".format(split, thr))
    print("Precision :", precision_score(y, pred, zero_division = 0))
    print("Recall    :", recall_score(y, pred, zero_division = 0))
    print("F1 Score  :", f1_score(y, pred, zero_division = 0))
    print("ROC-AUC   :", roc_auc_score(y, p))
    print("Confusion Matrix:\n", confusion_matrix(y, pred))


if __name__ == "__main__":
    # Load tokenized enc file (full dataset)
    enc = torch.load("/project/data/tokenized/enc_test.pt")


    # Load fine-tuned model
    model_path = "/project/results/finetuned_model"
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model = model.to("cuda")
    model.eval()

    # Run inference on chunks
    logits_chunks = infer_logits(model, enc)

    # Aggregate chunk → doc
    logits_docs = aggregate_mean(logits_chunks, enc["doc_mapping"])

    # Convert logits → probabilities
    probas = softmax_np(logits_docs)[:, 1]

    # True labels
    y = enc["labels"].numpy()

    # Choose best F1 threshold
    thr = best_threshold_f1(y, probas)

    # Predictions
    preds = (probas >= thr).astype(int)

    # Print metrics
    report("FINETUNED", y, preds, probas, thr)
