import csv
from datetime import datetime

# Map of labels to their respective indices in the JOB_FINISH line
FIELD_MAP = {
    "Event Type": 0,
    "Event Time": 2,
    "Job ID": 3,
    "Num Processors": 6,
    "Submit Time": 7,
    "User Name": 11,
    "Queue": 12,
    "Submission Host": 16,
    "CWD": 17,
    "Input File": 18,
    "Output File": 19,
    "Error File": 20,
    "Exec Hosts": 24,
    "Job Status": 28,
    "Job Name": 30,
    "Command": 31,
    "Project Name": 42,
    "Exit Status": 43,
    "Max Num Processors": 44,
    "Run Limit": 86,
    "Run Time": 112,
    "Effective Resource Request": 113,
    "Output Directory": 119,
    "Scheduling Overhead": 129,
}

def epoch_to_date(epoch):
    try:
        return datetime.utcfromtimestamp(int(epoch)).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return ""

def parse_job_finish_line(line):
    parts = [p.strip('"') for p in line.strip().split(" ")]
    row = {}
    for label, idx in FIELD_MAP.items():
        val = parts[idx] if idx < len(parts) else ""
        if label in ["Event Time", "Submit Time"]:
            val = epoch_to_date(val)
        row[label] = val
    return row

def convert_lsb_acct_to_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=FIELD_MAP.keys())
        writer.writeheader()
        for line in infile:
            if line.startswith('"JOB_FINISH"'):
                row = parse_job_finish_line(line)
                writer.writerow(row)

# Your file paths
input_file = '/home/lsf_home/work/zeus/logdir/lsb.acct'     
output_file = '/home/lsf_home/work/zeus/logdir/cleaned_lsb_acct.csv'

# Run the conversion
convert_lsb_acct_to_csv(input_file, output_file)
