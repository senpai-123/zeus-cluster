# Node Exporter Setup Guide

This document covers the installation and configuration of **Node Exporter**, and how to visualize its metrics in **Grafana** via **Prometheus**.

---

## What is Node Exporter?

[Node Exporter](https://github.com/prometheus/node_exporter) is a Prometheus exporter for **hardware and OS-level metrics** exposed by *nix kernels. It provides detailed insights into your system, such as:

- CPU usage
- Memory statistics
- Disk I/O
- Filesystem usage
- Network traffic
- Load averages
- System uptime

---

## Installation Steps

### 1. Download Node Exporter

```bash
wget https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-amd64.tar.gz
```
Link to latest [Releases](https://github.com/prometheus/node_exporter/releases)

### 2. Extract the Archive

```bash
tar -xvzf node_exporter-1.9.1.linux-amd64.tar.gz
```

### 3.Move the Binary
```bash
sudo mv node_exporter-1.9.1.linux-amd64/node_exporter /usr/local/bin/
```

### 4. Set Permissions
```bash
sudo chmod +x /usr/local/bin/node_exporter
sudo chown prometheus:prometheus /usr/local/bin/node_exporter
```

### 5. Create a Systemd Service File
```bash
sudo vim /etc/systemd/system/node_exporter.service
```

#### Refer to [node_exporter.service](https://github.com/senpai-123/zeus-cluster/blob/main/Prometheus-Grafana/Node-exporter/node_exporter.service) 

### 6. Start and Enable Node Exporter

```bash
sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter
sudo systemctl status node_exporter
```

### 7. Connect Node Exporter to Prometheus

Edit your Prometheus config `/etc/prometheus/prometheus.yml`. 
#### Refer to [prometheus.yml](https://github.com/senpai-123/zeus-cluster/blob/main/Prometheus-Grafana/prometheus.yml)
Then restart prometheus.

### 8. Visualize in Grafana

- Connect Prometheus as a Data Source in Grafana: Go to Grafana > Settings > Data Sources > Add data source
- Choose Prometheus-> URL: `http://localhost:9090` (or your Prometheus server IP)
- Click Save & Test
- Import Node Exporter Dashboard: Go to Dashboards > Import
- Use dashboard ID: 1860 (or search for Node Exporter Full on Grafana.com)
- Set your Prometheus data source
- Click Import
