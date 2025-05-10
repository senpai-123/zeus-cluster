# Job Accounting & Queue Setup in LSF

Once LSF is installed and configured, follow these steps to enable job accounting and define custom queues as per your HPC workload requirements.

---

## Job Accounting Path

LSF records job accounting data in the `lsb.acct` file. You can view it using:

```bash
cat /home/lsf_home/work/zeus/logdir/lsb.acct
```

## Configure Queues

Edit the lsb.queues file to define and customize your job queues:
```bash
sudo vim /home/lsf_home/conf/lsbatch/zeus/configdir/lsb.queues
```
### Refer to [`lsb.queues`](https://github.com/senpai-123/zeus-cluster/blob/main/LSF/lsb.queues)

After modifying the file, reconfigure the system:

```bash
badmin reconfigure
```

Check active queues with:

```bash
bqueues
```

### Expected Output:

<img width="497" alt="image" src="https://github.com/user-attachments/assets/c2d6662a-2f3f-4827-9304-3a1e35233b12" />

## Run a Test Job

Submit a simple test job to ensure everything is working:

```bash
bsub -q normal echo "Test job"
```

Check if the job was logged in `lsb.acct`:

```bash
cat /home/lsf_home/work/zeus/logdir/lsb.acct
```

## Submitting Real Jobs

You can now submit other jobs from HPC applications.

### See setup details here: [`HPC-Applications-setup`](https://github.com/senpai-123/zeus-cluster/tree/main/hpc-applications)

## View Job Accounting

Use the following commands for job accounting:

```bash
bacct -l <job_id>      # Show detailed info for a specific job
bacct -u <username>    # Show job history for a specific user
bjobs -u all           # Show jobs from all users
```

## Queue & Scheduling Policies

Queue-specific config:
```bash
sudo cat /home/lsf_home/conf/lsbatch/zeus/configdir/lsb.queues
#Priority, limits, scheduling rules, fairshare, etc., to set default 
```
Global scheduling config:
```bash
sudo cat /home/lsf_home/conf/lsbatch/zeus/configdir/lsb.params
```

After editing either of these files, always run:

```bash
badmin reconfigure
```

## Human-Readable Job History

The `lsb.acct` file is in a binary format that's hard to read manually.

Refer to the IBM documentation for format structure: [`IBM-lsb.acct`](https://www.ibm.com/docs/ro/spectrum-lsf/10.1.0?topic=files-lsbacct)

To simplify analysis, we created a custom Python script that:

- Converts the job history into a .csv file

- Transforms timestamps into human-readable date-time

- Extracts only necessary columns (you can customize this)

### Script: [`lsf_cleaned_data.py`](https://github.com/senpai-123/zeus-cluster/blob/main/LSF/lsf_cleaned_data.py)
