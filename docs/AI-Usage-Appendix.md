# AI Usage Disclosure Appendix

**Student Name:** Nathaniel Antonio 
**Assignment/Project Title:** Cloud Computing Final Project 
**Date:** 12/17/2025

---

## Instructions
**Complete this appendix whenever you use ANY artificial intelligence tools during your coursework.** This includes grammar checkers, code assistants, search engines with AI features, chatbots, or any other AI-powered tools. Attach this completed form to your assignment submission.

**If you did NOT use any AI tools, check here:** ☐ *No AI tools were used for this assignment*

---

## AI Tool Usage Log

**Complete one section below for EACH AI tool or session used:**

### AI Tool #1

**Tool Name/Platform:** ChatGPT  
*(e.g., ChatGPT, Grammarly, GitHub Copilot, Google Search AI Overview, Perplexity, etc.)*

**Date & Time of Use:** Nov. 22 - Dec. 17, 2025

**Purpose of Use:** grammar checking, code debugging, research assistance, brainstorming, general questions 
*(e.g., grammar checking, code debugging, research assistance, brainstorming, etc.)*

**Exact Prompt(s) or Query(ies) Used:**
```
[Paste the exact text you entered into the AI tool]

How to create a docker image 
How do I run it 
I only have my dockerfile I haven't built anything yet 
Do I need to run it locally? I thought you said it's not good for mac it's slow and I can't do cuda. 
I thought I n needed github reposithro. For Docker
Great question, Nat-Nat — and honestly, understanding the difference saves you a LOT of headaches when doing cloud projects. Let me break this down cleanly, in your vibe.

⭐ LOCAL = your actual Mac laptop
This is when you run Docker on your own computer.
✔ Pros:
	•	You control everything
	•	Fast builds if your Mac is powerful
	•	No Nautilus resource limits
	•	No Jupyter timeout issues
	•	Easiest to debug because you see everything directly
✔ Cons:
	•	You must have Docker Desktop installed
	•	Docker Desktop on Mac (especially M-chip) sometimes struggles with PyTorch GPU images (but CPU builds are fine)
	•	Your Mac cannot build GPU-enabled containers that actually use CUDA (because Mac has no CUDA)
But your Dockerfile uses CUDA (pytorch-cuda). That’s the problem:
❗ Your Mac CANNOT build CUDA images
macOS cannot run or emulate:
	•	CUDA runtime
	•	NVIDIA drivers
	•	GPU-enabled PyTorch containers
So your Docker build will fail locally because the base image:

pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime
requires CUDA, which Mac cannot handle.
This means:
❌ You should NOT build this image locally on your Mac.

⭐ JUPYTERHUB = Nautilus terminal on GP-ENGINE
This is running Docker commands inside Nautilus, where:
	•	GPU nodes exist
	•	CUDA drivers exist
	•	NVIDIA runtime is installed
	•	GPU-enabled PyTorch images can build
	•	Everything is Linux-based (compatible)
✔ Pros:
	•	Correct environment for CUDA-based builds
	•	Faster builds (A100/V100 nodes)
	•	No Docker Desktop needed
	•	You can push directly after building
	•	Works with your GPU Dockerfile
✔ Cons:
	•	JupyterHub session can time out after ~12 hours
	•	Storage is limited
	•	Must upload your repo to Nautilus (or git clone it there)
BUT: For a GPU-enabled ML container, this is the right place to build.

💛 TL;DR — Nat-Nat Edition
⭐ If you're building a CUDA-enabled ML Docker image (like yours):
→ Build it on Nautilus JupyterHub terminal
→ NOT on your Mac
Because:
	•	Your Mac has no NVIDIA GPU
	•	CUDA does not run on macOS
	•	GPU docker images cannot be built locally
	•	JupyterHub is the correct environment

⭐ So your next step is:
👉 Build your image inside the JupyterHub terminal.
Meaning: Go to: Nautilus / gp-engine / JupyterHub → Terminal
Then run:

git clone https://github.com/nathanielnat1993/cloud-computing-project.git
cd cloud-computing-project

# Login to GHCR
echo <YOUR_PAT> | docker login ghcr.io -u nathanielnat1993 --password-stdin

# Build CUDA image
docker build -t ghcr.io/nathanielnat1993/cloud-computing-project:latest .

# Push to GHCR
docker push ghcr.io/nathanielnat1993/cloud-computing-project:latest

If you'd like, I can guide you through these one at a time.
Just say:
👉 "Okay, let’s build the image on JupyterHub"

It says no command 
What does it mean? I can't use gou workload 

okay i copied the baseline-job yaml
is this a good commit comment. Added Dockerfile, yaml for my baseline model job, and my pvc yaml file
okay let's proceed with the image
i dont see read and write packages in permissions
no packages
i did select my cloud computing repo but there's no packages
wait how do. i login to ghcr?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ echo 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 | docker login ghcr.io -u nathanielnat1993 --password-stdin
bash: docker: command not found
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
how do i add that folder to my repo
what do i paste? what's the classic pat?
so this? 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
okay what's next. i pasted the pat
am i pushing this big ass file?
not th eparquet but the image
does it take a while it seemed to stop here but it says it's still running. #16 pushing layer 18defcb9e692 7.97GB / 8.07GB 242.8s
is there a way to change the commit comment
do i still need the pat?
okay it says it's completed
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl apply -f kubernetes/pvc.yaml
Error from server (Forbidden): error when retrieving current configuration of:
Resource: "/v1, Resource=persistentvolumeclaims", GroupVersionKind: "/v1, Kind=PersistentVolumeClaim"
Name: "naaxk6-pvc", Namespace: "default"
from server for: "kubernetes/pvc.yaml": persistentvolumeclaims "naaxk6-pvc" is forbidden: User "http://cilogon.org/serverF/users/406832" cannot get resource "persistentvolumeclaims" in API group "" in the namespace "default"
this worked. jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f kubernetes/pvc.yaml
persistentvolumeclaim/naaxk6-pvc created
kubectl -n gp-engine-mizzou-dsa-cloud why did i have to do this to run? do i need to update anything inmy files or code?
how come my class exercise it did not include the namespace but it still ran. apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: naaxk6-pv
spec:
  storageClassName: rook-cephfs	
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 50Gi
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl config view --minify
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://67.58.53.148:443
  name: nautilus
contexts:
- context:
    cluster: nautilus
    user: oidc
  name: nautilus
current-context: nautilus
kind: Config
preferences: {}
users:
- name: oidc
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1beta1
      args:
      - oidc-login
      - get-token
      - --token-cache-storage=disk
      - --oidc-issuer-url=https://authentik.nrp-nautilus.io/application/o/k8s/
      - --oidc-client-id=xrxBIaWxeRmGJUwSvaLjUzMEFZzQu2b4nk9I0B2W
      - --listen-address=0.0.0.0:8000
      - --oidc-extra-scope=profile,offline_access
      - --grant-type=device-code
      - --skip-open-browser
      command: kubectl
      env: null
      interactiveMode: IfAvailable
      provideClusterInfo: false
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
can i just not update teh files but instead just include this when i do something. gp-engine-mizzou-dsa-cloud
okay let's just add the namespace then
the 2nd one is not part of this project
hwo do i Make sure the image matches your real GHCR image.
it says no packages
oh okay so this is it. docker pull ghcr.io/nathanielnat1993/cloud-computing-project:latest
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl apply -f kubernetes/baseline_job.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> has no memory limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> has no resource requests
Error from server (Forbidden): error when creating "kubernetes/baseline_job.yaml": admission webhook "validation.gatekeeper.sh" denied the request: [container-must-have-limits-and-requests] container <baseline> does not have <{"cpu", "memory"}> requests defined
[container-must-have-limits-and-requests] container <baseline> does not have <{"memory"}> limits defined
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
also my base line yaml file is named baseline_job.yaml not baseline-job.yaml
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl apply -f kubernetes/baseline_job.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> cpu limit <4> is higher than the maximum allowed ratio of <1.2>
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> memory limit <32Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/baseline-job created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get pods -n gp-engine-mizzou-dsa-cloud
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-28xkh                 0/1     ContainerCreating   0          81s
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          7h50m
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          7h49m
pod-cc5m4-train                    0/1     Error               0          35h
pod-gcfpx-train                    1/1     Running             0          3h31m
pod-name-ljabxf                    1/1     Running             0          3h32m
pod-pvc-jm2rc                      1/1     Running             0          4h22m
pvc-checker                        0/1     Error               0          11h
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$  which one is mine
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl describe pod baseline-job-28xkh -n gp-engine-mizzou-dsa-cloud
Name:             baseline-job-28xkh
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-gpu-01.calit2.optiputer.net/67.58.51.142
Start Time:       Thu, 20 Nov 2025 09:35:10 +0000
Labels:           batch.kubernetes.io/controller-uid=dd27e9b3-3d3e-410e-8c07-1991eb12d4fa
                  batch.kubernetes.io/job-name=baseline-job
                  controller-uid=dd27e9b3-3d3e-410e-8c07-1991eb12d4fa
                  job-name=baseline-job
Annotations:      cni.projectcalico.org/containerID: 822880fa07d9a59b64a20c0c53adc4cef125f6050dcc7560cacd577f0d027f26
                  cni.projectcalico.org/podIP: 10.244.28.28/32
                  cni.projectcalico.org/podIPs: 10.244.28.28/32,fdf0:17b3:c3ec:1f79:10:0:5:eed8/128
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/baseline-job
Containers:
  baseline:
    Container ID:  
    Image:         ghcr.io/nathanielnat1993/cloud-computing-project:latest
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      python
      src/main.py
      --mode
      baseline
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:             4
      memory:          32Gi
      nvidia.com/gpu:  1
    Requests:
      cpu:             2
      memory:          16Gi
      nvidia.com/gpu:  1
    Environment:       <none>
    Mounts:
      /project/data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mbjv2 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-mbjv2:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason                  Age    From                     Message
  ----    ------                  ----   ----                     -------
  Normal  Scheduled               2m58s  default-scheduler        Successfully assigned gp-engine-mizzou-dsa-cloud/baseline-job-28xkh to k8s-gpu-01.calit2.optiputer.net
  Normal  SuccessfulAttachVolume  2m57s  attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-d64c959a-1fdb-4774-95aa-f6e337f1fc1a"
  Normal  Pulling                 2m53s  kubelet                  Pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
whit its running can i commit the changes to those yaml files
it still says container running
how long would it take?
in the meantime, do i need to put my parquet file in data folder?
can i put it in my data folder locally? i cloned the repo locally using the desktop app.
no. the file is stored locally since it's 800 mb
what should be teh commit comment
for the pcv explorer
/Users/nat-nat/Desktop/project-root/data/df_merged_filtered.parquet
i thought i had to run cd /Users/nat-nat/Desktop/project-root/data/df_merged_filtered.parquet first
(base) nat-nat@Mac data % kubectl cp df_merged_filtered.parquet \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet

Error from server (NotFound): pods "pvc-explorer" not found
(base) nat-nat@Mac data % 
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-28xkh                 0/1     ImagePullBackOff    0          22m
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          8h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          8h
pod-cc5m4-train                    0/1     Error               0          35h
pod-gcfpx-train                    1/1     Running             0          3h51m
pod-name-ljabxf                    1/1     Running             0          3h53m
pod-pvc-jm2rc                      1/1     Running             0          4h43m
pvc-checker                        0/1     Error               0          12h
pvc-explorer                       0/1     ContainerCreating   0          16s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
(base) nat-nat@Mac data % kubectl cp df_merged_filtered.parquet \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet
 okay so i pasted this but nothing happened. do i njust wait
do i do this step in terminal? like right now while running?
(base) nat-nat@Mac data % kubectl cp df_merged_filtered.parquet \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet

kubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- bash

E1120 00:01:13.751825   75620 v2.go:150] "Unhandled Error" err="next reader: read tcp 192.168.1.232:56890->67.58.53.148:443: i/o timeout"
E1120 00:01:13.751837   75620 v2.go:167] "Unhandled Error" err="next reader: read tcp 192.168.1.232:56890->67.58.53.148:443: i/o timeout"
E1120 00:01:13.751852   75620 v2.go:129] "Unhandled Error" err="next reader: read tcp 192.168.1.232:56890->67.58.53.148:443: i/o timeout"
E1120 00:01:13.753505   75620 v2.go:104] "Unhandled Error" err="write tcp 192.168.1.232:56890->67.58.53.148:443: use of closed network connection"
error: error reading from error stream: next reader: read tcp 192.168.1.232:56890->67.58.53.148:443: i/o timeout
(base) nat-nat@Mac data % kubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- bash

root@pvc-explorer:/# 
root@pvc-explorer:/# 
root@pvc-explorer:/# ls -lh /data
total 23M
-rw------- 1 root root 23M Nov 20 10:01 df_merged_filtered.parquet
root@pvc-explorer:/# 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get pods -n gp-engine-mizzou-dsa-cloud
NAME                               READY   STATUS             RESTARTS   AGE
baseline-job-28xkh                 0/1     ImagePullBackOff   0          27m
job-ljabxf-resnet18-train-qbksm    0/1     Completed          0          8h
job-ljabxf-simpledla-train-82bgh   0/1     Completed          0          8h
pod-cc5m4-train                    0/1     Error              0          35h
pod-gcfpx-train                    1/1     Running            0          3h57m
pod-name-ljabxf                    1/1     Running            0          3h58m
pod-pvc-jm2rc                      1/1     Running            0          4h49m
pvc-checker                        0/1     Error              0          12h
pvc-explorer                       1/1     Running            0          5m38s
command not found
i did it in my terminal mac
(base) nat-nat@Mac ~ % docker --version
docker images

Docker version 28.5.2, build ecc6942
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
(base) nat-nat@Mac ~ %  what's next
wait wait. cd /Users/nat-nat/Desktop/project-root this directory is not my repo directory. this is just a copy of that repo but is not connected ot github
/Users/nat-nat/Documents/GitHub/cloud-computing-project
i don't have my pat anymore
okay so i ran the code and right now the imga is buidling in my terminal
 1 warning found (use docker --debug to expand):
 - InvalidBaseImagePlatform: Base image pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime was pulled with platform "linux/amd64", expected "linux/arm64" for current build (line 2)
(base) nat-nat@Mac cloud-computing-project % 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl apply -f kubernetes/baseline_job.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> cpu limit <4> is higher than the maximum allowed ratio of <1.2>
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> memory limit <32Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/baseline-job created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
baseline-job-fm2s5                 0/1     ErrImagePull   0          45s
job-ljabxf-resnet18-train-qbksm    0/1     Completed      0          8h
job-ljabxf-simpledla-train-82bgh   0/1     Completed      0          8h
pod-cc5m4-train                    0/1     Error          0          36h
pod-gcfpx-train                    1/1     Running        0          4h21m
pod-name-ljabxf                    1/1     Running        0          4h22m
pod-pvc-jm2rc                      1/1     Running        0          5h12m
pvc-checker                        0/1     Error          0          12h
pvc-explorer                       1/1     Running        0          29m
ovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl describe pod baseline-job-fm2s5 -n gp-engine-mizzou-dsa-cloud
Name:             baseline-job-fm2s5
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-gpu-01.calit2.optiputer.net/67.58.51.142
Start Time:       Thu, 20 Nov 2025 10:25:42 +0000
Labels:           batch.kubernetes.io/controller-uid=e47b7fa8-8ef5-4f46-b407-71b70435ca5a
                  batch.kubernetes.io/job-name=baseline-job
                  controller-uid=e47b7fa8-8ef5-4f46-b407-71b70435ca5a
                  job-name=baseline-job
Annotations:      cni.projectcalico.org/containerID: f190fcff2cde4ac2faa00e55c149191bd5321eb70c96ef7710cb2f73386587de
                  cni.projectcalico.org/podIP: 10.244.28.51/32
                  cni.projectcalico.org/podIPs: 10.244.28.51/32,fdf0:17b3:c3ec:1f79:10:0:5:eed3/128
Status:           Pending
IP:               10.244.28.51
IPs:
  IP:           10.244.28.51
  IP:           fdf0:17b3:c3ec:1f79:10:0:5:eed3
Controlled By:  Job/baseline-job
Containers:
  baseline:
    Container ID:  
    Image:         ghcr.io/nathanielnat1993/cloud-computing-project:latest
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      python
      src/main.py
      --mode
      baseline
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:             4
      memory:          32Gi
      nvidia.com/gpu:  1
    Requests:
      cpu:             2
      memory:          16Gi
      nvidia.com/gpu:  1
    Environment:       <none>
    Mounts:
      /project/data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-chbbv (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-chbbv:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type     Reason                  Age                From                     Message
  ----     ------                  ----               ----                     -------
  Normal   Scheduled               83s                default-scheduler        Successfully assigned gp-engine-mizzou-dsa-cloud/baseline-job-fm2s5 to k8s-gpu-01.calit2.optiputer.net
  Normal   SuccessfulAttachVolume  82s                attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-d64c959a-1fdb-4774-95aa-f6e337f1fc1a"
  Normal   Pulling                 33s (x3 over 71s)  kubelet                  Pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
  Warning  Failed                  32s (x3 over 70s)  kubelet                  Failed to pull image "ghcr.io/nathanielnat1993/cloud-computing-project:latest": failed to pull and unpack image "ghcr.io/nathanielnat1993/cloud-computing-project:latest": failed to resolve reference "ghcr.io/nathanielnat1993/cloud-computing-project:latest": failed to authorize: failed to fetch anonymous token: unexpected status from GET request to https://ghcr.io/token?scope=repository%3Anathanielnat1993%2Fcloud-computing-project%3Apull&service=ghcr.io: 401 Unauthorized
  Warning  Failed                  32s (x3 over 70s)  kubelet                  Error: ErrImagePull
  Normal   BackOff                 3s (x4 over 69s)   kubelet                  Back-off pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
  Warning  Failed                  3s (x4 over 69s)   kubelet                  Error: ImagePullBackOff
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
it's still error. jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl describe pod baseline-job-lpbq9 -n gp-engine-mizzou-dsa-cloud
Name:             baseline-job-lpbq9
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-gpu-01.calit2.optiputer.net/67.58.51.142
Start Time:       Thu, 20 Nov 2025 10:29:53 +0000
Labels:           batch.kubernetes.io/controller-uid=83876d0d-0185-4c6e-984e-f0d3a5fbe21a
                  batch.kubernetes.io/job-name=baseline-job
                  controller-uid=83876d0d-0185-4c6e-984e-f0d3a5fbe21a
                  job-name=baseline-job
Annotations:      cni.projectcalico.org/containerID: e6185248139d7288fef2356846050b9e96b86aff066abd00c1f637f27886ac55
                  cni.projectcalico.org/podIP: 10.244.28.37/32
                  cni.projectcalico.org/podIPs: 10.244.28.37/32,fdf0:17b3:c3ec:1f79:10:0:5:eedc/128
Status:           Pending
IP:               10.244.28.37
IPs:
  IP:           10.244.28.37
  IP:           fdf0:17b3:c3ec:1f79:10:0:5:eedc
Controlled By:  Job/baseline-job
Containers:
  baseline:
    Container ID:  
    Image:         ghcr.io/nathanielnat1993/cloud-computing-project:latest
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      python
      src/main.py
      --mode
      baseline
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:             4
      memory:          32Gi
      nvidia.com/gpu:  1
    Requests:
      cpu:             2
      memory:          16Gi
      nvidia.com/gpu:  1
    Environment:       <none>
    Mounts:
      /project/data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6p9mm (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-6p9mm:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type     Reason                  Age                From                     Message
  ----     ------                  ----               ----                     -------
  Normal   Scheduled               87s                default-scheduler        Successfully assigned gp-engine-mizzou-dsa-cloud/baseline-job-lpbq9 to k8s-gpu-01.calit2.optiputer.net
  Normal   SuccessfulAttachVolume  86s                attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-d64c959a-1fdb-4774-95aa-f6e337f1fc1a"
  Normal   Pulling                 38s (x3 over 81s)  kubelet                  Pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
  Warning  Failed                  33s (x3 over 76s)  kubelet                  Failed to pull image "ghcr.io/nathanielnat1993/cloud-computing-project:latest": rpc error: code = NotFound desc = failed to pull and unpack image "ghcr.io/nathanielnat1993/cloud-computing-project:latest": no match for platform in manifest: not found
  Warning  Failed                  33s (x3 over 76s)  kubelet                  Error: ErrImagePull
  Normal   BackOff                 4s (x4 over 76s)   kubelet                  Back-off pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
  Warning  Failed                  4s (x4 over 76s)   kubelet                  Error: ImagePullBackOff
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
is it okay to run it from here? (base) nat-nat@Mac cloud-computing-project % 
[+] Building 136.3s (16/16) FINISHED                       docker:desktop-linux
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 682B                                       0.0s
 => [internal] load metadata for docker.io/pytorch/pytorch:2.3.0-cuda11.8  1.7s
 => [auth] pytorch/pytorch:pull token for registry-1.docker.io             0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [1/8] FROM docker.io/pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime@sh  0.0s
 => => resolve docker.io/pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime@sh  0.0s
 => [internal] load build context                                          0.0s
 => => transferring context: 648B                                          0.0s
 => CACHED [2/8] WORKDIR /project                                          0.0s
 => CACHED [3/8] COPY requirements.txt .                                   0.0s
 => [4/8] RUN pip install --no-cache-dir -r requirements.txt              32.7s
 => [5/8] COPY src/ ./src                                                  0.1s 
 => [6/8] COPY data/ ./data                                                0.0s 
 => [7/8] COPY results/ ./results                                          0.0s 
 => [8/8] RUN mkdir -p /project/results/figures                            0.1s 
 => exporting to image                                                   101.7s 
 => => exporting layers                                                   15.2s 
 => => exporting manifest sha256:e09dac094391236cdad3acd27ce5b833f60e6d8a  0.0s
 => => exporting config sha256:87a4a8fbf1e4788fef80ef5673f179e6c62ce13bc5  0.0s
 => => exporting attestation manifest sha256:ee9b9c385dd175c744445cfe66ab  0.0s
 => => exporting manifest list sha256:c34bb4ae9ff2152c22ead35a8437b031f6e  0.0s
 => => naming to ghcr.io/nathanielnat1993/cloud-computing-project:latest   0.0s
 => => pushing layers                                                     84.3s
 => => pushing manifest for ghcr.io/nathanielnat1993/cloud-computing-proj  2.0s
 => [auth] nathanielnat1993/cloud-computing-project:pull,push token for g  0.0s
 => [auth] nathanielnat1993/cloud-computing-project:pull,push token for g  0.0s
(base) nat-nat@Mac cloud-computing-project % 
why is the old one still saying this. baseline-job-lpbq9                 0/1     Terminating         0          6m50s
did we create this? pvc-checker
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get pods -n gp-engine-mizzou-dsa-cloud
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          4m4s
baseline-job-gzgwt                 0/1     Error       0          16m
baseline-job-lnx8r                 0/1     Error       0          6m55s
baseline-job-mchtz                 0/1     Error       0          9m48s
baseline-job-tc77t                 0/1     Error       0          8m27s
baseline-job-vr5c7                 0/1     Error       0          9m17s
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          9h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          9h
pod-cc5m4-train                    0/1     Error       0          36h
pod-gcfpx-train                    1/1     Running     0          4h47m
pod-name-ljabxf                    1/1     Running     0          4h49m
pod-pvc-jm2rc                      1/1     Running     0          5h39m
pvc-checker                        0/1     Error       0          13h
pvc-explorer                       1/1     Running     0          55m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl logs baseline-job-b668b -n gp-engine-mizzou-dsa-cloud
Traceback (most recent call last):
  File "/project/src/main.py", line 66, in <module>
    main()
  File "/project/src/main.py", line 56, in main
    df = pd.read_parquet("/project/data/df_merged_filtered.parquet")
  File "/opt/conda/lib/python3.10/site-packages/pandas/io/parquet.py", line 669, in read_parquet
    return impl.read(
  File "/opt/conda/lib/python3.10/site-packages/pandas/io/parquet.py", line 265, in read
    pa_table = self.api.parquet.read_table(
  File "/opt/conda/lib/python3.10/site-packages/pyarrow/parquet/core.py", line 1844, in read_table
    dataset = ParquetDataset(
  File "/opt/conda/lib/python3.10/site-packages/pyarrow/parquet/core.py", line 1413, in __init__
    [fragment], schema=schema or fragment.physical_schema,
  File "pyarrow/_dataset.pyx", line 1477, in pyarrow._dataset.Fragment.physical_schema.__get__
  File "pyarrow/error.pxi", line 155, in pyarrow.lib.pyarrow_internal_check_status
  File "pyarrow/error.pxi", line 92, in pyarrow.lib.check_status
pyarrow.lib.ArrowInvalid: Could not open Parquet input source '<Buffer>': Parquet magic bytes not found in footer. Either the file is corrupted or this is not a parquet file.
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
i have the file here it shows 823 mb
do we need to delete the old one first?
erged_filtered.parquet" \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet

E1120 00:58:18.743003   89625 v2.go:129] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
E1120 00:58:18.743021   89625 v2.go:150] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
E1120 00:58:18.743033   89625 v2.go:167] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
error: error reading from error stream: next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout
E1120 00:58:18.744714   89625 v2.go:104] "Unhandled Error" err="write tcp 192.168.1.232:57783->67.58.53.148:443: use of closed network connection"
(base) nat-nat@Mac ~ % 
how do i know how many chuhcks are there
save all our progress right now in memory. right now we're doing this in chunks. ill create a new chat but we're stilll in that process

okay now let's continue with my cloud computing projec. after pasting this. kubectl cp parquet_chunk_aa \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/parquet_chunk_aa how do i know to proceed with the next chunk
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- ls -lh /data
total 67M
-rw------- 1 root root 48M Nov 20 11:04 df_merged_filtered.parquet
-rw------- 1 root root 19M Nov 20 11:04 parquet_chunk_aa
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
but in the terminal mac it says thst chunk is 100mb
well in the terminal it's still not done i think. is this the reason why? (base) nat-nat@Mac data % kubectl cp parquet_chunk_aa \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/parquet_chunk_aa

this is going to take long huh?
total 96M
-rw------- 1 root root 66M Nov 20 11:09 df_merged_filtered.parquet
-rw------- 1 root root 30M Nov 20 11:09 parquet_chunk_aa
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$  is this normal? that there is the df_merged_filtered there and it seems to be growing in size. aren't we doingthe chunks
wait when did we try to cpoy the other one? i thoguht that one failed?
so how are we going to merge the chunks? into a single one?
wait. can't we just upload the one big file then? what was the problem with thst one?
Last login: Thu Nov 20 00:12:58 on ttys000
(base) nat-nat@Mac ~ % kubectl cp "/Users/nat-nat/Desktop/project-root/data/df_merged_filtered.parquet" \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet

E1120 00:58:18.743003   89625 v2.go:129] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
E1120 00:58:18.743021   89625 v2.go:150] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
E1120 00:58:18.743033   89625 v2.go:167] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
error: error reading from error stream: next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout
E1120 00:58:18.744714   89625 v2.go:104] "Unhandled Error" err="write tcp 192.168.1.232:57783->67.58.53.148:443: use of closed network connection"
(base) nat-nat@Mac ~ % cd "/Users/nat-nat/Desktop/project-root/data"
split -b 100m df_merged_filtered.parquet parquet_chunk_ is this the one where we tried ot upload it earlier ?
but remember it didn't fail it was still running? so im confused
but after that timeout it was still growing the size
okay so how do we merge the chunks in the simplest and not edit the code
can i just paste all teh chunk codes in one go? so i dont' have to do it after it's done? kubectl cp parquet_chunk_aa \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/parquet_chunk_ab
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/parquet_chunk_ab
E1120 01:24:47.918638   90353 v2.go:129] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57908->67.58.53.148:443: i/o timeout"
E1120 01:24:47.918662   90353 v2.go:167] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57908->67.58.53.148:443: i/o timeout"
E1120 01:24:47.918660   90353 v2.go:150] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57908->67.58.53.148:443: i/o timeout"
error: error reading from error stream: next reader: read tcp 192.168.1.232:57908->67.58.53.148:443: i/o timeout
do i delete the chunks first
bash: ubectl: command not found
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ ubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- rm /data/parquet_chunk_aa
bash: ubectl: command not found
which folder in nautilus jupyter should i upload it to
okay i uploaded it and it's showing. but does that mean its already uploaded or do i have to wait?
how long would it take? it's 800 mb
okay it's uploaded i think what's next
why it's saying 5mb? -rw-r--r-- 1 1000 users 5.0M Nov 20 11:40 df_merged_filtered.parquet
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- ls -lh /data
total 5.0M
-rw-r--r-- 1 1000 users 5.0M Nov 20 11:40 df_merged_filtered.parquet
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
it[s 785 mb
so on the bottom it says uploading what does that mean
okay so lets remove the one we uploaded to pvc first right? the 5 mb one?
why is it uploadkng slow?
can i refresht the webpage? is it safe?
it doesnt seem to be progressing

before thst. what is this file in jupyter project folder? 67.58.53.148:443:
how long would zipping take?
the zip file is still 700mb
lets try option 2
jupyter-naaxk6-missouri-edu---2351cae4
is this option fast?
(base) nat-nat@Mac data % scp "/Users/nat-nat/Desktop/project-root/data/df_merged_filtered.parquet" \
    naaxk6@login.hpc.missouri.edu:~/
ssh: Could not resolve hostname login.hpc.missouri.edu: nodename nor servname provided, or not known
scp: Connection closed
(base) nat-nat@Mac data % 
(base) nat-nat@Mac data % login.lewis.rnet.missouri.edu

zsh: command not found: login.lewis.rnet.missouri.edu
(base) nat-nat@Mac data % 
zsh: command not found: login.lewis.rnet.missouri.edu
(base) nat-nat@Mac data % ssh naaxk6@login.lewis.rnet.missouri.edu

ssh: Could not resolve hostname login.lewis.rnet.missouri.edu: nodename nor servname provided, or not known
(base) nat-nat@Mac data % 
ssh: Could not resolve hostname login.lewis.rnet.missouri.edu: nodename nor servname provided, or not known
(base) nat-nat@Mac data % ssh.nautilus.optiputer.net

zsh: command not found: ssh.nautilus.optiputer.net
(base) nat-nat@Mac data % ssh naaxk6@ssh.nautilus.optiputer.net

The authenticity of host 'ssh.nautilus.optiputer.net (128.114.109.67)' can't be established.
ED25519 key fingerprint is SHA256:Mt1GttcdLQbNLU3d2MJy5WGPBOBsNrsVw8awcvixTwI.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'ssh.nautilus.optiputer.net' (ED25519) to the list of known hosts.
naaxk6@ssh.nautilus.optiputer.net: Permission denied (publickey).
(base) nat-nat@Mac data % 
You have 16 outdated formulae installed.

Warning: No available formula with the name "jupyter-rsync". Did you mean jupyter-r?
==> Searching for similarly named formulae and casks...
==> Formulae
jupyter-r

To install jupyter-r, run:
  brew install jupyter-r

==> Casks
jupyterlab-app

To install jupyterlab-app, run:
  brew install --cask jupyterlab-app
(base) nat-nat@Mac data % 
https://gp-engine.nrp-nautilus.io/user/naaxk6@missouri.edu/lab/tree/cloud-computing-project. this is the webpage

is this option fast?
which one do i replace with my IP
10.244.189.72
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl port-forward -n gp-engine-mizzou-dsa-cloud pod/pvc-explorer 2222:22
Unable to listen on port 2222: Listeners failed to create with the following errors: [unable to create listener: Error listen tcp4 127.0.0.1:2222: bind: address already in use unable to create listener: Error listen tcp6 [::1]:2222: bind: address already in use]
error: unable to listen on any of the requested ports: [{2222 22}]
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
i mean i did it earlier
i did but i closed it
the file data coudlnt be opened
command not found
(base) nat-nat@Mac ~ % fuser -k 2223/tcp || true

Unknown option: k
fuser: [-cfu] file ...
	-c	file is treated as mount point
	-f	the report is only for the named files
	-u	print username of pid in parenthesis
(base) nat-nat@Mac ~ % 
bash: fuser: command not found
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl port-forward -n gp-engine-mizzou-dsa-cloud pod/pvc-explorer 2223:22
Unable to listen on port 2223: Listeners failed to create with the following errors: [unable to create listener: Error listen tcp4 127.0.0.1:2223: bind: address already in use unable to create listener: Error listen tcp6 [::1]:2223: bind: address already in use]
error: unable to listen on any of the requested ports: [{2223 22}]
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
the file data count'nt be opened again
do i need to stop somethign in my jupyter terminal and mac terminal
Connection to localhost port 2223 [tcp/rockwell-csp3] succeeded!
(base) nat-nat@Mac ~ % ps aux | grep kubectl

nat-nat          93003   0.0  0.0 435300400   1408 s001  S+    2:17AM   0:00.00 grep kubectl
(base) nat-nat@Mac ~ % 
it didn't return anything
(base) nat-nat@Mac ~ % lsof -i :2223

(base) nat-nat@Mac ~ % nc -zv localhost 2223

nc: connectx to localhost port 2223 (tcp) failed: Connection refused
nc: connectx to localhost port 2223 (tcp) failed: Connection refused
(base) nat-nat@Mac ~ % 
what about jupyter terminal. do we need to stop something there too
how do i kill this ress already in use unable to create listener: Error listen tcp6 [::1]:2222: bind: address already in use]
error: unable to listen on any of the requested ports: [{2222 22}]
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl port-forward -n gp-engine-mizzou-dsa-cloud pod/pvc-explorer 2223:22
kubectl port-forward -n gp-engine-mizzou-dsa-cloud pod/pvc-explorer 2223:22
Forwarding from 127.0.0.1:2223 -> 22
Forwarding from [::1]:2223 -> 22
^CForwarding from 127.0.0.1:2223 -> 22
Forwarding from [::1]:2223 -> 22
okay can we just continue this tomorrow? do i need to stop some jobs right now or pods or whatever
can we make sure it's not running something that might get me banned form nrp nautilus for violation of terms
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get jobs -n gp-engine-mizzou-dsa-cloud
NAME                         STATUS     COMPLETIONS   DURATION   AGE
baseline-job                 Failed     0/1           107m       107m
job-ljabxf-mobilenet-train   Complete   1/1           62m        10h
job-ljabxf-resnet18-train    Complete   1/1           169m       10h
job-ljabxf-simpledla-train   Complete   1/1           3h3m       10h
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get pods -n gp-engine-mizzou-dsa-cloud
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          95m
baseline-job-gzgwt                 0/1     Error       0          107m
baseline-job-lnx8r                 0/1     Error       0          97m
baseline-job-mchtz                 0/1     Error       0          100m
baseline-job-tc77t                 0/1     Error       0          99m
baseline-job-v8w89                 0/1     Error       0          89m
baseline-job-vr5c7                 0/1     Error       0          100m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          10h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          10h
pod-cc5m4-train                    0/1     Error       0          38h
pod-gcfpx-train                    0/1     Error       0          6h18m
pod-name-ljabxf                    0/1     Error       0          6h20m
pod-pvc-jm2rc                      0/1     Error       0          7h10m
pvc-checker                        0/1     Error       0          14h
pvc-explorer                       1/1     Running     0          146m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
how do i remove stop the chunk from uploading in jupyter
so im uploading a big file in jupyter. and i need it ot run overnight. would it automatically log out or would i be logged in as long as it's uploading
is thee another way aside form uploading the zip in jupyter? some faster way?
let's try option 1
okay i got several keys. west central etc
what's next after getting my keys
Last login: Thu Nov 20 02:15:49 on ttys001
(base) nat-nat@Mac ~ % aws configure

zsh: command not found: aws
(base) nat-nat@Mac ~ % 
aws-cli/2.32.1 Python/3.13.9 Darwin/25.2.0 source/arm64
(base) nat-nat@Mac ~ % aws configure

AWS Access Key ID [None]: 
i got an access key and secret key. which one do i need ot paste
okay im done. what's next
[default]
region = us-west-1
output = json
s3 =
    endpoint_url = http://cilogon.org/serverF/users/406832
(base) nat-nat@Mac ~ % aws s3 ls


An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.
(base) nat-nat@Mac ~ % 
West pool (default)	http://rook-ceph-rgw-nautiluss3.rook	https://s3-west.nrp-nautilus.io
An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.
(base) nat-nat@Mac ~ % nano ~/.aws/config

(base) nat-nat@Mac ~ % aws s3 ls


An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.
(base) nat-nat@Mac ~ % 
Pool	Inside endpoint	Outside endpoint
West pool (default)	http://rook-ceph-rgw-nautiluss3.rook	https://s3-west.nrp-nautilus.io which endpoint sould i be using?
is the default region name can be anything?
it says in my key westpool
its still doing this. AWS Access Key ID [****************4KF5]: R0ZXCEPSM6OBSGBX4KF5
AWS Secret Access Key [****************m7JA]: SB6JBk2Y1nCWFY4FV5qFCt7RzBp262CzIoZ6m7JA
Default region name [us-west-1]: us-west-1
Default output format [json]: json
(base) nat-nat@Mac ~ % nano ~/.aws/config

(base) nat-nat@Mac ~ % aws s3 ls


An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.
(base) nat-nat@Mac ~ % 


Pool west username: http://cilogon.org/serverF/users/406832
Pool west access key: R0ZXCEPSM6OBSGBX4KF5
Pool west secret key: SB6JBk2Y1nCWFY4FV5qFCt7RzBp262CzIoZ6m7JA
theres nothing. https://nrp.ai
(base) nat-nat@Mac ~ % curl --upload-file df_merged_filtered.parquet https://transfer.sh/df_merged_filtered.parquet

curl: cannot open 'df_merged_filtered.parquet'
curl: try 'curl --help' or 'curl --manual' for more information
curl: (26) Failed to open/read local data from file/application
(base) nat-nat@Mac ~ % 
(base) nat-nat@Mac data % curl --upload-file df_merged_filtered.parquet https://transfer.sh/df_merged_filtered.parquet

curl: (7) Failed to connect to transfer.sh port 443 after 696 ms: Could not connect to server
(base) nat-nat@Mac data % 
how long would the upload take?
curl: (7) Failed to connect to transfer.sh port 443 after 696 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://file.io

curl: (16) Error in the HTTP2 framing layer
(base) nat-nat@Mac data % 
(base) nat-nat@Mac data % curl -T df_merged_filtered.parquet https://bashupload.com/df_merged_filtered.parquet

curl: (7) Failed to connect to bashupload.com port 443 after 540 ms: Could not connect to server
(base) nat-nat@Mac data % 

-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_ac
-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_ad
-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_ae
-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_af
-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_ag
-rw-r--r--  1 nat-nat  staff    85M Nov 20 00:59 parquet_chunk_ah
-rw-r--r--@ 1 nat-nat  staff   1.2K Nov 19 01:08 README.md
(base) nat-nat@Mac data % curl --upload-file df_merged_filtered.parquet https://transfer.sh/df_merged_filtered.parquet

curl: (7) Failed to connect to transfer.sh port 443 after 696 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://file.io

curl: (16) Error in the HTTP2 framing layer
(base) nat-nat@Mac data % curl -T df_merged_filtered.parquet https://bashupload.com/df_merged_filtered.parquet

curl: (7) Failed to connect to bashupload.com port 443 after 540 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://oshi.at

curl: (60) SSL certificate problem: self-signed certificate
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the webpage mentioned above.
(base) nat-nat@Mac data % 
curl: (7) Failed to connect to transfer.sh port 443 after 696 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://file.io

curl: (16) Error in the HTTP2 framing layer
(base) nat-nat@Mac data % curl -T df_merged_filtered.parquet https://bashupload.com/df_merged_filtered.parquet

curl: (7) Failed to connect to bashupload.com port 443 after 540 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://oshi.at
would kt help if i connect to the school vpn?
im uploading the file in jupytre is there a way to check the status of the download using kubectl?
okay save all our progress for now in memory im gonna start a new chat

ChatGPT can make mistakes. Ch

okay so i uploaded the paruqt in jupyter. now how do we get it to our pvc
Error from server (Forbidden): persistentvolumeclaims is forbidden: User "http://cilogon.org/serverF/users/406832" cannot list resource "persistentvolumeclaims" in API group "" in the namespace "default"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
do you remember everthign whre wer stoppd previously
remember we have to do gp-engine-mizzou etc. so it doesn give the error,. and you aslo know hte name of our explorer pvc adn pvc name
no! do you even remember! kubectl -n gp-engine-mizzou-dsa-cloud get pods!
and the name is pvc_explorer! y
omg what is so wrong with you . the name of the parquet file is df_merged_filtered not nrd_preprocessed! i thouhgt you saved everyting in memory!!
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f kubernetes/pvc-explorer.yaml
error: the path "kubernetes/pvc-explorer.yaml" does not exist
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
pod/pvc-explorer configured
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          5h56m
baseline-job-gzgwt                 0/1     Error       0          6h9m
baseline-job-lnx8r                 0/1     Error       0          5h59m
baseline-job-mchtz                 0/1     Error       0          6h2m
baseline-job-tc77t                 0/1     Error       0          6h1m
baseline-job-v8w89                 0/1     Error       0          5h51m
baseline-job-vr5c7                 0/1     Error       0          6h2m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          14h
pod-cc5m4-train                    0/1     Error       0          42h
pod-dbkyd-train                    1/1     Running     0          4h21m
pod-gcfpx-train                    0/1     Error       0          10h
pod-name-ljabxf                    0/1     Error       0          10h
pod-pvc-jm2rc                      0/1     Error       0          11h
pvc-checker                        0/1     Error       0          18h
pvc-explorer                       0/1     Error       0          6h48m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$  what's going on
no that's not my pvc-explorer! my pvc exploreer name is pvc_explorer not pvc-explorer
oh wait this is my original one. apiVersion: v1
kind: Pod
metadata:
  name: pvc-explorer
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  containers:
  - name: explorer
    image: ubuntu:20.04
    command: ["sleep", "infinity"]
    volumeMounts:
    - mountPath: /data
      name: project-storage
  volumes:
  - name: project-storage
    persistentVolumeClaim:
      claimName: naaxk6-pvc the yaml name is pvc_explorer
what is going on here. See "man sudo_root" for details.
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f pvc_explorer.yaml -n gp-engine-mizzou-dsa-cloud
pod/pvc-explorer configured
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          6h5m
baseline-job-gzgwt                 0/1     Error       0          6h17m
baseline-job-lnx8r                 0/1     Error       0          6h8m
baseline-job-mchtz                 0/1     Error       0          6h10m
baseline-job-tc77t                 0/1     Error       0          6h9m
baseline-job-v8w89                 0/1     Error       0          5h59m
baseline-job-vr5c7                 0/1     Error       0          6h10m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          15h
pod-cc5m4-train                    0/1     Error       0          42h
pod-dbkyd-train                    1/1     Running     0          4h29m
pod-gcfpx-train                    0/1     Error       0          10h
pod-name-ljabxf                    0/1     Error       0          10h
pod-pvc-jm2rc                      0/1     Error       0          11h
pvc-checker                        0/1     Error       0          19h
pvc-explorer                       0/1     Error       0          6h56m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer
Name:             pvc-explorer
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             gpengine-uark.areon.net/208.90.105.170
Start Time:       Thu, 20 Nov 2025 09:57:02 +0000
Labels:           <none>
Annotations:      cni.projectcalico.org/containerID: 718a0f854cc86c3d4945b46ab6ab657f345179d35f6eb2153444342a6e0c7dee
                  cni.projectcalico.org/podIP: 
                  cni.projectcalico.org/podIPs: 
                  kubernetes.io/limit-ranger: LimitRanger plugin set: cpu, memory request for container explorer; cpu, memory limit for container explorer
                  nrp.ai/username: http://cilogon.org/serverF/users/406832
Status:           Failed
Reason:           DeadlineExceeded
Message:          Pod was active on the node longer than the specified deadline
IP:               10.244.189.72
IPs:
  IP:  10.244.189.72
Containers:
  explorer:
    Container ID:  containerd://bc7b2bc1dc1a7ae4e154b8eacfcd8e85f8e53a31030d40059c75a7599c356904
    Image:         ubuntu:20.04
    Image ID:      docker.io/library/ubuntu@sha256:8feb4d8ca5354def3d8fce243717141ce31e2c428701f6682bd2fafe15388214
    Port:          <none>
    Host Port:     <none>
    Command:
      sleep
      infinity
    State:          Terminated
      Reason:       Error
      Exit Code:    137
      Started:      Thu, 20 Nov 2025 09:57:24 +0000
      Finished:     Thu, 20 Nov 2025 15:57:33 +0000
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  1Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-96mln (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-96mln:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason            Age                From     Message
  ----    ------            ----               ----     -------
  Normal  Killing           57m                kubelet  Stopping container explorer
  Normal  DeadlineExceeded  56m (x4 over 57m)  kubelet  Pod was active on the node longer than the specified deadline
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
no wait. does that mean we can't use the job anymore?
im so confused. so how are we going ot run my pvc explorer yaml file and the job
  Normal  DeadlineExceeded  56m (x4 over 57m)  kubelet  Pod was active on the node longer than the specified deadline
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f pvc_explorer.yaml -n gp-engine-mizzou-dsa-cloud
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no resource limits
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no resource requests
Error from server (Forbidden): error when creating "pvc_explorer.yaml": admission webhook "validation.gatekeeper.sh" denied the request: [container-must-have-limits-and-requests] container <explorer> does not have <{"cpu", "memory"}> requests defined
[container-must-have-limits-and-requests] container <explorer> does not have <{"memory"}> limits defined
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
[container-must-have-limits-and-requests] container <explorer> does not have <{"memory"}> limits defined
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f pvc_explorer.yaml -n gp-engine-mizzou-dsa-cloud
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> memory limit <2Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/pvc-explorer created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
is project-storage in my original code? - name: project-storage
how come the name is different now.pvc-explorer-g8prl 
okay so what's next to put the parquet in the pvc
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud cp /home/jovyan/cloud-computing-project/data/df_merged_filtered.parquet pvc-explorer-g8prl:/data/
error: /home/jovyan/cloud-computing-project/data/df_merged_filtered.parquet doesn't exist in local filesystem
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ cd /home/jovyan/cloud-computing-project
ls -lh
total 886M
drwxr-sr-x 3 jovyan users   49 Nov 19 11:13 data
-rw-r--r-- 1 jovyan users 786M Nov 20 16:33 df_merged_filtered.parquet
-rw-r--r-- 1 jovyan users  643 Nov 20 03:54 Dockerfile
drwxr-sr-x 2 jovyan users   62 Nov 19 09:05 docs
drwxr-sr-x 3 jovyan users   98 Nov 20 16:58 kubernetes
-rw-r--r-- 1 jovyan users 100M Nov 20 12:21 parquet_chunk_aa
-rw-r--r-- 1 jovyan users 1.9K Nov 20 09:13 README.md
-rw-r--r-- 1 jovyan users   99 Nov 19 11:00 requirements.txt
drwxr-sr-x 4 jovyan users  109 Nov 19 11:13 results
drwxr-sr-x 2 jovyan users  191 Nov 20 03:54 src
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud cp /home/jovyan/cloud-computing-project/df_merged_filtered.parquet pvc-explorer-g8prl:/data/
E1120 17:04:23.988748   13085 v2.go:129] "Unhandled Error" err="next reader: read tcp 10.244.189.108:43714->67.58.53.148:443: i/o timeout"
E1120 17:04:23.988751   13085 v2.go:167] "Unhandled Error" err="next reader: read tcp 10.244.189.108:43714->67.58.53.148:443: i/o timeout"
E1120 17:04:23.988764   13085 v2.go:150] "Unhandled Error" err="next reader: read tcp 10.244.189.108:43714->67.58.53.148:443: i/o timeout"
E1120 17:04:23.990103   13085 v2.go:104] "Unhandled Error" err="write tcp 10.244.189.108:43714->67.58.53.148:443: use of closed network connection"
error: error reading from error stream: next reader: read tcp 10.244.189.108:43714->67.58.53.148:443: i/o timeout
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud cp --retries=10 /home/jovyan/cloud-computing-project/df_merged_filtered.parquet pvc-explorer-g8prl:/data/
error: context deadline exceeded
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud cp --retries=10 /home/jovyan/cloud-computing-project/df_merged_filtered.parquet pvc-explorer-g8prl:/data/
error: context deadline exceeded
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ cd /home/jovyan/cloud-computing-project
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ tar cf - df_merged_filtered.parquet | kubectl -n gp-engine-mizzou-dsa-cloud exec -i pvc-explorer-g8prl -- tar xf - -C /data
E1120 17:07:30.541871   13167 v2.go:167] "Unhandled Error" err="next reader: read tcp 10.244.189.108:50048->67.58.53.148:443: i/o timeout"
E1120 17:07:30.541896   13167 v2.go:129] "Unhandled Error" err="next reader: read tcp 10.244.189.108:50048->67.58.53.148:443: i/o timeout"
E1120 17:07:30.541904   13167 v2.go:150] "Unhandled Error" err="next reader: read tcp 10.244.189.108:50048->67.58.53.148:443: i/o timeout"
E1120 17:07:30.543073   13167 v2.go:104] "Unhandled Error" err="write tcp 10.244.189.108:50048->67.58.53.148:443: use of closed network connection"
E1120 17:07:30.543097   13167 websocket.go:500] Websocket Ping failed: write tcp 10.244.189.108:50048->67.58.53.148:443: use of closed network connection
error: error reading from error stream: next reader: read tcp 10.244.189.108:50048->67.58.53.148:443: i/o timeout
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
will using rthe school vpn work
when i do get pods the status is completed. is that okay?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud delete job pvc-explorer
kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
job.batch "pvc-explorer" deleted
error: the path "pvc_explorer.yaml" does not exist
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> memory limit <2Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/pvc-explorer created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
do we delete the old pvc-explorere that failed?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-b668b                 0/1     Error               0          6h24m
baseline-job-gzgwt                 0/1     Error               0          6h36m
baseline-job-lnx8r                 0/1     Error               0          6h26m
baseline-job-mchtz                 0/1     Error               0          6h29m
baseline-job-tc77t                 0/1     Error               0          6h28m
baseline-job-v8w89                 0/1     Error               0          6h18m
baseline-job-vr5c7                 0/1     Error               0          6h29m
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          15h
pod-cc5m4-train                    0/1     Error               0          42h
pod-dbkyd-train                    1/1     Running             0          4h48m
pod-gcfpx-train                    0/1     Error               0          11h
pod-name-ljabxf                    0/1     Error               0          11h
pod-pvc-jm2rc                      0/1     Error               0          11h
pvc-checker                        0/1     Error               0          19h
pvc-explorer                       0/1     Error               0          7h15m
pvc-explorer-f57fg                 0/1     ContainerCreating   0          42s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud delete job pvc-explorer --ignore-not-found=true
job.batch "pvc-explorer" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
it's still there! plus my new one is terminating! jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS        RESTARTS   AGE
baseline-job-b668b                 0/1     Error         0          6h25m
baseline-job-gzgwt                 0/1     Error         0          6h37m
baseline-job-lnx8r                 0/1     Error         0          6h28m
baseline-job-mchtz                 0/1     Error         0          6h31m
baseline-job-tc77t                 0/1     Error         0          6h29m
baseline-job-v8w89                 0/1     Error         0          6h19m
baseline-job-vr5c7                 0/1     Error         0          6h30m
job-ljabxf-resnet18-train-qbksm    0/1     Completed     0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed     0          15h
pod-cc5m4-train                    0/1     Error         0          42h
pod-dbkyd-train                    1/1     Running       0          4h50m
pod-ecc7r-train                    1/1     Running       0          17s
pod-gcfpx-train                    0/1     Error         0          11h
pod-name-ljabxf                    0/1     Error         0          11h
pod-pvc-jm2rc                      0/1     Error         0          12h
pvc-checker                        0/1     Error         0          19h
pvc-explorer                       0/1     Error         0          7h17m
pvc-explorer-f57fg                 0/1     Terminating   0          2m6s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 

jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS        RESTARTS   AGE
baseline-job-b668b                 0/1     Error         0          6h26m
baseline-job-gzgwt                 0/1     Error         0          6h39m
baseline-job-lnx8r                 0/1     Error         0          6h29m
baseline-job-mchtz                 0/1     Error         0          6h32m
baseline-job-tc77t                 0/1     Error         0          6h31m
baseline-job-v8w89                 0/1     Error         0          6h21m
baseline-job-vr5c7                 0/1     Error         0          6h32m
job-ljabxf-resnet18-train-qbksm    0/1     Completed     0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed     0          15h
pod-cc5m4-train                    0/1     Error         0          42h
pod-dbkyd-train                    1/1     Running       0          4h51m
pod-ecc7r-train                    1/1     Running       0          104s
pod-gcfpx-train                    0/1     Error         0          11h
pod-name-ljabxf                    0/1     Error         0          11h
pod-pvc-jm2rc                      0/1     Error         0          12h
pvc-checker                        0/1     Error         0          19h
pvc-explorer-f57fg                 0/1     Terminating   0          3m33s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-b668b                 0/1     Error               0          6h29m
baseline-job-gzgwt                 0/1     Error               0          6h41m
baseline-job-lnx8r                 0/1     Error               0          6h32m
baseline-job-mchtz                 0/1     Error               0          6h35m
baseline-job-tc77t                 0/1     Error               0          6h33m
baseline-job-v8w89                 0/1     Error               0          6h23m
baseline-job-vr5c7                 0/1     Error               0          6h34m
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          15h
pod-cc5m4-train                    0/1     Error               0          43h
pod-dbkyd-train                    1/1     Running             0          4h54m
pod-ecc7r-train                    1/1     Running             0          4m4s
pod-gcfpx-train                    0/1     Error               0          11h
pod-name-ljabxf                    0/1     Error               0          11h
pod-pvc-jm2rc                      0/1     Error               0          12h
pvc-checker                        0/1     Error               0          19h
pvc-explorer-c7lzj                 0/1     ContainerCreating   0          88s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-c7lzj
Name:             pvc-explorer-c7lzj
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-haosu-16.sdsc.optiputer.net/67.58.63.15
Start Time:       Thu, 20 Nov 2025 17:16:38 +0000
Labels:           batch.kubernetes.io/controller-uid=ae5de04a-6d5b-4af8-aa13-de1f8a46a996
                  batch.kubernetes.io/job-name=pvc-explorer
                  controller-uid=ae5de04a-6d5b-4af8-aa13-de1f8a46a996
                  job-name=pvc-explorer
Annotations:      cni.projectcalico.org/containerID: cd504c6725b6b39ebfb8e303f36b17b8f5a99fac1d20a30bff348a6c9b7a6a9a
                  cni.projectcalico.org/podIP: 10.244.206.141/32
                  cni.projectcalico.org/podIPs: 10.244.206.141/32,fdf0:17b3:c3ec:1f79:10:0:7:60a9/128
                  kubernetes.io/limit-ranger: LimitRanger plugin set: cpu limit for container explorer
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/pvc-explorer
Containers:
  explorer:
    Container ID:  
    Image:         ubuntu:22.04
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      bash
      -c
      sleep 600
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  2Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-g6fsv (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-g6fsv:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m53s  default-scheduler  Successfully assigned gp-engine-mizzou-dsa-cloud/pvc-explorer-c7lzj to k8s-haosu-16.sdsc.optiputer.net
  Normal  Pulling    2m48s  kubelet            Pulling image "ubuntu:22.04"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
what's teh different betweeen my old pvc_explorer code and this one with ubuntu. i think the old one didn't include it
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-c7lzj
Name:             pvc-explorer-c7lzj
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-haosu-16.sdsc.optiputer.net/67.58.63.15
Start Time:       Thu, 20 Nov 2025 17:16:38 +0000
Labels:           batch.kubernetes.io/controller-uid=ae5de04a-6d5b-4af8-aa13-de1f8a46a996
                  batch.kubernetes.io/job-name=pvc-explorer
                  controller-uid=ae5de04a-6d5b-4af8-aa13-de1f8a46a996
                  job-name=pvc-explorer
Annotations:      cni.projectcalico.org/containerID: cd504c6725b6b39ebfb8e303f36b17b8f5a99fac1d20a30bff348a6c9b7a6a9a
                  cni.projectcalico.org/podIP: 10.244.206.141/32
                  cni.projectcalico.org/podIPs: 10.244.206.141/32,fdf0:17b3:c3ec:1f79:10:0:7:60a9/128
                  kubernetes.io/limit-ranger: LimitRanger plugin set: cpu limit for container explorer
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/pvc-explorer
Containers:
  explorer:
    Container ID:  
    Image:         ubuntu:22.04
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      bash
      -c
      sleep 600
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  2Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-g6fsv (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-g6fsv:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  6m47s  default-scheduler  Successfully assigned gp-engine-mizzou-dsa-cloud/pvc-explorer-c7lzj to k8s-haosu-16.sdsc.optiputer.net
  Normal  Pulling    6m42s  kubelet            Pulling image "ubuntu:22.04"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-qdltj | grep Node:
Node:             k8s-haosu-16.sdsc.optiputer.net/67.58.63.15
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
do we need to edit the yaml file since its giving this warning? Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> memory limit <2Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/pvc-explorer created
I don't want to get banned. some of my classmates got banned
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-n77pj
Name:             pvc-explorer-n77pj
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-haosu-05.sdsc.optiputer.net/67.58.63.7
Start Time:       Thu, 20 Nov 2025 17:31:27 +0000
Labels:           batch.kubernetes.io/controller-uid=540e9d5a-8fa5-449a-b8cc-742d7cad1eb6
                  batch.kubernetes.io/job-name=pvc-explorer
                  controller-uid=540e9d5a-8fa5-449a-b8cc-742d7cad1eb6
                  job-name=pvc-explorer
Annotations:      cni.projectcalico.org/containerID: 4164f13a0cebfb628743f02496b2510720477ee7573fdcdb1672c6f1606a7c0a
                  cni.projectcalico.org/podIP: 10.244.107.131/32
                  cni.projectcalico.org/podIPs: 10.244.107.131/32,fdf0:17b3:c3ec:1f79:10:0:a:6dca/128
                  kubernetes.io/limit-ranger: LimitRanger plugin set: cpu limit for container explorer
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/pvc-explorer
Containers:
  explorer:
    Container ID:  
    Image:         ubuntu:22.04
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      bash
      -c
      sleep 600
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  2Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-g685b (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-g685b:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason                  Age   From                     Message
  ----    ------                  ----  ----                     -------
  Normal  Scheduled               40s   default-scheduler        Successfully assigned gp-engine-mizzou-dsa-cloud/pvc-explorer-n77pj to k8s-haosu-05.sdsc.optiputer.net
  Normal  SuccessfulAttachVolume  40s   attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-d64c959a-1fdb-4774-95aa-f6e337f1fc1a"
  Normal  Pulling                 33s   kubelet                  Pulling image "ubuntu:22.04"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> memory limit <2Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/pvc-explorer created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          6h45m
baseline-job-gzgwt                 0/1     Error       0          6h58m
baseline-job-lnx8r                 0/1     Error       0          6h48m
baseline-job-mchtz                 0/1     Error       0          6h51m
baseline-job-tc77t                 0/1     Error       0          6h50m
baseline-job-v8w89                 0/1     Error       0          6h40m
baseline-job-vr5c7                 0/1     Error       0          6h50m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          15h
pod-cc5m4-train                    0/1     Error       0          43h
pod-dbkyd-train                    1/1     Running     0          5h10m
pod-ecc7r-train                    1/1     Running     0          20m
pod-gcfpx-train                    0/1     Error       0          11h
pod-name-ljabxf                    0/1     Error       0          11h
pod-pvc-jm2rc                      0/1     Error       0          12h
pvc-checker                        0/1     Error       0          19h
pvc-explorer-m484g                 0/1     Pending     0          29s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-m484g | grep Node:
Node:             <none>
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-m484g
Name:             pvc-explorer-m484g
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             <none>
Labels:           batch.kubernetes.io/controller-uid=1c360f4e-1128-4b0c-9ed8-9860c010371d
                  batch.kubernetes.io/job-name=pvc-explorer
                  controller-uid=1c360f4e-1128-4b0c-9ed8-9860c010371d
                  job-name=pvc-explorer
Annotations:      kubernetes.io/limit-ranger: LimitRanger plugin set: cpu limit for container explorer
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/pvc-explorer
Containers:
  explorer:
    Image:      ubuntu:22.04
    Port:       <none>
    Host Port:  <none>
    Command:
      bash
      -c
      sleep 600
    Limits:
      cpu:     100m
      memory:  2Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wj9q4 (ro)
Conditions:
  Type           Status
  PodScheduled   False 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-wj9q4:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              nautilus.io/school=uark
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  82s   default-scheduler  0/521 nodes are available: 1 node(s) had untolerated taint {nautilus.io/issue: 1149}, 1 node(s) had untolerated taint {nautilus.io/issue: 1257}, 1 node(s) had untolerated taint {nautilus.io/issue: 1348}, 1 node(s) had untolerated taint {nautilus.io/issue: 1350}, 1 node(s) had untolerated taint {nautilus.io/issue: 1376}, 1 node(s) had untolerated taint {nautilus.io/issue: 1384}, 1 node(s) had untolerated taint {nautilus.io/issue: 1452}, 1 node(s) had untolerated taint {nautilus.io/issue: 1476}, 1 node(s) had untolerated taint {nautilus.io/issue: 1477}, 1 node(s) had untolerated taint {nautilus.io/issue: 1478}, 1 node(s) had untolerated taint {nautilus.io/issue: slow-network}, 1 node(s) had untolerated taint {nautilus.io/issue: testing}, 1 node(s) had untolerated taint {nautilus.io/reservation: csusb-cousins-lab}, 1 node(s) had untolerated taint {nautilus.io/reservation: hdr-ml-challenge}, 1 node(s) had untolerated taint {nautilus.io/reservation: internet2}, 1 node(s) had untolerated taint {nautilus.io/rese ...
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
give me the whole updated yaml file
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-mqhdf | grep Node:
Node:             k8s-haosu-16.sdsc.optiputer.net/67.58.63.15
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
this is the yaml. apiVersion: batch/v1
kind: Job
metadata:
  name: pvc-explorer
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  backoffLimit: 0
  template:
    spec:
      restartPolicy: Never
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/hostname
                operator: NotIn
                values:
                  - k8s-haosu-01
                  - k8s-haosu-02
                  - k8s-haosu-03
                  - k8s-haosu-04
                  - k8s-haosu-05
                  - k8s-haosu-06
                  - k8s-haosu-07
                  - k8s-haosu-16
      containers:
      - name: explorer
        image: ubuntu:22.04
        command: ["bash", "-c", "sleep 600"]

        volumeMounts:
        - name: project-storage
          mountPath: /data
        resources:
          requests:
            cpu: 100m
            memory: 1Gi
          limits:
            cpu: 200m
            memory: 2Gi
      volumes:
      - name: project-storage
        persistentVolumeClaim:
          claimName: naaxk6-pvc
give me the updated yaml without any spaces or comments
pvc-explorer-lcj8g                 1/1     Running       0          16s
pvc-explorer-mqhdf                 0/1     Terminating   0          3m33s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
Node:             gpn-fiona.usd.edu/206.209.0.13
i already split them. what's next
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-lcj8g | grep Node:
Node:             gpn-fiona.usd.edu/206.209.0.13
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ cd /home/jovyan/cloud-computing-project/
for f in parquet_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-lcj8g:/data/
done
error: parquet_chunk_* doesn't exist in local filesystem
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
the chunkcs are named df_chunk_
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ cd /home/jovyan/cloud-computing-project/
for f in df_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-lcj8g:/data/
done should i just wait?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ cd /home/jovyan/cloud-computing-project/
for f in parquet_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-lcj8g:/data/
done
error: parquet_chunk_* doesn't exist in local filesystem
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ cd /home/jovyan/cloud-computing-project/
for f in df_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-lcj8g:/data/
done
command terminated with exit code 137
E1120 17:51:14.539160   16573 v2.go:104] "Unhandled Error" err="write tcp 10.244.189.108:53876->67.58.53.148:443: write: broken pipe"
error: Internal error occurred: unable to upgrade connection: container not found ("explorer")
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
pvc-explorer-mqhdf                 0/1     Terminating   0          18m i wanna delete this one first
pvc-explorer-mqhdf                 0/1     Terminating   0          19m it's still there
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
error: the path "pvc_explorer.yaml" does not exist
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-b668b                 0/1     Error               0          7h10m
baseline-job-gzgwt                 0/1     Error               0          7h23m
baseline-job-lnx8r                 0/1     Error               0          7h13m
baseline-job-mchtz                 0/1     Error               0          7h16m
baseline-job-tc77t                 0/1     Error               0          7h15m
baseline-job-v8w89                 0/1     Error               0          7h5m
baseline-job-vr5c7                 0/1     Error               0          7h15m
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          16h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          16h
pod-cc5m4-train                    0/1     Error               0          43h
pod-dbkyd-train                    1/1     Running             0          5h35m
pod-gcfpx-train                    0/1     Error               0          11h
pod-name-ljabxf                    0/1     Error               0          11h
pod-pvc-jm2rc                      0/1     Error               0          12h
pvc-checker                        0/1     Error               0          20h
pvc-explorer-j4mzd                 0/1     ContainerCreating   0          32s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-j4mzd | grep Node:
Node:             k8s-haosu-15.sdsc.optiputer.net/67.58.63.14
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pod pvc-explorer-j4mzd -o yaml | grep -A20 affinity
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: NotIn
            values:
            - k8s-haosu-01
            - k8s-haosu-02
            - k8s-haosu-03
            - k8s-haosu-04
            - k8s-haosu-05
            - k8s-haosu-06
            - k8s-haosu-07
            - k8s-haosu-16
  containers:
  - command:
    - bash
    - -c
    - sleep 36000
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud delete pod pvc-checker --force --grace-period=0 --wait=false
Warning: Immediate deletion does not wait for confirmation that the running resource has been terminated. The resource may continue to run on the cluster indefinitely.
pod "pvc-checker" force deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
Error from server (BadRequest): error when creating "pvc_explorer.yaml": Job in version "v1" cannot be handled as a Job: json: cannot unmarshal string into Go struct field Volume.spec.template.spec.volumes.persistentVolumeClaim of type v1.PersistentVolumeClaimVolumeSource
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS              RESTARTS   AGE
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          16h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          16h
pod-cc5m4-train                    0/1     Error               0          43h
pod-dbkyd-train                    1/1     Running             0          5h44m
pod-gcfpx-train                    0/1     Error               0          12h
pod-name-ljabxf                    0/1     Error               0          12h
pod-pvc-jm2rc                      0/1     Error               0          12h
pvc-explorer-g46qp                 0/1     ContainerCreating   0          14s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-g46qp | grep Node:
Node:             k8s-haosu-15.sdsc.optiputer.net/67.58.63.14
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
k8s-haosu-15.sdsc.optiputer.net   Ready    <none>   5y310d   v1.31.12   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,cpu-feature.node.kubevirt.io/3dnowprefetch=true,cpu-feature.node.kubevirt.io/abm=true,cpu-feature.node.kubevirt.io/adx=true,cpu-feature.node.kubevirt.io/aes=true,cpu-feature.node.kubevirt.io/amd-ssbd=true,cpu-feature.node.kubevirt.io/amd-stibp=true,cpu-feature.node.kubevirt.io/apic=true,cpu-feature.node.kubevirt.io/arat=true,cpu-feature.node.kubevirt.io/arch-capabilities=true,cpu-feature.node.kubevirt.io/avx2=true,cpu-feature.node.kubevirt.io/avx512bw=true,cpu-feature.node.kubevirt.io/avx512cd=true,cpu-feature.node.kubevirt.io/avx512dq=true,cpu-feature.node.kubevirt.io/avx512f=true,cpu-feature.node.kubevirt.io/avx512vl=true,cpu-feature.node.kubevirt.io/avx512vnni=true,cpu-feature.node.kubevirt.io/avx=true,cpu-feature.node.kubevirt.io/bmi1=true,cpu-feature.node.kubevirt.io/bmi2=true,cpu-feature.node.kubevirt.io/clflush=true,cpu-feature.node.kubevirt.io/clflushopt=true,cpu-feature.node.kubevirt.io/clwb=true,cpu-feature.node.kubevirt.io/cmov=true,cpu-feature.node.kubevirt.io/cx16=true,cpu-feature.node.kubevirt.io/cx8=true,cpu-feature.node.kubevirt.io/de=true,cpu-feature.node.kubevirt.io/erms=true,cpu-feature.node.kubevirt.io/f16c=true,cpu-feature.node.kubevirt.io/fb-clear=true,cpu-feature.node.kubevirt.io/flush-l1d=true,cpu-feature.node.kubevirt.io/fma=true,cpu-feature.node.kubevirt.io/fpu=true,cpu-feature.node.kubevirt.io/fsgsbase=true,cpu-feature.node.kubevirt.io/fxsr=true,cpu-feature.node.kubevirt.io/gds-no=true,cpu-feature.node.kubevirt.io/hypervisor=true,cpu-feature.node.kubevirt.io/ibpb=true,cpu-feature.node.kubevirt.io/ibrs-all=true,cpu-feature.node.kubevirt.io/ibrs=true,cpu-feature.node.kubevirt.io/invpcid=true,cpu-feature.node.kubevirt.io/invtsc=true,cpu-feature.node.kubevirt.io/lahf_lm=true,cpu-feature.node.kubevirt.io/lm=true,cpu-feature.node.kubevirt.io/mca=true,cpu-feature.node.kubevirt.io/mce=true,cpu-feature.node.kubevirt.io/md-clear=true,cpu-feature.node.kubevirt.io/mds-no=true,cpu-feature.node.kubevirt.io/mmx=true,cpu-feature.node.kubevirt.io/movbe=true,cpu-feature.node.kubevirt.io/mpx=true,cpu-feature.node.kubevirt.io/msr=true,cpu-feature.node.kubevirt.io/mtrr=true,cpu-feature.node.kubevirt.io/nx=true,cpu-feature.node.kubevirt.io/pae=true,cpu-feature.node.kubevirt.io/pat=true,cpu-feature.node.kubevirt.io/pcid=true,cpu-feature.node.kubevirt.io/pclmuldq=true,cpu-feature.node.kubevirt.io/pdcm=true,cpu-feature.node.kubevirt.io/pdpe1gb=true,cpu-feature.node.kubevirt.io/pge=true,cpu-feature.node.kubevirt.io/pku=true,cpu-feature.node.kubevirt.io/pni=true,cpu-feature.node.kubevirt.io/popcnt=true,cpu-feature.node.kubevirt.io/pschange-mc-no=true,cpu-feature.node.kubevirt.io/psdp-no=true,cpu-feature.node.kubevirt.io/pse36=true,cpu-feature.node.kubevirt.io/pse=true,cpu-feature.node.kubevirt.io/rdctl-no=true,cpu-feature.node.kubevirt.io/rdrand=true,cpu-feature.node.kubevirt.io/rdseed=true,cpu-feature.node.kubevirt.io/rdtscp=true,cpu-feature.node.kubevirt.io/rfds-no=true,cpu-feature.node.kubevirt.io/sbdr-ssdp-no=true,cpu-feature.node.kubevirt.io/sep=true,cpu-feature.node.kubevirt.io/skip-l1dfl-vmentry=true,cpu-feature.node.kubevirt.io/smap=true,cpu-feature.node.kubevirt.io/smep=true,cpu-feature.node.kubevirt.io/spec-ctrl=true,cpu-feature.node.kubevirt.io/ss=true,cpu-feature.node.kubevirt.io/ssbd=true,cpu-feature.node.kubevirt.io/sse2=true,cpu-feature.node.kubevirt.io/sse4.1=true,cpu-feature.node.kubevirt.io/sse4.2=true,cpu-feature.node.kubevirt.io/sse=true,cpu-feature.node.kubevirt.io/ssse3=true,cpu-feature.node.kubevirt.io/stibp=true,cpu-feature.node.kubevirt.io/syscall=true,cpu-feature.node.kubevirt.io/tsc-deadline=true,cpu-feature.node.kubevirt.io/tsc=true,cpu-feature.node.kubevirt.io/tsc_adjust=true,cpu-feature.node.kubevirt.io/tsx-ctrl=true,cpu-feature.node.kubevirt.io/umip=true,cpu-feature.node.kubevirt.io/vme=true,cpu-feature.node.kubevirt.io/vmx-activity-hlt=true,cpu-feature.node.kubevirt.io/vmx-activity-wait-sipi=true,cpu-feature.node.kubevirt.io/vmx-apicv-register=true,cpu-feature.node.kubevirt.io/vmx-apicv-vid=true,cpu-feature.node.kubevirt.io/vmx-apicv-x2apic=true,cpu-feature.node.kubevirt.io/vmx-apicv-xapic=true,cpu-feature.node.kubevirt.io/vmx-cr3-load-noexit=true,cpu-feature.node.kubevirt.io/vmx-cr3-store-noexit=true,cpu-feature.node.kubevirt.io/vmx-cr8-load-exit=true,cpu-feature.node.kubevirt.io/vmx-cr8-store-exit=true,cpu-feature.node.kubevirt.io/vmx-desc-exit=true,cpu-feature.node.kubevirt.io/vmx-entry-ia32e-mode=true,cpu-feature.node.kubevirt.io/vmx-entry-load-bndcfgs=true,cpu-feature.node.kubevirt.io/vmx-entry-load-efer=true,cpu-feature.node.kubevirt.io/vmx-entry-load-pat=true,cpu-feature.node.kubevirt.io/vmx-entry-load-perf-global-ctrl=true,cpu-feature.node.kubevirt.io/vmx-entry-noload-debugctl=true,cpu-feature.node.kubevirt.io/vmx-ept-1gb=true,cpu-feature.node.kubevirt.io/vmx-ept-2mb=true,cpu-feature.node.kubevirt.io/vmx-ept-execonly=true,cpu-feature.node.kubevirt.io/vmx-ept=true,cpu-feature.node.kubevirt.io/vmx-eptad=true,cpu-feature.node.kubevirt.io/vmx-eptp-switching=true,cpu-feature.node.kubevirt.io/vmx-exit-ack-intr=true,cpu-feature.node.kubevirt.io/vmx-exit-clear-bndcfgs=true,cpu-feature.node.kubevirt.io/vmx-exit-load-efer=true,cpu-feature.node.kubevirt.io/vmx-exit-load-pat=true,cpu-feature.node.kubevirt.io/vmx-exit-load-perf-global-ctrl=true,cpu-feature.node.kubevirt.io/vmx-exit-nosave-debugctl=true,cpu-feature.node.kubevirt.io/vmx-exit-save-efer=true,cpu-feature.node.kubevirt.io/vmx-exit-save-pat=true,cpu-feature.node.kubevirt.io/vmx-exit-save-preemption-timer=true,cpu-feature.node.kubevirt.io/vmx-flexpriority=true,cpu-feature.node.kubevirt.io/vmx-hlt-exit=true,cpu-feature.node.kubevirt.io/vmx-ins-outs=true,cpu-feature.node.kubevirt.io/vmx-intr-exit=true,cpu-feature.node.kubevirt.io/vmx-invept-all-context=true,cpu-feature.node.kubevirt.io/vmx-invept-single-context=true,cpu-feature.node.kubevirt.io/vmx-invept=true,cpu-feature.node.kubevirt.io/vmx-invlpg-exit=true,cpu-feature.node.kubevirt.io/vmx-invpcid-exit=true,cpu-feature.node.kubevirt.io/vmx-invvpid-all-context=true,cpu-feature.node.kubevirt.io/vmx-invvpid-single-addr=true,cpu-feature.node.kubevirt.io/vmx-invvpid-single-context-noglobals=true,cpu-feature.node.kubevirt.io/vmx-invvpid=true,cpu-feature.node.kubevirt.io/vmx-io-bitmap=true,cpu-feature.node.kubevirt.io/vmx-io-exit=true,cpu-feature.node.kubevirt.io/vmx-monitor-exit=true,cpu-feature.node.kubevirt.io/vmx-movdr-exit=true,cpu-feature.node.kubevirt.io/vmx-msr-bitmap=true,cpu-feature.node.kubevirt.io/vmx-mtf=true,cpu-feature.node.kubevirt.io/vmx-mwait-exit=true,cpu-feature.node.kubevirt.io/vmx-nmi-exit=true,cpu-feature.node.kubevirt.io/vmx-page-walk-4=true,cpu-feature.node.kubevirt.io/vmx-pause-exit=true,cpu-feature.node.kubevirt.io/vmx-pml=true,cpu-feature.node.kubevirt.io/vmx-posted-intr=true,cpu-feature.node.kubevirt.io/vmx-preemption-timer=true,cpu-feature.node.kubevirt.io/vmx-rdpmc-exit=true,cpu-feature.node.kubevirt.io/vmx-rdrand-exit=true,cpu-feature.node.kubevirt.io/vmx-rdseed-exit=true,cpu-feature.node.kubevirt.io/vmx-rdtsc-exit=true,cpu-feature.node.kubevirt.io/vmx-rdtscp-exit=true,cpu-feature.node.kubevirt.io/vmx-secondary-ctls=true,cpu-feature.node.kubevirt.io/vmx-shadow-vmcs=true,cpu-feature.node.kubevirt.io/vmx-store-lma=true,cpu-feature.node.kubevirt.io/vmx-true-ctls=true,cpu-feature.node.kubevirt.io/vmx-tsc-offset=true,cpu-feature.node.kubevirt.io/vmx-tsc-scaling=true,cpu-feature.node.kubevirt.io/vmx-unrestricted-guest=true,cpu-feature.node.kubevirt.io/vmx-vintr-pending=true,cpu-feature.node.kubevirt.io/vmx-vmfunc=true,cpu-feature.node.kubevirt.io/vmx-vmwrite-vmexit-fields=true,cpu-feature.node.kubevirt.io/vmx-vnmi-pending=true,cpu-feature.node.kubevirt.io/vmx-vnmi=true,cpu-feature.node.kubevirt.io/vmx-vpid=true,cpu-feature.node.kubevirt.io/vmx-wbinvd-exit=true,cpu-feature.node.kubevirt.io/vmx-xsaves=true,cpu-feature.node.kubevirt.io/vmx=true,cpu-feature.node.kubevirt.io/x2apic=true,cpu-feature.node.kubevirt.io/xgetbv1=true,cpu-feature.node.kubevirt.io/xsave=true,cpu-feature.node.kubevirt.io/xsavec=true,cpu-feature.node.kubevirt.io/xsaveopt=true,cpu-feature.node.kubevirt.io/xsaves=true,cpu-model-migration.node.kubevirt.io/486-v1=true,cpu-model-migration.node.kubevirt.io/Broadwell-noTSX-IBRS=true,cpu-model-migration.node.kubevirt.io/Broadwell-noTSX=true,cpu-model-migration.node.kubevirt.io/Broadwell-v2=true,cpu-model-migration.node.kubevirt.io/Broadwell-v4=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server-noTSX=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server-v3=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server-v4=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server-v5=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server=true,cpu-model-migration.node.kubevirt.io/Conroe-v1=true,cpu-model-migration.node.kubevirt.io/Haswell-noTSX-IBRS=true,cpu-model-migration.node.kubevirt.io/Haswell-noTSX=true,cpu-model-migration.node.kubevirt.io/Haswell-v2=true,cpu-model-migration.node.kubevirt.io/Haswell-v4=true,cpu-model-migration.node.kubevirt.io/IvyBridge-IBRS=true,cpu-model-migration.node.kubevirt.io/IvyBridge-v1=true,cpu-model-migration.node.kubevirt.io/IvyBridge-v2=true,cpu-model-migration.node.kubevirt.io/IvyBridge=true,cpu-model-migration.node.kubevirt.io/Nehalem-IBRS=true,cpu-model-migration.node.kubevirt.io/Nehalem-v1=true,cpu-model-migration.node.kubevirt.io/Nehalem-v2=true,cpu-model-migration.node.kubevirt.io/Nehalem=true,cpu-model-migration.node.kubevirt.io/Opteron_G1-v1=true,cpu-model-migration.node.kubevirt.io/Opteron_G2-v1=true,cpu-model-migration.node.kubevirt.io/Penryn-v1=true,cpu-model-migration.node.kubevirt.io/Penryn=true,cpu-model-migration.node.kubevirt.io/SandyBridge-IBRS=true,cpu-model-migration.node.kubevirt.io/SandyBridge-v1=true,cpu-model-migration.node.kubevirt.io/SandyBridge-v2=true,cpu-model-migration.node.kubevirt.io/SandyBridge=true,cpu-model-migration.node.kubevirt.io/Skylake-Client-noTSX-IBRS=true,cpu-model-migration.node.kubevirt.io/Skylake-Client-v3=true,cpu-model-migration.node.kubevirt.io/Skylake-Client-v4=true,cpu-model-migration.node.kubevirt.io/Skylake-Server-noTSX-IBRS=true,cpu-model-migration.node.kubevirt.io/Skylake-Server-v3=true,cpu-model-migration.node.kubevirt.io/Skylake-Server-v4=true,cpu-model-migration.node.kubevirt.io/Skylake-Server-v5=true,cpu-model-migration.node.kubevirt.io/Westmere-IBRS=true,cpu-model-migration.node.kubevirt.io/Westmere-v1=true,cpu-model-migration.node.kubevirt.io/Westmere-v2=true,cpu-model-migration.node.kubevirt.io/Westmere=true,cpu-model-migration.node.kubevirt.io/core2duo-v1=true,cpu-model-migration.node.kubevirt.io/coreduo-v1=true,cpu-model-migration.node.kubevirt.io/kvm32-v1=true,cpu-model-migration.node.kubevirt.io/kvm64-v1=true,cpu-model-migration.node.kubevirt.io/n270-v1=true,cpu-model-migration.node.kubevirt.io/pentium-v1=true,cpu-model-migration.node.kubevirt.io/pentium2-v1=true,cpu-model-migration.node.kubevirt.io/pentium3-v1=true,cpu-model-migration.node.kubevirt.io/qemu32-v1=true,cpu-model-migration.node.kubevirt.io/qemu64-v1=true,cpu-model.node.kubevirt.io/486-v1=true,cpu-model.node.kubevirt.io/Broadwell-noTSX-IBRS=true,cpu-model.node.kubevirt.io/Broadwell-noTSX=true,cpu-model.node.kubevirt.io/Broadwell-v2=true,cpu-model.node.kubevirt.io/Broadwell-v4=true,cpu-model.node.kubevirt.io/Cascadelake-Server-noTSX=true,cpu-model.node.kubevirt.io/Cascadelake-Server-v3=true,cpu-model.node.kubevirt.io/Cascadelake-Server-v4=true,cpu-model.node.kubevirt.io/Cascadelake-Server-v5=true,cpu-model.node.kubevirt.io/Conroe-v1=true,cpu-model.node.kubevirt.io/Haswell-noTSX-IBRS=true,cpu-model.node.kubevirt.io/Haswell-noTSX=true,cpu-model.node.kubevirt.io/Haswell-v2=true,cpu-model.node.kubevirt.io/Haswell-v4=true,cpu-model.node.kubevirt.io/IvyBridge-IBRS=true,cpu-model.node.kubevirt.io/IvyBridge-v1=true,cpu-model.node.kubevirt.io/IvyBridge-v2=true,cpu-model.node.kubevirt.io/IvyBridge=true,cpu-model.node.kubevirt.io/Nehalem-IBRS=true,cpu-model.node.kubevirt.io/Nehalem-v1=true,cpu-model.node.kubevirt.io/Nehalem-v2=true,cpu-model.node.kubevirt.io/Nehalem=true,cpu-model.node.kubevirt.io/Opteron_G1-v1=true,cpu-model.node.kubevirt.io/Opteron_G2-v1=true,cpu-model.node.kubevirt.io/Penryn-v1=true,cpu-model.node.kubevirt.io/Penryn=true,cpu-model.node.kubevirt.io/SandyBridge-IBRS=true,cpu-model.node.kubevirt.io/SandyBridge-v1=true,cpu-model.node.kubevirt.io/SandyBridge-v2=true,cpu-model.node.kubevirt.io/SandyBridge=true,cpu-model.node.kubevirt.io/Skylake-Client-noTSX-IBRS=true,cpu-model.node.kubevirt.io/Skylake-Client-v3=true,cpu-model.node.kubevirt.io/Skylake-Client-v4=true,cpu-model.node.kubevirt.io/Skylake-Server-noTSX-IBRS=true,cpu-model.node.kubevirt.io/Skylake-Server-v3=true,cpu-model.node.kubevirt.io/Skylake-Server-v4=true,cpu-model.node.kubevirt.io/Skylake-Server-v5=true,cpu-model.node.kubevirt.io/Westmere-IBRS=true,cpu-model.node.kubevirt.io/Westmere-v1=true,cpu-model.node.kubevirt.io/Westmere-v2=true,cpu-model.node.kubevirt.io/Westmere=true,cpu-model.node.kubevirt.io/core2duo-v1=true,cpu-model.node.kubevirt.io/coreduo-v1=true,cpu-model.node.kubevirt.io/kvm32-v1=true,cpu-model.node.kubevirt.io/kvm64-v1=true,cpu-model.node.kubevirt.io/n270-v1=true,cpu-model.node.kubevirt.io/pentium-v1=true,cpu-model.node.kubevirt.io/pentium2-v1=true,cpu-model.node.kubevirt.io/pentium3-v1=true,cpu-model.node.kubevirt.io/qemu32-v1=true,cpu-model.node.kubevirt.io/qemu64-v1=true,cpu-timer.node.kubevirt.io/tsc-frequency=2100001000,cpu-timer.node.kubevirt.io/tsc-scalable=true,cpu-vendor.node.kubevirt.io/Intel=true,cpumanager=false,feature.node.kubernetes.io/cpu-cpuid.ADX=true,feature.node.kubernetes.io/cpu-cpuid.AESNI=true,feature.node.kubernetes.io/cpu-cpuid.AVX2=true,feature.node.kubernetes.io/cpu-cpuid.AVX512BW=true,feature.node.kubernetes.io/cpu-cpuid.AVX512CD=true,feature.node.kubernetes.io/cpu-cpuid.AVX512DQ=true,feature.node.kubernetes.io/cpu-cpuid.AVX512F=true,feature.node.kubernetes.io/cpu-cpuid.AVX512VL=true,feature.node.kubernetes.io/cpu-cpuid.AVX512VNNI=true,feature.node.kubernetes.io/cpu-cpuid.AVX=true,feature.node.kubernetes.io/cpu-cpuid.CMPXCHG8=true,feature.node.kubernetes.io/cpu-cpuid.FLUSH_L1D=true,feature.node.kubernetes.io/cpu-cpuid.FMA3=true,feature.node.kubernetes.io/cpu-cpuid.FXSR=true,feature.node.kubernetes.io/cpu-cpuid.FXSROPT=true,feature.node.kubernetes.io/cpu-cpuid.IA32_ARCH_CAP=true,feature.node.kubernetes.io/cpu-cpuid.IBPB=true,feature.node.kubernetes.io/cpu-cpuid.LAHF=true,feature.node.kubernetes.io/cpu-cpuid.MD_CLEAR=true,feature.node.kubernetes.io/cpu-cpuid.MOVBE=true,feature.node.kubernetes.io/cpu-cpuid.MPX=true,feature.node.kubernetes.io/cpu-cpuid.OSXSAVE=true,feature.node.kubernetes.io/cpu-cpuid.SPEC_CTRL_SSBD=true,feature.node.kubernetes.io/cpu-cpuid.STIBP=true,feature.node.kubernetes.io/cpu-cpuid.SYSCALL=true,feature.node.kubernetes.io/cpu-cpuid.SYSEE=true,feature.node.kubernetes.io/cpu-cpuid.VMX=true,feature.node.kubernetes.io/cpu-cpuid.X87=true,feature.node.kubernetes.io/cpu-cpuid.XGETBV1=true,feature.node.kubernetes.io/cpu-cpuid.XSAVE=true,feature.node.kubernetes.io/cpu-cpuid.XSAVEC=true,feature.node.kubernetes.io/cpu-cpuid.XSAVEOPT=true,feature.node.kubernetes.io/cpu-cpuid.XSAVES=true,feature.node.kubernetes.io/cpu-cstate.enabled=true,feature.node.kubernetes.io/cpu-hardware_multithreading=true,feature.node.kubernetes.io/cpu-model.family=6,feature.node.kubernetes.io/cpu-model.id=85,feature.node.kubernetes.io/cpu-model.vendor_id=Intel,feature.node.kubernetes.io/cpu-pstate.scaling_governor=performance,feature.node.kubernetes.io/cpu-pstate.status=active,feature.node.kubernetes.io/cpu-pstate.turbo=true,feature.node.kubernetes.io/cpu-rdt.RDTCMT=true,feature.node.kubernetes.io/cpu-rdt.RDTL3CA=true,feature.node.kubernetes.io/cpu-rdt.RDTMBA=true,feature.node.kubernetes.io/cpu-rdt.RDTMBM=true,feature.node.kubernetes.io/cpu-rdt.RDTMON=true,feature.node.kubernetes.io/kernel-config.NO_HZ=true,feature.node.kubernetes.io/kernel-config.NO_HZ_FULL=true,feature.node.kubernetes.io/kernel-version.full=6.8.0-87-generic,feature.node.kubernetes.io/kernel-version.major=6,feature.node.kubernetes.io/kernel-version.minor=8,feature.node.kubernetes.io/kernel-version.revision=0,feature.node.kubernetes.io/memory-numa=true,feature.node.kubernetes.io/network-sriov.capable=true,feature.node.kubernetes.io/pci-10de.present=true,feature.node.kubernetes.io/pci-15b3.present=true,feature.node.kubernetes.io/pci-15b3.sriov.capable=true,feature.node.kubernetes.io/pci-1a03.present=true,feature.node.kubernetes.io/pci-8086.present=true,feature.node.kubernetes.io/pci-8086.sriov.capable=true,feature.node.kubernetes.io/rdma.capable=true,feature.node.kubernetes.io/storage-nonrotationaldisk=true,feature.node.kubernetes.io/system-os_release.ID=ubuntu,feature.node.kubernetes.io/system-os_release.VERSION_ID.major=24,feature.node.kubernetes.io/system-os_release.VERSION_ID.minor=04,feature.node.kubernetes.io/system-os_release.VERSION_ID=24.04,host-endpoint=true,host-model-cpu.node.kubevirt.io/Cascadelake-Server=true,host-model-required-features.node.kubevirt.io/amd-ssbd=true,host-model-required-features.node.kubevirt.io/amd-stibp=true,host-model-required-features.node.kubevirt.io/arch-capabilities=true,host-model-required-features.node.kubevirt.io/fb-clear=true,host-model-required-features.node.kubevirt.io/flush-l1d=true,host-model-required-features.node.kubevirt.io/gds-no=true,host-model-required-features.node.kubevirt.io/hypervisor=true,host-model-required-features.node.kubevirt.io/ibpb=true,host-model-required-features.node.kubevirt.io/ibrs-all=true,host-model-required-features.node.kubevirt.io/ibrs=true,host-model-required-features.node.kubevirt.io/invtsc=true,host-model-required-features.node.kubevirt.io/md-clear=true,host-model-required-features.node.kubevirt.io/mds-no=true,host-model-required-features.node.kubevirt.io/mpx=true,host-model-required-features.node.kubevirt.io/pdcm=true,host-model-required-features.node.kubevirt.io/pku=true,host-model-required-features.node.kubevirt.io/pschange-mc-no=true,host-model-required-features.node.kubevirt.io/psdp-no=true,host-model-required-features.node.kubevirt.io/rdctl-no=true,host-model-required-features.node.kubevirt.io/rfds-no=true,host-model-required-features.node.kubevirt.io/sbdr-ssdp-no=true,host-model-required-features.node.kubevirt.io/skip-l1dfl-vmentry=true,host-model-required-features.node.kubevirt.io/ss=true,host-model-required-features.node.kubevirt.io/stibp=true,host-model-required-features.node.kubevirt.io/tsc_adjust=true,host-model-required-features.node.kubevirt.io/tsx-ctrl=true,host-model-required-features.node.kubevirt.io/umip=true,host-model-required-features.node.kubevirt.io/vmx-activity-hlt=true,host-model-required-features.node.kubevirt.io/vmx-activity-wait-sipi=true,host-model-required-features.node.kubevirt.io/vmx-apicv-register=true,host-model-required-features.node.kubevirt.io/vmx-apicv-vid=true,host-model-required-features.node.kubevirt.io/vmx-apicv-x2apic=true,host-model-required-features.node.kubevirt.io/vmx-apicv-xapic=true,host-model-required-features.node.kubevirt.io/vmx-cr3-load-noexit=true,host-model-required-features.node.kubevirt.io/vmx-cr3-store-noexit=true,host-model-required-features.node.kubevirt.io/vmx-cr8-load-exit=true,host-model-required-features.node.kubevirt.io/vmx-cr8-store-exit=true,host-model-required-features.node.kubevirt.io/vmx-desc-exit=true,host-model-required-features.node.kubevirt.io/vmx-entry-ia32e-mode=true,host-model-required-features.node.kubevirt.io/vmx-entry-load-bndcfgs=true,host-model-required-features.node.kubevirt.io/vmx-entry-load-efer=true,host-model-required-features.node.kubevirt.io/vmx-entry-load-pat=true,host-model-required-features.node.kubevirt.io/vmx-entry-load-perf-global-ctrl=true,host-model-required-features.node.kubevirt.io/vmx-entry-noload-debugctl=true,host-model-required-features.node.kubevirt.io/vmx-ept-1gb=true,host-model-required-features.node.kubevirt.io/vmx-ept-2mb=true,host-model-required-features.node.kubevirt.io/vmx-ept-execonly=true,host-model-required-features.node.kubevirt.io/vmx-ept=true,host-model-required-features.node.kubevirt.io/vmx-eptad=true,host-model-required-features.node.kubevirt.io/vmx-eptp-switching=true,host-model-required-features.node.kubevirt.io/vmx-exit-ack-intr=true,host-model-required-features.node.kubevirt.io/vmx-exit-clear-bndcfgs=true,host-model-required-features.node.kubevirt.io/vmx-exit-load-efer=true,host-model-required-features.node.kubevirt.io/vmx-exit-load-pat=true,host-model-required-features.node.kubevirt.io/vmx-exit-load-perf-global-ctrl=true,host-model-required-features.node.kubevirt.io/vmx-exit-nosave-debugctl=true,host-model-required-features.node.kubevirt.io/vmx-exit-save-efer=true,host-model-required-features.node.kubevirt.io/vmx-exit-save-pat=true,host-model-required-features.node.kubevirt.io/vmx-exit-save-preemption-timer=true,host-model-required-features.node.kubevirt.io/vmx-flexpriority=true,host-model-required-features.node.kubevirt.io/vmx-hlt-exit=true,host-model-required-features.node.kubevirt.io/vmx-ins-outs=true,host-model-required-features.node.kubevirt.io/vmx-intr-exit=true,host-model-required-features.node.kubevirt.io/vmx-invept-all-context=true,host-model-required-features.node.kubevirt.io/vmx-invept-single-context=true,host-model-required-features.node.kubevirt.io/vmx-invept=true,host-model-required-features.node.kubevirt.io/vmx-invlpg-exit=true,host-model-required-features.node.kubevirt.io/vmx-invpcid-exit=true,host-model-required-features.node.kubevirt.io/vmx-invvpid-all-context=true,host-model-required-features.node.kubevirt.io/vmx-invvpid-single-addr=true,host-model-required-features.node.kubevirt.io/vmx-invvpid-single-context-noglobals=true,host-model-required-features.node.kubevirt.io/vmx-invvpid=true,host-model-required-features.node.kubevirt.io/vmx-io-bitmap=true,host-model-required-features.node.kubevirt.io/vmx-io-exit=true,host-model-required-features.node.kubevirt.io/vmx-monitor-exit=true,host-model-required-features.node.kubevirt.io/vmx-movdr-exit=true,host-model-required-features.node.kubevirt.io/vmx-msr-bitmap=true,host-model-required-features.node.kubevirt.io/vmx-mtf=true,host-model-required-features.node.kubevirt.io/vmx-mwait-exit=true,host-model-required-features.node.kubevirt.io/vmx-nmi-exit=true,host-model-required-features.node.kubevirt.io/vmx-page-walk-4=true,host-model-required-features.node.kubevirt.io/vmx-pause-exit=true,host-model-required-features.node.kubevirt.io/vmx-pml=true,host-model-required-features.node.kubevirt.io/vmx-posted-intr=true,host-model-required-features.node.kubevirt.io/vmx-preemption-timer=true,host-model-required-features.node.kubevirt.io/vmx-rdpmc-exit=true,host-model-required-features.node.kubevirt.io/vmx-rdrand-exit=true,host-model-required-features.node.kubevirt.io/vmx-rdseed-exit=true,host-model-required-features.node.kubevirt.io/vmx-rdtsc-exit=true,host-model-required-features.node.kubevirt.io/vmx-rdtscp-exit=true,host-model-required-features.node.kubevirt.io/vmx-secondary-ctls=true,host-model-required-features.node.kubevirt.io/vmx-shadow-vmcs=true,host-model-required-features.node.kubevirt.io/vmx-store-lma=true,host-model-required-features.node.kubevirt.io/vmx-true-ctls=true,host-model-required-features.node.kubevirt.io/vmx-tsc-offset=true,host-model-required-features.node.kubevirt.io/vmx-tsc-scaling=true,host-model-required-features.node.kubevirt.io/vmx-unrestricted-guest=true,host-model-required-features.node.kubevirt.io/vmx-vintr-pending=true,host-model-required-features.node.kubevirt.io/vmx-vmfunc=true,host-model-required-features.node.kubevirt.io/vmx-vmwrite-vmexit-fields=true,host-model-required-features.node.kubevirt.io/vmx-vnmi-pending=true,host-model-required-features.node.kubevirt.io/vmx-vnmi=true,host-model-required-features.node.kubevirt.io/vmx-vpid=true,host-model-required-features.node.kubevirt.io/vmx-wbinvd-exit=true,host-model-required-features.node.kubevirt.io/vmx-xsaves=true,host-model-required-features.node.kubevirt.io/vmx=true,host-model-required-features.node.kubevirt.io/xsaves=true,hyperv.node.kubevirt.io/base=true,hyperv.node.kubevirt.io/frequencies=true,hyperv.node.kubevirt.io/ipi=true,hyperv.node.kubevirt.io/reenlightenment=true,hyperv.node.kubevirt.io/reset=true,hyperv.node.kubevirt.io/runtime=true,hyperv.node.kubevirt.io/synic2=true,hyperv.node.kubevirt.io/synic=true,hyperv.node.kubevirt.io/synictimer=true,hyperv.node.kubevirt.io/time=true,hyperv.node.kubevirt.io/tlbflush=true,hyperv.node.kubevirt.io/vpindex=true,kubernetes.io/arch=amd64,kubernetes.io/hostname=k8s-haosu-15.sdsc.optiputer.net,kubernetes.io/os=linux,kubevirt.io/ksm-enabled=false,kubevirt.io/schedulable=true,linbit.com/hostname=k8s-haosu-15.sdsc.optiputer.net,machine-type.node.kubevirt.io/pc-i440fx-rhel7.6.0=true,machine-type.node.kubevirt.io/pc-q35-rhel7.6.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.0.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.1.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.2.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.3.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.4.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.5.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.6.0=true,machine-type.node.kubevirt.io/pc-q35-rhel9.0.0=true,machine-type.node.kubevirt.io/pc-q35-rhel9.2.0=true,machine-type.node.kubevirt.io/pc-q35-rhel9.4.0=true,machine-type.node.kubevirt.io/pc-q35-rhel9.6.0=true,machine-type.node.kubevirt.io/pc=true,machine-type.node.kubevirt.io/q35=true,mtu=9000,nautilus.io/OSGInstitutionID=osg-htc.org_iid_06wup3aye2t7,nautilus.io/RORInstitutionID=ror.org_0168r3w48,nautilus.io/group=haosu,nautilus.io/ipv6=true,nautilus.io/linstor=true,nautilus.io/network=10000,netbox.io/site=sdsc,nvidia.com/cuda.driver-version.full=580.105.08,nvidia.com/cuda.driver-version.major=580,nvidia.com/cuda.driver-version.minor=105,nvidia.com/cuda.driver-version.revision=08,nvidia.com/cuda.driver.major=580,nvidia.com/cuda.driver.minor=105,nvidia.com/cuda.driver.rev=08,nvidia.com/cuda.runtime-version.full=13.0,nvidia.com/cuda.runtime-version.major=13,nvidia.com/cuda.runtime-version.minor=0,nvidia.com/cuda.runtime.major=13,nvidia.com/cuda.runtime.minor=0,nvidia.com/gfd.timestamp=1763656608,nvidia.com/gpu.compute.major=7,nvidia.com/gpu.compute.minor=5,nvidia.com/gpu.count=7,nvidia.com/gpu.deploy.container-toolkit=true,nvidia.com/gpu.deploy.dcgm-exporter=true,nvidia.com/gpu.deploy.dcgm=true,nvidia.com/gpu.deploy.device-plugin=true,nvidia.com/gpu.deploy.driver=true,nvidia.com/gpu.deploy.gpu-feature-discovery=true,nvidia.com/gpu.deploy.node-status-exporter=true,nvidia.com/gpu.deploy.operator-validator=true,nvidia.com/gpu.family=turing,nvidia.com/gpu.machine=G291-280-00,nvidia.com/gpu.memory=11264,nvidia.com/gpu.present=true,nvidia.com/gpu.product=NVIDIA-GeForce-RTX-2080-Ti,nvidia.com/gpu.replicas=1,nvidia.com/gpu.sharing-strategy=none,nvidia.com/mig.capable=false,nvidia.com/mig.strategy=single,nvidia.com/mps.capable=false,remediation.medik8s.io/exclude-from-remediation=true,scheduling.node.kubevirt.io/tsc-frequency-1995288000=true,scheduling.node.kubevirt.io/tsc-frequency-2100001000=true,topology.kubernetes.io/region=us-west,topology.kubernetes.io/zone=ucsd-sdsc
pvc-explorer-g46qp well this is running now. 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ cd /home/jovyan/cloud-computing-project/
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ for f in df_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-g46qp:/data/
done
command terminated with exit code 137
E1120 18:15:31.604910   18990 v2.go:104] "Unhandled Error" err="write tcp 10.244.189.108:43172->67.58.53.148:443: write: broken pipe"
error: Internal error occurred: unable to upgrade connection: container not found ("explorer")
error: cannot exec into a container in a completed pod; current phase is Failed
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
what about this one? apiVersion: batch/v1
kind: Job
metadata:
  name: pvc-explorer
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  backoffLimit: 0
  template:
    spec:
      restartPolicy: Never
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: nautilus.io/group
                operator: NotIn
                values:
                - haosu
      containers:
      - name: explorer
        image: ubuntu:22.04
        command: ["bash","-c","sleep 36000"]
        volumeMounts:
        - name: project-storage
          mountPath: /data
        resources:
          requests:
            cpu: 100m
            memory: 1Gi
          limits:
            cpu: 200m
            memory: 2Gi
      volumes:
      - name: project-storage
        persistentVolumeClaim:
          claimName: naaxk6-pvc
we alredy did the 3600 and it still crashed
apiVersion: batch/v1
kind: Job
metadata:
  name: pvc-explorer
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  backoffLimit: 0
  template:
    spec:
      restartPolicy: Never
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: nautilus.io/group
                operator: NotIn
                values:
                - haosu
      containers:
      - name: explorer
        image: ubuntu:22.04
        command: ["bash","-c","sleep 36000"]
        volumeMounts:
        - name: project-storage
          mountPath: /data
        resources:
          requests:
            cpu: 100m
            memory: 1Gi
          limits:
            cpu: 200m
            memory: 2Gi
      volumes:
      - name: project-storage
        persistentVolumeClaim:
          claimName: naaxk6-pvc so which one is better that one or this one?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          16h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          16h
pod-cc5m4-train                    0/1     Error       0          44h
pod-dbkyd-train                    0/1     Error       0          6h7m
pod-gcfpx-train                    0/1     Error       0          12h
pod-name-ljabxf                    0/1     Error       0          12h
pod-pvc-jm2rc                      0/1     Error       0          13h
pvc-explorer-k6l6z                 0/1     Pending     0          51s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-k6l6z | grep -A10 "FailedScheduling"
  Warning  FailedScheduling  75s   default-scheduler  0/521 nodes are available: 1 node(s) had untolerated taint {nautilus.io/issue: 1149}, 1 node(s) had untolerated taint {nautilus.io/issue: 1257}, 1 node(s) had untolerated taint {nautilus.io/issue: 1348}, 1 node(s) had untolerated taint {nautilus.io/issue: 1350}, 1 node(s) had untolerated taint {nautilus.io/issue: 1376}, 1 node(s) had untolerated taint {nautilus.io/issue: 1384}, 1 node(s) had untolerated taint {nautilus.io/issue: 1452}, 1 node(s) had untolerated taint {nautilus.io/issue: 1476}, 1 node(s) had untolerated taint {nautilus.io/issue: 1477}, 1 node(s) had untolerated taint {nautilus.io/issue: 1478}, 1 node(s) had untolerated taint {nautilus.io/issue: slow-network}, 1 node(s) had untolerated taint {nautilus.io/issue: testing}, 1 node(s) had untolerated taint {nautilus.io/reservation: csusb-cousins-lab}, 1 node(s) had untolerated taint {nautilus.io/reservation: hdr-ml-challenge}, 1 node(s) had untolerated taint {nautilus.io/reservation: internet2}, 1 node(s) had untolerated taint {nautilus.io/rese ...
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
fiona worked earlier
it's been 16 mins and still pending
yes
apiVersion: batch/v1
kind: Job
metadata:
  name: job-data-download-naaxk6
spec:
  template:
    spec:
      automountServiceAccountToken: false
      containers:
      - name: pod-data-download-naaxk6
        image: ubuntu:20.04
        command: ["/bin/sh","-c"]
        args:
        - cp -r /ccdata/* /data/
        volumeMounts:
        - mountPath: /ccdata
          name: source
        - mountPath: /data
          name: destination 
        resources:
            limits:
              memory: 10Gi
              cpu: "4"
            requests:
              memory: 10Gi
              cpu: "4"     
      volumes:
      - name: source
        persistentVolumeClaim:
          claimName: cloudcomp-data
      - name: destination
        persistentVolumeClaim:
          claimName: naaxk6-pv
      restartPolicy: Never      
  backoffLimit: 0 woudl this work? this is what we used in our practice

no i mean this structure but we just tweak it instead of avoiding hoisu
no we don't restrict it to those nodes
but in the code i gave you we did 10 gi each
give me the code to run the thing now the chunks to load it
pvc-explorer-w6xv4                 1/1     Running     0          84s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ POD=pvc-explorer-w6xv4

for f in df_chunk_*; do
    echo "Uploading $f ..."
    kubectl -n gp-engine-mizzou-dsa-cloud cp "$f" "$POD":/data/
    sleep 1
done
Uploading df_chunk_aa ...
so far it doesn't seem like it's stoppig. its still running. jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ POD=pvc-explorer-w6xv4

for f in df_chunk_*; do
    echo "Uploading $f ..."
    kubectl -n gp-engine-mizzou-dsa-cloud cp "$f" "$POD":/data/
    sleep 1
done
Uploading df_chunk_aa ...
Uploading df_chunk_ab ...
they are still uploading yay! tho very slow
do you think i would be able to upload the whole parquet file?
830 mb
am in in violation here. Utilization violations
Allowed: GPU: >40%CPU: 20% - 200%Memory 20% - 150% Ignored: Memory: ≤2 GBCPU: ≤1
Namespace
Name
GPU util
CPU util
Mem util
GPU requested
CPU requested
Mem requested
gp-engine-mizzou-dsa-cloud	pvc-explorer-w6xv4		0%	0%		4	10 GB
well how come we're not using cpu when the code is still running and the files are being transferred to pvc
but it's needed riht?
so my pvc is only allowed 10 gb of storage?
is it done? for f in df_chunk_*; do
    echo "Uploading $f ..."
    kubectl -n gp-engine-mizzou-dsa-cloud cp "$f" "$POD":/data/
    sleep 1
done
Uploading df_chunk_aa ...
Uploading df_chunk_ab ...
Uploading df_chunk_ac ...
Uploading df_chunk_ad ...
Uploading df_chunk_ae ...
Uploading df_chunk_af ...
Uploading df_chunk_ag ...
Uploading df_chunk_ah ...
Uploading df_chunk_ai ...
Uploading df_chunk_aj ...
Uploading df_chunk_ak ...
Uploading df_chunk_al ...
Uploading df_chunk_am ...
Uploading df_chunk_an ...
Uploading df_chunk_ao ...
Uploading df_chunk_ap ...
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud exec -it $POD -- ls -lh /data
total 818M
-rw-r--r-- 1 1000 users 50M Nov 20 19:13 df_chunk_aa
-rw-r--r-- 1 1000 users 50M Nov 20 19:23 df_chunk_ab
-rw-r--r-- 1 1000 users 50M Nov 20 19:31 df_chunk_ac
-rw-r--r-- 1 1000 users 50M Nov 20 19:44 df_chunk_ad
-rw-r--r-- 1 1000 users 50M Nov 20 19:54 df_chunk_ae
-rw-r--r-- 1 1000 users 50M Nov 20 20:06 df_chunk_af
-rw-r--r-- 1 1000 users 50M Nov 20 20:16 df_chunk_ag
-rw-r--r-- 1 1000 users 50M Nov 20 20:26 df_chunk_ah
-rw-r--r-- 1 1000 users 50M Nov 20 20:37 df_chunk_ai
-rw-r--r-- 1 1000 users 50M Nov 20 20:48 df_chunk_aj
-rw-r--r-- 1 1000 users 50M Nov 20 20:58 df_chunk_ak
-rw-r--r-- 1 1000 users 50M Nov 20 21:08 df_chunk_al
-rw-r--r-- 1 1000 users 50M Nov 20 21:20 df_chunk_am
-rw-r--r-- 1 1000 users 50M Nov 20 21:31 df_chunk_an
-rw-r--r-- 1 1000 users 50M Nov 20 21:39 df_chunk_ao
-rw-r--r-- 1 1000 users 36M Nov 20 21:45 df_chunk_ap
-rw------- 1 root root  33M Nov 20 17:09 df_merged_filtered.parquet
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
okay now let's try to upload the full parquet file as well
do we still need the connection right now? what else do we need to do?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud cp df_merged_filtered.parquet pvc-explorer-w6xv4:/data/
E1120 22:20:23.303335   22966 v2.go:167] "Unhandled Error" err="next reader: read tcp 10.244.189.108:51610->67.58.53.148:443: i/o timeout"
E1120 22:20:23.303445   22966 v2.go:129] "Unhandled Error" err="next reader: read tcp 10.244.189.108:51610->67.58.53.148:443: i/o timeout"
E1120 22:20:23.303450   22966 v2.go:150] "Unhandled Error" err="next reader: read tcp 10.244.189.108:51610->67.58.53.148:443: i/o timeout"
E1120 22:20:23.304851   22966 websocket.go:500] Websocket Ping failed: write tcp 10.244.189.108:51610->67.58.53.148:443: use of closed network connection
error: error reading from error stream: next reader: read tcp 10.244.189.108:51610->67.58.53.148:443: i/o timeout
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
before i delete it., don't we need to merge the chunks first
okay so we run teh base line job now?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run verify --image=ubuntu:22.04 -it --rm -- sh -c "ls -lh /data" --overrides='
{
  "apiVersion": "v1",
  "spec": {
    "containers":[{
      "name": "verify",
      "image": "ubuntu:22.04",
      "command":["bash","-c","ls -lh /data"],
      "volumeMounts":[{"mountPath":"/data","name":"project-storage"}]
    }],
    "volumes":[{"name":"project-storage","persistentVolumeClaim":{"claimName":"naaxk6-pvc"}}]
  }
}'
If you don't see a command prompt, try pressing enter.
warning: couldn't attach to pod/verify, falling back to streaming logs: Internal error occurred: unable to upgrade connection: container verify not found in pod verify_gp-engine-mizzou-dsa-cloud
ls: cannot access '/data': No such file or directory
pod "verify" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
-rw-r--r-- 1 1000 users 50M Nov 20 19:13 df_chunk_aa
-rw-r--r-- 1 1000 users 50M Nov 20 19:23 df_chunk_ab
-rw-r--r-- 1 1000 users 50M Nov 20 19:31 df_chunk_ac
-rw-r--r-- 1 1000 users 50M Nov 20 19:44 df_chunk_ad
-rw-r--r-- 1 1000 users 50M Nov 20 19:54 df_chunk_ae
-rw-r--r-- 1 1000 users 50M Nov 20 20:06 df_chunk_af
-rw-r--r-- 1 1000 users 50M Nov 20 20:16 df_chunk_ag
-rw-r--r-- 1 1000 users 50M Nov 20 20:26 df_chunk_ah
-rw-r--r-- 1 1000 users 50M Nov 20 20:37 df_chunk_ai
-rw-r--r-- 1 1000 users 50M Nov 20 20:48 df_chunk_aj
-rw-r--r-- 1 1000 users 50M Nov 20 20:58 df_chunk_ak
-rw-r--r-- 1 1000 users 50M Nov 20 21:08 df_chunk_al
-rw-r--r-- 1 1000 users 50M Nov 20 21:20 df_chunk_am
-rw-r--r-- 1 1000 users 50M Nov 20 21:31 df_chunk_an
-rw-r--r-- 1 1000 users 50M Nov 20 21:39 df_chunk_ao
-rw-r--r-- 1 1000 users 36M Nov 20 21:45 df_chunk_ap
-rw------- 1 root root  55M Nov 20 22:28 df_merged_filtered.parquet
pod "verify" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$  why is the df_merged filetered there
is this good? apiVersion: batch/v1
kind: Job
metadata:
  name: baseline-job
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: baseline
        image: ghcr.io/nathanielnat1993/cloud-computing-project:latest
        command: ["python", "src/main.py", "--mode", "baseline"]
        volumeMounts:
        - mountPath: /project/data
          name: project-storage
        resources:
          requests:
            cpu: "2"
            memory: "16Gi"
            nvidia.com/gpu: 1
          limits:
            cpu: "4"
            memory: "32Gi"
            nvidia.com/gpu: 1
      volumes:
      - name: project-storage
        persistentVolumeClaim:
          claimName: naaxk6-pvc
this is my main import argparse
import pandas as pd

from preprocessing import apply_cleaning, stratified_group_split
from tokenization import load_tokenizer, tokenize_overflow_fixed_pt

from baseline_model import (
    load_bioclincial_bert_encoder,
    chunk_embeddings,
    aggregate_docs,
    train_logistic_regression,
)

from baseline_evaluate import (
    evaluate_with_target_recall,
    report_metrics
)


def run_baseline(df_train, df_val, df_test, tokenizer):
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc   = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc  = tokenize_overflow_fixed_pt(df_test, tokenizer)

    encoder = load_bioclincial_bert_encoder()

    train_chunk_emb = chunk_embeddings(train_enc, encoder)
    val_chunk_emb   = chunk_embeddings(val_enc, encoder)
    test_chunk_emb  = chunk_embeddings(test_enc, encoder)

    train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
    val_doc_emb   = aggregate_docs(val_chunk_emb,   val_enc["doc_mapping"])
    test_doc_emb  = aggregate_docs(test_chunk_emb,  test_enc["doc_mapping"])

    y_train = df_train["readmitted"].to_numpy()
    y_val   = df_val["readmitted"].to_numpy()
    y_test  = df_test["readmitted"].to_numpy()

    clf = train_logistic_regression(train_doc_emb, y_train)

    val_p  = clf.predict_proba(val_doc_emb)[:, 1]
    test_p = clf.predict_proba(test_doc_emb)[:, 1]

    best_t, val_pred  = evaluate_with_target_recall(y_val,  val_p,  target_recall=0.75)
    _,      test_pred = evaluate_with_target_recall(y_test, test_p, target_recall=0.75)

    report_metrics("VAL",  y_val,  val_pred,  val_p,  best_t)
    report_metrics("TEST", y_test, test_pred, test_p, best_t)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="baseline", choices=["baseline"])
    args = parser.parse_args()

    df = pd.read_parquet("/project/data/df_merged_filtered.parquet")
    df = apply_cleaning(df)
    df_train, df_val, df_test = stratified_group_split(df)

    tokenizer = load_tokenizer()

    run_baseline(df_train, df_val, df_test, tokenizer)


if __name__ == "__main__":
    main()
well no! since we uploaded the chunks! and thta 55mb failed
omg no! that df_merged_filtered in the pvc failed remember! that' why its only 55mb instead of 825!
omg remember we were going to merge all those chunks and make it df_merged_filtered!
will this replace htat broken df_merged_filered one
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, pyarrow, numpy, python-dateutil, pandas
Successfully installed numpy-2.2.6 pandas-2.3.3 pyarrow-22.0.0 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip is available: 23.0.1 -> 25.3
[notice] To update, run: pip install --upgrade pip
root@merge:/# 
root@merge:/# 
print("Done! Final file size:")
import os
print(os.path.getsize("/data/df_merged_filtered.parquet") / (1024*1024), "MB")
EOF

Finding chunk files in /data...
Found 16 chunks: ['/data/df_chunk_aa', '/data/df_chunk_ab', '/data/df_chunk_ac', '/data/df_chunk_ad', '/data/df_chunk_ae', '/data/df_chunk_af', '/data/df_chunk_ag', '/data/df_chunk_ah', '/data/df_chunk_ai', '/data/df_chunk_aj', '/data/df_chunk_ak', '/data/df_chunk_al', '/data/df_chunk_am', '/data/df_chunk_an', '/data/df_chunk_ao', '/data/df_chunk_ap']
Reading: /data/df_chunk_aa
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
  File "/usr/local/lib/python3.10/site-packages/pandas/io/parquet.py", line 669, in read_parquet
    return impl.read(
  File "/usr/local/lib/python3.10/site-packages/pandas/io/parquet.py", line 265, in read
    pa_table = self.api.parquet.read_table(
  File "/usr/local/lib/python3.10/site-packages/pyarrow/parquet/core.py", line 1844, in read_table
    dataset = ParquetDataset(
  File "/usr/local/lib/python3.10/site-packages/pyarrow/parquet/core.py", line 1413, in __init__
    [fragment], schema=schema or fragment.physical_schema,
  File "pyarrow/_dataset.pyx", line 1477, in pyarrow._dataset.Fragment.physical_schema.__get__
  File "pyarrow/error.pxi", line 155, in pyarrow.lib.pyarrow_internal_check_status
  File "pyarrow/error.pxi", line 92, in pyarrow.lib.check_status
pyarrow.lib.ArrowInvalid: Could not open Parquet input source '<Buffer>': Parquet magic bytes not found in footer. Either the file is corrupted or this is not a parquet file.
root@merge:/# 
root@merge:/# 
root@merge:/# cat /data/df_chunk_* > /data/df_merged_reassembled.parquet it's taking a while
why did we name the reassembled parquet that instead of df_merged_filtered
it;s still runnign. hwo long would it take?
is it done? root@merge:/# cat /data/df_chunk_* > /data/df_merged_reassembled.parquet
root@merge:/# 
path = "/data/df_merged_reassembled.parquet"

print("File size (MB):", os.path.getsize(path)/(1024*1024))

try:
    df = pd.read_parquet(path)
    print("SUCCESS: Parquet is readable!")
    print(df.head())
except Exception as e:
    print("ERROR reading parquet:")
    print(e)
EOF
File size (MB): 785.0076446533203
Session ended, resume using 'kubectl attach merge -c merge -i -t' command when the pod is running
pod "merge" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
File size (MB): 785.0076446533203
Session ended, resume using 'kubectl attach merge -c merge -i -t' command when the pod is running
pod "merge" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run verify-parquet \
  --image=python:3.10-slim \
  -it --rm \
  --overrides='
{
  "apiVersion": "v1",
  "spec": {
    "containers":[{
      "name": "verify-parquet",
      "image": "python:3.10-slim",
      "command":["bash","-c","pip install pandas pyarrow && python3 - << EOF
import pandas as pd, os
path = \"/data/df_merged_reassembled.parquet\"
print(\"File size (MB):\", os.path.getsize(path)/(1024*1024))
try:
    df = pd.read_parquet(path)
    print(\"SUCCESS — Parquet is readable!\\n\", df.head())
except Exception as e:
    print(\"ERROR reading parquet:\")
    print(e)
EOF"],
      "volumeMounts":[{"mountPath":"/data","name":"project-storage"}]
    }],
    "volumes":[{"name":"project-storage","persistentVolumeClaim":{"claimName":"naaxk6-pvc"}}]
  }
}'
error: Invalid JSON Patch
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run verify-parquet \
  --image=python:3.10-slim \
  -it --rm \
  --overrides='
{
  "apiVersion": "v1",
  "spec": {
    "containers":[{
      "name": "verify-parquet",
      "image": "python:3.10-slim",
      "command":["bash","-c","pip install pandas pyarrow && python3 - << EOF
import pandas as pd, os
path = \"/data/df_merged_reassembled.parquet\"
print(\"File size (MB):\", os.path.getsize(path)/(1024*1024))
try:
    df = pd.read_parquet(path)
    print(\"SUCCESS — Parquet is readable!\\n\", df.head())
except Exception as e:
    print(\"ERROR reading parquet:\")
    print(e)
EOF"],
      "volumeMounts":[{"mountPath":"/data","name":"project-storage"}]
    }],
    "volumes":[{"name":"project-storage","persistentVolumeClaim":{"claimName":"naaxk6-pvc"}}]
  }
}'
error: Invalid JSON Patch
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run verify-parquet \
  --image=python:3.10-slim \
  -it --rm \
  --overrides='{
    "apiVersion": "v1",
    "spec": {
      "containers": [{
        "name": "verify-parquet",
        "image": "python:3.10-slim",
        "command": [
          "bash",
          "-c",
          "pip install pandas pyarrow && python3 - <<\"EOF\"\nimport pandas as pd, os\npath = \"/data/df_merged_reassembled.parquet\"\nprint(\"File size (MB):\", os.path.getsize(path)/(1024*1024))\ntry:\n    df = pd.read_parquet(path)\n    print(\"SUCCESS — Parquet is readable!\\n\", df.head())\nexcept Exception as e:\n    print(\"ERROR reading parquet:\")\n    print(e)\nEOF"
        ],
        "volumeMounts": [{
          "mountPath": "/data",
          "name": "project-storage"
        }]
      }],
      "volumes": [{
        "name": "project-storage",
        "persistentVolumeClaim": { "claimName": "naaxk6-pvc" }
      }]
    }
  }'
error: Unable to use a TTY - container verify-parquet did not allocate one
If you don't see a command prompt, try pressing enter.
Collecting pandas
  Downloading pandas-2.3.3-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 17.0 MB/s eta 0:00:00
Collecting pyarrow
  Downloading pyarrow-22.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (47.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.6/47.6 MB 7.8 MB/s eta 0:00:00
Collecting numpy>=1.22.4
  Downloading numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 12.8 MB/s eta 0:00:00
Collecting tzdata>=2022.7
  Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 93.1 MB/s eta 0:00:00
Collecting pytz>=2020.1
  Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 509.2/509.2 kB 138.1 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 101.6 MB/s eta 0:00:00
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, pyarrow, numpy, python-dateutil, pandas
Successfully installed numpy-2.2.6 pandas-2.3.3 pyarrow-22.0.0 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip is available: 23.0.1 -> 25.3
[notice] To update, run: pip install --upgrade pip
pod "verify-parquet" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
try:
    df = pd.read_parquet(path)
    print('SUCCESS — Parquet is readable!')
    print(df.head())
except Exception as e:
    print('ERROR reading parquet:')
    print(e)
EOF
python3 /verify.py"
If you don't see a command prompt, try pressing enter.
Collecting pandas
  Downloading pandas-2.3.3-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 10.1 MB/s eta 0:00:00
Collecting pyarrow
  Downloading pyarrow-22.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (47.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.6/47.6 MB 4.9 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 65.5 MB/s eta 0:00:00
Collecting tzdata>=2022.7
  Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 75.9 MB/s eta 0:00:00
Collecting pytz>=2020.1
  Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 509.2/509.2 kB 5.3 MB/s eta 0:00:00
Collecting numpy>=1.22.4
  Downloading numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 8.6 MB/s eta 0:00:00
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, pyarrow, numpy, python-dateutil, pandas
Successfully installed numpy-2.2.6 pandas-2.3.3 pyarrow-22.0.0 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip is available: 23.0.1 -> 25.3
[notice] To update, run: pip install --upgrade pip
python3: can't open file '/verify.py': [Errno 2] No such file or directory
pod "verify-parquet" deleted
pod gp-engine-mizzou-dsa-cloud/verify-parquet terminated (Error)
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
    print(df.head())
except Exception as e:
    print('ERROR reading parquet:')
    print(e)
EOF
  " \
  --overrides='{
    "apiVersion": "v1",
    "spec": {
      "volumes": [{
        "name": "project-storage",
        "persistentVolumeClaim": { "claimName": "naaxk6-pvc" }
      }],
      "containers": [{
        "name": "verify-parquet",
        "image": "python:3.10-slim",
        "command": ["bash","-c","sleep infinity"],
        "volumeMounts": [{
          "mountPath": "/data",
          "name": "project-storage"
        }]
      }]
    }
  }'
If you don't see a command prompt, try pressing enter.

Checking file...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "/usr/local/lib/python3.10/genericpath.py", line 50, in getsize
    return os.stat(filename).st_size
FileNotFoundError: [Errno 2] No such file or directory: '/data/df_merged_reassembled.parquet'
Session ended, resume using 'kubectl attach verify-parquet -c verify-parquet -i -t' command when the pod is running
pod "verify-parquet" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
ovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run list-pvc \
  --image=ubuntu:22.04 \
  -it --rm --command -- bash -c "
    ls -lh /data
  " \
  --overrides='{
    "apiVersion": "v1",
    "spec": {
      "containers": [{
        "name": "list-pvc",
        "image": "ubuntu:22.04",
        "command": ["bash","-c","ls -lh /data"],
        "volumeMounts": [{
          "mountPath": "/data",
          "name": "project-storage"
        }]
      }],
      "volumes": [{
        "name": "project-storage",
        "persistentVolumeClaim": { "claimName": "naaxk6-pvc" }
      }]
    }
  }'
If you don't see a command prompt, try pressing enter.
warning: couldn't attach to pod/list-pvc, falling back to streaming logs: Internal error occurred: unable to upgrade connection: container list-pvc not found in pod list-pvc_gp-engine-mizzou-dsa-cloud
ls: cannot access '/data': No such file or directory
pod "list-pvc" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
why can't we just use an existing pod yaml to chck the contgent of the pvc
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud exec -it inspect-pvc -- bash
error: Internal error occurred: unable to upgrade connection: container not found ("inspector")
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud exec -it inspect-pvc -- bash
root@inspect-pvc:/# ls -lh /data
total 1.6G
-rw-r--r-- 1 1000 users  50M Nov 20 19:13 df_chunk_aa
-rw-r--r-- 1 1000 users  50M Nov 20 19:23 df_chunk_ab
-rw-r--r-- 1 1000 users  50M Nov 20 19:31 df_chunk_ac
-rw-r--r-- 1 1000 users  50M Nov 20 19:44 df_chunk_ad
-rw-r--r-- 1 1000 users  50M Nov 20 19:54 df_chunk_ae
-rw-r--r-- 1 1000 users  50M Nov 20 20:06 df_chunk_af
-rw-r--r-- 1 1000 users  50M Nov 20 20:16 df_chunk_ag
-rw-r--r-- 1 1000 users  50M Nov 20 20:26 df_chunk_ah
-rw-r--r-- 1 1000 users  50M Nov 20 20:37 df_chunk_ai
-rw-r--r-- 1 1000 users  50M Nov 20 20:48 df_chunk_aj
-rw-r--r-- 1 1000 users  50M Nov 20 20:58 df_chunk_ak
-rw-r--r-- 1 1000 users  50M Nov 20 21:08 df_chunk_al
-rw-r--r-- 1 1000 users  50M Nov 20 21:20 df_chunk_am
-rw-r--r-- 1 1000 users  50M Nov 20 21:31 df_chunk_an
-rw-r--r-- 1 1000 users  50M Nov 20 21:39 df_chunk_ao
-rw-r--r-- 1 1000 users  36M Nov 20 21:45 df_chunk_ap
-rw------- 1 root root   55M Nov 20 22:28 df_merged_filtered.parquet
-rw-r--r-- 1 root root  786M Nov 20 23:26 df_merged_reassembled.parquet
no i want to keep the name
okay now what' snext
root@inspect-pvc:/# rm /data/df_merged_filtered.parquet
mv /data/df_merged_reassembled.parquet /data/df_merged_filtered.parquet
ls -lh /data
total 1.6G
-rw-r--r-- 1 1000 users  50M Nov 20 19:13 df_chunk_aa
-rw-r--r-- 1 1000 users  50M Nov 20 19:23 df_chunk_ab
-rw-r--r-- 1 1000 users  50M Nov 20 19:31 df_chunk_ac
-rw-r--r-- 1 1000 users  50M Nov 20 19:44 df_chunk_ad
-rw-r--r-- 1 1000 users  50M Nov 20 19:54 df_chunk_ae
-rw-r--r-- 1 1000 users  50M Nov 20 20:06 df_chunk_af
-rw-r--r-- 1 1000 users  50M Nov 20 20:16 df_chunk_ag
-rw-r--r-- 1 1000 users  50M Nov 20 20:26 df_chunk_ah
-rw-r--r-- 1 1000 users  50M Nov 20 20:37 df_chunk_ai
-rw-r--r-- 1 1000 users  50M Nov 20 20:48 df_chunk_aj
-rw-r--r-- 1 1000 users  50M Nov 20 20:58 df_chunk_ak
-rw-r--r-- 1 1000 users  50M Nov 20 21:08 df_chunk_al
-rw-r--r-- 1 1000 users  50M Nov 20 21:20 df_chunk_am
-rw-r--r-- 1 1000 users  50M Nov 20 21:31 df_chunk_an
-rw-r--r-- 1 1000 users  50M Nov 20 21:39 df_chunk_ao
-rw-r--r-- 1 1000 users  36M Nov 20 21:45 df_chunk_ap
-rw-r--r-- 1 root root  786M Nov 20 23:26 df_merged_filtered.parquet
root@inspect-pvc:/# 
i dont see it. jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud delete pod inspect-pvc
pod "inspect-pvc" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f baseline-job.yaml
error: the path "baseline-job.yaml" does not exist
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f baseline_job.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> cpu limit <4> is higher than the maximum allowed ratio of <1.2>
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> memory limit <32Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/baseline-job configured
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-data-download-jlc3q-q47vk      0/1     Pending     0          71m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          22h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          22h
pod-cc5m4-train                    0/1     Error       0          2d1h
pod-dbkyd-train                    0/1     Error       0          11h
pod-pvc-jlc3q                      1/1     Running     0          76m
pod-pvc-jm2rc                      1/1     Running     0          63m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-data-download-jlc3q-q47vk      0/1     Pending     0          71m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          22h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          22h
pod-cc5m4-train                    0/1     Error       0          2d1h
pod-dbkyd-train                    0/1     Error       0          11h
pod-pvc-jlc3q                      1/1     Running     0          76m
pod-pvc-jm2rc                      1/1     Running     0          63m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe job baseline-job | grep -A5 Events
Events:            <none>
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
my baselne yaml file is named baseline_job.yaml
whats next. 
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> cpu limit <4> is higher than the maximum allowed ratio of <1.2>
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> memory limit <32Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/baseline-job configured
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-data-download-jlc3q-q47vk      0/1     Pending     0          76m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          22h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          22h
pod-cc5m4-train                    0/1     Error       0          2d1h
pod-dbkyd-train                    0/1     Error       0          11h
pod-pvc-jlc3q                      1/1     Running     0          81m
pod-pvc-jm2rc                      1/1     Running     0          68m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-data-download-jlc3q-q47vk      0/1     Pending     0          76m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          22h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          22h
pod-cc5m4-train                    0/1     Error       0          2d1h
pod-dbkyd-train                    0/1     Error       0          11h
pod-pvc-jlc3q                      1/1     Running     0          81m
pod-pvc-jm2rc                      1/1     Running     0          68m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get jobs baseline-job
NAME           STATUS   COMPLETIONS   DURATION   AGE
baseline-job   Failed   0/1           13h        13h
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
save all our progress for now. i need to start a new chat
save our progress in memory. number 2. remember everything
like what we did last night. save everything in memory all our progress so ghat when i start a new chat we know wher ewe are
I mean save all our progress about where we are in my project. You did it so many times before why are you being difficult right now
Also do not gaslight me with "Breathe, seriously" or "calm down" 
You're always gaslighting me

ChatGPT can make mistakes. Check important info.


```

