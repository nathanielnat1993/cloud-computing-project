# Project Setup
This document describes how to set up and run the project on the Nautilus Kubernetes platform. All modeling experiments were executed on Nautilus using containerized workloads. Local execution was limited to early data preparation steps prior to text preprocessing.

## Prerequisites
- Access to the Nautilus Kubernetes cluster
- Membership in the class namespace gp-engine-mizzou-dsa-cloud
- kubectl configured to point to Nautilus
- Access to the GitLab container registry
- Source code for this project is available in the class GitLab repository:
https://gitlab.nrp-nautilus.io/nathanielnat1993/cloud-computing-project

## Container Image
All jobs use a custom Docker image built on top of the official PyTorch CUDA runtime image. The image includes all required Python dependencies and a cached copy of BioClinicalBERT to support offline execution on Nautilus. The image is stored in the GitLab container registry and referenced directly in the Kubernetes job manifests.

## Persistent Storage Setup
A persistent volume claim (PVC) is used to store input data, tokenized outputs, trained models, logs, and evaluation results.

Create the PVC:
kubectl apply -f kubernetes/pvc.yaml -n gp-engine-mizzou-dsa-cloud

Verify the PVC is bound:
kubectl get pvc -n gp-engine-mizzou-dsa-cloud

(Optional) Launch the PVC inspection pod:
kubectl apply -f kubernetes/pvc-access.yaml -n gp-engine-mizzou-dsa-cloud

(Optional) Inspect PVC contents:
kubectl exec -it pvc-access -n gp-engine-mizzou-dsa-cloud -- sh
ls /project/storage

## Running the Baseline Model
Launch the baseline job:
kubectl apply -f kubernetes/baseline_job.yaml -n gp-engine-mizzou-dsa-cloud

Monitor execution:
kubectl get pods -n gp-engine-mizzou-dsa-cloud
kubectl logs <baseline-pod-name> -n gp-engine-mizzou-dsa-cloud

The baseline job performs text preprocessing, tokenization, embedding generation using BioClinicalBERT, and logistic regression training.

## Running the Fine-Tuning Model
Launch the fine-tuning job:
kubectl apply -f kubernetes/finetune_job.yaml -n gp-engine-mizzou-dsa-cloud

Monitor execution:
kubectl get pods -n gp-engine-mizzou-dsa-cloud
kubectl logs <finetune-pod-name> -n gp-engine-mizzou-dsa-cloud

The fine-tuning job trains only the BioClinicalBERT classification head while keeping encoder layers frozen.

## Outputs
All outputs are written to the shared PVC and persist across job runs. These include tokenized datasets, trained model artifacts, evaluation metrics, plots, and execution logs. Results are summarized in docs/RESULTS.md.

## Reproducibility
The project can be reproduced by rebuilding the Docker image, applying the PVC and job manifests, and re-running the Kubernetes Jobs. Fixed random states were used for data splitting to ensure consistent results across runs.
