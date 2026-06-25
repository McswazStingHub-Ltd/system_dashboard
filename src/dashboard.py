from src.cpu_monitor import show_cpu_info
from src.memory_monitor import show_memory_info
from src.disk_monitor import show_disk_info

def main():
    print("\n=== SYSTEM DASHBOARD ===")

    show_cpu_info()
    show_memory_info()
    show_disk_info()

if __name__ == "__main__":
    main()