**Complete AI Output/Response:**
```
[Paste the full, unedited response from the AI tool]

How to create a docker image 
How do I run it 
I only have my dockerfile I haven't built anything yet 
Do I need to run it locally? I thought you said it's not good for mac it's slow and I can't do cuda. 
I thought I n needed github reposithro. For Docker
Great question, Nat-Nat — and honestly, understanding the difference saves you a LOT of headaches when doing cloud projects. Let me break this down cleanly, in your vibe.

⭐ LOCAL = your actual Mac laptop
This is when you run Docker on your own computer.
✔ Pros:
	•	You control everything
	•	Fast builds if your Mac is powerful
	•	No Nautilus resource limits
	•	No Jupyter timeout issues
	•	Easiest to debug because you see everything directly
✔ Cons:
	•	You must have Docker Desktop installed
	•	Docker Desktop on Mac (especially M-chip) sometimes struggles with PyTorch GPU images (but CPU builds are fine)
	•	Your Mac cannot build GPU-enabled containers that actually use CUDA (because Mac has no CUDA)
But your Dockerfile uses CUDA (pytorch-cuda). That’s the problem:
❗ Your Mac CANNOT build CUDA images
macOS cannot run or emulate:
	•	CUDA runtime
	•	NVIDIA drivers
	•	GPU-enabled PyTorch containers
So your Docker build will fail locally because the base image:

pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime
requires CUDA, which Mac cannot handle.
This means:
❌ You should NOT build this image locally on your Mac.

⭐ JUPYTERHUB = Nautilus terminal on GP-ENGINE
This is running Docker commands inside Nautilus, where:
	•	GPU nodes exist
	•	CUDA drivers exist
	•	NVIDIA runtime is installed
	•	GPU-enabled PyTorch images can build
	•	Everything is Linux-based (compatible)
✔ Pros:
	•	Correct environment for CUDA-based builds
	•	Faster builds (A100/V100 nodes)
	•	No Docker Desktop needed
	•	You can push directly after building
	•	Works with your GPU Dockerfile
✔ Cons:
	•	JupyterHub session can time out after ~12 hours
	•	Storage is limited
	•	Must upload your repo to Nautilus (or git clone it there)
BUT: For a GPU-enabled ML container, this is the right place to build.

💛 TL;DR — Nat-Nat Edition
⭐ If you're building a CUDA-enabled ML Docker image (like yours):
→ Build it on Nautilus JupyterHub terminal
→ NOT on your Mac
Because:
	•	Your Mac has no NVIDIA GPU
	•	CUDA does not run on macOS
	•	GPU docker images cannot be built locally
	•	JupyterHub is the correct environment

⭐ So your next step is:
👉 Build your image inside the JupyterHub terminal.
Meaning: Go to: Nautilus / gp-engine / JupyterHub → Terminal
Then run:

git clone https://github.com/nathanielnat1993/cloud-computing-project.git
cd cloud-computing-project

# Login to GHCR
echo <YOUR_PAT> | docker login ghcr.io -u nathanielnat1993 --password-stdin

# Build CUDA image
docker build -t ghcr.io/nathanielnat1993/cloud-computing-project:latest .

# Push to GHCR
docker push ghcr.io/nathanielnat1993/cloud-computing-project:latest

If you'd like, I can guide you through these one at a time.
Just say:
👉 "Okay, let’s build the image on JupyterHub"

It says no command 
What does it mean? I can't use gou workload 

okay let's continue my cloud computing project. where did we stop
import torch
from transformers import AutoTokenizer


def load_tokenizer():
    return AutoTokenizer.from_pretrained(
        "emilyalsentzer/Bio_ClinicalBERT",
        use_fast=True
    )


def tokenize_overflow_fixed_pt(
    df,
    tokenizer,
    text_col="text",
    label_col="readmitted",
    max_len=512,
    stride=128,
    batch_size=500
):
    ids_parts = []
    mask_parts = []
    map_all = []
    n = len(df)

    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        texts = df[text_col].iloc[start:end].astype(str).tolist()

        enc = tokenizer(
            texts,
            truncation=True,
            padding="max_length",
            max_length=max_len,
            stride=stride,
            return_overflowing_tokens=True,
            return_attention_mask=True,
            return_tensors="pt",
        )

        ids_parts.append(enc["input_ids"])
        mask_parts.append(enc["attention_mask"])

        batch_map = enc["overflow_to_sample_mapping"]
        map_all.extend([start + int(m) for m in batch_map])

        del enc, texts

    input_ids = torch.cat(ids_parts, dim=0)
    attention_mask = torch.cat(mask_parts, dim=0)
    mapping = torch.tensor(map_all, dtype=torch.long)

    base_labels = torch.tensor(df[label_col].tolist(), dtype=torch.long)
    chunk_labels = base_labels[mapping]

    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": chunk_labels,
        "doc_mapping": mapping,
    } for the tokenizatioon part. did i compromise on teh tokenization part?
what would be the benefit of it?
im confused. padding = True or False
is that all i need to change just the padding to False?
well i don't want to change all teh other codes. i want to keep them as is. so which one should i use
is this using gpu? # Tokenizing the splits into chunks, and using rust implementation for faster tokenization.

import torch
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("emilyalsentzer/Bio_ClinicalBERT", use_fast = True)

def tokenize_overflow_fixed_pt(df, text_col = "text", label_col = "readmitted",
                               max_len = 512, stride = 128, batch_size = 500):
    ids_parts, mask_parts, map_all = [], [], []
    n = len(df)

    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        texts = df[text_col].iloc[start:end].astype(str).tolist()
        enc = tok(texts, truncation=True, padding=True, max_length=max_len, stride=stride, return_overflowing_tokens=True,
                  return_attention_mask=True, return_tensors="pt")

        ids_parts.append(enc["input_ids"])
        mask_parts.append(enc["attention_mask"])

        batch_map = enc["overflow_to_sample_mapping"]
        map_all.extend([start + int(m) for m in batch_map])

        del enc, texts

    input_ids = torch.cat(ids_parts, dim=0)
    attention_mask = torch.cat(mask_parts, dim=0)
    mapping = torch.tensor(map_all, dtype=torch.long)

    base_labels = torch.tensor(df[label_col].tolist(), dtype=torch.long)
    chunk_labels = base_labels[mapping]

    return {"input_ids": input_ids, "attention_mask": attention_mask, "labels": chunk_labels, "doc_mapping": mapping,}

train_enc = tokenize_overflow_fixed_pt(df_train)
val_enc   = tokenize_overflow_fixed_pt(df_val)
test_enc  = tokenize_overflow_fixed_pt(df_test)

print("train chunks / docs:", train_enc["input_ids"].shape[0], len(df_train))
print("val chunks / docs:", val_enc["input_ids"].shape[0],   len(df_val))
print("test chunks / docs:", test_enc["input_ids"].shape[0],  len(df_test))
is this using gpu? # Getting embeddings from BioClinicalBERT

from transformers import AutoModel

enc_model = AutoModel.from_pretrained("emilyalsentzer/Bio_ClinicalBERT").to('cuda')
enc_model.eval()

@torch.inference_mode()
def chunk_embeddings(enc, bs=32, use_cls=False):
    X, M = enc["input_ids"], enc["attention_mask"]
    outs = []
    with torch.amp.autocast('cuda'):
        for i in range(0, X.size(0), bs):
            ids  = X[i:i+bs].to('cuda', non_blocking = True)
            mask = M[i:i+bs].to('cuda', non_blocking = True)
            out = enc_model(input_ids = ids, attention_mask = mask, output_hidden_states = False)
            h = out.last_hidden_state
            if use_cls:
                emb = h[:, 0, :]
            else:
                mask_f = mask.unsqueeze(-1).float()
                emb = (h * mask_f).sum(dim=1) / mask_f.sum(dim=1).clamp(min=1e-6)
            outs.append(emb.cpu())
    return torch.cat(outs, dim=0)

def aggregate_docs(chunk_emb: torch.Tensor, doc_map: torch.Tensor):
    E = chunk_emb.numpy()
    D = doc_map.numpy().astype(np.int64)
    n = int(D.max()) + 1 if D.size else 0
    sums = np.zeros((n, E.shape[1]), dtype = np.float32)
    counts = np.zeros(n, dtype = np.int64)
    np.add.at(sums, D, E)
    np.add.at(counts, D, 1)
    return (sums / counts[:, None]).astype(np.float32)

train_chunk_emb = chunk_embeddings(train_enc, bs = 32, use_cls = False)
val_chunk_emb   = chunk_embeddings(val_enc,   bs = 32, use_cls = False)
test_chunk_emb  = chunk_embeddings(test_enc,  bs = 32, use_cls = False)

train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
val_doc_emb   = aggregate_docs(val_chunk_emb,   val_enc["doc_mapping"])
test_doc_emb  = aggregate_docs(test_chunk_emb,  test_enc["doc_mapping"])
what about this code. am i compromising with this code?
im not fine tuning yet. this is just embeddings
so if i am using A100 fo rthis code it should be faster than a weaker gpu right?
does this code aligh with the other codes in my .py files and the dockerfile? i want to make sure tey all work together
this is my docker file. # Use an official PyTorch GPU-enabled runtime
FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime

# Set working directory inside the container
WORKDIR /project

# Copy dependency list into container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code, data folder (empty), and results folder (empty)
COPY src/ ./src
COPY data/ ./data
COPY results/ ./results

# Ensure results folder exists
RUN mkdir -p /project/results/figures

# Set Python path so imports work across src/
ENV PYTHONPATH=/project

# Run the main script when the container starts
CMD ["python", "src/main.py"]
so my dockerfile is correct no changes needed?
does this use gpu? # Training using Logistic Regression

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

y_train = df_train["readmitted"].to_numpy()
y_val   = df_val["readmitted"].to_numpy()
y_test  = df_test["readmitted"].to_numpy()

Xtr, Xva, Xte = train_doc_emb, val_doc_emb, test_doc_emb

clf = LogisticRegression(max_iter = 2000, class_weight = "balanced", n_jobs = -1, solver = "saga", C=1.0)
clf.fit(Xtr, y_train)

val_p  = clf.predict_proba(Xva)[:, 1]
test_p = clf.predict_proba(Xte)[:, 1]

ts = np.linspace(0.01, 0.99, 99)
from sklearn.metrics import f1_score
thr = ts[int(np.argmax([f1_score(y_val, (val_p>=t).astype(int)) for t in ts]))]

val_pred  = (val_p  >= thr)
is it possible that with changing padding to true when i train my logistic regression it won't stop runnikng? it's been alost an hour the trainng logistic code running
 # Getting embeddings from BioClinicalBERT

from transformers import AutoModel

enc_model = AutoModel.from_pretrained("emilyalsentzer/Bio_ClinicalBERT").to('cuda')
enc_model.eval()

@torch.inference_mode()
def chunk_embeddings(enc, bs=32, use_cls=False):
    X, M = enc["input_ids"], enc["attention_mask"]
    outs = []
    with torch.amp.autocast('cuda'):
        for i in range(0, X.size(0), bs):
            ids  = X[i:i+bs].to('cuda', non_blocking = True)
            mask = M[i:i+bs].to('cuda', non_blocking = True)
            out = enc_model(input_ids = ids, attention_mask = mask, output_hidden_states = False)
            h = out.last_hidden_state
            if use_cls:
                emb = h[:, 0, :]
            else:
                mask_f = mask.unsqueeze(-1).float()
                emb = (h * mask_f).sum(dim=1) / mask_f.sum(dim=1).clamp(min=1e-6)
            outs.append(emb.cpu())
    return torch.cat(outs, dim=0)

def aggregate_docs(chunk_emb: torch.Tensor, doc_map: torch.Tensor):
    E = chunk_emb.numpy()
    D = doc_map.numpy().astype(np.int64)
    n = int(D.max()) + 1 if D.size else 0
    sums = np.zeros((n, E.shape[1]), dtype = np.float32)
    counts = np.zeros(n, dtype = np.int64)
    np.add.at(sums, D, E)
    np.add.at(counts, D, 1)
    return (sums / counts[:, None]).astype(np.float32)

train_chunk_emb = chunk_embeddings(train_enc, bs = 32, use_cls = False)
val_chunk_emb   = chunk_embeddings(val_enc,   bs = 32, use_cls = False)
test_chunk_emb  = chunk_embeddings(test_enc,  bs = 32, use_cls = False)

train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
val_doc_emb   = aggregate_docs(val_chunk_emb,   val_enc["doc_mapping"])
test_doc_emb  = aggregate_docs(test_chunk_emb,  test_enc["doc_mapping"]) # Training using Logistic Regression

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

y_train = df_train["readmitted"].to_numpy()
y_val   = df_val["readmitted"].to_numpy()
y_test  = df_test["readmitted"].to_numpy()

Xtr, Xva, Xte = train_doc_emb, val_doc_emb, test_doc_emb

clf = LogisticRegression(max_iter = 2000, class_weight = "balanced", n_jobs = -1, solver = "saga", C=1.0)
clf.fit(Xtr, y_train)

val_p  = clf.predict_proba(Xva)[:, 1]
test_p = clf.predict_proba(Xte)[:, 1]

ts = np.linspace(0.01, 0.99, 99)
from sklearn.metrics import f1_score
thr = ts[int(np.argmax([f1_score(y_val, (val_p>=t).astype(int)) for t in ts]))]

val_pred  = (val_p  >= thr)
test_pred = (test_p >= thr)
Created python scripts for preprocessing and tokenization from my NLP project.
is that accurate for my commit
Created python scripts for preprocessing and tokenization from my NLP project. i did put the scrips for those
import torch
from transformers import AutoTokenizer

# Load the tokenizer = BioClinicalBERT
def load_tokenizer():
    return AutoTokenizer.from_pretrained(
        "emilyalsentzer/Bio_ClinicalBERT",
        use_fast=True
    )

# This function tokenizes the embeddings into 512 tokens
def tokenize_overflow_fixed_pt(
    df,
    tokenizer,
    text_col="text",
    label_col="readmitted",
    max_len=512,
    stride=128,
    batch_size=500
):
    ids_parts = []
    mask_parts = []
    map_all = []
    n = len(df)

    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        texts = df[text_col].iloc[start:end].astype(str).tolist()

        enc = tokenizer(
            texts,
            truncation=True,
            padding="max_length",
            max_length=max_len,
            stride=stride,
            return_overflowing_tokens=True,
            return_attention_mask=True,
            return_tensors="pt",
        )

        ids_parts.append(enc["input_ids"])
        mask_parts.append(enc["attention_mask"])

        batch_map = enc["overflow_to_sample_mapping"]
        map_all.extend([start + int(m) for m in batch_map])

        del enc, texts

    input_ids = torch.cat(ids_parts, dim=0)
    attention_mask = torch.cat(mask_parts, dim=0)
    mapping = torch.tensor(map_all, dtype=torch.long)

    base_labels = torch.tensor(df[label_col].tolist(), dtype=torch.long)
    chunk_labels = base_labels[mapping]

    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": chunk_labels,
        "doc_mapping": mapping,
    }
no this code works. i just need a comment for that function
import numpy as np
import torch
from transformers import AutoModel
from sklearn.linear_model import LogisticRegression

# Load the model for encoding
def load_bioclincial_bert_encoder():
    model = AutoModel.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")
    model = model.to("cuda")
    model.eval()
    return model

# 
@torch.inference_mode()
def chunk_embeddings(enc, encoder, batch_size=32, use_cls=False):
    input_ids = enc["input_ids"]
    attention_mask = enc["attention_mask"]
    outs = []

    with torch.amp.autocast("cuda"):
        for i in range(0, input_ids.size(0), batch_size):
            ids = input_ids[i:i + batch_size].to("cuda", non_blocking=True)
            mask = attention_mask[i:i + batch_size].to("cuda", non_blocking=True)

            out = encoder(
                input_ids=ids,
                attention_mask=mask,
                output_hidden_states=False
            )

            h = out.last_hidden_state
            if use_cls:
                emb = h[:, 0, :]
            else:
                mask_f = mask.unsqueeze(-1).float()
                emb = (h * mask_f).sum(dim=1) / mask_f.sum(dim=1).clamp(min=1e-6)

            outs.append(emb.cpu())

    return torch.cat(outs, dim=0)


def aggregate_docs(chunk_emb, doc_map):
    E = chunk_emb.numpy()
    D = doc_map.numpy().astype(np.int64)
    n = int(D.max()) + 1 if D.size else 0

    sums = np.zeros((n, E.shape[1]), dtype=np.float32)
    counts = np.zeros(n, dtype=np.int64)

    np.add.at(sums, D, E)
    np.add.at(counts, D, 1)

    return (sums / counts[:, None]).astype(np.float32)

# Trains the Logistic Regression baseline model from the embeddings
def train_logistic_regression(X_train, y_train):
    clf = LogisticRegression(
        max_iter=2000,
        class_weight="balanced",
        n_jobs=-1,
        solver="saga",
        C=1.0
    )
    clf.fit(X_train, y_train)
    return clf
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
)


def evaluate_with_threshold(y_true, probas):
    thresholds = np.linspace(0.01, 0.99, 99)
    f1_vals = [f1_score(y_true, (probas >= t).astype(int)) for t in thresholds]
    best_t = thresholds[int(np.argmax(f1_vals))]
    preds = (probas >= best_t).astype(int)
    return best_t, preds


def report_metrics(name, y_true, y_pred, probas, threshold):
    print("\n{} threshold = {:.3f}".format(name, threshold))
    print("acc :", accuracy_score(y_true, y_pred))
    print("prec:", precision_score(y_true, y_pred, zero_division=0))
    print("rec :", recall_score(y_true, y_pred, zero_division=0))
    print("f1  :", f1_score(y_true, y_pred, zero_division=0))
    print("auc :", roc_auc_score(y_true, probas))
    print("cmat:\n", confusion_matrix(y_true, y_pred))
is the threshold based on the f1 score? would it it be better if recall?
give me the corrected code for rrecall
yes
shoudl i also do pr auc?
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
so right now. i just want to test it out first using the base line mode. is my main .py okay with just running the baseline model?
you're the one that gave me the code for main
import argparse
import pandas as pd

from preprocessing import apply_cleaning, stratified_group_split
from tokenization import load_tokenizer, tokenize_overflow_fixed_pt

from baseline_model import (
    load_bioclincial_bert_encoder,
    chunk_embeddings,
    aggregate_docs,
    train_logistic_regression,
)
from baseline_evaluate import evaluate_with_threshold, report_metrics

from finetune_model import (
    subset_by_docs,
    finetune_classifier,
    infer_logits
)
from finetune_evaluate import (
    softmax_np,
    aggregate_mean,
    best_threshold_f1,
    report as report_ft
)


def run_baseline(df_train, df_val, df_test, tokenizer):
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc = tokenize_overflow_fixed_pt(df_test, tokenizer)

    encoder = load_bioclincial_bert_encoder()

    train_chunk_emb = chunk_embeddings(train_enc, encoder)
    val_chunk_emb = chunk_embeddings(val_enc, encoder)
    test_chunk_emb = chunk_embeddings(test_enc, encoder)

    train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
    val_doc_emb = aggregate_docs(val_chunk_emb, val_enc["doc_mapping"])
    test_doc_emb = aggregate_docs(test_chunk_emb, test_enc["doc_mapping"])

    y_train = df_train["readmitted"].to_numpy()
    y_val = df_val["readmitted"].to_numpy()
    y_test = df_test["readmitted"].to_numpy()

    clf = train_logistic_regression(train_doc_emb, y_train)

    val_p = clf.predict_proba(val_doc_emb)[:, 1]
    test_p = clf.predict_proba(test_doc_emb)[:, 1]

    best_t, val_pred = evaluate_with_threshold(y_val, val_p)
    _, test_pred = evaluate_with_threshold(y_test, test_p)

    report_metrics("VAL", y_val, val_pred, val_p, best_t)
    report_metrics("TEST", y_test, test_pred, test_p, best_t)


def run_finetune(df_train, df_val, df_test, tokenizer):
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc = tokenize_overflow_fixed_pt(df_test, tokenizer)

    train_small = subset_by_docs(train_enc, doc_count=10000)

    model = finetune_classifier(train_small)

    val_logits = infer_logits(model, val_enc)
    test_logits = infer_logits(model, test_enc)

    val_doc_logits = aggregate_mean(val_logits, val_enc["doc_mapping"])
    test_doc_logits = aggregate_mean(test_logits, test_enc["doc_mapping"])

    val_p = softmax_np(val_doc_logits)[:, 1]
    test_p = softmax_np(test_doc_logits)[:, 1]

    y_val = df_val["readmitted"].to_numpy()
    y_test = df_test["readmitted"].to_numpy()

    thr = best_threshold_f1(y_val, val_p)

    val_pred = (val_p >= thr)
    test_pred = (test_p >= thr)

    report_ft("VAL", y_val, val_pred, val_p, thr)
    report_ft("TEST", y_test, test_pred, test_p, thr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True,
                        choices=["baseline", "finetune", "both"])
    args = parser.parse_args()

    df = pd.read_parquet("/project/data/df_merged_filtered.parquet")

    df = apply_cleaning(df)
    df_train, df_val, df_test = stratified_group_split(df)

    tokenizer = load_tokenizer()

    if args.mode == "baseline":
        run_baseline(df_train, df_val, df_test, tokenizer)

    elif args.mode == "finetune":
        run_finetune(df_train, df_val, df_test, tokenizer)

    elif args.mode == "both":
        run_baseline(df_train, df_val, df_test, tokenizer)
        run_finetune(df_train, df_val, df_test, tokenizer)


if __name__ == "__main__":
    main()
so im using the github mobile app and i already added the .ds_store in in .gitignore but it's still asking me if i want to cmmit it. 
fatal: Authentication failed for 'https://github.com/nathanielnat1993/cloud-computing-project.git/'
(base) nat-nat@Mac cloud-computing-project % git push
Username for 'https://github.com': nathanielnat1993
Password for 'https://nathanielnat1993@github.com':  how come it's not working authentication failed wrong password or something. I copied my password and pasted it
where in settings do i go for tokens
Okay then what do i need to jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ git push
To github.com:nathanielnat1993/cloud-computing-project.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:nathanielnat1993/cloud-computing-project.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
is it okay for me to still use this main.py even though i only plan to just use the baseline mofel for now and not run the finetune? import argparse
import pandas as pd

from preprocessing import apply_cleaning, stratified_group_split
from tokenization import load_tokenizer, tokenize_overflow_fixed_pt

from baseline_model import (
    load_bioclincial_bert_encoder,
    chunk_embeddings,
    aggregate_docs,
    train_logistic_regression,
)
from baseline_evaluate import evaluate_with_threshold, report_metrics

from finetune_model import (
    subset_by_docs,
    finetune_classifier,
    infer_logits
)
from finetune_evaluate import (
    softmax_np,
    aggregate_mean,
    best_threshold_f1,
    report as report_ft
)


def run_baseline(df_train, df_val, df_test, tokenizer):
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc = tokenize_overflow_fixed_pt(df_test, tokenizer)

    encoder = load_bioclincial_bert_encoder()

    train_chunk_emb = chunk_embeddings(train_enc, encoder)
    val_chunk_emb = chunk_embeddings(val_enc, encoder)
    test_chunk_emb = chunk_embeddings(test_enc, encoder)

    train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
    val_doc_emb = aggregate_docs(val_chunk_emb, val_enc["doc_mapping"])
    test_doc_emb = aggregate_docs(test_chunk_emb, test_enc["doc_mapping"])

    y_train = df_train["readmitted"].to_numpy()
    y_val = df_val["readmitted"].to_numpy()
    y_test = df_test["readmitted"].to_numpy()

    clf = train_logistic_regression(train_doc_emb, y_train)

    val_p = clf.predict_proba(val_doc_emb)[:, 1]
    test_p = clf.predict_proba(test_doc_emb)[:, 1]

    best_t, val_pred = evaluate_with_threshold(y_val, val_p)
    _, test_pred = evaluate_with_threshold(y_test, test_p)

    report_metrics("VAL", y_val, val_pred, val_p, best_t)
    report_metrics("TEST", y_test, test_pred, test_p, best_t)


def run_finetune(df_train, df_val, df_test, tokenizer):
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc = tokenize_overflow_fixed_pt(df_test, tokenizer)

    train_small = subset_by_docs(train_enc, doc_count=10000)

    model = finetune_classifier(train_small)

    val_logits = infer_logits(model, val_enc)
    test_logits = infer_logits(model, test_enc)

    val_doc_logits = aggregate_mean(val_logits, val_enc["doc_mapping"])
    test_doc_logits = aggregate_mean(test_logits, test_enc["doc_mapping"])

    val_p = softmax_np(val_doc_logits)[:, 1]
    test_p = softmax_np(test_doc_logits)[:, 1]

    y_val = df_val["readmitted"].to_numpy()
    y_test = df_test["readmitted"].to_numpy()

    thr = best_threshold_f1(y_val, val_p)

    val_pred = (val_p >= thr)
    test_pred = (test_p >= thr)

    report_ft("VAL", y_val, val_pred, val_p, thr)
    report_ft("TEST", y_test, test_pred, test_p, thr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True,
                        choices=["baseline", "finetune", "both"])
    args = parser.parse_args()

    df = pd.read_parquet("/project/data/df_merged_filtered.parquet")

    df = apply_cleaning(df)
    df_train, df_val, df_test = stratified_group_split(df)

    tokenizer = load_tokenizer()

    if args.mode == "baseline":
        run_baseline(df_train, df_val, df_test, tokenizer)

    elif args.mode == "finetune":
        run_finetune(df_train, df_val, df_test, tokenizer)

    elif args.mode == "both":
        run_baseline(df_train, df_val, df_test, tokenizer)
        run_finetune(df_train, df_val, df_test, tokenizer)


if __name__ == "__main__":
    main()
import argparse
import pandas as pd

from preprocessing import apply_cleaning, stratified_group_split
from tokenization import load_tokenizer, tokenize_overflow_fixed_pt

from baseline_model import (
    load_bioclincial_bert_encoder,
    chunk_embeddings,
    aggregate_docs,
    train_logistic_regression,
)
from baseline_evaluate import evaluate_with_threshold, report_metrics

from finetune_model import (
    subset_by_docs,
    finetune_classifier,
    infer_logits
)
from finetune_evaluate import (
    softmax_np,
    aggregate_mean,
    best_threshold_f1,
    report as report_ft
)


def run_baseline(df_train, df_val, df_test, tokenizer):
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc = tokenize_overflow_fixed_pt(df_test, tokenizer)

    encoder = load_bioclincial_bert_encoder()

    train_chunk_emb = chunk_embeddings(train_enc, encoder)
    val_chunk_emb = chunk_embeddings(val_enc, encoder)
    test_chunk_emb = chunk_embeddings(test_enc, encoder)

    train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
    val_doc_emb = aggregate_docs(val_chunk_emb, val_enc["doc_mapping"])
    test_doc_emb = aggregate_docs(test_chunk_emb, test_enc["doc_mapping"])

    y_train = df_train["readmitted"].to_numpy()
    y_val = df_val["readmitted"].to_numpy()
    y_test = df_test["readmitted"].to_numpy()

    clf = train_logistic_regression(train_doc_emb, y_train)

    val_p = clf.predict_proba(val_doc_emb)[:, 1]
    test_p = clf.predict_proba(test_doc_emb)[:, 1]

    best_t, val_pred = evaluate_with_threshold(y_val, val_p)
    _, test_pred = evaluate_with_threshold(y_test, test_p)

    report_metrics("VAL", y_val, val_pred, val_p, best_t)
    report_metrics("TEST", y_test, test_pred, test_p, best_t)


def run_finetune(df_train, df_val, df_test, tokenizer):
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc = tokenize_overflow_fixed_pt(df_test, tokenizer)

    train_small = subset_by_docs(train_enc, doc_count=10000)

    model = finetune_classifier(train_small)

    val_logits = infer_logits(model, val_enc)
    test_logits = infer_logits(model, test_enc)

    val_doc_logits = aggregate_mean(val_logits, val_enc["doc_mapping"])
    test_doc_logits = aggregate_mean(test_logits, test_enc["doc_mapping"])

    val_p = softmax_np(val_doc_logits)[:, 1]
    test_p = softmax_np(test_doc_logits)[:, 1]

    y_val = df_val["readmitted"].to_numpy()
    y_test = df_test["readmitted"].to_numpy()

    thr = best_threshold_f1(y_val, val_p)

    val_pred = (val_p >= thr)
    test_pred = (test_p >= thr)

    report_ft("VAL", y_val, val_pred, val_p, thr)
    report_ft("TEST", y_test, test_pred, test_p, thr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True,
                        choices=["baseline", "finetune", "both"])
    args = parser.parse_args()

    df = pd.read_parquet("/project/data/df_merged_filtered.parquet")

    df = apply_cleaning(df)
    df_train, df_val, df_test = stratified_group_split(df)

    tokenizer = load_tokenizer()

    if args.mode == "baseline":
        run_baseline(df_train, df_val, df_test, tokenizer)

    elif args.mode == "finetune":
        run_finetune(df_train, df_val, df_test, tokenizer)

    elif args.mode == "both":
        run_baseline(df_train, df_val, df_test, tokenizer)
        run_finetune(df_train, df_val, df_test, tokenizer)


if __name__ == "__main__":
    main() revise it to remove the fine tune one for now.
what do you mean f1 based. didn't we change it to recall?
okay also give me the version with the fine tuning included there
i like how the other one is formatted like one lines
give me the one for just the baseline version
do we also need to change gthis one to recall focused? import numpy as np
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


def softmax_np(x):
    x = x - x.max(axis=1, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=1, keepdims=True)


def aggregate_mean(logits_tensor, doc_map_tensor):
    L = logits_tensor.numpy()
    D = doc_map_tensor.numpy()
    n = int(D.max()) + 1 if D.size else 0

    sums = np.zeros((n, L.shape[1]), dtype=np.float32)
    np.add.at(sums, D, L)
    counts = np.bincount(D, minlength=n).astype(np.float32)[:, None]

    return sums / counts


def best_threshold_f1(y, p):
    ts = np.linspace(0.01, 0.99, 99)
    f1s = [f1_score(y, (p >= t).astype(int)) for t in ts]
    return ts[int(np.argmax(f1s))]


def report(split, y, pred, p, thr):
    print("\n{} @threshold = {:.3f}".format(split, thr))
    print("precision:", precision_score(y, pred, zero_division=0))
    print("recall   :", recall_score(y, pred, zero_division=0))
    print("f1       :", f1_score(y, pred, zero_division=0))
    print("roc_auc  :", roc_auc_score(y, p))
    print("cmat:\n", confusion_matrix(y, pred))
so is this right? import numpy as np
import torch
import torch.nn.functional as F
from transformers import (
    AutoModelForSequenceClassification,
    get_linear_schedule_with_warmup
)
from collections import Counter


def subset_by_docs(enc, doc_count, seed=42):
    rng = np.random.default_rng(seed)
    n_docs = int(enc["doc_mapping"].max()) + 1
    pick = rng.choice(n_docs, size=min(doc_count, n_docs), replace=False)
    mask = torch.isin(enc["doc_mapping"], torch.tensor(pick))
    return {k: v[mask] for k, v in enc.items()}


def load_classifier():
    model = AutoModelForSequenceClassification.from_pretrained(
        "emilyalsentzer/Bio_ClinicalBERT",
        num_labels=2
    )
    model = model.to("cuda")
    model.train()
    return model


def prepare_class_weights(enc):
    cnt = Counter(enc["labels"].tolist())
    w0, w1 = cnt.get(0, 1), cnt.get(1, 1)
    cls_w = torch.tensor(
        [(w0 + w1) / (2 * w0), (w0 + w1) / (2 * w1)],
        device="cuda",
        dtype=torch.float
    )
    return cls_w


def batch_iter(enc, bs):
    X = enc["input_ids"]
    M = enc["attention_mask"]
    Y = enc["labels"]

    idx = torch.randperm(X.size(0))
    for i in range(0, X.size(0), bs):
        j = idx[i:i + bs]
        yield X[j], M[j], Y[j]


def finetune_classifier(enc, max_steps=3000, bs=16, lr=1e-3):
    model = load_classifier()

    for name, param in model.named_parameters():
        if not name.startswith("classifier"):
            param.requires_grad = False

    cls_w = prepare_class_weights(enc)

    opt = torch.optim.AdamW(
        filter(lambda p: p.requires_grad, model.parameters()),
        lr=lr
    )
    warmup = int(max_steps * 0.06)
    sched = get_linear_schedule_with_warmup(
        opt,
        num_warmup_steps=warmup,
        num_training_steps=max_steps
    )

    scaler = torch.cuda.amp.GradScaler(enabled=True)

    step = 0
    for ids, mask, y in batch_iter(enc, bs):
        if step >= max_steps:
            break

        ids = ids.to("cuda")
        mask = mask.to("cuda")
        y = y.to("cuda")

        opt.zero_grad(set_to_none=True)

        with torch.amp.autocast("cuda"):
            out = model(input_ids=ids, attention_mask=mask)
            loss = F.cross_entropy(out.logits, y, weight=cls_w)

        scaler.scale(loss).backward()
        scaler.step(opt)
        scaler.update()
        sched.step()

        step += 1

    model.eval()
    return model


@torch.inference_mode()
def infer_logits(model, enc, bs=32):
    DEVICE = next(model.parameters()).device
    X = enc["input_ids"]
    M = enc["attention_mask"]
    outs = []

    with torch.amp.autocast("cuda" if DEVICE.type == "cuda" else "cpu"):
        for i in range(0, X.size(0), bs):
            ids = X[i:i + bs].to(DEVICE, non_blocking=True)
            mask = M[i:i + bs].to(DEVICE, non_blocking=True)
            outs.append(model(input_ids=ids, attention_mask=mask).logits.cpu())

    return torch.cat(outs, dim=0)
okay for this one just kind of mimic how the other one is formatte with the names for the report. import numpy as np
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


def softmax_np(x):
    x = x - x.max(axis=1, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=1, keepdims=True)


def aggregate_mean(logits_tensor, doc_map_tensor):
    L = logits_tensor.numpy()
    D = doc_map_tensor.numpy()
    n = int(D.max()) + 1 if D.size else 0

    sums = np.zeros((n, L.shape[1]), dtype=np.float32)
    np.add.at(sums, D, L)
    counts = np.bincount(D, minlength=n).astype(np.float32)[:, None]

    return sums / counts


def best_threshold_f1(y, p):
    ts = np.linspace(0.01, 0.99, 99)
    f1s = [f1_score(y, (p >= t).astype(int)) for t in ts]
    return ts[int(np.argmax(f1s))]


def report(split, y, pred, p, thr):
    print("\n{} @threshold = {:.3f}".format(split, thr))
    print("precision:", precision_score(y, pred, zero_division=0))
    print("recall   :", recall_score(y, pred, zero_division=0))
    print("f1       :", f1_score(y, pred, zero_division=0))
    print("roc_auc  :", roc_auc_score(y, p))
    print("cmat:\n", confusion_matrix(y, pred))
is my dockerfile righr? # Use an official PyTorch GPU-enabled runtime
FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime

# Set working directory inside the container
WORKDIR /project

# Copy dependency list into container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code, data folder (empty), and results folder (empty)
COPY src/ ./src
COPY data/ ./data
COPY results/ ./results

# Ensure results folder exists
RUN mkdir -p /project/results/figures

# Set Python path so imports work across src/
ENV PYTHONPATH=/project

# Run the main script when the container starts
CMD ["python", "src/main.py"]
why does the results folder says empty? there are files there but empty
no what im saying is why did you put it's empty when its not
what should be the next step? my yaml files are still empty and the docs folder files are still empty
wait. should i put my parquet file in data folder?
what no. the docs folder has thiese. docs/
|_ SETUP.md # Detailed setup and execution guide
|_ CLOUD_SETUP.md # Nautilus-specific instructions
|_ RESULTS.md # Results summary and analysis
well for now let's not worry about the fine tuning. as for gpu, yes i plan on using gpu but how do i know if by default nautilus provides gpu? I chdcked and I can request for A100 but Im not sure if that means I also get to use weaker gpu if I don't request
but how do i request gpu
No i mean on the NRP website there's a button to request A100 GPU. But does that mean if I don't request i can't put gpu in my yaml file?
okay. let's proceed with the yaml files
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: project-pvc
spec:
  storageClassName: rook-cephfs	
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 50Gi.  is this okay if i put storageclassname?
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: naaxk6-pvc
spec:
  storageClassName: rook-cephfs
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 50Gi i changed the name
should i copy this in the pvc.yml file?
what about the baseline-job yaml
what's my imga name?
i don't know. we've only been using nautilus/gp-engine
how come we never had to create an image in class when we ran pods and created a pvc
okay so how do we do this
what's the difference between local and jupyterhub
did we already create the baseline job yaml
wehre did you get that nathaniel nat image name from
where did you get hte project-storage name
this is my job copy yamp apiVersion: batch/v1
kind: Job
metadata:
  name: job-data-download-naaxk6
spec:
  template:
    spec:
      automountServiceAccountToken: false
      containers:
      - name: pod-data-download-naaxk6
        image: ubuntu:20.04
        command: ["/bin/sh","-c"]
        args:
        - cp -r /ccdata/* /data/
        volumeMounts:
        - mountPath: /ccdata
          name: source
        - mountPath: /data
          name: destination 
        resources:
            limits:
              memory: 10Gi
              cpu: "4"
            requests:
              memory: 10Gi
              cpu: "4"     
      volumes:
      - name: source
        persistentVolumeClaim:
          claimName: cloudcomp-data
      - name: destination
        persistentVolumeClaim:
          claimName: naaxk6-pv
      restartPolicy: Never      
  backoffLimit: 0
okay i copied the baseline-job yaml
is this a good commit comment. Added Dockerfile, yaml for my baseline model job, and my pvc yaml file
okay let's proceed with the image
i dont see read and write packages in permissions
no packages
i did select my cloud computing repo but there's no packages
wait how do. i login to ghcr?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ echo 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 | docker login ghcr.io -u nathanielnat1993 --password-stdin
bash: docker: command not found
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
how do i add that folder to my repo
what do i paste? what's the classic pat?
so this? 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
okay what's next. i pasted the pat
am i pushing this big ass file?
not th eparquet but the image
does it take a while it seemed to stop here but it says it's still running. #16 pushing layer 18defcb9e692 7.97GB / 8.07GB 242.8s
is there a way to change the commit comment
do i still need the pat?
okay it says it's completed
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl apply -f kubernetes/pvc.yaml
Error from server (Forbidden): error when retrieving current configuration of:
Resource: "/v1, Resource=persistentvolumeclaims", GroupVersionKind: "/v1, Kind=PersistentVolumeClaim"
Name: "naaxk6-pvc", Namespace: "default"
from server for: "kubernetes/pvc.yaml": persistentvolumeclaims "naaxk6-pvc" is forbidden: User "http://cilogon.org/serverF/users/406832" cannot get resource "persistentvolumeclaims" in API group "" in the namespace "default"
this worked. jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f kubernetes/pvc.yaml
persistentvolumeclaim/naaxk6-pvc created
kubectl -n gp-engine-mizzou-dsa-cloud why did i have to do this to run? do i need to update anything inmy files or code?
how come my class exercise it did not include the namespace but it still ran. apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: naaxk6-pv
spec:
  storageClassName: rook-cephfs	
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 50Gi
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl config view --minify
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://67.58.53.148:443
  name: nautilus
contexts:
- context:
    cluster: nautilus
    user: oidc
  name: nautilus
current-context: nautilus
kind: Config
preferences: {}
users:
- name: oidc
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1beta1
      args:
      - oidc-login
      - get-token
      - --token-cache-storage=disk
      - --oidc-issuer-url=https://authentik.nrp-nautilus.io/application/o/k8s/
      - --oidc-client-id=xrxBIaWxeRmGJUwSvaLjUzMEFZzQu2b4nk9I0B2W
      - --listen-address=0.0.0.0:8000
      - --oidc-extra-scope=profile,offline_access
      - --grant-type=device-code
      - --skip-open-browser
      command: kubectl
      env: null
      interactiveMode: IfAvailable
      provideClusterInfo: false
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
can i just not update teh files but instead just include this when i do something. gp-engine-mizzou-dsa-cloud
okay let's just add the namespace then
the 2nd one is not part of this project
hwo do i Make sure the image matches your real GHCR image.
it says no packages
oh okay so this is it. docker pull ghcr.io/nathanielnat1993/cloud-computing-project:latest
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl apply -f kubernetes/baseline_job.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> has no memory limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> has no resource requests
Error from server (Forbidden): error when creating "kubernetes/baseline_job.yaml": admission webhook "validation.gatekeeper.sh" denied the request: [container-must-have-limits-and-requests] container <baseline> does not have <{"cpu", "memory"}> requests defined
[container-must-have-limits-and-requests] container <baseline> does not have <{"memory"}> limits defined
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
also my base line yaml file is named baseline_job.yaml not baseline-job.yaml
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl apply -f kubernetes/baseline_job.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> cpu limit <4> is higher than the maximum allowed ratio of <1.2>
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> memory limit <32Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/baseline-job created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get pods -n gp-engine-mizzou-dsa-cloud
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-28xkh                 0/1     ContainerCreating   0          81s
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          7h50m
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          7h49m
pod-cc5m4-train                    0/1     Error               0          35h
pod-gcfpx-train                    1/1     Running             0          3h31m
pod-name-ljabxf                    1/1     Running             0          3h32m
pod-pvc-jm2rc                      1/1     Running             0          4h22m
pvc-checker                        0/1     Error               0          11h
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$  which one is mine
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl describe pod baseline-job-28xkh -n gp-engine-mizzou-dsa-cloud
Name:             baseline-job-28xkh
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-gpu-01.calit2.optiputer.net/67.58.51.142
Start Time:       Thu, 20 Nov 2025 09:35:10 +0000
Labels:           batch.kubernetes.io/controller-uid=dd27e9b3-3d3e-410e-8c07-1991eb12d4fa
                  batch.kubernetes.io/job-name=baseline-job
                  controller-uid=dd27e9b3-3d3e-410e-8c07-1991eb12d4fa
                  job-name=baseline-job
Annotations:      cni.projectcalico.org/containerID: 822880fa07d9a59b64a20c0c53adc4cef125f6050dcc7560cacd577f0d027f26
                  cni.projectcalico.org/podIP: 10.244.28.28/32
                  cni.projectcalico.org/podIPs: 10.244.28.28/32,fdf0:17b3:c3ec:1f79:10:0:5:eed8/128
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/baseline-job
Containers:
  baseline:
    Container ID:  
    Image:         ghcr.io/nathanielnat1993/cloud-computing-project:latest
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      python
      src/main.py
      --mode
      baseline
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:             4
      memory:          32Gi
      nvidia.com/gpu:  1
    Requests:
      cpu:             2
      memory:          16Gi
      nvidia.com/gpu:  1
    Environment:       <none>
    Mounts:
      /project/data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-mbjv2 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-mbjv2:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason                  Age    From                     Message
  ----    ------                  ----   ----                     -------
  Normal  Scheduled               2m58s  default-scheduler        Successfully assigned gp-engine-mizzou-dsa-cloud/baseline-job-28xkh to k8s-gpu-01.calit2.optiputer.net
  Normal  SuccessfulAttachVolume  2m57s  attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-d64c959a-1fdb-4774-95aa-f6e337f1fc1a"
  Normal  Pulling                 2m53s  kubelet                  Pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
whit its running can i commit the changes to those yaml files
it still says container running
how long would it take?
in the meantime, do i need to put my parquet file in data folder?
can i put it in my data folder locally? i cloned the repo locally using the desktop app.
no. the file is stored locally since it's 800 mb
what should be teh commit comment
for the pcv explorer
/Users/nat-nat/Desktop/project-root/data/df_merged_filtered.parquet
i thought i had to run cd /Users/nat-nat/Desktop/project-root/data/df_merged_filtered.parquet first
(base) nat-nat@Mac data % kubectl cp df_merged_filtered.parquet \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet

Error from server (NotFound): pods "pvc-explorer" not found
(base) nat-nat@Mac data % 
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-28xkh                 0/1     ImagePullBackOff    0          22m
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          8h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          8h
pod-cc5m4-train                    0/1     Error               0          35h
pod-gcfpx-train                    1/1     Running             0          3h51m
pod-name-ljabxf                    1/1     Running             0          3h53m
pod-pvc-jm2rc                      1/1     Running             0          4h43m
pvc-checker                        0/1     Error               0          12h
pvc-explorer                       0/1     ContainerCreating   0          16s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
(base) nat-nat@Mac data % kubectl cp df_merged_filtered.parquet \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet
 okay so i pasted this but nothing happened. do i njust wait
do i do this step in terminal? like right now while running?
(base) nat-nat@Mac data % kubectl cp df_merged_filtered.parquet \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet

kubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- bash

E1120 00:01:13.751825   75620 v2.go:150] "Unhandled Error" err="next reader: read tcp 192.168.1.232:56890->67.58.53.148:443: i/o timeout"
E1120 00:01:13.751837   75620 v2.go:167] "Unhandled Error" err="next reader: read tcp 192.168.1.232:56890->67.58.53.148:443: i/o timeout"
E1120 00:01:13.751852   75620 v2.go:129] "Unhandled Error" err="next reader: read tcp 192.168.1.232:56890->67.58.53.148:443: i/o timeout"
E1120 00:01:13.753505   75620 v2.go:104] "Unhandled Error" err="write tcp 192.168.1.232:56890->67.58.53.148:443: use of closed network connection"
error: error reading from error stream: next reader: read tcp 192.168.1.232:56890->67.58.53.148:443: i/o timeout
(base) nat-nat@Mac data % kubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- bash

root@pvc-explorer:/# 
root@pvc-explorer:/# 
root@pvc-explorer:/# ls -lh /data
total 23M
-rw------- 1 root root 23M Nov 20 10:01 df_merged_filtered.parquet
root@pvc-explorer:/# 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get pods -n gp-engine-mizzou-dsa-cloud
NAME                               READY   STATUS             RESTARTS   AGE
baseline-job-28xkh                 0/1     ImagePullBackOff   0          27m
job-ljabxf-resnet18-train-qbksm    0/1     Completed          0          8h
job-ljabxf-simpledla-train-82bgh   0/1     Completed          0          8h
pod-cc5m4-train                    0/1     Error              0          35h
pod-gcfpx-train                    1/1     Running            0          3h57m
pod-name-ljabxf                    1/1     Running            0          3h58m
pod-pvc-jm2rc                      1/1     Running            0          4h49m
pvc-checker                        0/1     Error              0          12h
pvc-explorer                       1/1     Running            0          5m38s
command not found
i did it in my terminal mac
(base) nat-nat@Mac ~ % docker --version
docker images

Docker version 28.5.2, build ecc6942
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
(base) nat-nat@Mac ~ %  what's next
wait wait. cd /Users/nat-nat/Desktop/project-root this directory is not my repo directory. this is just a copy of that repo but is not connected ot github
/Users/nat-nat/Documents/GitHub/cloud-computing-project
i don't have my pat anymore
okay so i ran the code and right now the imga is buidling in my terminal
 1 warning found (use docker --debug to expand):
 - InvalidBaseImagePlatform: Base image pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime was pulled with platform "linux/amd64", expected "linux/arm64" for current build (line 2)
(base) nat-nat@Mac cloud-computing-project % 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl apply -f kubernetes/baseline_job.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> cpu limit <4> is higher than the maximum allowed ratio of <1.2>
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> memory limit <32Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/baseline-job created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
baseline-job-fm2s5                 0/1     ErrImagePull   0          45s
job-ljabxf-resnet18-train-qbksm    0/1     Completed      0          8h
job-ljabxf-simpledla-train-82bgh   0/1     Completed      0          8h
pod-cc5m4-train                    0/1     Error          0          36h
pod-gcfpx-train                    1/1     Running        0          4h21m
pod-name-ljabxf                    1/1     Running        0          4h22m
pod-pvc-jm2rc                      1/1     Running        0          5h12m
pvc-checker                        0/1     Error          0          12h
pvc-explorer                       1/1     Running        0          29m
ovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl describe pod baseline-job-fm2s5 -n gp-engine-mizzou-dsa-cloud
Name:             baseline-job-fm2s5
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-gpu-01.calit2.optiputer.net/67.58.51.142
Start Time:       Thu, 20 Nov 2025 10:25:42 +0000
Labels:           batch.kubernetes.io/controller-uid=e47b7fa8-8ef5-4f46-b407-71b70435ca5a
                  batch.kubernetes.io/job-name=baseline-job
                  controller-uid=e47b7fa8-8ef5-4f46-b407-71b70435ca5a
                  job-name=baseline-job
Annotations:      cni.projectcalico.org/containerID: f190fcff2cde4ac2faa00e55c149191bd5321eb70c96ef7710cb2f73386587de
                  cni.projectcalico.org/podIP: 10.244.28.51/32
                  cni.projectcalico.org/podIPs: 10.244.28.51/32,fdf0:17b3:c3ec:1f79:10:0:5:eed3/128
Status:           Pending
IP:               10.244.28.51
IPs:
  IP:           10.244.28.51
  IP:           fdf0:17b3:c3ec:1f79:10:0:5:eed3
Controlled By:  Job/baseline-job
Containers:
  baseline:
    Container ID:  
    Image:         ghcr.io/nathanielnat1993/cloud-computing-project:latest
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      python
      src/main.py
      --mode
      baseline
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:             4
      memory:          32Gi
      nvidia.com/gpu:  1
    Requests:
      cpu:             2
      memory:          16Gi
      nvidia.com/gpu:  1
    Environment:       <none>
    Mounts:
      /project/data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-chbbv (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-chbbv:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type     Reason                  Age                From                     Message
  ----     ------                  ----               ----                     -------
  Normal   Scheduled               83s                default-scheduler        Successfully assigned gp-engine-mizzou-dsa-cloud/baseline-job-fm2s5 to k8s-gpu-01.calit2.optiputer.net
  Normal   SuccessfulAttachVolume  82s                attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-d64c959a-1fdb-4774-95aa-f6e337f1fc1a"
  Normal   Pulling                 33s (x3 over 71s)  kubelet                  Pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
  Warning  Failed                  32s (x3 over 70s)  kubelet                  Failed to pull image "ghcr.io/nathanielnat1993/cloud-computing-project:latest": failed to pull and unpack image "ghcr.io/nathanielnat1993/cloud-computing-project:latest": failed to resolve reference "ghcr.io/nathanielnat1993/cloud-computing-project:latest": failed to authorize: failed to fetch anonymous token: unexpected status from GET request to https://ghcr.io/token?scope=repository%3Anathanielnat1993%2Fcloud-computing-project%3Apull&service=ghcr.io: 401 Unauthorized
  Warning  Failed                  32s (x3 over 70s)  kubelet                  Error: ErrImagePull
  Normal   BackOff                 3s (x4 over 69s)   kubelet                  Back-off pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
  Warning  Failed                  3s (x4 over 69s)   kubelet                  Error: ImagePullBackOff
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
it's still error. jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl describe pod baseline-job-lpbq9 -n gp-engine-mizzou-dsa-cloud
Name:             baseline-job-lpbq9
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-gpu-01.calit2.optiputer.net/67.58.51.142
Start Time:       Thu, 20 Nov 2025 10:29:53 +0000
Labels:           batch.kubernetes.io/controller-uid=83876d0d-0185-4c6e-984e-f0d3a5fbe21a
                  batch.kubernetes.io/job-name=baseline-job
                  controller-uid=83876d0d-0185-4c6e-984e-f0d3a5fbe21a
                  job-name=baseline-job
Annotations:      cni.projectcalico.org/containerID: e6185248139d7288fef2356846050b9e96b86aff066abd00c1f637f27886ac55
                  cni.projectcalico.org/podIP: 10.244.28.37/32
                  cni.projectcalico.org/podIPs: 10.244.28.37/32,fdf0:17b3:c3ec:1f79:10:0:5:eedc/128
Status:           Pending
IP:               10.244.28.37
IPs:
  IP:           10.244.28.37
  IP:           fdf0:17b3:c3ec:1f79:10:0:5:eedc
Controlled By:  Job/baseline-job
Containers:
  baseline:
    Container ID:  
    Image:         ghcr.io/nathanielnat1993/cloud-computing-project:latest
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      python
      src/main.py
      --mode
      baseline
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:             4
      memory:          32Gi
      nvidia.com/gpu:  1
    Requests:
      cpu:             2
      memory:          16Gi
      nvidia.com/gpu:  1
    Environment:       <none>
    Mounts:
      /project/data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6p9mm (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-6p9mm:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type     Reason                  Age                From                     Message
  ----     ------                  ----               ----                     -------
  Normal   Scheduled               87s                default-scheduler        Successfully assigned gp-engine-mizzou-dsa-cloud/baseline-job-lpbq9 to k8s-gpu-01.calit2.optiputer.net
  Normal   SuccessfulAttachVolume  86s                attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-d64c959a-1fdb-4774-95aa-f6e337f1fc1a"
  Normal   Pulling                 38s (x3 over 81s)  kubelet                  Pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
  Warning  Failed                  33s (x3 over 76s)  kubelet                  Failed to pull image "ghcr.io/nathanielnat1993/cloud-computing-project:latest": rpc error: code = NotFound desc = failed to pull and unpack image "ghcr.io/nathanielnat1993/cloud-computing-project:latest": no match for platform in manifest: not found
  Warning  Failed                  33s (x3 over 76s)  kubelet                  Error: ErrImagePull
  Normal   BackOff                 4s (x4 over 76s)   kubelet                  Back-off pulling image "ghcr.io/nathanielnat1993/cloud-computing-project:latest"
  Warning  Failed                  4s (x4 over 76s)   kubelet                  Error: ImagePullBackOff
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
is it okay to run it from here? (base) nat-nat@Mac cloud-computing-project % 
[+] Building 136.3s (16/16) FINISHED                       docker:desktop-linux
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 682B                                       0.0s
 => [internal] load metadata for docker.io/pytorch/pytorch:2.3.0-cuda11.8  1.7s
 => [auth] pytorch/pytorch:pull token for registry-1.docker.io             0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [1/8] FROM docker.io/pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime@sh  0.0s
 => => resolve docker.io/pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime@sh  0.0s
 => [internal] load build context                                          0.0s
 => => transferring context: 648B                                          0.0s
 => CACHED [2/8] WORKDIR /project                                          0.0s
 => CACHED [3/8] COPY requirements.txt .                                   0.0s
 => [4/8] RUN pip install --no-cache-dir -r requirements.txt              32.7s
 => [5/8] COPY src/ ./src                                                  0.1s 
 => [6/8] COPY data/ ./data                                                0.0s 
 => [7/8] COPY results/ ./results                                          0.0s 
 => [8/8] RUN mkdir -p /project/results/figures                            0.1s 
 => exporting to image                                                   101.7s 
 => => exporting layers                                                   15.2s 
 => => exporting manifest sha256:e09dac094391236cdad3acd27ce5b833f60e6d8a  0.0s
 => => exporting config sha256:87a4a8fbf1e4788fef80ef5673f179e6c62ce13bc5  0.0s
 => => exporting attestation manifest sha256:ee9b9c385dd175c744445cfe66ab  0.0s
 => => exporting manifest list sha256:c34bb4ae9ff2152c22ead35a8437b031f6e  0.0s
 => => naming to ghcr.io/nathanielnat1993/cloud-computing-project:latest   0.0s
 => => pushing layers                                                     84.3s
 => => pushing manifest for ghcr.io/nathanielnat1993/cloud-computing-proj  2.0s
 => [auth] nathanielnat1993/cloud-computing-project:pull,push token for g  0.0s
 => [auth] nathanielnat1993/cloud-computing-project:pull,push token for g  0.0s
(base) nat-nat@Mac cloud-computing-project % 
why is the old one still saying this. baseline-job-lpbq9                 0/1     Terminating         0          6m50s
did we create this? pvc-checker
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get pods -n gp-engine-mizzou-dsa-cloud
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          4m4s
baseline-job-gzgwt                 0/1     Error       0          16m
baseline-job-lnx8r                 0/1     Error       0          6m55s
baseline-job-mchtz                 0/1     Error       0          9m48s
baseline-job-tc77t                 0/1     Error       0          8m27s
baseline-job-vr5c7                 0/1     Error       0          9m17s
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          9h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          9h
pod-cc5m4-train                    0/1     Error       0          36h
pod-gcfpx-train                    1/1     Running     0          4h47m
pod-name-ljabxf                    1/1     Running     0          4h49m
pod-pvc-jm2rc                      1/1     Running     0          5h39m
pvc-checker                        0/1     Error       0          13h
pvc-explorer                       1/1     Running     0          55m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl logs baseline-job-b668b -n gp-engine-mizzou-dsa-cloud
Traceback (most recent call last):
  File "/project/src/main.py", line 66, in <module>
    main()
  File "/project/src/main.py", line 56, in main
    df = pd.read_parquet("/project/data/df_merged_filtered.parquet")
  File "/opt/conda/lib/python3.10/site-packages/pandas/io/parquet.py", line 669, in read_parquet
    return impl.read(
  File "/opt/conda/lib/python3.10/site-packages/pandas/io/parquet.py", line 265, in read
    pa_table = self.api.parquet.read_table(
  File "/opt/conda/lib/python3.10/site-packages/pyarrow/parquet/core.py", line 1844, in read_table
    dataset = ParquetDataset(
  File "/opt/conda/lib/python3.10/site-packages/pyarrow/parquet/core.py", line 1413, in __init__
    [fragment], schema=schema or fragment.physical_schema,
  File "pyarrow/_dataset.pyx", line 1477, in pyarrow._dataset.Fragment.physical_schema.__get__
  File "pyarrow/error.pxi", line 155, in pyarrow.lib.pyarrow_internal_check_status
  File "pyarrow/error.pxi", line 92, in pyarrow.lib.check_status
pyarrow.lib.ArrowInvalid: Could not open Parquet input source '<Buffer>': Parquet magic bytes not found in footer. Either the file is corrupted or this is not a parquet file.
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
i have the file here it shows 823 mb
do we need to delete the old one first?
erged_filtered.parquet" \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet

E1120 00:58:18.743003   89625 v2.go:129] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
E1120 00:58:18.743021   89625 v2.go:150] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
E1120 00:58:18.743033   89625 v2.go:167] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
error: error reading from error stream: next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout
E1120 00:58:18.744714   89625 v2.go:104] "Unhandled Error" err="write tcp 192.168.1.232:57783->67.58.53.148:443: use of closed network connection"
(base) nat-nat@Mac ~ % 
how do i know how many chuhcks are there
save all our progress right now in memory. right now we're doing this in chunks. ill create a new chat but we're stilll in that process

okay now let's continue with my cloud computing projec. after pasting this. kubectl cp parquet_chunk_aa \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/parquet_chunk_aa how do i know to proceed with the next chunk
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- ls -lh /data
total 67M
-rw------- 1 root root 48M Nov 20 11:04 df_merged_filtered.parquet
-rw------- 1 root root 19M Nov 20 11:04 parquet_chunk_aa
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
but in the terminal mac it says thst chunk is 100mb
well in the terminal it's still not done i think. is this the reason why? (base) nat-nat@Mac data % kubectl cp parquet_chunk_aa \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/parquet_chunk_aa

this is going to take long huh?
total 96M
-rw------- 1 root root 66M Nov 20 11:09 df_merged_filtered.parquet
-rw------- 1 root root 30M Nov 20 11:09 parquet_chunk_aa
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$  is this normal? that there is the df_merged_filtered there and it seems to be growing in size. aren't we doingthe chunks
wait when did we try to cpoy the other one? i thoguht that one failed?
so how are we going to merge the chunks? into a single one?
wait. can't we just upload the one big file then? what was the problem with thst one?
Last login: Thu Nov 20 00:12:58 on ttys000
(base) nat-nat@Mac ~ % kubectl cp "/Users/nat-nat/Desktop/project-root/data/df_merged_filtered.parquet" \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/df_merged_filtered.parquet

E1120 00:58:18.743003   89625 v2.go:129] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
E1120 00:58:18.743021   89625 v2.go:150] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
E1120 00:58:18.743033   89625 v2.go:167] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout"
error: error reading from error stream: next reader: read tcp 192.168.1.232:57783->67.58.53.148:443: i/o timeout
E1120 00:58:18.744714   89625 v2.go:104] "Unhandled Error" err="write tcp 192.168.1.232:57783->67.58.53.148:443: use of closed network connection"
(base) nat-nat@Mac ~ % cd "/Users/nat-nat/Desktop/project-root/data"
split -b 100m df_merged_filtered.parquet parquet_chunk_ is this the one where we tried ot upload it earlier ?
but remember it didn't fail it was still running? so im confused
but after that timeout it was still growing the size
okay so how do we merge the chunks in the simplest and not edit the code
can i just paste all teh chunk codes in one go? so i dont' have to do it after it's done? kubectl cp parquet_chunk_aa \
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/parquet_chunk_ab
  gp-engine-mizzou-dsa-cloud/pvc-explorer:/data/parquet_chunk_ab
E1120 01:24:47.918638   90353 v2.go:129] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57908->67.58.53.148:443: i/o timeout"
E1120 01:24:47.918662   90353 v2.go:167] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57908->67.58.53.148:443: i/o timeout"
E1120 01:24:47.918660   90353 v2.go:150] "Unhandled Error" err="next reader: read tcp 192.168.1.232:57908->67.58.53.148:443: i/o timeout"
error: error reading from error stream: next reader: read tcp 192.168.1.232:57908->67.58.53.148:443: i/o timeout
do i delete the chunks first
bash: ubectl: command not found
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ ubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- rm /data/parquet_chunk_aa
bash: ubectl: command not found
which folder in nautilus jupyter should i upload it to
okay i uploaded it and it's showing. but does that mean its already uploaded or do i have to wait?
how long would it take? it's 800 mb
okay it's uploaded i think what's next
why it's saying 5mb? -rw-r--r-- 1 1000 users 5.0M Nov 20 11:40 df_merged_filtered.parquet
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl exec -it pvc-explorer -n gp-engine-mizzou-dsa-cloud -- ls -lh /data
total 5.0M
-rw-r--r-- 1 1000 users 5.0M Nov 20 11:40 df_merged_filtered.parquet
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
it[s 785 mb
so on the bottom it says uploading what does that mean
okay so lets remove the one we uploaded to pvc first right? the 5 mb one?
why is it uploadkng slow?
can i refresht the webpage? is it safe?
it doesnt seem to be progressing

before thst. what is this file in jupyter project folder? 67.58.53.148:443:
how long would zipping take?
the zip file is still 700mb
lets try option 2
jupyter-naaxk6-missouri-edu---2351cae4
is this option fast?
(base) nat-nat@Mac data % scp "/Users/nat-nat/Desktop/project-root/data/df_merged_filtered.parquet" \
    naaxk6@login.hpc.missouri.edu:~/
ssh: Could not resolve hostname login.hpc.missouri.edu: nodename nor servname provided, or not known
scp: Connection closed
(base) nat-nat@Mac data % 
(base) nat-nat@Mac data % login.lewis.rnet.missouri.edu

zsh: command not found: login.lewis.rnet.missouri.edu
(base) nat-nat@Mac data % 
zsh: command not found: login.lewis.rnet.missouri.edu
(base) nat-nat@Mac data % ssh naaxk6@login.lewis.rnet.missouri.edu

ssh: Could not resolve hostname login.lewis.rnet.missouri.edu: nodename nor servname provided, or not known
(base) nat-nat@Mac data % 
ssh: Could not resolve hostname login.lewis.rnet.missouri.edu: nodename nor servname provided, or not known
(base) nat-nat@Mac data % ssh.nautilus.optiputer.net

zsh: command not found: ssh.nautilus.optiputer.net
(base) nat-nat@Mac data % ssh naaxk6@ssh.nautilus.optiputer.net

The authenticity of host 'ssh.nautilus.optiputer.net (128.114.109.67)' can't be established.
ED25519 key fingerprint is SHA256:Mt1GttcdLQbNLU3d2MJy5WGPBOBsNrsVw8awcvixTwI.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'ssh.nautilus.optiputer.net' (ED25519) to the list of known hosts.
naaxk6@ssh.nautilus.optiputer.net: Permission denied (publickey).
(base) nat-nat@Mac data % 
You have 16 outdated formulae installed.

Warning: No available formula with the name "jupyter-rsync". Did you mean jupyter-r?
==> Searching for similarly named formulae and casks...
==> Formulae
jupyter-r

To install jupyter-r, run:
  brew install jupyter-r

==> Casks
jupyterlab-app

To install jupyterlab-app, run:
  brew install --cask jupyterlab-app
(base) nat-nat@Mac data % 
https://gp-engine.nrp-nautilus.io/user/naaxk6@missouri.edu/lab/tree/cloud-computing-project. this is the webpage

is this option fast?
which one do i replace with my IP
10.244.189.72
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl port-forward -n gp-engine-mizzou-dsa-cloud pod/pvc-explorer 2222:22
Unable to listen on port 2222: Listeners failed to create with the following errors: [unable to create listener: Error listen tcp4 127.0.0.1:2222: bind: address already in use unable to create listener: Error listen tcp6 [::1]:2222: bind: address already in use]
error: unable to listen on any of the requested ports: [{2222 22}]
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
i mean i did it earlier
i did but i closed it
the file data coudlnt be opened
command not found
(base) nat-nat@Mac ~ % fuser -k 2223/tcp || true

Unknown option: k
fuser: [-cfu] file ...
	-c	file is treated as mount point
	-f	the report is only for the named files
	-u	print username of pid in parenthesis
(base) nat-nat@Mac ~ % 
bash: fuser: command not found
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl port-forward -n gp-engine-mizzou-dsa-cloud pod/pvc-explorer 2223:22
Unable to listen on port 2223: Listeners failed to create with the following errors: [unable to create listener: Error listen tcp4 127.0.0.1:2223: bind: address already in use unable to create listener: Error listen tcp6 [::1]:2223: bind: address already in use]
error: unable to listen on any of the requested ports: [{2223 22}]
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
the file data count'nt be opened again
do i need to stop somethign in my jupyter terminal and mac terminal
Connection to localhost port 2223 [tcp/rockwell-csp3] succeeded!
(base) nat-nat@Mac ~ % ps aux | grep kubectl

nat-nat          93003   0.0  0.0 435300400   1408 s001  S+    2:17AM   0:00.00 grep kubectl
(base) nat-nat@Mac ~ % 
it didn't return anything
(base) nat-nat@Mac ~ % lsof -i :2223

(base) nat-nat@Mac ~ % nc -zv localhost 2223

nc: connectx to localhost port 2223 (tcp) failed: Connection refused
nc: connectx to localhost port 2223 (tcp) failed: Connection refused
(base) nat-nat@Mac ~ % 
what about jupyter terminal. do we need to stop something there too
how do i kill this ress already in use unable to create listener: Error listen tcp6 [::1]:2222: bind: address already in use]
error: unable to listen on any of the requested ports: [{2222 22}]
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl port-forward -n gp-engine-mizzou-dsa-cloud pod/pvc-explorer 2223:22
kubectl port-forward -n gp-engine-mizzou-dsa-cloud pod/pvc-explorer 2223:22
Forwarding from 127.0.0.1:2223 -> 22
Forwarding from [::1]:2223 -> 22
^CForwarding from 127.0.0.1:2223 -> 22
Forwarding from [::1]:2223 -> 22
okay can we just continue this tomorrow? do i need to stop some jobs right now or pods or whatever
can we make sure it's not running something that might get me banned form nrp nautilus for violation of terms
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get jobs -n gp-engine-mizzou-dsa-cloud
NAME                         STATUS     COMPLETIONS   DURATION   AGE
baseline-job                 Failed     0/1           107m       107m
job-ljabxf-mobilenet-train   Complete   1/1           62m        10h
job-ljabxf-resnet18-train    Complete   1/1           169m       10h
job-ljabxf-simpledla-train   Complete   1/1           3h3m       10h
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl get pods -n gp-engine-mizzou-dsa-cloud
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          95m
baseline-job-gzgwt                 0/1     Error       0          107m
baseline-job-lnx8r                 0/1     Error       0          97m
baseline-job-mchtz                 0/1     Error       0          100m
baseline-job-tc77t                 0/1     Error       0          99m
baseline-job-v8w89                 0/1     Error       0          89m
baseline-job-vr5c7                 0/1     Error       0          100m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          10h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          10h
pod-cc5m4-train                    0/1     Error       0          38h
pod-gcfpx-train                    0/1     Error       0          6h18m
pod-name-ljabxf                    0/1     Error       0          6h20m
pod-pvc-jm2rc                      0/1     Error       0          7h10m
pvc-checker                        0/1     Error       0          14h
pvc-explorer                       1/1     Running     0          146m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
how do i remove stop the chunk from uploading in jupyter
so im uploading a big file in jupyter. and i need it ot run overnight. would it automatically log out or would i be logged in as long as it's uploading
is thee another way aside form uploading the zip in jupyter? some faster way?
let's try option 1
okay i got several keys. west central etc
what's next after getting my keys
Last login: Thu Nov 20 02:15:49 on ttys001
(base) nat-nat@Mac ~ % aws configure

zsh: command not found: aws
(base) nat-nat@Mac ~ % 
aws-cli/2.32.1 Python/3.13.9 Darwin/25.2.0 source/arm64
(base) nat-nat@Mac ~ % aws configure

AWS Access Key ID [None]: 
i got an access key and secret key. which one do i need ot paste
okay im done. what's next
[default]
region = us-west-1
output = json
s3 =
    endpoint_url = http://cilogon.org/serverF/users/406832
(base) nat-nat@Mac ~ % aws s3 ls


An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.
(base) nat-nat@Mac ~ % 
West pool (default)	http://rook-ceph-rgw-nautiluss3.rook	https://s3-west.nrp-nautilus.io
An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.
(base) nat-nat@Mac ~ % nano ~/.aws/config

(base) nat-nat@Mac ~ % aws s3 ls


An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.
(base) nat-nat@Mac ~ % 
Pool	Inside endpoint	Outside endpoint
West pool (default)	http://rook-ceph-rgw-nautiluss3.rook	https://s3-west.nrp-nautilus.io which endpoint sould i be using?
is the default region name can be anything?
it says in my key westpool
its still doing this. AWS Access Key ID [****************4KF5]: R0ZXCEPSM6OBSGBX4KF5
AWS Secret Access Key [****************m7JA]: SB6JBk2Y1nCWFY4FV5qFCt7RzBp262CzIoZ6m7JA
Default region name [us-west-1]: us-west-1
Default output format [json]: json
(base) nat-nat@Mac ~ % nano ~/.aws/config

(base) nat-nat@Mac ~ % aws s3 ls


An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.
(base) nat-nat@Mac ~ % 


Pool west username: http://cilogon.org/serverF/users/406832
Pool west access key: R0ZXCEPSM6OBSGBX4KF5
Pool west secret key: SB6JBk2Y1nCWFY4FV5qFCt7RzBp262CzIoZ6m7JA
theres nothing. https://nrp.ai
(base) nat-nat@Mac ~ % curl --upload-file df_merged_filtered.parquet https://transfer.sh/df_merged_filtered.parquet

curl: cannot open 'df_merged_filtered.parquet'
curl: try 'curl --help' or 'curl --manual' for more information
curl: (26) Failed to open/read local data from file/application
(base) nat-nat@Mac ~ % 
(base) nat-nat@Mac data % curl --upload-file df_merged_filtered.parquet https://transfer.sh/df_merged_filtered.parquet

curl: (7) Failed to connect to transfer.sh port 443 after 696 ms: Could not connect to server
(base) nat-nat@Mac data % 
how long would the upload take?
curl: (7) Failed to connect to transfer.sh port 443 after 696 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://file.io

curl: (16) Error in the HTTP2 framing layer
(base) nat-nat@Mac data % 
(base) nat-nat@Mac data % curl -T df_merged_filtered.parquet https://bashupload.com/df_merged_filtered.parquet

curl: (7) Failed to connect to bashupload.com port 443 after 540 ms: Could not connect to server
(base) nat-nat@Mac data % 

-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_ac
-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_ad
-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_ae
-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_af
-rw-r--r--  1 nat-nat  staff   100M Nov 20 00:59 parquet_chunk_ag
-rw-r--r--  1 nat-nat  staff    85M Nov 20 00:59 parquet_chunk_ah
-rw-r--r--@ 1 nat-nat  staff   1.2K Nov 19 01:08 README.md
(base) nat-nat@Mac data % curl --upload-file df_merged_filtered.parquet https://transfer.sh/df_merged_filtered.parquet

curl: (7) Failed to connect to transfer.sh port 443 after 696 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://file.io

curl: (16) Error in the HTTP2 framing layer
(base) nat-nat@Mac data % curl -T df_merged_filtered.parquet https://bashupload.com/df_merged_filtered.parquet

curl: (7) Failed to connect to bashupload.com port 443 after 540 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://oshi.at

curl: (60) SSL certificate problem: self-signed certificate
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the webpage mentioned above.
(base) nat-nat@Mac data % 
curl: (7) Failed to connect to transfer.sh port 443 after 696 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://file.io

curl: (16) Error in the HTTP2 framing layer
(base) nat-nat@Mac data % curl -T df_merged_filtered.parquet https://bashupload.com/df_merged_filtered.parquet

curl: (7) Failed to connect to bashupload.com port 443 after 540 ms: Could not connect to server
(base) nat-nat@Mac data % curl -F "file=@df_merged_filtered.parquet" https://oshi.at
would kt help if i connect to the school vpn?
im uploading the file in jupytre is there a way to check the status of the download using kubectl?
okay save all our progress for now in memory im gonna start a new chat

ChatGPT can make mistakes. Ch

okay so i uploaded the paruqt in jupyter. now how do we get it to our pvc
Error from server (Forbidden): persistentvolumeclaims is forbidden: User "http://cilogon.org/serverF/users/406832" cannot list resource "persistentvolumeclaims" in API group "" in the namespace "default"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
do you remember everthign whre wer stoppd previously
remember we have to do gp-engine-mizzou etc. so it doesn give the error,. and you aslo know hte name of our explorer pvc adn pvc name
no! do you even remember! kubectl -n gp-engine-mizzou-dsa-cloud get pods!
and the name is pvc_explorer! y
omg what is so wrong with you . the name of the parquet file is df_merged_filtered not nrd_preprocessed! i thouhgt you saved everyting in memory!!
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f kubernetes/pvc-explorer.yaml
error: the path "kubernetes/pvc-explorer.yaml" does not exist
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
pod/pvc-explorer configured
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          5h56m
baseline-job-gzgwt                 0/1     Error       0          6h9m
baseline-job-lnx8r                 0/1     Error       0          5h59m
baseline-job-mchtz                 0/1     Error       0          6h2m
baseline-job-tc77t                 0/1     Error       0          6h1m
baseline-job-v8w89                 0/1     Error       0          5h51m
baseline-job-vr5c7                 0/1     Error       0          6h2m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          14h
pod-cc5m4-train                    0/1     Error       0          42h
pod-dbkyd-train                    1/1     Running     0          4h21m
pod-gcfpx-train                    0/1     Error       0          10h
pod-name-ljabxf                    0/1     Error       0          10h
pod-pvc-jm2rc                      0/1     Error       0          11h
pvc-checker                        0/1     Error       0          18h
pvc-explorer                       0/1     Error       0          6h48m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$  what's going on
no that's not my pvc-explorer! my pvc exploreer name is pvc_explorer not pvc-explorer
oh wait this is my original one. apiVersion: v1
kind: Pod
metadata:
  name: pvc-explorer
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  containers:
  - name: explorer
    image: ubuntu:20.04
    command: ["sleep", "infinity"]
    volumeMounts:
    - mountPath: /data
      name: project-storage
  volumes:
  - name: project-storage
    persistentVolumeClaim:
      claimName: naaxk6-pvc the yaml name is pvc_explorer
what is going on here. See "man sudo_root" for details.
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f pvc_explorer.yaml -n gp-engine-mizzou-dsa-cloud
pod/pvc-explorer configured
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          6h5m
baseline-job-gzgwt                 0/1     Error       0          6h17m
baseline-job-lnx8r                 0/1     Error       0          6h8m
baseline-job-mchtz                 0/1     Error       0          6h10m
baseline-job-tc77t                 0/1     Error       0          6h9m
baseline-job-v8w89                 0/1     Error       0          5h59m
baseline-job-vr5c7                 0/1     Error       0          6h10m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          15h
pod-cc5m4-train                    0/1     Error       0          42h
pod-dbkyd-train                    1/1     Running     0          4h29m
pod-gcfpx-train                    0/1     Error       0          10h
pod-name-ljabxf                    0/1     Error       0          10h
pod-pvc-jm2rc                      0/1     Error       0          11h
pvc-checker                        0/1     Error       0          19h
pvc-explorer                       0/1     Error       0          6h56m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer
Name:             pvc-explorer
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             gpengine-uark.areon.net/208.90.105.170
Start Time:       Thu, 20 Nov 2025 09:57:02 +0000
Labels:           <none>
Annotations:      cni.projectcalico.org/containerID: 718a0f854cc86c3d4945b46ab6ab657f345179d35f6eb2153444342a6e0c7dee
                  cni.projectcalico.org/podIP: 
                  cni.projectcalico.org/podIPs: 
                  kubernetes.io/limit-ranger: LimitRanger plugin set: cpu, memory request for container explorer; cpu, memory limit for container explorer
                  nrp.ai/username: http://cilogon.org/serverF/users/406832
Status:           Failed
Reason:           DeadlineExceeded
Message:          Pod was active on the node longer than the specified deadline
IP:               10.244.189.72
IPs:
  IP:  10.244.189.72
Containers:
  explorer:
    Container ID:  containerd://bc7b2bc1dc1a7ae4e154b8eacfcd8e85f8e53a31030d40059c75a7599c356904
    Image:         ubuntu:20.04
    Image ID:      docker.io/library/ubuntu@sha256:8feb4d8ca5354def3d8fce243717141ce31e2c428701f6682bd2fafe15388214
    Port:          <none>
    Host Port:     <none>
    Command:
      sleep
      infinity
    State:          Terminated
      Reason:       Error
      Exit Code:    137
      Started:      Thu, 20 Nov 2025 09:57:24 +0000
      Finished:     Thu, 20 Nov 2025 15:57:33 +0000
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  1Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-96mln (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-96mln:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason            Age                From     Message
  ----    ------            ----               ----     -------
  Normal  Killing           57m                kubelet  Stopping container explorer
  Normal  DeadlineExceeded  56m (x4 over 57m)  kubelet  Pod was active on the node longer than the specified deadline
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
no wait. does that mean we can't use the job anymore?
im so confused. so how are we going ot run my pvc explorer yaml file and the job
  Normal  DeadlineExceeded  56m (x4 over 57m)  kubelet  Pod was active on the node longer than the specified deadline
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f pvc_explorer.yaml -n gp-engine-mizzou-dsa-cloud
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no resource limits
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no resource requests
Error from server (Forbidden): error when creating "pvc_explorer.yaml": admission webhook "validation.gatekeeper.sh" denied the request: [container-must-have-limits-and-requests] container <explorer> does not have <{"cpu", "memory"}> requests defined
[container-must-have-limits-and-requests] container <explorer> does not have <{"memory"}> limits defined
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
[container-must-have-limits-and-requests] container <explorer> does not have <{"memory"}> limits defined
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f pvc_explorer.yaml -n gp-engine-mizzou-dsa-cloud
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> memory limit <2Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/pvc-explorer created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
is project-storage in my original code? - name: project-storage
how come the name is different now.pvc-explorer-g8prl 
okay so what's next to put the parquet in the pvc
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud cp /home/jovyan/cloud-computing-project/data/df_merged_filtered.parquet pvc-explorer-g8prl:/data/
error: /home/jovyan/cloud-computing-project/data/df_merged_filtered.parquet doesn't exist in local filesystem
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ cd /home/jovyan/cloud-computing-project
ls -lh
total 886M
drwxr-sr-x 3 jovyan users   49 Nov 19 11:13 data
-rw-r--r-- 1 jovyan users 786M Nov 20 16:33 df_merged_filtered.parquet
-rw-r--r-- 1 jovyan users  643 Nov 20 03:54 Dockerfile
drwxr-sr-x 2 jovyan users   62 Nov 19 09:05 docs
drwxr-sr-x 3 jovyan users   98 Nov 20 16:58 kubernetes
-rw-r--r-- 1 jovyan users 100M Nov 20 12:21 parquet_chunk_aa
-rw-r--r-- 1 jovyan users 1.9K Nov 20 09:13 README.md
-rw-r--r-- 1 jovyan users   99 Nov 19 11:00 requirements.txt
drwxr-sr-x 4 jovyan users  109 Nov 19 11:13 results
drwxr-sr-x 2 jovyan users  191 Nov 20 03:54 src
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud cp /home/jovyan/cloud-computing-project/df_merged_filtered.parquet pvc-explorer-g8prl:/data/
E1120 17:04:23.988748   13085 v2.go:129] "Unhandled Error" err="next reader: read tcp 10.244.189.108:43714->67.58.53.148:443: i/o timeout"
E1120 17:04:23.988751   13085 v2.go:167] "Unhandled Error" err="next reader: read tcp 10.244.189.108:43714->67.58.53.148:443: i/o timeout"
E1120 17:04:23.988764   13085 v2.go:150] "Unhandled Error" err="next reader: read tcp 10.244.189.108:43714->67.58.53.148:443: i/o timeout"
E1120 17:04:23.990103   13085 v2.go:104] "Unhandled Error" err="write tcp 10.244.189.108:43714->67.58.53.148:443: use of closed network connection"
error: error reading from error stream: next reader: read tcp 10.244.189.108:43714->67.58.53.148:443: i/o timeout
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud cp --retries=10 /home/jovyan/cloud-computing-project/df_merged_filtered.parquet pvc-explorer-g8prl:/data/
error: context deadline exceeded
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud cp --retries=10 /home/jovyan/cloud-computing-project/df_merged_filtered.parquet pvc-explorer-g8prl:/data/
error: context deadline exceeded
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ cd /home/jovyan/cloud-computing-project
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ tar cf - df_merged_filtered.parquet | kubectl -n gp-engine-mizzou-dsa-cloud exec -i pvc-explorer-g8prl -- tar xf - -C /data
E1120 17:07:30.541871   13167 v2.go:167] "Unhandled Error" err="next reader: read tcp 10.244.189.108:50048->67.58.53.148:443: i/o timeout"
E1120 17:07:30.541896   13167 v2.go:129] "Unhandled Error" err="next reader: read tcp 10.244.189.108:50048->67.58.53.148:443: i/o timeout"
E1120 17:07:30.541904   13167 v2.go:150] "Unhandled Error" err="next reader: read tcp 10.244.189.108:50048->67.58.53.148:443: i/o timeout"
E1120 17:07:30.543073   13167 v2.go:104] "Unhandled Error" err="write tcp 10.244.189.108:50048->67.58.53.148:443: use of closed network connection"
E1120 17:07:30.543097   13167 websocket.go:500] Websocket Ping failed: write tcp 10.244.189.108:50048->67.58.53.148:443: use of closed network connection
error: error reading from error stream: next reader: read tcp 10.244.189.108:50048->67.58.53.148:443: i/o timeout
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
will using rthe school vpn work
when i do get pods the status is completed. is that okay?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud delete job pvc-explorer
kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
job.batch "pvc-explorer" deleted
error: the path "pvc_explorer.yaml" does not exist
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> memory limit <2Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/pvc-explorer created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
do we delete the old pvc-explorere that failed?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-b668b                 0/1     Error               0          6h24m
baseline-job-gzgwt                 0/1     Error               0          6h36m
baseline-job-lnx8r                 0/1     Error               0          6h26m
baseline-job-mchtz                 0/1     Error               0          6h29m
baseline-job-tc77t                 0/1     Error               0          6h28m
baseline-job-v8w89                 0/1     Error               0          6h18m
baseline-job-vr5c7                 0/1     Error               0          6h29m
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          15h
pod-cc5m4-train                    0/1     Error               0          42h
pod-dbkyd-train                    1/1     Running             0          4h48m
pod-gcfpx-train                    0/1     Error               0          11h
pod-name-ljabxf                    0/1     Error               0          11h
pod-pvc-jm2rc                      0/1     Error               0          11h
pvc-checker                        0/1     Error               0          19h
pvc-explorer                       0/1     Error               0          7h15m
pvc-explorer-f57fg                 0/1     ContainerCreating   0          42s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud delete job pvc-explorer --ignore-not-found=true
job.batch "pvc-explorer" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
it's still there! plus my new one is terminating! jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS        RESTARTS   AGE
baseline-job-b668b                 0/1     Error         0          6h25m
baseline-job-gzgwt                 0/1     Error         0          6h37m
baseline-job-lnx8r                 0/1     Error         0          6h28m
baseline-job-mchtz                 0/1     Error         0          6h31m
baseline-job-tc77t                 0/1     Error         0          6h29m
baseline-job-v8w89                 0/1     Error         0          6h19m
baseline-job-vr5c7                 0/1     Error         0          6h30m
job-ljabxf-resnet18-train-qbksm    0/1     Completed     0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed     0          15h
pod-cc5m4-train                    0/1     Error         0          42h
pod-dbkyd-train                    1/1     Running       0          4h50m
pod-ecc7r-train                    1/1     Running       0          17s
pod-gcfpx-train                    0/1     Error         0          11h
pod-name-ljabxf                    0/1     Error         0          11h
pod-pvc-jm2rc                      0/1     Error         0          12h
pvc-checker                        0/1     Error         0          19h
pvc-explorer                       0/1     Error         0          7h17m
pvc-explorer-f57fg                 0/1     Terminating   0          2m6s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 

jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS        RESTARTS   AGE
baseline-job-b668b                 0/1     Error         0          6h26m
baseline-job-gzgwt                 0/1     Error         0          6h39m
baseline-job-lnx8r                 0/1     Error         0          6h29m
baseline-job-mchtz                 0/1     Error         0          6h32m
baseline-job-tc77t                 0/1     Error         0          6h31m
baseline-job-v8w89                 0/1     Error         0          6h21m
baseline-job-vr5c7                 0/1     Error         0          6h32m
job-ljabxf-resnet18-train-qbksm    0/1     Completed     0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed     0          15h
pod-cc5m4-train                    0/1     Error         0          42h
pod-dbkyd-train                    1/1     Running       0          4h51m
pod-ecc7r-train                    1/1     Running       0          104s
pod-gcfpx-train                    0/1     Error         0          11h
pod-name-ljabxf                    0/1     Error         0          11h
pod-pvc-jm2rc                      0/1     Error         0          12h
pvc-checker                        0/1     Error         0          19h
pvc-explorer-f57fg                 0/1     Terminating   0          3m33s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-b668b                 0/1     Error               0          6h29m
baseline-job-gzgwt                 0/1     Error               0          6h41m
baseline-job-lnx8r                 0/1     Error               0          6h32m
baseline-job-mchtz                 0/1     Error               0          6h35m
baseline-job-tc77t                 0/1     Error               0          6h33m
baseline-job-v8w89                 0/1     Error               0          6h23m
baseline-job-vr5c7                 0/1     Error               0          6h34m
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          15h
pod-cc5m4-train                    0/1     Error               0          43h
pod-dbkyd-train                    1/1     Running             0          4h54m
pod-ecc7r-train                    1/1     Running             0          4m4s
pod-gcfpx-train                    0/1     Error               0          11h
pod-name-ljabxf                    0/1     Error               0          11h
pod-pvc-jm2rc                      0/1     Error               0          12h
pvc-checker                        0/1     Error               0          19h
pvc-explorer-c7lzj                 0/1     ContainerCreating   0          88s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-c7lzj
Name:             pvc-explorer-c7lzj
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-haosu-16.sdsc.optiputer.net/67.58.63.15
Start Time:       Thu, 20 Nov 2025 17:16:38 +0000
Labels:           batch.kubernetes.io/controller-uid=ae5de04a-6d5b-4af8-aa13-de1f8a46a996
                  batch.kubernetes.io/job-name=pvc-explorer
                  controller-uid=ae5de04a-6d5b-4af8-aa13-de1f8a46a996
                  job-name=pvc-explorer
Annotations:      cni.projectcalico.org/containerID: cd504c6725b6b39ebfb8e303f36b17b8f5a99fac1d20a30bff348a6c9b7a6a9a
                  cni.projectcalico.org/podIP: 10.244.206.141/32
                  cni.projectcalico.org/podIPs: 10.244.206.141/32,fdf0:17b3:c3ec:1f79:10:0:7:60a9/128
                  kubernetes.io/limit-ranger: LimitRanger plugin set: cpu limit for container explorer
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/pvc-explorer
Containers:
  explorer:
    Container ID:  
    Image:         ubuntu:22.04
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      bash
      -c
      sleep 600
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  2Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-g6fsv (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-g6fsv:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m53s  default-scheduler  Successfully assigned gp-engine-mizzou-dsa-cloud/pvc-explorer-c7lzj to k8s-haosu-16.sdsc.optiputer.net
  Normal  Pulling    2m48s  kubelet            Pulling image "ubuntu:22.04"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
what's teh different betweeen my old pvc_explorer code and this one with ubuntu. i think the old one didn't include it
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-c7lzj
Name:             pvc-explorer-c7lzj
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-haosu-16.sdsc.optiputer.net/67.58.63.15
Start Time:       Thu, 20 Nov 2025 17:16:38 +0000
Labels:           batch.kubernetes.io/controller-uid=ae5de04a-6d5b-4af8-aa13-de1f8a46a996
                  batch.kubernetes.io/job-name=pvc-explorer
                  controller-uid=ae5de04a-6d5b-4af8-aa13-de1f8a46a996
                  job-name=pvc-explorer
Annotations:      cni.projectcalico.org/containerID: cd504c6725b6b39ebfb8e303f36b17b8f5a99fac1d20a30bff348a6c9b7a6a9a
                  cni.projectcalico.org/podIP: 10.244.206.141/32
                  cni.projectcalico.org/podIPs: 10.244.206.141/32,fdf0:17b3:c3ec:1f79:10:0:7:60a9/128
                  kubernetes.io/limit-ranger: LimitRanger plugin set: cpu limit for container explorer
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/pvc-explorer
Containers:
  explorer:
    Container ID:  
    Image:         ubuntu:22.04
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      bash
      -c
      sleep 600
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  2Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-g6fsv (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-g6fsv:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  6m47s  default-scheduler  Successfully assigned gp-engine-mizzou-dsa-cloud/pvc-explorer-c7lzj to k8s-haosu-16.sdsc.optiputer.net
  Normal  Pulling    6m42s  kubelet            Pulling image "ubuntu:22.04"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-qdltj | grep Node:
Node:             k8s-haosu-16.sdsc.optiputer.net/67.58.63.15
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
do we need to edit the yaml file since its giving this warning? Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> memory limit <2Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/pvc-explorer created
I don't want to get banned. some of my classmates got banned
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-n77pj
Name:             pvc-explorer-n77pj
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             k8s-haosu-05.sdsc.optiputer.net/67.58.63.7
Start Time:       Thu, 20 Nov 2025 17:31:27 +0000
Labels:           batch.kubernetes.io/controller-uid=540e9d5a-8fa5-449a-b8cc-742d7cad1eb6
                  batch.kubernetes.io/job-name=pvc-explorer
                  controller-uid=540e9d5a-8fa5-449a-b8cc-742d7cad1eb6
                  job-name=pvc-explorer
Annotations:      cni.projectcalico.org/containerID: 4164f13a0cebfb628743f02496b2510720477ee7573fdcdb1672c6f1606a7c0a
                  cni.projectcalico.org/podIP: 10.244.107.131/32
                  cni.projectcalico.org/podIPs: 10.244.107.131/32,fdf0:17b3:c3ec:1f79:10:0:a:6dca/128
                  kubernetes.io/limit-ranger: LimitRanger plugin set: cpu limit for container explorer
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/pvc-explorer
Containers:
  explorer:
    Container ID:  
    Image:         ubuntu:22.04
    Image ID:      
    Port:          <none>
    Host Port:     <none>
    Command:
      bash
      -c
      sleep 600
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     100m
      memory:  2Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-g685b (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-g685b:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type    Reason                  Age   From                     Message
  ----    ------                  ----  ----                     -------
  Normal  Scheduled               40s   default-scheduler        Successfully assigned gp-engine-mizzou-dsa-cloud/pvc-explorer-n77pj to k8s-haosu-05.sdsc.optiputer.net
  Normal  SuccessfulAttachVolume  40s   attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-d64c959a-1fdb-4774-95aa-f6e337f1fc1a"
  Normal  Pulling                 33s   kubelet                  Pulling image "ubuntu:22.04"
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> has no cpu limit
Warning: [container-must-meet-memory-and-cpu-ratio] container <explorer> memory limit <2Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/pvc-explorer created
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
baseline-job-b668b                 0/1     Error       0          6h45m
baseline-job-gzgwt                 0/1     Error       0          6h58m
baseline-job-lnx8r                 0/1     Error       0          6h48m
baseline-job-mchtz                 0/1     Error       0          6h51m
baseline-job-tc77t                 0/1     Error       0          6h50m
baseline-job-v8w89                 0/1     Error       0          6h40m
baseline-job-vr5c7                 0/1     Error       0          6h50m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          15h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          15h
pod-cc5m4-train                    0/1     Error       0          43h
pod-dbkyd-train                    1/1     Running     0          5h10m
pod-ecc7r-train                    1/1     Running     0          20m
pod-gcfpx-train                    0/1     Error       0          11h
pod-name-ljabxf                    0/1     Error       0          11h
pod-pvc-jm2rc                      0/1     Error       0          12h
pvc-checker                        0/1     Error       0          19h
pvc-explorer-m484g                 0/1     Pending     0          29s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-m484g | grep Node:
Node:             <none>
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-m484g
Name:             pvc-explorer-m484g
Namespace:        gp-engine-mizzou-dsa-cloud
Priority:         0
Service Account:  default
Node:             <none>
Labels:           batch.kubernetes.io/controller-uid=1c360f4e-1128-4b0c-9ed8-9860c010371d
                  batch.kubernetes.io/job-name=pvc-explorer
                  controller-uid=1c360f4e-1128-4b0c-9ed8-9860c010371d
                  job-name=pvc-explorer
Annotations:      kubernetes.io/limit-ranger: LimitRanger plugin set: cpu limit for container explorer
Status:           Pending
IP:               
IPs:              <none>
Controlled By:    Job/pvc-explorer
Containers:
  explorer:
    Image:      ubuntu:22.04
    Port:       <none>
    Host Port:  <none>
    Command:
      bash
      -c
      sleep 600
    Limits:
      cpu:     100m
      memory:  2Gi
    Requests:
      cpu:     100m
      memory:  1Gi
    Environment:
      NVIDIA_VISIBLE_DEVICES:  none
    Mounts:
      /data from project-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wj9q4 (ro)
Conditions:
  Type           Status
  PodScheduled   False 
Volumes:
  project-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  naaxk6-pvc
    ReadOnly:   false
  kube-api-access-wj9q4:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              nautilus.io/school=uark
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                             nvidia.com/gpu:PreferNoSchedule op=Exists
Events:
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  82s   default-scheduler  0/521 nodes are available: 1 node(s) had untolerated taint {nautilus.io/issue: 1149}, 1 node(s) had untolerated taint {nautilus.io/issue: 1257}, 1 node(s) had untolerated taint {nautilus.io/issue: 1348}, 1 node(s) had untolerated taint {nautilus.io/issue: 1350}, 1 node(s) had untolerated taint {nautilus.io/issue: 1376}, 1 node(s) had untolerated taint {nautilus.io/issue: 1384}, 1 node(s) had untolerated taint {nautilus.io/issue: 1452}, 1 node(s) had untolerated taint {nautilus.io/issue: 1476}, 1 node(s) had untolerated taint {nautilus.io/issue: 1477}, 1 node(s) had untolerated taint {nautilus.io/issue: 1478}, 1 node(s) had untolerated taint {nautilus.io/issue: slow-network}, 1 node(s) had untolerated taint {nautilus.io/issue: testing}, 1 node(s) had untolerated taint {nautilus.io/reservation: csusb-cousins-lab}, 1 node(s) had untolerated taint {nautilus.io/reservation: hdr-ml-challenge}, 1 node(s) had untolerated taint {nautilus.io/reservation: internet2}, 1 node(s) had untolerated taint {nautilus.io/rese ...
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
give me the whole updated yaml file
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-mqhdf | grep Node:
Node:             k8s-haosu-16.sdsc.optiputer.net/67.58.63.15
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
this is the yaml. apiVersion: batch/v1
kind: Job
metadata:
  name: pvc-explorer
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  backoffLimit: 0
  template:
    spec:
      restartPolicy: Never
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: kubernetes.io/hostname
                operator: NotIn
                values:
                  - k8s-haosu-01
                  - k8s-haosu-02
                  - k8s-haosu-03
                  - k8s-haosu-04
                  - k8s-haosu-05
                  - k8s-haosu-06
                  - k8s-haosu-07
                  - k8s-haosu-16
      containers:
      - name: explorer
        image: ubuntu:22.04
        command: ["bash", "-c", "sleep 600"]

        volumeMounts:
        - name: project-storage
          mountPath: /data
        resources:
          requests:
            cpu: 100m
            memory: 1Gi
          limits:
            cpu: 200m
            memory: 2Gi
      volumes:
      - name: project-storage
        persistentVolumeClaim:
          claimName: naaxk6-pvc
give me the updated yaml without any spaces or comments
pvc-explorer-lcj8g                 1/1     Running       0          16s
pvc-explorer-mqhdf                 0/1     Terminating   0          3m33s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
Node:             gpn-fiona.usd.edu/206.209.0.13
i already split them. what's next
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-lcj8g | grep Node:
Node:             gpn-fiona.usd.edu/206.209.0.13
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ cd /home/jovyan/cloud-computing-project/
for f in parquet_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-lcj8g:/data/
done
error: parquet_chunk_* doesn't exist in local filesystem
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
the chunkcs are named df_chunk_
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ cd /home/jovyan/cloud-computing-project/
for f in df_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-lcj8g:/data/
done should i just wait?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ cd /home/jovyan/cloud-computing-project/
for f in parquet_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-lcj8g:/data/
done
error: parquet_chunk_* doesn't exist in local filesystem
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ cd /home/jovyan/cloud-computing-project/
for f in df_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-lcj8g:/data/
done
command terminated with exit code 137
E1120 17:51:14.539160   16573 v2.go:104] "Unhandled Error" err="write tcp 10.244.189.108:53876->67.58.53.148:443: write: broken pipe"
error: Internal error occurred: unable to upgrade connection: container not found ("explorer")
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
error: cannot exec into a container in a completed pod; current phase is Succeeded
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
pvc-explorer-mqhdf                 0/1     Terminating   0          18m i wanna delete this one first
pvc-explorer-mqhdf                 0/1     Terminating   0          19m it's still there
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
error: the path "pvc_explorer.yaml" does not exist
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS              RESTARTS   AGE
baseline-job-b668b                 0/1     Error               0          7h10m
baseline-job-gzgwt                 0/1     Error               0          7h23m
baseline-job-lnx8r                 0/1     Error               0          7h13m
baseline-job-mchtz                 0/1     Error               0          7h16m
baseline-job-tc77t                 0/1     Error               0          7h15m
baseline-job-v8w89                 0/1     Error               0          7h5m
baseline-job-vr5c7                 0/1     Error               0          7h15m
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          16h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          16h
pod-cc5m4-train                    0/1     Error               0          43h
pod-dbkyd-train                    1/1     Running             0          5h35m
pod-gcfpx-train                    0/1     Error               0          11h
pod-name-ljabxf                    0/1     Error               0          11h
pod-pvc-jm2rc                      0/1     Error               0          12h
pvc-checker                        0/1     Error               0          20h
pvc-explorer-j4mzd                 0/1     ContainerCreating   0          32s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-j4mzd | grep Node:
Node:             k8s-haosu-15.sdsc.optiputer.net/67.58.63.14
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pod pvc-explorer-j4mzd -o yaml | grep -A20 affinity
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: NotIn
            values:
            - k8s-haosu-01
            - k8s-haosu-02
            - k8s-haosu-03
            - k8s-haosu-04
            - k8s-haosu-05
            - k8s-haosu-06
            - k8s-haosu-07
            - k8s-haosu-16
  containers:
  - command:
    - bash
    - -c
    - sleep 36000
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud delete pod pvc-checker --force --grace-period=0 --wait=false
Warning: Immediate deletion does not wait for confirmation that the running resource has been terminated. The resource may continue to run on the cluster indefinitely.
pod "pvc-checker" force deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud apply -f pvc_explorer.yaml
Error from server (BadRequest): error when creating "pvc_explorer.yaml": Job in version "v1" cannot be handled as a Job: json: cannot unmarshal string into Go struct field Volume.spec.template.spec.volumes.persistentVolumeClaim of type v1.PersistentVolumeClaimVolumeSource
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS              RESTARTS   AGE
job-ljabxf-resnet18-train-qbksm    0/1     Completed           0          16h
job-ljabxf-simpledla-train-82bgh   0/1     Completed           0          16h
pod-cc5m4-train                    0/1     Error               0          43h
pod-dbkyd-train                    1/1     Running             0          5h44m
pod-gcfpx-train                    0/1     Error               0          12h
pod-name-ljabxf                    0/1     Error               0          12h
pod-pvc-jm2rc                      0/1     Error               0          12h
pvc-explorer-g46qp                 0/1     ContainerCreating   0          14s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-g46qp | grep Node:
Node:             k8s-haosu-15.sdsc.optiputer.net/67.58.63.14
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
k8s-haosu-15.sdsc.optiputer.net   Ready    <none>   5y310d   v1.31.12   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,cpu-feature.node.kubevirt.io/3dnowprefetch=true,cpu-feature.node.kubevirt.io/abm=true,cpu-feature.node.kubevirt.io/adx=true,cpu-feature.node.kubevirt.io/aes=true,cpu-feature.node.kubevirt.io/amd-ssbd=true,cpu-feature.node.kubevirt.io/amd-stibp=true,cpu-feature.node.kubevirt.io/apic=true,cpu-feature.node.kubevirt.io/arat=true,cpu-feature.node.kubevirt.io/arch-capabilities=true,cpu-feature.node.kubevirt.io/avx2=true,cpu-feature.node.kubevirt.io/avx512bw=true,cpu-feature.node.kubevirt.io/avx512cd=true,cpu-feature.node.kubevirt.io/avx512dq=true,cpu-feature.node.kubevirt.io/avx512f=true,cpu-feature.node.kubevirt.io/avx512vl=true,cpu-feature.node.kubevirt.io/avx512vnni=true,cpu-feature.node.kubevirt.io/avx=true,cpu-feature.node.kubevirt.io/bmi1=true,cpu-feature.node.kubevirt.io/bmi2=true,cpu-feature.node.kubevirt.io/clflush=true,cpu-feature.node.kubevirt.io/clflushopt=true,cpu-feature.node.kubevirt.io/clwb=true,cpu-feature.node.kubevirt.io/cmov=true,cpu-feature.node.kubevirt.io/cx16=true,cpu-feature.node.kubevirt.io/cx8=true,cpu-feature.node.kubevirt.io/de=true,cpu-feature.node.kubevirt.io/erms=true,cpu-feature.node.kubevirt.io/f16c=true,cpu-feature.node.kubevirt.io/fb-clear=true,cpu-feature.node.kubevirt.io/flush-l1d=true,cpu-feature.node.kubevirt.io/fma=true,cpu-feature.node.kubevirt.io/fpu=true,cpu-feature.node.kubevirt.io/fsgsbase=true,cpu-feature.node.kubevirt.io/fxsr=true,cpu-feature.node.kubevirt.io/gds-no=true,cpu-feature.node.kubevirt.io/hypervisor=true,cpu-feature.node.kubevirt.io/ibpb=true,cpu-feature.node.kubevirt.io/ibrs-all=true,cpu-feature.node.kubevirt.io/ibrs=true,cpu-feature.node.kubevirt.io/invpcid=true,cpu-feature.node.kubevirt.io/invtsc=true,cpu-feature.node.kubevirt.io/lahf_lm=true,cpu-feature.node.kubevirt.io/lm=true,cpu-feature.node.kubevirt.io/mca=true,cpu-feature.node.kubevirt.io/mce=true,cpu-feature.node.kubevirt.io/md-clear=true,cpu-feature.node.kubevirt.io/mds-no=true,cpu-feature.node.kubevirt.io/mmx=true,cpu-feature.node.kubevirt.io/movbe=true,cpu-feature.node.kubevirt.io/mpx=true,cpu-feature.node.kubevirt.io/msr=true,cpu-feature.node.kubevirt.io/mtrr=true,cpu-feature.node.kubevirt.io/nx=true,cpu-feature.node.kubevirt.io/pae=true,cpu-feature.node.kubevirt.io/pat=true,cpu-feature.node.kubevirt.io/pcid=true,cpu-feature.node.kubevirt.io/pclmuldq=true,cpu-feature.node.kubevirt.io/pdcm=true,cpu-feature.node.kubevirt.io/pdpe1gb=true,cpu-feature.node.kubevirt.io/pge=true,cpu-feature.node.kubevirt.io/pku=true,cpu-feature.node.kubevirt.io/pni=true,cpu-feature.node.kubevirt.io/popcnt=true,cpu-feature.node.kubevirt.io/pschange-mc-no=true,cpu-feature.node.kubevirt.io/psdp-no=true,cpu-feature.node.kubevirt.io/pse36=true,cpu-feature.node.kubevirt.io/pse=true,cpu-feature.node.kubevirt.io/rdctl-no=true,cpu-feature.node.kubevirt.io/rdrand=true,cpu-feature.node.kubevirt.io/rdseed=true,cpu-feature.node.kubevirt.io/rdtscp=true,cpu-feature.node.kubevirt.io/rfds-no=true,cpu-feature.node.kubevirt.io/sbdr-ssdp-no=true,cpu-feature.node.kubevirt.io/sep=true,cpu-feature.node.kubevirt.io/skip-l1dfl-vmentry=true,cpu-feature.node.kubevirt.io/smap=true,cpu-feature.node.kubevirt.io/smep=true,cpu-feature.node.kubevirt.io/spec-ctrl=true,cpu-feature.node.kubevirt.io/ss=true,cpu-feature.node.kubevirt.io/ssbd=true,cpu-feature.node.kubevirt.io/sse2=true,cpu-feature.node.kubevirt.io/sse4.1=true,cpu-feature.node.kubevirt.io/sse4.2=true,cpu-feature.node.kubevirt.io/sse=true,cpu-feature.node.kubevirt.io/ssse3=true,cpu-feature.node.kubevirt.io/stibp=true,cpu-feature.node.kubevirt.io/syscall=true,cpu-feature.node.kubevirt.io/tsc-deadline=true,cpu-feature.node.kubevirt.io/tsc=true,cpu-feature.node.kubevirt.io/tsc_adjust=true,cpu-feature.node.kubevirt.io/tsx-ctrl=true,cpu-feature.node.kubevirt.io/umip=true,cpu-feature.node.kubevirt.io/vme=true,cpu-feature.node.kubevirt.io/vmx-activity-hlt=true,cpu-feature.node.kubevirt.io/vmx-activity-wait-sipi=true,cpu-feature.node.kubevirt.io/vmx-apicv-register=true,cpu-feature.node.kubevirt.io/vmx-apicv-vid=true,cpu-feature.node.kubevirt.io/vmx-apicv-x2apic=true,cpu-feature.node.kubevirt.io/vmx-apicv-xapic=true,cpu-feature.node.kubevirt.io/vmx-cr3-load-noexit=true,cpu-feature.node.kubevirt.io/vmx-cr3-store-noexit=true,cpu-feature.node.kubevirt.io/vmx-cr8-load-exit=true,cpu-feature.node.kubevirt.io/vmx-cr8-store-exit=true,cpu-feature.node.kubevirt.io/vmx-desc-exit=true,cpu-feature.node.kubevirt.io/vmx-entry-ia32e-mode=true,cpu-feature.node.kubevirt.io/vmx-entry-load-bndcfgs=true,cpu-feature.node.kubevirt.io/vmx-entry-load-efer=true,cpu-feature.node.kubevirt.io/vmx-entry-load-pat=true,cpu-feature.node.kubevirt.io/vmx-entry-load-perf-global-ctrl=true,cpu-feature.node.kubevirt.io/vmx-entry-noload-debugctl=true,cpu-feature.node.kubevirt.io/vmx-ept-1gb=true,cpu-feature.node.kubevirt.io/vmx-ept-2mb=true,cpu-feature.node.kubevirt.io/vmx-ept-execonly=true,cpu-feature.node.kubevirt.io/vmx-ept=true,cpu-feature.node.kubevirt.io/vmx-eptad=true,cpu-feature.node.kubevirt.io/vmx-eptp-switching=true,cpu-feature.node.kubevirt.io/vmx-exit-ack-intr=true,cpu-feature.node.kubevirt.io/vmx-exit-clear-bndcfgs=true,cpu-feature.node.kubevirt.io/vmx-exit-load-efer=true,cpu-feature.node.kubevirt.io/vmx-exit-load-pat=true,cpu-feature.node.kubevirt.io/vmx-exit-load-perf-global-ctrl=true,cpu-feature.node.kubevirt.io/vmx-exit-nosave-debugctl=true,cpu-feature.node.kubevirt.io/vmx-exit-save-efer=true,cpu-feature.node.kubevirt.io/vmx-exit-save-pat=true,cpu-feature.node.kubevirt.io/vmx-exit-save-preemption-timer=true,cpu-feature.node.kubevirt.io/vmx-flexpriority=true,cpu-feature.node.kubevirt.io/vmx-hlt-exit=true,cpu-feature.node.kubevirt.io/vmx-ins-outs=true,cpu-feature.node.kubevirt.io/vmx-intr-exit=true,cpu-feature.node.kubevirt.io/vmx-invept-all-context=true,cpu-feature.node.kubevirt.io/vmx-invept-single-context=true,cpu-feature.node.kubevirt.io/vmx-invept=true,cpu-feature.node.kubevirt.io/vmx-invlpg-exit=true,cpu-feature.node.kubevirt.io/vmx-invpcid-exit=true,cpu-feature.node.kubevirt.io/vmx-invvpid-all-context=true,cpu-feature.node.kubevirt.io/vmx-invvpid-single-addr=true,cpu-feature.node.kubevirt.io/vmx-invvpid-single-context-noglobals=true,cpu-feature.node.kubevirt.io/vmx-invvpid=true,cpu-feature.node.kubevirt.io/vmx-io-bitmap=true,cpu-feature.node.kubevirt.io/vmx-io-exit=true,cpu-feature.node.kubevirt.io/vmx-monitor-exit=true,cpu-feature.node.kubevirt.io/vmx-movdr-exit=true,cpu-feature.node.kubevirt.io/vmx-msr-bitmap=true,cpu-feature.node.kubevirt.io/vmx-mtf=true,cpu-feature.node.kubevirt.io/vmx-mwait-exit=true,cpu-feature.node.kubevirt.io/vmx-nmi-exit=true,cpu-feature.node.kubevirt.io/vmx-page-walk-4=true,cpu-feature.node.kubevirt.io/vmx-pause-exit=true,cpu-feature.node.kubevirt.io/vmx-pml=true,cpu-feature.node.kubevirt.io/vmx-posted-intr=true,cpu-feature.node.kubevirt.io/vmx-preemption-timer=true,cpu-feature.node.kubevirt.io/vmx-rdpmc-exit=true,cpu-feature.node.kubevirt.io/vmx-rdrand-exit=true,cpu-feature.node.kubevirt.io/vmx-rdseed-exit=true,cpu-feature.node.kubevirt.io/vmx-rdtsc-exit=true,cpu-feature.node.kubevirt.io/vmx-rdtscp-exit=true,cpu-feature.node.kubevirt.io/vmx-secondary-ctls=true,cpu-feature.node.kubevirt.io/vmx-shadow-vmcs=true,cpu-feature.node.kubevirt.io/vmx-store-lma=true,cpu-feature.node.kubevirt.io/vmx-true-ctls=true,cpu-feature.node.kubevirt.io/vmx-tsc-offset=true,cpu-feature.node.kubevirt.io/vmx-tsc-scaling=true,cpu-feature.node.kubevirt.io/vmx-unrestricted-guest=true,cpu-feature.node.kubevirt.io/vmx-vintr-pending=true,cpu-feature.node.kubevirt.io/vmx-vmfunc=true,cpu-feature.node.kubevirt.io/vmx-vmwrite-vmexit-fields=true,cpu-feature.node.kubevirt.io/vmx-vnmi-pending=true,cpu-feature.node.kubevirt.io/vmx-vnmi=true,cpu-feature.node.kubevirt.io/vmx-vpid=true,cpu-feature.node.kubevirt.io/vmx-wbinvd-exit=true,cpu-feature.node.kubevirt.io/vmx-xsaves=true,cpu-feature.node.kubevirt.io/vmx=true,cpu-feature.node.kubevirt.io/x2apic=true,cpu-feature.node.kubevirt.io/xgetbv1=true,cpu-feature.node.kubevirt.io/xsave=true,cpu-feature.node.kubevirt.io/xsavec=true,cpu-feature.node.kubevirt.io/xsaveopt=true,cpu-feature.node.kubevirt.io/xsaves=true,cpu-model-migration.node.kubevirt.io/486-v1=true,cpu-model-migration.node.kubevirt.io/Broadwell-noTSX-IBRS=true,cpu-model-migration.node.kubevirt.io/Broadwell-noTSX=true,cpu-model-migration.node.kubevirt.io/Broadwell-v2=true,cpu-model-migration.node.kubevirt.io/Broadwell-v4=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server-noTSX=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server-v3=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server-v4=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server-v5=true,cpu-model-migration.node.kubevirt.io/Cascadelake-Server=true,cpu-model-migration.node.kubevirt.io/Conroe-v1=true,cpu-model-migration.node.kubevirt.io/Haswell-noTSX-IBRS=true,cpu-model-migration.node.kubevirt.io/Haswell-noTSX=true,cpu-model-migration.node.kubevirt.io/Haswell-v2=true,cpu-model-migration.node.kubevirt.io/Haswell-v4=true,cpu-model-migration.node.kubevirt.io/IvyBridge-IBRS=true,cpu-model-migration.node.kubevirt.io/IvyBridge-v1=true,cpu-model-migration.node.kubevirt.io/IvyBridge-v2=true,cpu-model-migration.node.kubevirt.io/IvyBridge=true,cpu-model-migration.node.kubevirt.io/Nehalem-IBRS=true,cpu-model-migration.node.kubevirt.io/Nehalem-v1=true,cpu-model-migration.node.kubevirt.io/Nehalem-v2=true,cpu-model-migration.node.kubevirt.io/Nehalem=true,cpu-model-migration.node.kubevirt.io/Opteron_G1-v1=true,cpu-model-migration.node.kubevirt.io/Opteron_G2-v1=true,cpu-model-migration.node.kubevirt.io/Penryn-v1=true,cpu-model-migration.node.kubevirt.io/Penryn=true,cpu-model-migration.node.kubevirt.io/SandyBridge-IBRS=true,cpu-model-migration.node.kubevirt.io/SandyBridge-v1=true,cpu-model-migration.node.kubevirt.io/SandyBridge-v2=true,cpu-model-migration.node.kubevirt.io/SandyBridge=true,cpu-model-migration.node.kubevirt.io/Skylake-Client-noTSX-IBRS=true,cpu-model-migration.node.kubevirt.io/Skylake-Client-v3=true,cpu-model-migration.node.kubevirt.io/Skylake-Client-v4=true,cpu-model-migration.node.kubevirt.io/Skylake-Server-noTSX-IBRS=true,cpu-model-migration.node.kubevirt.io/Skylake-Server-v3=true,cpu-model-migration.node.kubevirt.io/Skylake-Server-v4=true,cpu-model-migration.node.kubevirt.io/Skylake-Server-v5=true,cpu-model-migration.node.kubevirt.io/Westmere-IBRS=true,cpu-model-migration.node.kubevirt.io/Westmere-v1=true,cpu-model-migration.node.kubevirt.io/Westmere-v2=true,cpu-model-migration.node.kubevirt.io/Westmere=true,cpu-model-migration.node.kubevirt.io/core2duo-v1=true,cpu-model-migration.node.kubevirt.io/coreduo-v1=true,cpu-model-migration.node.kubevirt.io/kvm32-v1=true,cpu-model-migration.node.kubevirt.io/kvm64-v1=true,cpu-model-migration.node.kubevirt.io/n270-v1=true,cpu-model-migration.node.kubevirt.io/pentium-v1=true,cpu-model-migration.node.kubevirt.io/pentium2-v1=true,cpu-model-migration.node.kubevirt.io/pentium3-v1=true,cpu-model-migration.node.kubevirt.io/qemu32-v1=true,cpu-model-migration.node.kubevirt.io/qemu64-v1=true,cpu-model.node.kubevirt.io/486-v1=true,cpu-model.node.kubevirt.io/Broadwell-noTSX-IBRS=true,cpu-model.node.kubevirt.io/Broadwell-noTSX=true,cpu-model.node.kubevirt.io/Broadwell-v2=true,cpu-model.node.kubevirt.io/Broadwell-v4=true,cpu-model.node.kubevirt.io/Cascadelake-Server-noTSX=true,cpu-model.node.kubevirt.io/Cascadelake-Server-v3=true,cpu-model.node.kubevirt.io/Cascadelake-Server-v4=true,cpu-model.node.kubevirt.io/Cascadelake-Server-v5=true,cpu-model.node.kubevirt.io/Conroe-v1=true,cpu-model.node.kubevirt.io/Haswell-noTSX-IBRS=true,cpu-model.node.kubevirt.io/Haswell-noTSX=true,cpu-model.node.kubevirt.io/Haswell-v2=true,cpu-model.node.kubevirt.io/Haswell-v4=true,cpu-model.node.kubevirt.io/IvyBridge-IBRS=true,cpu-model.node.kubevirt.io/IvyBridge-v1=true,cpu-model.node.kubevirt.io/IvyBridge-v2=true,cpu-model.node.kubevirt.io/IvyBridge=true,cpu-model.node.kubevirt.io/Nehalem-IBRS=true,cpu-model.node.kubevirt.io/Nehalem-v1=true,cpu-model.node.kubevirt.io/Nehalem-v2=true,cpu-model.node.kubevirt.io/Nehalem=true,cpu-model.node.kubevirt.io/Opteron_G1-v1=true,cpu-model.node.kubevirt.io/Opteron_G2-v1=true,cpu-model.node.kubevirt.io/Penryn-v1=true,cpu-model.node.kubevirt.io/Penryn=true,cpu-model.node.kubevirt.io/SandyBridge-IBRS=true,cpu-model.node.kubevirt.io/SandyBridge-v1=true,cpu-model.node.kubevirt.io/SandyBridge-v2=true,cpu-model.node.kubevirt.io/SandyBridge=true,cpu-model.node.kubevirt.io/Skylake-Client-noTSX-IBRS=true,cpu-model.node.kubevirt.io/Skylake-Client-v3=true,cpu-model.node.kubevirt.io/Skylake-Client-v4=true,cpu-model.node.kubevirt.io/Skylake-Server-noTSX-IBRS=true,cpu-model.node.kubevirt.io/Skylake-Server-v3=true,cpu-model.node.kubevirt.io/Skylake-Server-v4=true,cpu-model.node.kubevirt.io/Skylake-Server-v5=true,cpu-model.node.kubevirt.io/Westmere-IBRS=true,cpu-model.node.kubevirt.io/Westmere-v1=true,cpu-model.node.kubevirt.io/Westmere-v2=true,cpu-model.node.kubevirt.io/Westmere=true,cpu-model.node.kubevirt.io/core2duo-v1=true,cpu-model.node.kubevirt.io/coreduo-v1=true,cpu-model.node.kubevirt.io/kvm32-v1=true,cpu-model.node.kubevirt.io/kvm64-v1=true,cpu-model.node.kubevirt.io/n270-v1=true,cpu-model.node.kubevirt.io/pentium-v1=true,cpu-model.node.kubevirt.io/pentium2-v1=true,cpu-model.node.kubevirt.io/pentium3-v1=true,cpu-model.node.kubevirt.io/qemu32-v1=true,cpu-model.node.kubevirt.io/qemu64-v1=true,cpu-timer.node.kubevirt.io/tsc-frequency=2100001000,cpu-timer.node.kubevirt.io/tsc-scalable=true,cpu-vendor.node.kubevirt.io/Intel=true,cpumanager=false,feature.node.kubernetes.io/cpu-cpuid.ADX=true,feature.node.kubernetes.io/cpu-cpuid.AESNI=true,feature.node.kubernetes.io/cpu-cpuid.AVX2=true,feature.node.kubernetes.io/cpu-cpuid.AVX512BW=true,feature.node.kubernetes.io/cpu-cpuid.AVX512CD=true,feature.node.kubernetes.io/cpu-cpuid.AVX512DQ=true,feature.node.kubernetes.io/cpu-cpuid.AVX512F=true,feature.node.kubernetes.io/cpu-cpuid.AVX512VL=true,feature.node.kubernetes.io/cpu-cpuid.AVX512VNNI=true,feature.node.kubernetes.io/cpu-cpuid.AVX=true,feature.node.kubernetes.io/cpu-cpuid.CMPXCHG8=true,feature.node.kubernetes.io/cpu-cpuid.FLUSH_L1D=true,feature.node.kubernetes.io/cpu-cpuid.FMA3=true,feature.node.kubernetes.io/cpu-cpuid.FXSR=true,feature.node.kubernetes.io/cpu-cpuid.FXSROPT=true,feature.node.kubernetes.io/cpu-cpuid.IA32_ARCH_CAP=true,feature.node.kubernetes.io/cpu-cpuid.IBPB=true,feature.node.kubernetes.io/cpu-cpuid.LAHF=true,feature.node.kubernetes.io/cpu-cpuid.MD_CLEAR=true,feature.node.kubernetes.io/cpu-cpuid.MOVBE=true,feature.node.kubernetes.io/cpu-cpuid.MPX=true,feature.node.kubernetes.io/cpu-cpuid.OSXSAVE=true,feature.node.kubernetes.io/cpu-cpuid.SPEC_CTRL_SSBD=true,feature.node.kubernetes.io/cpu-cpuid.STIBP=true,feature.node.kubernetes.io/cpu-cpuid.SYSCALL=true,feature.node.kubernetes.io/cpu-cpuid.SYSEE=true,feature.node.kubernetes.io/cpu-cpuid.VMX=true,feature.node.kubernetes.io/cpu-cpuid.X87=true,feature.node.kubernetes.io/cpu-cpuid.XGETBV1=true,feature.node.kubernetes.io/cpu-cpuid.XSAVE=true,feature.node.kubernetes.io/cpu-cpuid.XSAVEC=true,feature.node.kubernetes.io/cpu-cpuid.XSAVEOPT=true,feature.node.kubernetes.io/cpu-cpuid.XSAVES=true,feature.node.kubernetes.io/cpu-cstate.enabled=true,feature.node.kubernetes.io/cpu-hardware_multithreading=true,feature.node.kubernetes.io/cpu-model.family=6,feature.node.kubernetes.io/cpu-model.id=85,feature.node.kubernetes.io/cpu-model.vendor_id=Intel,feature.node.kubernetes.io/cpu-pstate.scaling_governor=performance,feature.node.kubernetes.io/cpu-pstate.status=active,feature.node.kubernetes.io/cpu-pstate.turbo=true,feature.node.kubernetes.io/cpu-rdt.RDTCMT=true,feature.node.kubernetes.io/cpu-rdt.RDTL3CA=true,feature.node.kubernetes.io/cpu-rdt.RDTMBA=true,feature.node.kubernetes.io/cpu-rdt.RDTMBM=true,feature.node.kubernetes.io/cpu-rdt.RDTMON=true,feature.node.kubernetes.io/kernel-config.NO_HZ=true,feature.node.kubernetes.io/kernel-config.NO_HZ_FULL=true,feature.node.kubernetes.io/kernel-version.full=6.8.0-87-generic,feature.node.kubernetes.io/kernel-version.major=6,feature.node.kubernetes.io/kernel-version.minor=8,feature.node.kubernetes.io/kernel-version.revision=0,feature.node.kubernetes.io/memory-numa=true,feature.node.kubernetes.io/network-sriov.capable=true,feature.node.kubernetes.io/pci-10de.present=true,feature.node.kubernetes.io/pci-15b3.present=true,feature.node.kubernetes.io/pci-15b3.sriov.capable=true,feature.node.kubernetes.io/pci-1a03.present=true,feature.node.kubernetes.io/pci-8086.present=true,feature.node.kubernetes.io/pci-8086.sriov.capable=true,feature.node.kubernetes.io/rdma.capable=true,feature.node.kubernetes.io/storage-nonrotationaldisk=true,feature.node.kubernetes.io/system-os_release.ID=ubuntu,feature.node.kubernetes.io/system-os_release.VERSION_ID.major=24,feature.node.kubernetes.io/system-os_release.VERSION_ID.minor=04,feature.node.kubernetes.io/system-os_release.VERSION_ID=24.04,host-endpoint=true,host-model-cpu.node.kubevirt.io/Cascadelake-Server=true,host-model-required-features.node.kubevirt.io/amd-ssbd=true,host-model-required-features.node.kubevirt.io/amd-stibp=true,host-model-required-features.node.kubevirt.io/arch-capabilities=true,host-model-required-features.node.kubevirt.io/fb-clear=true,host-model-required-features.node.kubevirt.io/flush-l1d=true,host-model-required-features.node.kubevirt.io/gds-no=true,host-model-required-features.node.kubevirt.io/hypervisor=true,host-model-required-features.node.kubevirt.io/ibpb=true,host-model-required-features.node.kubevirt.io/ibrs-all=true,host-model-required-features.node.kubevirt.io/ibrs=true,host-model-required-features.node.kubevirt.io/invtsc=true,host-model-required-features.node.kubevirt.io/md-clear=true,host-model-required-features.node.kubevirt.io/mds-no=true,host-model-required-features.node.kubevirt.io/mpx=true,host-model-required-features.node.kubevirt.io/pdcm=true,host-model-required-features.node.kubevirt.io/pku=true,host-model-required-features.node.kubevirt.io/pschange-mc-no=true,host-model-required-features.node.kubevirt.io/psdp-no=true,host-model-required-features.node.kubevirt.io/rdctl-no=true,host-model-required-features.node.kubevirt.io/rfds-no=true,host-model-required-features.node.kubevirt.io/sbdr-ssdp-no=true,host-model-required-features.node.kubevirt.io/skip-l1dfl-vmentry=true,host-model-required-features.node.kubevirt.io/ss=true,host-model-required-features.node.kubevirt.io/stibp=true,host-model-required-features.node.kubevirt.io/tsc_adjust=true,host-model-required-features.node.kubevirt.io/tsx-ctrl=true,host-model-required-features.node.kubevirt.io/umip=true,host-model-required-features.node.kubevirt.io/vmx-activity-hlt=true,host-model-required-features.node.kubevirt.io/vmx-activity-wait-sipi=true,host-model-required-features.node.kubevirt.io/vmx-apicv-register=true,host-model-required-features.node.kubevirt.io/vmx-apicv-vid=true,host-model-required-features.node.kubevirt.io/vmx-apicv-x2apic=true,host-model-required-features.node.kubevirt.io/vmx-apicv-xapic=true,host-model-required-features.node.kubevirt.io/vmx-cr3-load-noexit=true,host-model-required-features.node.kubevirt.io/vmx-cr3-store-noexit=true,host-model-required-features.node.kubevirt.io/vmx-cr8-load-exit=true,host-model-required-features.node.kubevirt.io/vmx-cr8-store-exit=true,host-model-required-features.node.kubevirt.io/vmx-desc-exit=true,host-model-required-features.node.kubevirt.io/vmx-entry-ia32e-mode=true,host-model-required-features.node.kubevirt.io/vmx-entry-load-bndcfgs=true,host-model-required-features.node.kubevirt.io/vmx-entry-load-efer=true,host-model-required-features.node.kubevirt.io/vmx-entry-load-pat=true,host-model-required-features.node.kubevirt.io/vmx-entry-load-perf-global-ctrl=true,host-model-required-features.node.kubevirt.io/vmx-entry-noload-debugctl=true,host-model-required-features.node.kubevirt.io/vmx-ept-1gb=true,host-model-required-features.node.kubevirt.io/vmx-ept-2mb=true,host-model-required-features.node.kubevirt.io/vmx-ept-execonly=true,host-model-required-features.node.kubevirt.io/vmx-ept=true,host-model-required-features.node.kubevirt.io/vmx-eptad=true,host-model-required-features.node.kubevirt.io/vmx-eptp-switching=true,host-model-required-features.node.kubevirt.io/vmx-exit-ack-intr=true,host-model-required-features.node.kubevirt.io/vmx-exit-clear-bndcfgs=true,host-model-required-features.node.kubevirt.io/vmx-exit-load-efer=true,host-model-required-features.node.kubevirt.io/vmx-exit-load-pat=true,host-model-required-features.node.kubevirt.io/vmx-exit-load-perf-global-ctrl=true,host-model-required-features.node.kubevirt.io/vmx-exit-nosave-debugctl=true,host-model-required-features.node.kubevirt.io/vmx-exit-save-efer=true,host-model-required-features.node.kubevirt.io/vmx-exit-save-pat=true,host-model-required-features.node.kubevirt.io/vmx-exit-save-preemption-timer=true,host-model-required-features.node.kubevirt.io/vmx-flexpriority=true,host-model-required-features.node.kubevirt.io/vmx-hlt-exit=true,host-model-required-features.node.kubevirt.io/vmx-ins-outs=true,host-model-required-features.node.kubevirt.io/vmx-intr-exit=true,host-model-required-features.node.kubevirt.io/vmx-invept-all-context=true,host-model-required-features.node.kubevirt.io/vmx-invept-single-context=true,host-model-required-features.node.kubevirt.io/vmx-invept=true,host-model-required-features.node.kubevirt.io/vmx-invlpg-exit=true,host-model-required-features.node.kubevirt.io/vmx-invpcid-exit=true,host-model-required-features.node.kubevirt.io/vmx-invvpid-all-context=true,host-model-required-features.node.kubevirt.io/vmx-invvpid-single-addr=true,host-model-required-features.node.kubevirt.io/vmx-invvpid-single-context-noglobals=true,host-model-required-features.node.kubevirt.io/vmx-invvpid=true,host-model-required-features.node.kubevirt.io/vmx-io-bitmap=true,host-model-required-features.node.kubevirt.io/vmx-io-exit=true,host-model-required-features.node.kubevirt.io/vmx-monitor-exit=true,host-model-required-features.node.kubevirt.io/vmx-movdr-exit=true,host-model-required-features.node.kubevirt.io/vmx-msr-bitmap=true,host-model-required-features.node.kubevirt.io/vmx-mtf=true,host-model-required-features.node.kubevirt.io/vmx-mwait-exit=true,host-model-required-features.node.kubevirt.io/vmx-nmi-exit=true,host-model-required-features.node.kubevirt.io/vmx-page-walk-4=true,host-model-required-features.node.kubevirt.io/vmx-pause-exit=true,host-model-required-features.node.kubevirt.io/vmx-pml=true,host-model-required-features.node.kubevirt.io/vmx-posted-intr=true,host-model-required-features.node.kubevirt.io/vmx-preemption-timer=true,host-model-required-features.node.kubevirt.io/vmx-rdpmc-exit=true,host-model-required-features.node.kubevirt.io/vmx-rdrand-exit=true,host-model-required-features.node.kubevirt.io/vmx-rdseed-exit=true,host-model-required-features.node.kubevirt.io/vmx-rdtsc-exit=true,host-model-required-features.node.kubevirt.io/vmx-rdtscp-exit=true,host-model-required-features.node.kubevirt.io/vmx-secondary-ctls=true,host-model-required-features.node.kubevirt.io/vmx-shadow-vmcs=true,host-model-required-features.node.kubevirt.io/vmx-store-lma=true,host-model-required-features.node.kubevirt.io/vmx-true-ctls=true,host-model-required-features.node.kubevirt.io/vmx-tsc-offset=true,host-model-required-features.node.kubevirt.io/vmx-tsc-scaling=true,host-model-required-features.node.kubevirt.io/vmx-unrestricted-guest=true,host-model-required-features.node.kubevirt.io/vmx-vintr-pending=true,host-model-required-features.node.kubevirt.io/vmx-vmfunc=true,host-model-required-features.node.kubevirt.io/vmx-vmwrite-vmexit-fields=true,host-model-required-features.node.kubevirt.io/vmx-vnmi-pending=true,host-model-required-features.node.kubevirt.io/vmx-vnmi=true,host-model-required-features.node.kubevirt.io/vmx-vpid=true,host-model-required-features.node.kubevirt.io/vmx-wbinvd-exit=true,host-model-required-features.node.kubevirt.io/vmx-xsaves=true,host-model-required-features.node.kubevirt.io/vmx=true,host-model-required-features.node.kubevirt.io/xsaves=true,hyperv.node.kubevirt.io/base=true,hyperv.node.kubevirt.io/frequencies=true,hyperv.node.kubevirt.io/ipi=true,hyperv.node.kubevirt.io/reenlightenment=true,hyperv.node.kubevirt.io/reset=true,hyperv.node.kubevirt.io/runtime=true,hyperv.node.kubevirt.io/synic2=true,hyperv.node.kubevirt.io/synic=true,hyperv.node.kubevirt.io/synictimer=true,hyperv.node.kubevirt.io/time=true,hyperv.node.kubevirt.io/tlbflush=true,hyperv.node.kubevirt.io/vpindex=true,kubernetes.io/arch=amd64,kubernetes.io/hostname=k8s-haosu-15.sdsc.optiputer.net,kubernetes.io/os=linux,kubevirt.io/ksm-enabled=false,kubevirt.io/schedulable=true,linbit.com/hostname=k8s-haosu-15.sdsc.optiputer.net,machine-type.node.kubevirt.io/pc-i440fx-rhel7.6.0=true,machine-type.node.kubevirt.io/pc-q35-rhel7.6.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.0.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.1.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.2.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.3.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.4.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.5.0=true,machine-type.node.kubevirt.io/pc-q35-rhel8.6.0=true,machine-type.node.kubevirt.io/pc-q35-rhel9.0.0=true,machine-type.node.kubevirt.io/pc-q35-rhel9.2.0=true,machine-type.node.kubevirt.io/pc-q35-rhel9.4.0=true,machine-type.node.kubevirt.io/pc-q35-rhel9.6.0=true,machine-type.node.kubevirt.io/pc=true,machine-type.node.kubevirt.io/q35=true,mtu=9000,nautilus.io/OSGInstitutionID=osg-htc.org_iid_06wup3aye2t7,nautilus.io/RORInstitutionID=ror.org_0168r3w48,nautilus.io/group=haosu,nautilus.io/ipv6=true,nautilus.io/linstor=true,nautilus.io/network=10000,netbox.io/site=sdsc,nvidia.com/cuda.driver-version.full=580.105.08,nvidia.com/cuda.driver-version.major=580,nvidia.com/cuda.driver-version.minor=105,nvidia.com/cuda.driver-version.revision=08,nvidia.com/cuda.driver.major=580,nvidia.com/cuda.driver.minor=105,nvidia.com/cuda.driver.rev=08,nvidia.com/cuda.runtime-version.full=13.0,nvidia.com/cuda.runtime-version.major=13,nvidia.com/cuda.runtime-version.minor=0,nvidia.com/cuda.runtime.major=13,nvidia.com/cuda.runtime.minor=0,nvidia.com/gfd.timestamp=1763656608,nvidia.com/gpu.compute.major=7,nvidia.com/gpu.compute.minor=5,nvidia.com/gpu.count=7,nvidia.com/gpu.deploy.container-toolkit=true,nvidia.com/gpu.deploy.dcgm-exporter=true,nvidia.com/gpu.deploy.dcgm=true,nvidia.com/gpu.deploy.device-plugin=true,nvidia.com/gpu.deploy.driver=true,nvidia.com/gpu.deploy.gpu-feature-discovery=true,nvidia.com/gpu.deploy.node-status-exporter=true,nvidia.com/gpu.deploy.operator-validator=true,nvidia.com/gpu.family=turing,nvidia.com/gpu.machine=G291-280-00,nvidia.com/gpu.memory=11264,nvidia.com/gpu.present=true,nvidia.com/gpu.product=NVIDIA-GeForce-RTX-2080-Ti,nvidia.com/gpu.replicas=1,nvidia.com/gpu.sharing-strategy=none,nvidia.com/mig.capable=false,nvidia.com/mig.strategy=single,nvidia.com/mps.capable=false,remediation.medik8s.io/exclude-from-remediation=true,scheduling.node.kubevirt.io/tsc-frequency-1995288000=true,scheduling.node.kubevirt.io/tsc-frequency-2100001000=true,topology.kubernetes.io/region=us-west,topology.kubernetes.io/zone=ucsd-sdsc
pvc-explorer-g46qp well this is running now. 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ cd /home/jovyan/cloud-computing-project/
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ for f in df_chunk_*; do
  kubectl -n gp-engine-mizzou-dsa-cloud cp $f pvc-explorer-g46qp:/data/
done
command terminated with exit code 137
E1120 18:15:31.604910   18990 v2.go:104] "Unhandled Error" err="write tcp 10.244.189.108:43172->67.58.53.148:443: write: broken pipe"
error: Internal error occurred: unable to upgrade connection: container not found ("explorer")
error: cannot exec into a container in a completed pod; current phase is Failed
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
Error from server (NotFound): pods "pvc-explorer-g46qp" not found
what about this one? apiVersion: batch/v1
kind: Job
metadata:
  name: pvc-explorer
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  backoffLimit: 0
  template:
    spec:
      restartPolicy: Never
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: nautilus.io/group
                operator: NotIn
                values:
                - haosu
      containers:
      - name: explorer
        image: ubuntu:22.04
        command: ["bash","-c","sleep 36000"]
        volumeMounts:
        - name: project-storage
          mountPath: /data
        resources:
          requests:
            cpu: 100m
            memory: 1Gi
          limits:
            cpu: 200m
            memory: 2Gi
      volumes:
      - name: project-storage
        persistentVolumeClaim:
          claimName: naaxk6-pvc
we alredy did the 3600 and it still crashed
apiVersion: batch/v1
kind: Job
metadata:
  name: pvc-explorer
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  backoffLimit: 0
  template:
    spec:
      restartPolicy: Never
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: nautilus.io/group
                operator: NotIn
                values:
                - haosu
      containers:
      - name: explorer
        image: ubuntu:22.04
        command: ["bash","-c","sleep 36000"]
        volumeMounts:
        - name: project-storage
          mountPath: /data
        resources:
          requests:
            cpu: 100m
            memory: 1Gi
          limits:
            cpu: 200m
            memory: 2Gi
      volumes:
      - name: project-storage
        persistentVolumeClaim:
          claimName: naaxk6-pvc so which one is better that one or this one?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          16h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          16h
pod-cc5m4-train                    0/1     Error       0          44h
pod-dbkyd-train                    0/1     Error       0          6h7m
pod-gcfpx-train                    0/1     Error       0          12h
pod-name-ljabxf                    0/1     Error       0          12h
pod-pvc-jm2rc                      0/1     Error       0          13h
pvc-explorer-k6l6z                 0/1     Pending     0          51s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe pod pvc-explorer-k6l6z | grep -A10 "FailedScheduling"
  Warning  FailedScheduling  75s   default-scheduler  0/521 nodes are available: 1 node(s) had untolerated taint {nautilus.io/issue: 1149}, 1 node(s) had untolerated taint {nautilus.io/issue: 1257}, 1 node(s) had untolerated taint {nautilus.io/issue: 1348}, 1 node(s) had untolerated taint {nautilus.io/issue: 1350}, 1 node(s) had untolerated taint {nautilus.io/issue: 1376}, 1 node(s) had untolerated taint {nautilus.io/issue: 1384}, 1 node(s) had untolerated taint {nautilus.io/issue: 1452}, 1 node(s) had untolerated taint {nautilus.io/issue: 1476}, 1 node(s) had untolerated taint {nautilus.io/issue: 1477}, 1 node(s) had untolerated taint {nautilus.io/issue: 1478}, 1 node(s) had untolerated taint {nautilus.io/issue: slow-network}, 1 node(s) had untolerated taint {nautilus.io/issue: testing}, 1 node(s) had untolerated taint {nautilus.io/reservation: csusb-cousins-lab}, 1 node(s) had untolerated taint {nautilus.io/reservation: hdr-ml-challenge}, 1 node(s) had untolerated taint {nautilus.io/reservation: internet2}, 1 node(s) had untolerated taint {nautilus.io/rese ...
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
fiona worked earlier
it's been 16 mins and still pending
yes
apiVersion: batch/v1
kind: Job
metadata:
  name: job-data-download-naaxk6
spec:
  template:
    spec:
      automountServiceAccountToken: false
      containers:
      - name: pod-data-download-naaxk6
        image: ubuntu:20.04
        command: ["/bin/sh","-c"]
        args:
        - cp -r /ccdata/* /data/
        volumeMounts:
        - mountPath: /ccdata
          name: source
        - mountPath: /data
          name: destination 
        resources:
            limits:
              memory: 10Gi
              cpu: "4"
            requests:
              memory: 10Gi
              cpu: "4"     
      volumes:
      - name: source
        persistentVolumeClaim:
          claimName: cloudcomp-data
      - name: destination
        persistentVolumeClaim:
          claimName: naaxk6-pv
      restartPolicy: Never      
  backoffLimit: 0 woudl this work? this is what we used in our practice

no i mean this structure but we just tweak it instead of avoiding hoisu
no we don't restrict it to those nodes
but in the code i gave you we did 10 gi each
give me the code to run the thing now the chunks to load it
pvc-explorer-w6xv4                 1/1     Running     0          84s
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ POD=pvc-explorer-w6xv4

for f in df_chunk_*; do
    echo "Uploading $f ..."
    kubectl -n gp-engine-mizzou-dsa-cloud cp "$f" "$POD":/data/
    sleep 1
done
Uploading df_chunk_aa ...
so far it doesn't seem like it's stoppig. its still running. jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ POD=pvc-explorer-w6xv4

for f in df_chunk_*; do
    echo "Uploading $f ..."
    kubectl -n gp-engine-mizzou-dsa-cloud cp "$f" "$POD":/data/
    sleep 1
done
Uploading df_chunk_aa ...
Uploading df_chunk_ab ...
they are still uploading yay! tho very slow
do you think i would be able to upload the whole parquet file?
830 mb
am in in violation here. Utilization violations
Allowed: GPU: >40%CPU: 20% - 200%Memory 20% - 150% Ignored: Memory: ≤2 GBCPU: ≤1
Namespace
Name
GPU util
CPU util
Mem util
GPU requested
CPU requested
Mem requested
gp-engine-mizzou-dsa-cloud	pvc-explorer-w6xv4		0%	0%		4	10 GB
well how come we're not using cpu when the code is still running and the files are being transferred to pvc
but it's needed riht?
so my pvc is only allowed 10 gb of storage?
is it done? for f in df_chunk_*; do
    echo "Uploading $f ..."
    kubectl -n gp-engine-mizzou-dsa-cloud cp "$f" "$POD":/data/
    sleep 1
done
Uploading df_chunk_aa ...
Uploading df_chunk_ab ...
Uploading df_chunk_ac ...
Uploading df_chunk_ad ...
Uploading df_chunk_ae ...
Uploading df_chunk_af ...
Uploading df_chunk_ag ...
Uploading df_chunk_ah ...
Uploading df_chunk_ai ...
Uploading df_chunk_aj ...
Uploading df_chunk_ak ...
Uploading df_chunk_al ...
Uploading df_chunk_am ...
Uploading df_chunk_an ...
Uploading df_chunk_ao ...
Uploading df_chunk_ap ...
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud exec -it $POD -- ls -lh /data
total 818M
-rw-r--r-- 1 1000 users 50M Nov 20 19:13 df_chunk_aa
-rw-r--r-- 1 1000 users 50M Nov 20 19:23 df_chunk_ab
-rw-r--r-- 1 1000 users 50M Nov 20 19:31 df_chunk_ac
-rw-r--r-- 1 1000 users 50M Nov 20 19:44 df_chunk_ad
-rw-r--r-- 1 1000 users 50M Nov 20 19:54 df_chunk_ae
-rw-r--r-- 1 1000 users 50M Nov 20 20:06 df_chunk_af
-rw-r--r-- 1 1000 users 50M Nov 20 20:16 df_chunk_ag
-rw-r--r-- 1 1000 users 50M Nov 20 20:26 df_chunk_ah
-rw-r--r-- 1 1000 users 50M Nov 20 20:37 df_chunk_ai
-rw-r--r-- 1 1000 users 50M Nov 20 20:48 df_chunk_aj
-rw-r--r-- 1 1000 users 50M Nov 20 20:58 df_chunk_ak
-rw-r--r-- 1 1000 users 50M Nov 20 21:08 df_chunk_al
-rw-r--r-- 1 1000 users 50M Nov 20 21:20 df_chunk_am
-rw-r--r-- 1 1000 users 50M Nov 20 21:31 df_chunk_an
-rw-r--r-- 1 1000 users 50M Nov 20 21:39 df_chunk_ao
-rw-r--r-- 1 1000 users 36M Nov 20 21:45 df_chunk_ap
-rw------- 1 root root  33M Nov 20 17:09 df_merged_filtered.parquet
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
okay now let's try to upload the full parquet file as well
do we still need the connection right now? what else do we need to do?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud cp df_merged_filtered.parquet pvc-explorer-w6xv4:/data/
E1120 22:20:23.303335   22966 v2.go:167] "Unhandled Error" err="next reader: read tcp 10.244.189.108:51610->67.58.53.148:443: i/o timeout"
E1120 22:20:23.303445   22966 v2.go:129] "Unhandled Error" err="next reader: read tcp 10.244.189.108:51610->67.58.53.148:443: i/o timeout"
E1120 22:20:23.303450   22966 v2.go:150] "Unhandled Error" err="next reader: read tcp 10.244.189.108:51610->67.58.53.148:443: i/o timeout"
E1120 22:20:23.304851   22966 websocket.go:500] Websocket Ping failed: write tcp 10.244.189.108:51610->67.58.53.148:443: use of closed network connection
error: error reading from error stream: next reader: read tcp 10.244.189.108:51610->67.58.53.148:443: i/o timeout
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
before i delete it., don't we need to merge the chunks first
okay so we run teh base line job now?
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run verify --image=ubuntu:22.04 -it --rm -- sh -c "ls -lh /data" --overrides='
{
  "apiVersion": "v1",
  "spec": {
    "containers":[{
      "name": "verify",
      "image": "ubuntu:22.04",
      "command":["bash","-c","ls -lh /data"],
      "volumeMounts":[{"mountPath":"/data","name":"project-storage"}]
    }],
    "volumes":[{"name":"project-storage","persistentVolumeClaim":{"claimName":"naaxk6-pvc"}}]
  }
}'
If you don't see a command prompt, try pressing enter.
warning: couldn't attach to pod/verify, falling back to streaming logs: Internal error occurred: unable to upgrade connection: container verify not found in pod verify_gp-engine-mizzou-dsa-cloud
ls: cannot access '/data': No such file or directory
pod "verify" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
-rw-r--r-- 1 1000 users 50M Nov 20 19:13 df_chunk_aa
-rw-r--r-- 1 1000 users 50M Nov 20 19:23 df_chunk_ab
-rw-r--r-- 1 1000 users 50M Nov 20 19:31 df_chunk_ac
-rw-r--r-- 1 1000 users 50M Nov 20 19:44 df_chunk_ad
-rw-r--r-- 1 1000 users 50M Nov 20 19:54 df_chunk_ae
-rw-r--r-- 1 1000 users 50M Nov 20 20:06 df_chunk_af
-rw-r--r-- 1 1000 users 50M Nov 20 20:16 df_chunk_ag
-rw-r--r-- 1 1000 users 50M Nov 20 20:26 df_chunk_ah
-rw-r--r-- 1 1000 users 50M Nov 20 20:37 df_chunk_ai
-rw-r--r-- 1 1000 users 50M Nov 20 20:48 df_chunk_aj
-rw-r--r-- 1 1000 users 50M Nov 20 20:58 df_chunk_ak
-rw-r--r-- 1 1000 users 50M Nov 20 21:08 df_chunk_al
-rw-r--r-- 1 1000 users 50M Nov 20 21:20 df_chunk_am
-rw-r--r-- 1 1000 users 50M Nov 20 21:31 df_chunk_an
-rw-r--r-- 1 1000 users 50M Nov 20 21:39 df_chunk_ao
-rw-r--r-- 1 1000 users 36M Nov 20 21:45 df_chunk_ap
-rw------- 1 root root  55M Nov 20 22:28 df_merged_filtered.parquet
pod "verify" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$  why is the df_merged filetered there
is this good? apiVersion: batch/v1
kind: Job
metadata:
  name: baseline-job
  namespace: gp-engine-mizzou-dsa-cloud
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: baseline
        image: ghcr.io/nathanielnat1993/cloud-computing-project:latest
        command: ["python", "src/main.py", "--mode", "baseline"]
        volumeMounts:
        - mountPath: /project/data
          name: project-storage
        resources:
          requests:
            cpu: "2"
            memory: "16Gi"
            nvidia.com/gpu: 1
          limits:
            cpu: "4"
            memory: "32Gi"
            nvidia.com/gpu: 1
      volumes:
      - name: project-storage
        persistentVolumeClaim:
          claimName: naaxk6-pvc
this is my main import argparse
import pandas as pd

from preprocessing import apply_cleaning, stratified_group_split
from tokenization import load_tokenizer, tokenize_overflow_fixed_pt

from baseline_model import (
    load_bioclincial_bert_encoder,
    chunk_embeddings,
    aggregate_docs,
    train_logistic_regression,
)

from baseline_evaluate import (
    evaluate_with_target_recall,
    report_metrics
)


def run_baseline(df_train, df_val, df_test, tokenizer):
    train_enc = tokenize_overflow_fixed_pt(df_train, tokenizer)
    val_enc   = tokenize_overflow_fixed_pt(df_val, tokenizer)
    test_enc  = tokenize_overflow_fixed_pt(df_test, tokenizer)

    encoder = load_bioclincial_bert_encoder()

    train_chunk_emb = chunk_embeddings(train_enc, encoder)
    val_chunk_emb   = chunk_embeddings(val_enc, encoder)
    test_chunk_emb  = chunk_embeddings(test_enc, encoder)

    train_doc_emb = aggregate_docs(train_chunk_emb, train_enc["doc_mapping"])
    val_doc_emb   = aggregate_docs(val_chunk_emb,   val_enc["doc_mapping"])
    test_doc_emb  = aggregate_docs(test_chunk_emb,  test_enc["doc_mapping"])

    y_train = df_train["readmitted"].to_numpy()
    y_val   = df_val["readmitted"].to_numpy()
    y_test  = df_test["readmitted"].to_numpy()

    clf = train_logistic_regression(train_doc_emb, y_train)

    val_p  = clf.predict_proba(val_doc_emb)[:, 1]
    test_p = clf.predict_proba(test_doc_emb)[:, 1]

    best_t, val_pred  = evaluate_with_target_recall(y_val,  val_p,  target_recall=0.75)
    _,      test_pred = evaluate_with_target_recall(y_test, test_p, target_recall=0.75)

    report_metrics("VAL",  y_val,  val_pred,  val_p,  best_t)
    report_metrics("TEST", y_test, test_pred, test_p, best_t)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="baseline", choices=["baseline"])
    args = parser.parse_args()

    df = pd.read_parquet("/project/data/df_merged_filtered.parquet")
    df = apply_cleaning(df)
    df_train, df_val, df_test = stratified_group_split(df)

    tokenizer = load_tokenizer()

    run_baseline(df_train, df_val, df_test, tokenizer)


if __name__ == "__main__":
    main()
well no! since we uploaded the chunks! and thta 55mb failed
omg no! that df_merged_filtered in the pvc failed remember! that' why its only 55mb instead of 825!
omg remember we were going to merge all those chunks and make it df_merged_filtered!
will this replace htat broken df_merged_filered one
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, pyarrow, numpy, python-dateutil, pandas
Successfully installed numpy-2.2.6 pandas-2.3.3 pyarrow-22.0.0 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip is available: 23.0.1 -> 25.3
[notice] To update, run: pip install --upgrade pip
root@merge:/# 
root@merge:/# 
print("Done! Final file size:")
import os
print(os.path.getsize("/data/df_merged_filtered.parquet") / (1024*1024), "MB")
EOF

Finding chunk files in /data...
Found 16 chunks: ['/data/df_chunk_aa', '/data/df_chunk_ab', '/data/df_chunk_ac', '/data/df_chunk_ad', '/data/df_chunk_ae', '/data/df_chunk_af', '/data/df_chunk_ag', '/data/df_chunk_ah', '/data/df_chunk_ai', '/data/df_chunk_aj', '/data/df_chunk_ak', '/data/df_chunk_al', '/data/df_chunk_am', '/data/df_chunk_an', '/data/df_chunk_ao', '/data/df_chunk_ap']
Reading: /data/df_chunk_aa
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
  File "/usr/local/lib/python3.10/site-packages/pandas/io/parquet.py", line 669, in read_parquet
    return impl.read(
  File "/usr/local/lib/python3.10/site-packages/pandas/io/parquet.py", line 265, in read
    pa_table = self.api.parquet.read_table(
  File "/usr/local/lib/python3.10/site-packages/pyarrow/parquet/core.py", line 1844, in read_table
    dataset = ParquetDataset(
  File "/usr/local/lib/python3.10/site-packages/pyarrow/parquet/core.py", line 1413, in __init__
    [fragment], schema=schema or fragment.physical_schema,
  File "pyarrow/_dataset.pyx", line 1477, in pyarrow._dataset.Fragment.physical_schema.__get__
  File "pyarrow/error.pxi", line 155, in pyarrow.lib.pyarrow_internal_check_status
  File "pyarrow/error.pxi", line 92, in pyarrow.lib.check_status
pyarrow.lib.ArrowInvalid: Could not open Parquet input source '<Buffer>': Parquet magic bytes not found in footer. Either the file is corrupted or this is not a parquet file.
root@merge:/# 
root@merge:/# 
root@merge:/# cat /data/df_chunk_* > /data/df_merged_reassembled.parquet it's taking a while
why did we name the reassembled parquet that instead of df_merged_filtered
it;s still runnign. hwo long would it take?
is it done? root@merge:/# cat /data/df_chunk_* > /data/df_merged_reassembled.parquet
root@merge:/# 
path = "/data/df_merged_reassembled.parquet"

print("File size (MB):", os.path.getsize(path)/(1024*1024))

try:
    df = pd.read_parquet(path)
    print("SUCCESS: Parquet is readable!")
    print(df.head())
except Exception as e:
    print("ERROR reading parquet:")
    print(e)
EOF
File size (MB): 785.0076446533203
Session ended, resume using 'kubectl attach merge -c merge -i -t' command when the pod is running
pod "merge" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
File size (MB): 785.0076446533203
Session ended, resume using 'kubectl attach merge -c merge -i -t' command when the pod is running
pod "merge" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run verify-parquet \
  --image=python:3.10-slim \
  -it --rm \
  --overrides='
{
  "apiVersion": "v1",
  "spec": {
    "containers":[{
      "name": "verify-parquet",
      "image": "python:3.10-slim",
      "command":["bash","-c","pip install pandas pyarrow && python3 - << EOF
import pandas as pd, os
path = \"/data/df_merged_reassembled.parquet\"
print(\"File size (MB):\", os.path.getsize(path)/(1024*1024))
try:
    df = pd.read_parquet(path)
    print(\"SUCCESS — Parquet is readable!\\n\", df.head())
except Exception as e:
    print(\"ERROR reading parquet:\")
    print(e)
EOF"],
      "volumeMounts":[{"mountPath":"/data","name":"project-storage"}]
    }],
    "volumes":[{"name":"project-storage","persistentVolumeClaim":{"claimName":"naaxk6-pvc"}}]
  }
}'
error: Invalid JSON Patch
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run verify-parquet \
  --image=python:3.10-slim \
  -it --rm \
  --overrides='
{
  "apiVersion": "v1",
  "spec": {
    "containers":[{
      "name": "verify-parquet",
      "image": "python:3.10-slim",
      "command":["bash","-c","pip install pandas pyarrow && python3 - << EOF
import pandas as pd, os
path = \"/data/df_merged_reassembled.parquet\"
print(\"File size (MB):\", os.path.getsize(path)/(1024*1024))
try:
    df = pd.read_parquet(path)
    print(\"SUCCESS — Parquet is readable!\\n\", df.head())
except Exception as e:
    print(\"ERROR reading parquet:\")
    print(e)
EOF"],
      "volumeMounts":[{"mountPath":"/data","name":"project-storage"}]
    }],
    "volumes":[{"name":"project-storage","persistentVolumeClaim":{"claimName":"naaxk6-pvc"}}]
  }
}'
error: Invalid JSON Patch
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run verify-parquet \
  --image=python:3.10-slim \
  -it --rm \
  --overrides='{
    "apiVersion": "v1",
    "spec": {
      "containers": [{
        "name": "verify-parquet",
        "image": "python:3.10-slim",
        "command": [
          "bash",
          "-c",
          "pip install pandas pyarrow && python3 - <<\"EOF\"\nimport pandas as pd, os\npath = \"/data/df_merged_reassembled.parquet\"\nprint(\"File size (MB):\", os.path.getsize(path)/(1024*1024))\ntry:\n    df = pd.read_parquet(path)\n    print(\"SUCCESS — Parquet is readable!\\n\", df.head())\nexcept Exception as e:\n    print(\"ERROR reading parquet:\")\n    print(e)\nEOF"
        ],
        "volumeMounts": [{
          "mountPath": "/data",
          "name": "project-storage"
        }]
      }],
      "volumes": [{
        "name": "project-storage",
        "persistentVolumeClaim": { "claimName": "naaxk6-pvc" }
      }]
    }
  }'
error: Unable to use a TTY - container verify-parquet did not allocate one
If you don't see a command prompt, try pressing enter.
Collecting pandas
  Downloading pandas-2.3.3-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 17.0 MB/s eta 0:00:00
Collecting pyarrow
  Downloading pyarrow-22.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (47.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.6/47.6 MB 7.8 MB/s eta 0:00:00
Collecting numpy>=1.22.4
  Downloading numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 12.8 MB/s eta 0:00:00
Collecting tzdata>=2022.7
  Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 93.1 MB/s eta 0:00:00
Collecting pytz>=2020.1
  Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 509.2/509.2 kB 138.1 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 101.6 MB/s eta 0:00:00
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, pyarrow, numpy, python-dateutil, pandas
Successfully installed numpy-2.2.6 pandas-2.3.3 pyarrow-22.0.0 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip is available: 23.0.1 -> 25.3
[notice] To update, run: pip install --upgrade pip
pod "verify-parquet" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
try:
    df = pd.read_parquet(path)
    print('SUCCESS — Parquet is readable!')
    print(df.head())
except Exception as e:
    print('ERROR reading parquet:')
    print(e)
EOF
python3 /verify.py"
If you don't see a command prompt, try pressing enter.
Collecting pandas
  Downloading pandas-2.3.3-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.8/12.8 MB 10.1 MB/s eta 0:00:00
Collecting pyarrow
  Downloading pyarrow-22.0.0-cp310-cp310-manylinux_2_28_x86_64.whl (47.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.6/47.6 MB 4.9 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.2
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 229.9/229.9 kB 65.5 MB/s eta 0:00:00
Collecting tzdata>=2022.7
  Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 75.9 MB/s eta 0:00:00
Collecting pytz>=2020.1
  Downloading pytz-2025.2-py2.py3-none-any.whl (509 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 509.2/509.2 kB 5.3 MB/s eta 0:00:00
Collecting numpy>=1.22.4
  Downloading numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 8.6 MB/s eta 0:00:00
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, tzdata, six, pyarrow, numpy, python-dateutil, pandas
Successfully installed numpy-2.2.6 pandas-2.3.3 pyarrow-22.0.0 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip is available: 23.0.1 -> 25.3
[notice] To update, run: pip install --upgrade pip
python3: can't open file '/verify.py': [Errno 2] No such file or directory
pod "verify-parquet" deleted
pod gp-engine-mizzou-dsa-cloud/verify-parquet terminated (Error)
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
    print(df.head())
except Exception as e:
    print('ERROR reading parquet:')
    print(e)
EOF
  " \
  --overrides='{
    "apiVersion": "v1",
    "spec": {
      "volumes": [{
        "name": "project-storage",
        "persistentVolumeClaim": { "claimName": "naaxk6-pvc" }
      }],
      "containers": [{
        "name": "verify-parquet",
        "image": "python:3.10-slim",
        "command": ["bash","-c","sleep infinity"],
        "volumeMounts": [{
          "mountPath": "/data",
          "name": "project-storage"
        }]
      }]
    }
  }'
If you don't see a command prompt, try pressing enter.

Checking file...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "/usr/local/lib/python3.10/genericpath.py", line 50, in getsize
    return os.stat(filename).st_size
FileNotFoundError: [Errno 2] No such file or directory: '/data/df_merged_reassembled.parquet'
Session ended, resume using 'kubectl attach verify-parquet -c verify-parquet -i -t' command when the pod is running
pod "verify-parquet" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
ovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ kubectl -n gp-engine-mizzou-dsa-cloud run list-pvc \
  --image=ubuntu:22.04 \
  -it --rm --command -- bash -c "
    ls -lh /data
  " \
  --overrides='{
    "apiVersion": "v1",
    "spec": {
      "containers": [{
        "name": "list-pvc",
        "image": "ubuntu:22.04",
        "command": ["bash","-c","ls -lh /data"],
        "volumeMounts": [{
          "mountPath": "/data",
          "name": "project-storage"
        }]
      }],
      "volumes": [{
        "name": "project-storage",
        "persistentVolumeClaim": { "claimName": "naaxk6-pvc" }
      }]
    }
  }'
If you don't see a command prompt, try pressing enter.
warning: couldn't attach to pod/list-pvc, falling back to streaming logs: Internal error occurred: unable to upgrade connection: container list-pvc not found in pod list-pvc_gp-engine-mizzou-dsa-cloud
ls: cannot access '/data': No such file or directory
pod "list-pvc" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project$ 
why can't we just use an existing pod yaml to chck the contgent of the pvc
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud exec -it inspect-pvc -- bash
error: Internal error occurred: unable to upgrade connection: container not found ("inspector")
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud exec -it inspect-pvc -- bash
root@inspect-pvc:/# ls -lh /data
total 1.6G
-rw-r--r-- 1 1000 users  50M Nov 20 19:13 df_chunk_aa
-rw-r--r-- 1 1000 users  50M Nov 20 19:23 df_chunk_ab
-rw-r--r-- 1 1000 users  50M Nov 20 19:31 df_chunk_ac
-rw-r--r-- 1 1000 users  50M Nov 20 19:44 df_chunk_ad
-rw-r--r-- 1 1000 users  50M Nov 20 19:54 df_chunk_ae
-rw-r--r-- 1 1000 users  50M Nov 20 20:06 df_chunk_af
-rw-r--r-- 1 1000 users  50M Nov 20 20:16 df_chunk_ag
-rw-r--r-- 1 1000 users  50M Nov 20 20:26 df_chunk_ah
-rw-r--r-- 1 1000 users  50M Nov 20 20:37 df_chunk_ai
-rw-r--r-- 1 1000 users  50M Nov 20 20:48 df_chunk_aj
-rw-r--r-- 1 1000 users  50M Nov 20 20:58 df_chunk_ak
-rw-r--r-- 1 1000 users  50M Nov 20 21:08 df_chunk_al
-rw-r--r-- 1 1000 users  50M Nov 20 21:20 df_chunk_am
-rw-r--r-- 1 1000 users  50M Nov 20 21:31 df_chunk_an
-rw-r--r-- 1 1000 users  50M Nov 20 21:39 df_chunk_ao
-rw-r--r-- 1 1000 users  36M Nov 20 21:45 df_chunk_ap
-rw------- 1 root root   55M Nov 20 22:28 df_merged_filtered.parquet
-rw-r--r-- 1 root root  786M Nov 20 23:26 df_merged_reassembled.parquet
no i want to keep the name
okay now what' snext
root@inspect-pvc:/# rm /data/df_merged_filtered.parquet
mv /data/df_merged_reassembled.parquet /data/df_merged_filtered.parquet
ls -lh /data
total 1.6G
-rw-r--r-- 1 1000 users  50M Nov 20 19:13 df_chunk_aa
-rw-r--r-- 1 1000 users  50M Nov 20 19:23 df_chunk_ab
-rw-r--r-- 1 1000 users  50M Nov 20 19:31 df_chunk_ac
-rw-r--r-- 1 1000 users  50M Nov 20 19:44 df_chunk_ad
-rw-r--r-- 1 1000 users  50M Nov 20 19:54 df_chunk_ae
-rw-r--r-- 1 1000 users  50M Nov 20 20:06 df_chunk_af
-rw-r--r-- 1 1000 users  50M Nov 20 20:16 df_chunk_ag
-rw-r--r-- 1 1000 users  50M Nov 20 20:26 df_chunk_ah
-rw-r--r-- 1 1000 users  50M Nov 20 20:37 df_chunk_ai
-rw-r--r-- 1 1000 users  50M Nov 20 20:48 df_chunk_aj
-rw-r--r-- 1 1000 users  50M Nov 20 20:58 df_chunk_ak
-rw-r--r-- 1 1000 users  50M Nov 20 21:08 df_chunk_al
-rw-r--r-- 1 1000 users  50M Nov 20 21:20 df_chunk_am
-rw-r--r-- 1 1000 users  50M Nov 20 21:31 df_chunk_an
-rw-r--r-- 1 1000 users  50M Nov 20 21:39 df_chunk_ao
-rw-r--r-- 1 1000 users  36M Nov 20 21:45 df_chunk_ap
-rw-r--r-- 1 root root  786M Nov 20 23:26 df_merged_filtered.parquet
root@inspect-pvc:/# 
i dont see it. jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud delete pod inspect-pvc
pod "inspect-pvc" deleted
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f baseline-job.yaml
error: the path "baseline-job.yaml" does not exist
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl apply -f baseline_job.yaml
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> cpu limit <4> is higher than the maximum allowed ratio of <1.2>
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> memory limit <32Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/baseline-job configured
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-data-download-jlc3q-q47vk      0/1     Pending     0          71m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          22h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          22h
pod-cc5m4-train                    0/1     Error       0          2d1h
pod-dbkyd-train                    0/1     Error       0          11h
pod-pvc-jlc3q                      1/1     Running     0          76m
pod-pvc-jm2rc                      1/1     Running     0          63m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-data-download-jlc3q-q47vk      0/1     Pending     0          71m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          22h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          22h
pod-cc5m4-train                    0/1     Error       0          2d1h
pod-dbkyd-train                    0/1     Error       0          11h
pod-pvc-jlc3q                      1/1     Running     0          76m
pod-pvc-jm2rc                      1/1     Running     0          63m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud describe job baseline-job | grep -A5 Events
Events:            <none>
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
my baselne yaml file is named baseline_job.yaml
whats next. 
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> cpu limit <4> is higher than the maximum allowed ratio of <1.2>
Warning: [container-must-meet-memory-and-cpu-ratio] container <baseline> memory limit <32Gi> is higher than the maximum allowed ratio of <1.2>
job.batch/baseline-job configured
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-data-download-jlc3q-q47vk      0/1     Pending     0          76m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          22h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          22h
pod-cc5m4-train                    0/1     Error       0          2d1h
pod-dbkyd-train                    0/1     Error       0          11h
pod-pvc-jlc3q                      1/1     Running     0          81m
pod-pvc-jm2rc                      1/1     Running     0          68m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get pods
NAME                               READY   STATUS      RESTARTS   AGE
job-data-download-jlc3q-q47vk      0/1     Pending     0          76m
job-ljabxf-resnet18-train-qbksm    0/1     Completed   0          22h
job-ljabxf-simpledla-train-82bgh   0/1     Completed   0          22h
pod-cc5m4-train                    0/1     Error       0          2d1h
pod-dbkyd-train                    0/1     Error       0          11h
pod-pvc-jlc3q                      1/1     Running     0          81m
pod-pvc-jm2rc                      1/1     Running     0          68m
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ kubectl -n gp-engine-mizzou-dsa-cloud get jobs baseline-job
NAME           STATUS   COMPLETIONS   DURATION   AGE
baseline-job   Failed   0/1           13h        13h
jovyan@jupyter-naaxk6-missouri-edu---2351cae4:~/cloud-computing-project/kubernetes$ 
save all our progress for now. i need to start a new chat
save our progress in memory. number 2. remember everything
like what we did last night. save everything in memory all our progress so ghat when i start a new chat we know wher ewe are
I mean save all our progress about where we are in my project. You did it so many times before why are you being difficult right now
Also do not gaslight me with "Breathe, seriously" or "calm down" 
You're always gaslighting me

ChatGPT can make mistakes. Check important info.


```

