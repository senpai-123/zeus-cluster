# LSF Exporter Setup Guide

This guide explains how to install and run the **LSF Exporter** for Prometheus and how to connect it to **Grafana** for visualizing job and node metrics in an IBM Spectrum LSF cluster.

---

## What is LSF Exporter?

[LSF Exporter](https://github.com/a270443177/lsf_exporter) is a Prometheus exporter that gathers **LSF cluster metrics** such as:

- Running/pending job statistics
- Host/node load, usage, and availability
- Queue and slot information

It exposes these metrics at `http://<host>:9818/metrics` so Prometheus can scrape and store them.

---

## Prerequisites

- Go installed (>=1.17)
- LSF environment already configured and `lsload`, `bhosts`, `bjobs` accessible from shell

---

## Installation Steps

### 1. Ensure Go is Installed

Check if Go is available:

```bash
printenv | grep go
which go
go version
```
If not, install and set the PATH:
```bash
echo 'export PATH=/usr/local/go/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### 2. Install LSF Exporter
```bash
go install github.com/a270443177/lsf_exporter@latest
```
Confirm:
```bash
ls $GOPATH/bin
```
### 3. Run the Exporter
```bash
$GOPATH/bin/lsf_exporter
```
You should see metrics served at port 9818.

### 4. Run as Background Service
To keep it running in the background:
```bash
nohup $GOPATH/bin/lsf_exporter > lsf_exporter.log 2>&1 &
```

### 5. Confirm It's Running
```bash
lsof -i :9818
netstat -tcnlp | grep 9818
```

Expected output:

<img width="613" alt="image" src="https://github.com/user-attachments/assets/5a25160e-f910-4786-aa61-5da6724f5f53" />

### 6. Connect LSF Exporter to Prometheus

Edit your Prometheus config `/etc/prometheus/prometheus.yml`. 
#### Refer to [prometheus.yml](https://github.com/senpai-123/zeus-cluster/blob/main/Prometheus-Grafana/prometheus.yml)
Then restart prometheus.

### 7. Visualize in Grafana

- Check for the metrics at `http://<lsf-exporter-ip>:9818/metrics`
- Connect Prometheus as a Data Source in Grafana: Go to Grafana > Settings > Data Sources > Add data source
- Choose Prometheus-> URL: `http://localhost:9090` (or your Prometheus server IP)
- Click Save & Test
- **Custom Dasboard link: [LSF-Grafana-Dashboard](https://github.com/senpai-123/zeus-cluster/blob/main/Prometheus-Grafana/Lsf-exporter/LSF-graf-dashboard.md)**
