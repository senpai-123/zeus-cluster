# Prometheus Setup Guide

This guide outlines the steps to install and set up **Prometheus** on a Linux system.

## What is Prometheus?

[Prometheus](https://prometheus.io/) is an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts when specified conditions are observed.

---

## Installation Steps

### 1. Download and Extract Prometheus

```bash
wget https://github.com/prometheus/prometheus/releases/download/v3.3.0-rc.1/prometheus-3.3.0-rc.1.linux-amd64.tar.gz
tar -xvzf prometheus-3.3.0-rc.1.linux-amd64.tar.gz
cd prometheus-3.3.0-rc.1.linux-amd64
```
For latest releases visit: [Releases](https://github.com/prometheus/prometheus/releases)

### 2. Create a Prometheus User
```bash
sudo useradd --no-create-home --shell /bin/false prometheus
```

### 3. Move Binaries to `/usr/local/bin`

```bash
sudo cp prometheus /usr/local/bin/
sudo cp promtool /usr/local/bin/
```
### 4. Set Ownership

```bash
sudo chown prometheus:prometheus /usr/local/bin/prometheus
```

### 5. Create Configuration and Data Directories

```bash
sudo mkdir -p /etc/prometheus
sudo mkdir -p /var/lib/prometheus
```

### 6. Copy Config Files and Consoles

```bash
sudo cp -r consoles/ console_libraries/ /etc/prometheus/
sudo cp prometheus.yml /etc/prometheus/
```

### Link to full: [prometheus.yml](https://github.com/senpai-123/zeus-cluster/blob/main/Prometheus-Grafana/prometheus.yml)

### 7. Set Proper Permissions

```bash
sudo chown -R prometheus:prometheus /etc/prometheus
sudo chown -R prometheus:prometheus /var/lib/prometheus
sudo chmod -R 755 /etc/prometheus
```

### 8. Create a systemd Service File

```bash
sudo vim /etc/systemd/system/prometheus.service
```
### Link to: [prometheus.service](https://github.com/senpai-123/zeus-cluster/blob/main/Prometheus-Grafana/prometheus.service)

### 9. Start and Enable Prometheus

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus
sudo systemctl status prometheus
```

### 10. Access Prometheus

**Once Prometheus is running, you can access the web interface at: `http://<your-server-ip>:9090`**