**How You Used This Output:**  
*(Describe step-by-step what you did with the AI-generated content)*
```
[Example: "I used the AI's code suggestion as a starting point, then modified the variable names to match my dataset, added error handling, and tested it with my specific data."]

1. I asked AI for a starting template (ex. script structure, Dockerfile, or Kubernetes YAML examples)
2. I copied only the parts that were relevant and removed anything that didn’t match my project
3. I changed names and paths to match my repo and Nautilus setup (folder structure, PVC mount path, input/output locations)
4. I updated the code to match my model and data workflow (preprocessing, tokenization, baseline model, fine-tuning, and evaluation)
5. When something failed, I checked pod logs and errors and either fixed it myself or asked AI to explain the error and suggest options
6. I reran and tested the jobs until they produced the expected outputs and metrics
7. I kept the final version only if I understood what it was doing and it worked correctly


```

---

### AI Tool #2 *(Copy this section if you used additional tools)*

**Tool Name/Platform:** ________________________________

**Date & Time of Use:** ________________________________

**Purpose of Use:** ________________________________

**Exact Prompt(s) or Query(ies) Used:**
```




```

**Complete AI Output/Response:**
```




```

**How You Used This Output:**
```




```

---

## Final Work Attribution

**Percentage of final work that is your original contribution:** ___70__%
**Brief summary of your independent work process:**  
*(Describe the parts of the assignment you completed entirely on your own)*
```
This project was based on my previous NLP project that I worked on earlier this semester. For this class, I took that work and split it into separate scripts, containerized it with Docker, and ran it on Nautilus. I handled the overall setup, running the jobs, fixing issues when things failed, and checking the results. I used AI frequently to help break the code apart and work through errors, but the core logic and final results are my own.



```

