import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    average_precision_score
)

# This selects the smallest threshold that reaches at least my target recall of 0.75
# If there's no threshold that meets the target, select the threshold that gives the highest recall
def evaluate_with_target_recall(y_true, probas, target_recall=0.75):
    thresholds = np.linspace(0.01, 0.99, 99)
    recalls = [recall_score(y_true, (probas >= t).astype(int)) for t in thresholds]
    valid_idxs = [i for i, r in enumerate(recalls) if r >= target_recall]
    if valid_idxs:
        best_t = thresholds[min(valid_idxs)]
    else:
        best_t = thresholds[int(np.argmax(recalls))]
    preds = (probas >= best_t).astype(int)
    return best_t, preds

# Display results
def report_metrics(name, y_true, y_pred, probas, threshold):
    print("\n=== {} Metrics (threshold = {:.3f}) ===".format(name, threshold))
    print("Accuracy :", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred, zero_division=0))
    print("Recall   :", recall_score(y_true, y_pred, zero_division=0))
    print("F1 Score :", f1_score(y_true, y_pred, zero_division=0))
    print("ROC-AUC  :", roc_auc_score(y_true, probas))
    print("PR-AUC   :", average_precision_score(y_true, probas))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
