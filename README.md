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

- **Name:**  k3s-demo-server
- **AMI:** Ubuntu Server 22.04 LTS
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


-**Configure kubectl:**

mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown $USER:$USER ~/.kube/config
chmod 600 ~/.kube/config
export KUBECONFIG=~/.kube/config


