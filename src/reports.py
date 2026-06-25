from datetime import datetime
import os
import psutil


def generate_report():
    report = f"""
SYSTEM DASHBOARD REPORT
Generated: {datetime.now()}

CPU Cores: {os.cpu_count()}

RAM Total: {round(psutil.virtual_memory().total / (1024**3), 2)} GB
RAM Usage: {psutil.virtual_memory().percent} %

Disk Total: {round(psutil.disk_usage('/').total / (1024**3), 2)} GB
Disk Used : {round(psutil.disk_usage('/').used / (1024**3), 2)} GB
Disk Free : {round(psutil.disk_usage('/').free / (1024**3), 2)} GB
"""

    with open("system_report.txt", "w") as f:
        f.write(report)

    print("Report exported to system_report.txt")
