# Grafana Setup Guide

This guide provides steps to install and configure **Grafana** on a Linux system using the RPM package.

---
## What is Grafana?

[Grafana](https://grafana.com/) is an open-source analytics and visualization platform. It allows you to query, visualize, alert on, and explore your metrics no matter where they are stored. Grafana is commonly used with data sources like **Prometheus**, **InfluxDB**, and **Graphite**.

---

## Installation Steps

### 1. Download Grafana Enterprise

```bash
wget https://dl.grafana.com/enterprise/release/grafana-enterprise-11.6.0-1.x86_64.rpm
```
Link to latest [Releases](https://grafana.com/grafana/download)

### 2. Install Grafana

```bash
sudo dnf install -y grafana-enterprise-11.6.0-1.x86_64.rpm
```

### 3. Start and Enable Grafana Service

```bash
sudo systemctl daemon-reexec
sudo systemctl start grafana-server
sudo systemctl enable --now grafana-server
sudo systemctl status grafana-server
```
### 4. Access Grafana

**Once Grafana is running, open your browser and navigate to: `http://<your-server-ip>:3000`**

