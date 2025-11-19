# Data Folder

This folder contains documentation related to the input data used in this project.
The actual MIMIC Notes dataset is not included in this repository due to licensing, size constraints, and PHI restrictions associated with the MIMIC-IV database.

## About the Dataset

This project uses a subset of discharge summaries from the MIMIC-IV notes database for predicting 30-day hospital readmissions using BioClinicalBERT.
MIMIC-IV contains protected health information (PHI) and can only be accessed by credentialed users who complete the required training.

## Why the Data Is Not Included

* MIMIC-IV is restricted and does not allow redistribution.
* Dataset files are too large for GitHub.
* All data used in this project is stored securely on Nautilus Persistent Volume Claim (PVC).

## How the Data Is Accessed in the Cloud

During Nautilus execution:

* The input dataset (parquet file) is placed inside the PVC mounted at /project/data/.
* The Kubernetes Job automatically reads data from this directory before preprocessing and model training.

## Notes

* Users must obtain access to MIMIC-IV from PhysioNet and download the data themselves.