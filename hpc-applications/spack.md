# HPC Application Installation Using Spack with Amazon EFS

## What is Spack?

**Spack** is a flexible package manager designed for **high-performance computing (HPC)** environments. It allows users to build and manage multiple versions and configurations of scientific software on different platforms and architectures. It supports dependency management, compiler variations, and allows for easy module generation and environment management.

**Learn more:** [Spack Installation Website](https://spack-tutorial.readthedocs.io/en/latest/tutorial_basics.html)

---

## Spack Setup on Shared Filesystem (Amazon EFS)

I used a shared filesystem (Amazon EFS) mounted at `/apps` to install HPC applications centrally so they could be used across multiple servers.

### Step-by-Step Installation

#### 1. Install Required Dependencies
```bash
sudo dnf install gcc-gfortran redhat-lsb-core python3 unzip
#Note: Python 3 version ≥ 3.5 is required for Spack.
```
#### 2. Clone Spack Repository
```bash
git clone -c feature.manyFiles=true --depth=2 https://github.com/spack/spack.git
```

#### 3. Source the Spack Environment
```bash
. spack/share/spack/setup-env.sh
```

#### 4. Add Spack to .bashrc for Persistent Use
```bash
echo 'source $HOME/spack/share/spack/setup-env.sh' >> ~/.bashrc
source ~/.bashrc
```
### Useful Spack CLI Commands
```bash
| Command                                  | Description                                               |
| ---------------------------------------- | --------------------------------------------------------- |
| `spack spec <package-name>`              | Shows a detailed dependency graph and build plan          |
| `spack versions <package-name>`          | Lists available versions of the package                   |
| `spack install <package-name%@compiler>` | Installs the package with a specific version and compiler |
| `spack location -i <package-name>`       | Displays the installation path of a package               |
| `spack compilers`                        | Lists all detected compilers on the system                |
| `spack compiler info <compiler>`         | Shows detailed info about a specific compiler             |
| `spack load <package-name>`              | Loads the package into the current shell session          |
| `spack uninstall -y <package-name>`      | Uninstalls the specified package without confirmation     |
```
### Spack Special Syntax

-`@` is used to specify a version

-`%` is used to specify a compiler

#### Example: Install Bowtie2 with Specific Version and Compiler
```bash
spack install bowtie2@2.4.1%gcc
```

### Where Are Packages Stored?
Spack uses a built-in repository for package definitions:

```bash
cd $HOME/spack/var/spack/repos/builtin/
```

### Set Up Module Paths
To enable Lmod-based environment modules:

```bash

spack config add modules:default:enable:[lmod]
spack find --path lmod
spack config get modules

echo 'export MODULEPATH=$SPACK_ROOT/share/spack/lmod/linux-rhel8-x86_64/Core:$MODULEPATH' >> ~/.bashrc
echo 'export MODULEPATH=$SPACK_ROOT/share/spack/lmod/linux-rhel8-x86_64:$MODULEPATH' >> ~/.bashrc

#Reload your shell to apply:
source ~/.bashrc
```

### Installed Applications for Testing
Using Spack, I installed and tested the following HPC applications:

-Bowtie2
-HPL (High-Performance Linpack)
-MPI (e.g., OpenMPI)
-BLAST

These were tested to validate application access and performance across nodes in the HPC cluster using the shared EFS.


