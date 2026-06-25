import psutil

def show_cpu_info():
    print("\n=== CPU Information ===")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU Cores: {psutil.cpu_count()}")
