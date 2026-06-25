import os

def get_cpu_count():
    return os.cpu_count()

def show_cpu_info():
    print("\n=== CPU Information ===")
    print(f"CPU Cores: {get_cpu_count()}")
