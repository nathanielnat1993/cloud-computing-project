# CLOUD_SETUP.md
## 1. Nautilus Setup
All experiments were executed on the Nautilus Kubernetes platform.
- **Cluster:** Nautilus (National Research Platform)
- **Namespace:** `gp-engine-mizzou-dsa-cloud`
Access to the cluster was configured using the assigned namespace.

## 2. Persistent Volume Claim (PVC) Configuration
A persistent volume claim (PVC) was created to support shared storage across Kubernetes Jobs.
- **PVC name:** `naaxk6-pvc`
- **Storage class:** `rook-cephfs`
- **Access mode:** `ReadWriteMany`
- **Requested storage:** 50 GiB
- **Mount path:** `/project/storage`
The PVC was used to store input datasets, tokenized data, model outputs, evaluation metrics, logs, and generated figures.
kubectl apply -f kubernetes/pvc.yaml -n gp-engine-mizzou-dsa-cloud

## 3. Container Image
A custom Docker image was used for all jobs.
- **Base image:** `pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime`
- **Registry:** Nautilus GitLab Container Registry
- **Image:** `gitlab-registry.nrp-nautilus.io/nathanielnat1993/cloud-computing-project`
The image includes PyTorch with CUDA 11.8, Hugging Face Transformers, scikit-learn, and a pre-downloaded BioClinicalBERT model and tokenizer. The container entry point executes `main.py`.

## 4. Kubernetes Job Execution
### 4.1 Baseline Job
- **Manifest:** `kubernetes/baseline_job.yaml`
- **Mode:** `--mode baseline`
- **Resources:** CPU 1, Memory 12 GiB, GPU 1
kubectl apply -f kubernetes/baseline_job.yaml -n gp-engine-mizzou-dsa-cloud
kubectl get pods -n gp-engine-mizzou-dsa-cloud
kubectl logs <baseline-pod-name> -n gp-engine-mizzou-dsa-cloud

### 4.2 Fine-Tuning Job
- **Manifest:** `kubernetes/finetune_job.yaml`
- **Mode:** `--mode finetune`
- **Resources:** CPU 2, Memory 16 GiB, GPU 1
kubectl apply -f kubernetes/finetune_job.yaml -n gp-engine-mizzou-dsa-cloud
kubectl get pods -n gp-engine-mizzou-dsa-cloud
kubectl logs <finetune-pod-name> -n gp-engine-mizzou-dsa-cloud

## 5. PVC Inspection and Debugging
A utility pod was used to inspect the contents of the persistent volume.
- **Manifest:** `kubernetes/pvc-access.yaml`
kubectl apply -f kubernetes/pvc-access.yaml -n gp-engine-mizzou-dsa-cloud
kubectl exec -it pvc-access -- sh -n gp-engine-mizzou-dsa-cloud
ls /project/storage

## 6. Reproducibility
To reproduce the project:
1. Build and push the Docker image
2. Apply the PVC manifest
3. Upload the dataset to the PVC
4. Run the baseline job
5. Run the fine-tuning job
All results persist on the shared PVC across job executions.
