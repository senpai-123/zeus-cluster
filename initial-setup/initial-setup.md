# AWS Cluster Setup Guide

This project documents the setup of both **Slurm** and **LSF** clusters on AWS using EC2 instances. Each scheduler will have:
- 1 Master node
- 2 Compute nodes

---

## 1. Cluster Architecture

- **Total EC2 Instances**: 6
  - **Slurm**: 1 master + 2 compute
  - **LSF**: 1 master + 2 compute
- **Shared Subnet**: All instances should be in the same subnet for easier internal communication.

---

## 2. EC2 Instance Setup

- Launch 6 EC2 instances (Amazon Linux / CentOS / RHEL as per your need)
- Modify **inbound rules** of the Security Group:
  - Allow `SSH` (port 22)
  - Allow `All TCP` and `All UDP` traffic 

---

## 3. SSH Access via PuTTY

Configure **PuTTY** for each instance using the `.ppk` key for authentication

---

## 4. Set Hostnames (for easier management)

On each server, set a recognizable hostname:

```bash
sudo hostnamectl set-hostname slurm-master   # example
```

---

## 5. Generate SSH Key (on master)

```bash
ssh-keygen -t rsa
```

---

## 6. Set Up Passwordless SSH

- Copy the public key to all compute nodes:
 
```bash
cat ~/.ssh/id_rsa.pub
```
- Then, on each compute node, paste the public key here:

```bash
sudo vim ~/.ssh/authorized_keys
```

---

## 7. Update /etc/hosts

Add all private IPs with their corresponding hostnames for name resolution:

 ```bash
sudo vim /etc/hosts
```

Example:
```bash
172.31.28.51  slurm-master
172.31.18.149 slurm-compute1
172.31.22.102 slurm-compute2
...
```

---

## 8. Verify SSH Connectivity
From the master node, try:

```bash
ssh slurm-compute1
ssh slurm-compute2
```

Repeat the check between all nodes to ensure passwordless SSH is functioning.
