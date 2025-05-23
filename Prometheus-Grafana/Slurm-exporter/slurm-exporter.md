# Slurm Exporter for Prometheus & Grafana

The **Slurm Exporter** exposes metrics from a Slurm workload manager in a Prometheus-compatible format. These metrics can be visualized in **Grafana** to monitor Slurm jobs, nodes, utilization, and more.
Refer to the link for [Slurm Exporter Github](https://github.com/vpenso/prometheus-slurm-exporter)

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/vpenso/prometheus-slurm-exporter.git
cd prometheus-slurm-exporter
```

### 2. Install Go (if not already installed)
```bash
sudo dnf install golang -y
# OR install manually:
curl -LO https://go.dev/dl/go1.22.2.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.22.2.linux-amd64.tar.gz
```

### 3. Set up Go Environment
```bash
export PATH=$PATH:/usr/local/go/bin
export GOPATH=$HOME/go
source ~/.bashrc
```

### 4. Build the Exporter
```bash
go version
go build
```

### 5. Run the Exporter
```bash
nohup ./prometheus-slurm-exporter -listen-address=":9817" &
```

### 6. Verify the Exporter is Running
```bash
sudo lsof -i :9817
netstat -tcnlp | grep 9817
```
### 7. Connect SLURM Exporter to Prometheus

Edit your Prometheus config `/etc/prometheus/prometheus.yml`. 
#### Refer to [prometheus.yml](https://github.com/senpai-123/zeus-cluster/blob/main/Prometheus-Grafana/prometheus.yml)
Then restart prometheus.


### 8. Visualizing in Grafana

- Connect Prometheus as a Data Source in Grafana: Go to Grafana > Settings > Data Sources > Add data source
- Choose Prometheus-> URL: `http://localhost:9090` (or your Prometheus server IP)
- Click Save & Test
- Import a default Slurm dashboard from [Grafana Labs](https://grafana.com/grafana/dashboards/4323-slurm-dashboard/) or use your own
- **Edit or create panels using PromQL queries : [Edited Dashboard](https://github.com/senpai-123/zeus-cluster/blob/main/Prometheus-Grafana/Slurm-exporter/SLURM-graf-dashboard.md)**
