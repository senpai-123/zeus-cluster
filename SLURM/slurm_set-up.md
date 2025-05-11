# SLURM Installation Guide

After installing **Munge**, proceed with SLURM setup. 
### Refer to [`Munge Setup`](https://github.com/senpai-123/zeus-cluster/blob/main/SLURM/munge_set-up.md) before continuing.  
This guide also includes the **SLURM accounting database setup using MariaDB**.

---

## Install SLURM Dependencies (RHEL 8)

Ensure all dependencies are installed:

```bash
sudo dnf install -y gcc gcc-c++ perl make autoconf automake libtool wget pam-devel munge-libs openssl openssl-devel numactl numactl-devel hwloc hwloc-devel lua lua-devel readline readline-devel rrdtool rrdtool-devel ncurses ncurses-devel libibmad libibumad libcurl-devel lua-devel glibc glibc-devel glib2 glib2-devel zlib zlib-devel json-c json-c-devel libevent libevent-devel git mariadb mariadb-server mariadb-devel systemd-devel kernel-headers kernel-devel dbus dbus-devel munge munge-libs munge-devel python3 python3-devel libarchive
```

Enable the CRB (CodeReady Builder) repo:

```bash
sudo dnf config-manager --set-enabled crb
```

If CRB is not available, install packages manually:

- [`hwloc-devel`](https://repo.almalinux.org/almalinux/8/PowerTools/x86_64/os/Packages/hwloc-devel-2.2.0-3.el8.x86_64.rpm)
- [`lua-devel`](https://repo.almalinux.org/almalinux/8/PowerTools/x86_64/os/Packages/lua-devel-5.3.4-12.el8.x86_64.rpm)
- [`rrdtool-devel`](https://repo.almalinux.org/almalinux/8/PowerTools/x86_64/os/Packages/rrdtool-devel-1.7.0-16.el8.i686.rpm)
- [`munge-devel`](https://repo.almalinux.org/almalinux/8/PowerTools/x86_64/os/Packages/munge-devel-0.5.13-2.el8.x86_64.rpm)

## MariaDB (SLURM Accounting Database)

### On master node only:

Start and enable MariaDB:

```bash
sudo systemctl start mariadb
sudo systemctl status mariadb
sudo systemctl enable mariadb
```

Secure the MariaDB installation:

```bash
mysql_secure_installation
```
**You may press ENTER to skip setting a root password and other settings.**

Create the slurm user:

```bash
sudo useradd -r -m -s /sbin/nologin slurm
```

Configure the SLURM accounting database:

```sql
create database slurm_acct_db;
sudo mysql -u root -p
GRANT ALL PRIVILEGES ON slurm_acct_db.* TO 'slurm'@'%' IDENTIFIED BY 'slurm_zeus';
GRANT ALL PRIVILEGES ON slurm_acct_db.* TO 'slurm'@'slurm-master' IDENTIFIED BY 'slurm_zeus';
FLUSH PRIVILEGES;
EXIT
```

Create a new config file:

```bash
sudo vim /etc/my.cnf.d/innodb.cnf
```

Add:

```bash
[mysqld]			
 innodb_buffer_pool_size=1024M 			
 innodb_log_file_size=64M 			
 innodb_lock_wait_timeout=900
```		

Apply changes:

```bash
sudo systemctl stop mariadb 		
sudo mv /var/lib/mysql/ib_logfile? /tmp/		
sudo systemctl start mariadb		
```

## Download and Install SLURM (RPM Build) 

**Get latest version from [`Slurm Download`](https://www.schedmd.com/download-slurm/)** 

```bash
wget https://download.schedmd.com/slurm/slurm-24.11.5.tar.bz2
```

Install required tools:

```bash
sudo dnf install -y rpm-build
mkdir -p ~/rpmbuild/{BUILD,RPMs,SOURCES,SPECS,SRPMS}
mv slurm-24.11.5.tar.bz2  ~/rpmbuild/SOURCES/
cd ~/rpmbuild/SOURCES/
rpmbuild -ta slurm-24.11.5.tar.bz2
cd ~/rpmbuild/RPMS/x86_64/
sudo dnf --nogpgcheck localinstall slurm-*
```

## Configure `slurmdbd.conf` 

Edit the config:

```bash
sudo vim /etc/slurm/slurmdbd.conf 
```
### Refer to [`slurmdbd.conf`](https://github.com/senpai-123/zeus-cluster/blob/main/SLURM/slurmdbd.conf)

Set permissions:

```bash
sudo chown slurm:slurm /etc/slurm/slurmdbd.conf
sudo chmod 600 /etc/slurm/slurmdbd.conf
```

Start SLURM database daemon:

```bash
sudo systemctl start slurmdbd
sudo systemctl status slurmdbd
sudo systemctl enable slurmdbd
```

## Configure `slurm.conf`

**Ensure the same `slurm.conf` file and permissions across all nodes.**

Edit:

```bash
sudo vim /etc/slurm/slurm.conf
```

### Refer to [`slurm.conf`](https://github.com/senpai-123/zeus-cluster/blob/main/SLURM/slurm.conf)
To create your own `slurm.conf` refer to [`Slurm Configuration Tool`](https://slurm.schedmd.com/configurator.html)

Set permissions:

```bash
sudo chown slurm:slurm /etc/slurm/slurm.conf
sudo chmod 644 /etc/slurm/slurm.conf
```

## Setup SLURM Directories

### On master node:

```bash
sudo mkdir -p /var/spool/slurmctld
sudo chown -R slurm:slurm /var/spool/slurmctld
sudo chmod 755 /var/spool/slurmctld

sudo mkdir /var/log/slurm
sudo touch /var/log/slurm/slurmctld.log
sudo touch /var/log/slurm/slurm_jobacct.log
sudo touch /var/log/slurm/slurm_jobcomp.log
sudo chown -R slurm:slurm /var/log/slurm/
```

### On compute node:

```bash
sudo mkdir -p /var/spool/slurmd				
sudo chown slurm:slurm /var/spool/slurmd				
sudo chmod 755 /var/spool/slurmd
			
sudo mkdir /var/log/slurm/				
sudo touch /var/log/slurm/slurmd.log				
sudo chown -R slurm:slurm /var/log/slurm/slurmd.log
```

## Test Configuration

Run this on each compute node to check system details:

```bash
slurmd -C
```

Example output:

<img width="479" alt="image" src="https://github.com/user-attachments/assets/83700de7-3afb-4073-9716-da2d858af9c0" />

## Start SLURM Daemons

### On Compute Nodes:

```bash
sudo systemctl start slurmd.service
sudo systemctl status slurmd.service
sudo systemctl enable slurmd.service
```

### On Master Node:

```bash
sudo systemctl start slurmctld.service
sudo systemctl status slurmctld.service
sudo systemctl enable slurmctld.service
```

### References:

- [Installation Guide](https://southgreenplatform.github.io/trainings/hpc/slurminstallation/)
- [Official Slurm Documentation](https://slurm.schedmd.com/documentation.html)

