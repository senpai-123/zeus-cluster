# Munge Setup

Before installing SLURM, we need to install **Munge**, which is a crucial authentication service.

---

## What is Munge?

**MUNGE (MUNGE Uid 'N' Gid Emporium)** is an authentication service for creating and validating credentials. It is required by SLURM to securely authenticate and authorize user jobs across multiple nodes in the cluster. Munge must be installed and configured identically on the master and all compute nodes.

---

## Install Required Dependencies (for RHEL 8)

Ensure all necessary dependencies are installed for Munge:

```bash
sudo dnf update -y openssh
sudo dnf groupinstall "Development Tools" -y 
sudo dnf install -y dnf-plugins-core
```

## Install Munge from Source

Refer to [`Munge-Realeases`](https://github.com/dun/munge/releases/)

```bash
wget https://github.com/dun/munge/releases/download/munge-0.5.16/munge-0.5.16.tar.xz
tar xJf munge-0.5.16.tar.xz
cd munge-0.5.16
./configure \
  --prefix=/usr \
  --sysconfdir=/etc \
  --localstatedir=/var \
  --runstatedir=/run
make
make check
sudo make install
```

## Configure Munge

Set correct ownership and permissions:

```bash
sudo chown -R munge:munge /etc/munge /var/lib/munge /var/log/munge
sudo chmod 0700 /etc/munge /var/lib/munge
sudo chmod 0755 /var/log/munge
```

On the master node only, generate the key:

```bash
sudo /usr/sbin/create-munge-key
```

Now, securely copy the key to all compute nodes:

```bash
scp /etc/munge/munge.key user@compute-node:/etc/munge/munge.key
```

Verify checksum consistency on all nodes:

```bash
sudo cat /etc/munge/munge.key | sha256sum
```

## Start and Enable Munge

On all nodes (master + compute):

```bash
sudo systemctl start munge
sudo systemctl status munge
sudo systemctl enable munge
```

### Munge is now active and ready, paving the way for SLURM installation.
