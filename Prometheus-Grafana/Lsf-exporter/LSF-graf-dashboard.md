# Custom Grafana Dashboard for LSF Exporter

This guide outlines the process to create a **custom Grafana dashboard** using metrics from the **LSF Exporter**. It assumes Prometheus is already scraping the LSF Exporter endpoint and Grafana is connected to the Prometheus data source.

---

## Steps to Create Dashboard

1. Go to **Grafana → + Create → Dashboard**
2. Click on **Add a new panel**
3. Set the **Data Source** to Prometheus
4. Use the PromQL queries below in respective panels
5. Choose the appropriate **panel visualization** (Pie, Stat, Gauge, Time series, etc.)
6. Save your dashboard

---

## Panel Configurations
### 1. For LSF Statistics: (Pie)
#### Ok Nodes 
```promql
count(lsf_bhost_host_status == 1)
```
#### Closed Nodes
```promql
count(lsf_bhost_host_status == 0)
```

### 2. For Running Jobs: (Stat)
```promql
sum(lsf_bhost_runingjob_count)
```

### 3. For Pending Jobs: (Stat)
```promql
sum(lsf_bqueues_pendingjob_count)
```

### 4. For Total LSF Nodes: (Gauge)
```promql
count(lsf_lshosts_ncpus{server_type="servers"})
```

### 5. For Total No. of Cores: (Gauge)
```promql
sum(lsf_lshosts_ncpus{server_type="servers"})
```

### 6. or Job statistics: (Status History)
#### Total running Jobs
```promql
sum(lsf_bhost_runingjob_count) 
```
#### Total pending Jobs
```promql
sum(lsf_bqueues_pendingjob_count)
```
#### Total Suspended Jobs
```promql
sum(lsf_bhost_ssuspjob_count) + sum(lsf_bhost_ususpjob_count) 
```

### 7. For LSF Utilization: (Stat)
#### Min Utilization
```promql
min(lsf_bhost_runingjob_count / on(host_name) lsf_lshosts_ncpus{server_type="servers"}) * 100 
```
#### Max Utilization
```promql
max(lsf_bhost_runingjob_count / on(host_name) lsf_lshosts_ncpus{server_type="servers"}) *100  
```
#### Avg Utilization
```promql
avg(lsf_bhost_runingjob_count / on(host_name) lsf_lshosts_ncpus{server_type="servers"}) *100  
```

### 8. Running Jobs for each Queue: (Time-Series)
```promql
sum(lsf_bqueues_runingjob_count) by (queues_name)
```

### 9. Pending for each Queue: (Time-Series)
```promql
sum(lsf_bqueues_pendingjob_count) by (queues_name)
```

### 10. Expected Output:

![image](https://github.com/user-attachments/assets/1c9b8dba-fb46-4d6c-b18f-8f62f795d6f8)




