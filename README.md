# Deploy-a-Simple-Python-Flask-App-on-EC2-K3s-NodePort-
Deploy a Python Flask app on a cost-effective k3s single-node cluster on AWS EC2 (t3.medium, Ubuntu 22.04), using NodePort to avoid LoadBalancer issues.

# k3s-flask-nodeport-demo
Guide to deploying a Python Flask app on a Single-Node K3s Kubernetes cluster using NodePort on AWS EC2

---

## 🚀 Deploy a Simple Python Flask App on EC2 (K3s + NodePort)
**Purpose:** Deploy a Python Flask app on a cost-effective k3s single-node cluster on AWS EC2 (t3.medium, Ubuntu 22.04), using NodePort to avoid LoadBalancer issues.

---

### ✅ Assumptions
- EC2:  t3.medium, Ubuntu 22.04
- Access to AWS Console / CLI
- SSH access with key pair

---

### 1️⃣ Launch EC2 Instance
Go to AWS EC2 Console and configure:

- **Name:**  `k3s-demo-server`
- **AMI:** `Ubuntu Server 22.04 LTS`
- **Instance Type:** `t3.medium`
- **VPC:** Default
- **Subnet:** Public Subnet
- **Auto-assign Public IP:** Enabled
- **Storage:** 8 GiB (gp3)

**Security Group - `k3s-sg`:**
- SSH (22): My IP
- HTTP (80): `0.0.0.0/0`
- Custom TCP (6443): My IP (k3s API)
- Custom TCP (30000): `0.0.0.0/0` (NodePort)

---

### 2️⃣ Install K3s
```bash
sudo apt update
curl -sfL https://get.k3s.io | sh -
```

-**Configure kubectl:**
```bash
mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown $USER:$USER ~/.kube/config
chmod 600 ~/.kube/config
export KUBECONFIG=~/.kube/config

```
-**Verify:**
```bash
kubectl get nodes
kubectl get pods -A
```

### 3️⃣ Prepare Flask App with Docker

- Install Docker:
```bash
sudo apt install -y docker.io
sudo usermod -aG docker ubuntu
newgrp docker
```
- Create app directory:
```bash
mkdir python-app && cd python-app
```
- Create app.py:
```bash
nano app.py
```
copy the content from app.py
inside paste the content from app.py
then save the file with ctrl + o
press enter to save the file with the name
now exit with ctrl + x

- Create requirements.txt:
```bash
nano requirements.txt
```
copy the content from requirements.txt
inside paste the content 
then save the file with ctrl + o
press enter to save the file with the name
now exit with ctrl + x

- Create Dockerfile:
```bash
nano Dockerfile
```
copy the content from Dockerfile
inside paste the content 
then save the file with ctrl + o
press enter to save the file with the name
now exit with ctrl + x

### 4️⃣ Push Image to Docker Hub
```bash
docker login
docker build -t docker.io/<your-username>/python-app:latest .
docker push docker.io/<your-username>/python-app:latest
```
***at <your-username> use your docker username***
### 5️⃣ Deploy Flask App on K3s

- Create k3s-deployment.yaml:
```bash
nano k3s-deployment.yaml
```
copy the content from k3s-deployment.yaml 
inside paste the content
then save the file with ctrl + o
press enter to save the file with the name
now exit with ctrl + x

***at <your-username> use your docker username***

- Apply and verify:
```bash
kubectl apply -f k3s-deployment.yaml
kubectl get pods -n default
kubectl get svc -n default
kubectl logs -l app=python-app -n default
```

### 6️⃣ Expose App with NodePort

- Create python-app-nodeport.yaml:
```bash
nano  python-app-nodeport.yaml
```
copy the content from  python-app-nodeport.yaml
inside paste the content
then save the file with ctrl + o
press enter to save the file with the name
now exit with ctrl + x

- Apply and check:
```bash
kubectl apply -f python-app-nodeport.yaml
kubectl get svc python-app-nodeport -n default
```

Update Security Group:

Port: 30000, Source: 0.0.0.0/0 (or restrict to your IP)


### 7️⃣ Test the App

- Local (on EC2):
```bash
kubectl port-forward svc/python-app 8080:80 -n default
```
- Browser (external):
visit the following on your browser
```bash
http://<EC2-PUBLIC-IP>:30000
```

### 9️⃣ Clean Up
```bash
kubectl delete svc python-app-nodeport -n default
kubectl delete svc python-app -n default
kubectl delete deployment python-app -n default
sudo /usr/local/bin/k3s-uninstall.sh
```

Terminate EC2 instance from AWS Console

Delete Docker image or repository from Docker Hub

Monitor usage via AWS Billing Dashboard


### 🎉 You're Done!
You've successfully deployed and exposed a Flask app on a lightweight K3s Kubernetes cluster hosted on AWS EC2.
