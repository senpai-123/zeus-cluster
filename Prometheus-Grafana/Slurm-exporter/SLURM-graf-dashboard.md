# Customized SLURM Grafana Dashboard

This dashboard is a modified version of the default SLURM dashboard for **Prometheus + Grafana**. It helps visualize key SLURM metrics like node status, job counts, CPU utilization, and partition-level statistics.

---
## Panel Configurations
### 1. For SLURM Statistics: (Pie)
#### Idle Nodes
```promql
slurm_nodes_idle
```
#### Mixed Nodes
```promql
slurm_nodes_mix
```
#### Allocated Nodes
```promql
slurm_nodes_alloc
```
#### Failed Nodes
```promql
slurm_nodes_fail
```
#### Drained Nodes
```promql
slurm_nodes_drain
```
#### Down Nodes
```promql
slurm_nodes_down
```
#### Error Nodes
```promql
slurm_nodes_err
```

### 2. For Running Jobs: (Stat)
```promql
slurm_queue_running
```

### 3. For Pending Jobs: (Stat)
```promql
slurm_queue_pending
```

### 4. For Total SLURM Nodes: (Gauge)
```promql
slurm_nodes_idle
+ slurm_nodes_alloc
+ slurm_nodes_down
+ slurm_nodes_drain
+ slurm_nodes_fail
+ slurm_nodes_mix
+ slurm_nodes_resv
+ slurm_nodes_maint
+ slurm_nodes_comp
+ slurm_nodes_err
```

### 5. For Total No. of Cores: (Gauge)
```promql
slurm_cpus_total
```

### 6. For Job Statistics: (Status History)
#### Pending Jobs
```promql
slurm_queue_pending
```
#### Suspended Jobs
```promql
slurm_queue_suspended
```
#### Failed Jobs
```promql
slurm_queue_failed
```
#### Preempted Jobs
```promql
slurm_queue_preempted
```
#### Timedout Jobs
```promql
slurm_queue_timeout
```
#### Completing Jobs
```promql
slurm_queue_completing
```
#### Cancelled Jobs
```promql
slurm_queue_cancelled
```
#### Node Fail Jobs
```promql
slurm_queue_node_fail
```

### 7. For SLURM Utilization: (Stat)
#### Min Utilization
```promql
min((slurm_node_cpu_alloc / slurm_node_cpu_total) * 100)
```
#### Max Utilization
```promql
max((slurm_node_cpu_alloc / slurm_node_cpu_total) * 100)  
```
#### Avg Utilization
```promql
avg((slurm_node_cpu_alloc / slurm_node_cpu_total) * 100) 
```

### 8. For DEBUG Partition: (Time-Series)
#### Idle CPUs
```promql
slurm_partition_cpus_idle{partition="debug"}
```
#### Total CPUs
```promql
slurm_partition_cpus_total{partition="debug"}
```
#### Allocated CPUs
```promql
slurm_partition_cpus_total{partition="debug"} - slurm_partition_cpus_idle{partition="debug"}
```

### 9. For HIGHPRIO Partition: (Time-Series)
#### Idle CPUs
```promql
slurm_partition_cpus_idle{partition="highprio"}
```
#### Total CPUs
```promql
slurm_partition_cpus_total{partition="highprio"}
```
#### Allocated CPUs
```promql
slurm_partition_cpus_total{partition="highprio"} - slurm_partition_cpus_idle{partition="highprio"}
```

### 10. Expected Output:

![image](https://github.com/user-attachments/assets/1e95c635-25aa-4d53-89d0-e3249ca67286)
