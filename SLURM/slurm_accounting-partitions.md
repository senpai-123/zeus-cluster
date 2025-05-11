# SLURM Accounting & Partitions Setup

Once the database is set up, you can configure SLURM job accounting, add users and accounts, create partitions, and set up Quality of Service (QoS) rules to manage job priorities and scheduling policies.
### Refer to [`Slurm-setup`](https://github.com/senpai-123/zeus-cluster/blob/main/SLURM/slurm_set-up.md), to setup the database.
---

## SLURM Accounting & User Setup

SLURM uses `sacct`, `sreport`, and QoS rules to track and control job execution.

#### Useful Accounting Commands:

| Command    | Description                     |
| ---------- | ------------------------------- |
| `sacct`    | Detailed job information        |
| `sreport`  | High-level utilization reports  |
| `sacctmgr` | Manage accounts, users, and QoS |

### Add Default Account and User

```bash
sudo sacctmgr add account default Description="Default account"
sudo sacctmgr add user ec2-user Account=default Cluster=zeus
```

## QoS and Partition Setup

Check Existing QoS:

```bash
sacctmgr show qos
```

Add QoS:

```bash
sudo sacctmgr add qos normal
sudo sacctmgr add qos highprio Preempt=normal Priority=10000
sudo sacctmgr modify qos normal set PreemptMode=REQUEUE
```

Modify Partitions to Use QoS:

```bash
sudo sacctmgr modify partition debug set qos=normal
sudo sacctmgr modify partition highprio set qos=highprio
```

Restart Daemon After Changes:

```bash
sudo systemctl restart slurmdbd
sudo systemctl status slurmdbd
```

## Test Partition and Scheduling

Submit Jobs with Partitions and QoS:

```bash
srun --partition=debug --qos=normal sleep 120 &
srun --partition=highprio --qos=highprio --ntasks=1 --time=00:02:00 sleep 60
```

Check Partitions:

```bash
sinfo
# or
scontrol show partition
```

#### Expected Output Example:

<img width="371" alt="image" src="https://github.com/user-attachments/assets/8cdc0996-f42f-4cb2-8667-346e404f6a7f" />


## Accounting and Reporting Examples

Run the following commands to get detailed accounting reports:

```bash
sacct -S today
sacct --starttime=2025-05-01 --endtime=$(date +%Y-%m-%d)
sacct --allusers --format=JobID,User,Start,End,State,ExitCode
sacct --starttime=2025-01-01 --endtime=$(date +%Y-%m-%d)
sacct --format=JobID,JobName,User,Partition,State,Elapsed,NodeList,CPUTimeRAW,MaxRSS
sacct --starttime=$(date -d "1 year ago" +%Y-%m-%d) --endtime=$(date +%Y-%m-%d) --state=FAILED --format=JobID,JobName,User,Partition,State,Start,End,Elapsed
sacct --starttime=$(date -d "3 months ago" +%Y-%m-%d) --endtime=$(date +%Y-%m-%d) --format=JobID,JobName,User,Partition,State,Start,End,Elapsed
sacct -j <job_id> --format=JobID,JobName,Partition,State,Elapsed,CPUTime,MaxRSS
```

Cluster and User Utilization Reports:

```bash
sreport cluster AccountUtilizationByUser start=$(date -d "3 months ago" +%Y-%m-%d) end=$(date +%Y-%m-%d)
```

Export to File and Analyze:

```bash
sacct --starttime=$(date -d "3 months ago" +%Y-%m-%d) --endtime=now --format=JobID,User,JobName,Partition,State,Start,End,Elapsed,CPUTime,AllocCPUs,NodeList  > slurm_jobs_report.txt

# Split jobs by application (assuming $3 is the application field)
awk '{print > $3 "_jobs.txt"}' slurm_jobs_report.txt

# Create app summary
awk '{count[$3]++} END {for (app in count) print app, count[app]}' slurm_jobs_report.txt > app_summary.txt
```
