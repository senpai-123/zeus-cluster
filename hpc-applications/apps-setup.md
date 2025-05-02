# Setting Up a Shared Filesystem (EFS) for HPC Applications on AWS

To enable access to shared applications across multiple HPC schedulers/servers in a cloud environment, I created a shared filesystem using **Amazon EFS (Elastic File System)**. This allows applications to be installed once and accessed from multiple nodes.

## Steps to Set Up EFS

### 1. Create an Amazon EFS
- Go to the Amazon EFS Console
- Create a new file system. In my case, I named it `hpc-applications`
- Ensure it is accessible within your VPC and mount targets are configured for the availability zones your instances are running in

### 2. Mount the EFS on a Linux Server

I used the **"Mount via DNS"** option with the **NFS client**.

#### On each server:
```bash
# Install NFS utilities
sudo dnf install -y nfs-utils  

# Create a mount point
sudo mkdir -p /apps

# Mount the EFS (replace the placeholder with the actual DNS name from AWS)
sudo mount -t nfs4 -o nfsvers=4.1,tcp <your-efs-dns>:/ /apps

# Verify the mount
df -h /apps
