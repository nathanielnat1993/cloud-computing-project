## Repository
https://gitlab.nrp-nautilus.io/nathanielnat1993/cloud-computing-project

## 1. Requirements
- Access to Nautilus
- Namespace: gp-engine-mizzou-dsa-cloud
- kubectl configured
- Access to GitLab container registry

## 2. Create Persistent Volume Claim (PVC)
kubectl apply -f kubernetes/pvc.yaml -n gp-engine-mizzou-dsa-cloud
<br>
kubectl get pvc -n gp-engine-mizzou-dsa-cloud

## 3. (Optional) Inspect PVC
kubectl apply -f kubernetes/pvc-access.yaml -n gp-engine-mizzou-dsa-cloud
<br>
kubectl exec -it pvc-access -n gp-engine-mizzou-dsa-cloud -- sh
<br>
ls /project/storage

## 4. Dataset Location
The merged and feature-engineered dataset MUST be stored in:
<br>
/project/storage/data/
<br>
Example:
/project/storage/data/df_merged_filtered.parquet
<br>
Verify:
<br>
kubectl exec -it pvc-access -n gp-engine-mizzou-dsa-cloud -- ls /project/storage/data

## 5. Run Baseline Job
kubectl apply -f kubernetes/baseline_job.yaml -n gp-engine-mizzou-dsa-cloud
<br>
kubectl get pods -n gp-engine-mizzou-dsa-cloud
<br>
kubectl logs <baseline-pod-name> -n gp-engine-mizzou-dsa-cloud

## 6. Run Fine-Tuning Job
kubectl apply -f kubernetes/finetune_job.yaml -n gp-engine-mizzou-dsa-cloud
<br>
kubectl get pods -n gp-engine-mizzou-dsa-cloud
<br>
kubectl logs <finetune-pod-name> -n gp-engine-mizzou-dsa-cloud

## 7. Outputs
All outputs are written to:
<br>
/project/storage/
<br>
Metrics, logs, and figures persist across job runs.
