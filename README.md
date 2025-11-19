# Predicting 30-Day Hospital Readmissions Using BioClinicalBERT

This cloud-based project trains and evaluates a transformer-based classification model (BioClinicalBERT) using discharge summaries from the MIMIC-IV dataset.  
The goal is to predict whether a patient will be readmitted within 30 days after discharge.
The entire workflow is deployed and executed on the Nautilus Cloud Platform using:

- Docker containerization  
- Kubernetes Jobs  
- Persistent Volume Claims (PVCs)  
- GPU acceleration
- Reproducible .py scripts converted from a Jupyter Notebook from my previous NLP project

# Project Structure

```
project-root/
|_ README.md # Project overview and setup instructions
|_ Dockerfile # Container image definition
|_ requirements.txt # Python dependencies (or environment.yml for conda)
|
|_ kubernetes/
|   |_ pvc.yaml # Persistent volume claim
|   |_ baseline_job.yaml # Job manifest for the baseline model
|   |_ finetune_job.yaml # Job manifest for the full fine-tuned model
|
|_ src/
|   |_ preprocessing.py # Data preprocessing scripts
|   |_ tokenization.py # BioClinicalBERT Tokenization script
|   |_ baseline_model.py # Baseline model definition and training script (Logistic Rregression)
|   |_ baseline_evaluate.py # Evaluation metrics for the baseline model (Logistic Regression)
|   |_ finetune_model.py # Full BioClinicalBERT fine-tuning on GPU
|   |_ finetune_evaluate.py # Evaluation script for the full fine-tuning model
|   |_ main.py # Main execution script
|
|_ data/
|   |_ README.md # Data source and access instructions
|
|
|_ results/
|   |_ metrics.json # Quantitative results
|   |_ figures/ # Generated plots and visualizations
|   |_ execution_log.txt # Nautilus job output and timing
|
|_ docs/
    |_ SETUP.md # Detailed setup and execution guide
    |_ CLOUD_SETUP.md # Nautilus-specific instructions
    |_ RESULTS.md # Results summary and analysis
```