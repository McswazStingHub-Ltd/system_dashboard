import os

def show_cpu_info():
    print("\n=== CPU Information ===")
    print(f"CPU Cores: {os.cpu_count()}")
