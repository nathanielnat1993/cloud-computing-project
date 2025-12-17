## Environment
- Platform: Nautilus
- Namespace: gp-engine-mizzou-dsa-cloud
- Registry: GitLab Container Registry

## Nautilus Commands
kubectl apply -f kubernetes/pvc.yaml -n gp-engine-mizzou-dsa-cloud
<br>
kubectl apply -f kubernetes/baseline_job.yaml -n gp-engine-mizzou-dsa-cloud
<br>
kubectl apply -f kubernetes/finetune_job.yaml -n gp-engine-mizzou-dsa-cloud
<br>
kubectl get pods -n gp-engine-mizzou-dsa-cloud
<br>
kubectl logs <pod-name> -n gp-engine-mizzou-dsa-cloud
<br>
kubectl describe pod <pod-name> -n gp-engine-mizzou-dsa-cloud
