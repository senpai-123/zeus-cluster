# IBM LSF Community Edition Installation Guide on HPC Cluster

This guide provides step-by-step instructions to install the IBM LSF (Load Sharing Facility) Community Edition on an HPC cluster using the latest available version.

---

## Prerequisites

1. IBM Account - Required to download the LSF installer.
2. Download the latest **LSF Community Edition tarball** from IBM:  
   [IBM LSF Community Edition](https://www.ibm.com/products/spectrum-lsf/community-edition)
3. Upload the `.tar.gz` file to your desired instance directory.

---

## Directory Setup

```bash
sudo mkdir /home/lsf_install_files
sudo mkdir /home/lsf_home

sudo cp /apps/lsfsce10.2.0.12-x86_64.tar.gz /home/lsf_install_files/
sudo chown ec2-user:ec2-user -R /home/lsf_install_files/

sudo useradd lsfadmin
sudo chown -R lsfadmin:lsfadmin /home/lsf_home/
```

## Extract and Install LSF
 
```bash
cd /home/lsf_install_files/
tar -xvzf lsfsce10.2.0.12-x86_64.tar.gz

cd lsfsce10.2.0.12-x86_64/lsf/
tar -vxf lsf10.1_lsfinstall_linux_x86_64.tar.Z

cd lsf10.1_lsfinstall
vim install.config  # Edit based on README instructions and ensure it matches across master and compute nodes
```

#### Refer to [`install.config`]()  

You can customize `install.config` according to your requirements. Below are the key parameters to update:

- `LSF_TOP`: Path where you want LSF to be installed.
- `LSF_ADMINS`: List of admin users allowed to manage the LSF system.
- `LSF_CLUSTER_NAME`: A name for your LSF cluster.
- `LSF_MASTER_LIST`: Hostnames of the LSF master servers.
- `LSF_TARDIR`: Path to the directory containing the LSF installation tarballs.
- `CONFIGURATION_TEMPLATE`: Set to `default` or another template of your choice.
- `LSF_ADD_SERVERS`: Hostnames of compute servers to be added.
- `LSF_ADD_CLIENTS`: (Optional) Hostnames of client-only nodes.
- `ENABLE_DYNAMIC_HOSTS`: Set to `Y` to enable dynamic host addition.
- `LSF_DYNAMIC_HOST_WAIT_TIME`: Time in seconds to wait before adding a dynamic host.

Make sure to keep this configuration consistent across all nodes in your cluster.


## Dependencies and Permissions

```bash
sudo dnf install ed  # Required for install.config to work

sudo chmod 755 /home/lsf_home

sudo ./lsfinstall -f install.config
```

## Post Installtion

```bash
cd /home/lsf_home/conf/
source profile.lsf  # Add to .bashrc for persistence

sudo dnf install -y libnsl  # Required by LSF daemons
```

## Set permissions for LSF Binaries

```bash
sudo chmod u+s /home/lsf_home/10.1/linux2.6-glibc2.3-x86_64/bin/bctrld

sudo chown root:root /home/lsf_home/10.1/linux2.6-glibc2.3-x86_64/bin/{badmin,lsadmin}
sudo chown root:root /home/lsf_home/10.1/linux2.6-glibc2.3-x86_64/etc/eauth

sudo chmod 4755 /home/lsf_home/10.1/linux2.6-glibc2.3-x86_64/bin/{badmin,lsadmin}
sudo chmod 4755 /home/lsf_home/10.1/linux2.6-glibc2.3-x86_64/etc/eauth
```

## Configure `lsf.sudoers`

```bash
sudo vim /etc/lsf.sudoers
```
Add the following lines:

```bash
LSF_STARTUP_USERS="lsfadmin ec2-user"
LSF_STARTUP_PATH=/home/lsf_home/10.1/linux2.6-glibc2.3-x86_64/etc/
#[esc] wq!

sudo chmod 600 /etc/lsf.sudoers
sudo chown root:root /etc/lsf.sudoers
```

## Configure `lsf.conf`

```bash
sudo vim /home/lsf_home/conf/lsf.conf
```
Add these lines (ensure consistency on master and compute nodes):

```bash
LSF_ACCT=Y
LSB_ACCTDIR=/home/lsf_home/work/zeus/logdir/lsb.acct
LSF_RSH=ssh
LSF_RSH_PORT=22
```

## Disable iptables (Important)

```bash
sudo systemctl stop iptables  # Run this on all instances
```

## Start LSF Daemons

#### On Master Node:

```bash
lsadmin ckconfig
lsadmin limstartup
lsadmin resstartup
badmin ckconfig
badmin mbdrestart
badmin hstartup
badmin hopen
badmin qopen

lsid     # Verify
bhosts   # Verify
```

#### On Compute Node:

```bash
lsadmin ckconfig
lsadmin limstartup
lsadmin resstartup
badmin ckconfig
badmin mbdrestart
badmin hstartup
badmin hopen
badmin qopen

lsid     # Verify
bhosts   # Verify
```

### Notes

- Always ensure `install.config` and `lsf.conf` files are **identical across master and compute nodes**.
- Add `source /home/lsf_home/conf/profile.lsf` to your `.bashrc` for persistent environment setup.



