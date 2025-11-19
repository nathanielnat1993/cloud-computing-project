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
|   |_ job.yaml # Job manifest
|
|_ src/
|   |_ preprocessing.py # Data preprocessing scripts
|   |_ model.py # Model definition and training script
|   |_ evaluate.py # Evaluation metrics
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