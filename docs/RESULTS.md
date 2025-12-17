# Results

## Computational Performance

All experiments ran as Kubernetes Jobs in the gp-engine-mizzou-dsa-cloud namespace.

Baseline job
- Runtime: 80 minutes
- Resources: CPU 1, Memory 12 GiB, GPU 1
- Status: Completed

Fine-tuning job
- Runtime: 22 minutes
- Resources: CPU 2, Memory 16 GiB, GPU 1
- Status: Completed

## Model Performance (Test Set)

Baseline model
- Precision: 0.26
- Recall: 0.76
- F1-score: 0.38
- ROC-AUC: 0.68
- PR-AUC: 0.35

Lightly fine-tuned model
- Precision: 0.22
- Recall: 0.81
- F1-score: 0.35
- ROC-AUC: 0.63
- PR-AUC: 0.28

Recall improved with fine-tuning at the cost of precision.

## Visualizations

Baseline - Validation  
![ROC](../results/figures/validation_baseline_roc_curve.png)  
![PR](../results/figures/validation_baseline_pr_curve.png)

Baseline - Test  
![ROC](../results/figures/test_baseline_roc_curve.png)  
![PR](../results/figures/test_baseline_pr_curve.png)

Fine-tuned - Validation  
![ROC](../results/figures/finetuned_validation_roc_curve.png)  
![PR](../results/figures/finetuned_validation_pr_curve.png)

Fine-tuned - Test  
![ROC](../results/figures/finetuned_test_roc_curve.png)  
![PR](../results/figures/finetuned_test_pr_curve.png)