**Learning reflection:**  
*(What did you learn through this process? How did the AI tool help or hinder your understanding?)*
```

Through this process, I learned how to take an existing ML project and actually make it run in a cloud environment. I got more comfortable with Docker, Kubernetes Jobs, PVCs, and reading pod logs to figure out why things failed. Running jobs on Nautilus made it clear that small mistakes in paths, resources, or configs can break everything, and that debugging in the cloud is very different from running code locally.

AI was mainly useful as a support tool when I needed examples, help breaking code into scripts, or explanations for error messages. It didn’t always apply cleanly to my setup, so I still had to test things, debug failures, and figure out what was actually going wrong. In the end, AI helped a lot and saved me time as well when I was researching for articles and other literatures, but I was responsible for getting the pipeline to run correctly from start to finish.

```

---

## Academic Integrity Acknowledgment

By submitting this appendix, I affirm that:
- [X] I have disclosed ALL AI tool usage for this assignment
- [X] The prompts and outputs listed above are complete and accurate
- [X] I understand that undisclosed AI usage constitutes academic dishonesty
- [X] The final submitted work represents my understanding of the course material

**Student Signature:** ______________Nathaniel Antonio__________________  
**Date:** ____________12/17/2025____________________

---

*Submit this completed appendix along with your assignment. Failure to include this form when AI tools were used will be treated as academic dishonesty under university policy.*