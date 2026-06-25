import psutil

def show_disk_info():
    disk = psutil.disk_usage('/')

    print("\n=== Storage Information ===")
    print(f"Total: {round(disk.total/(1024**3))} GB")
    print(f"Used : {round(disk.used/(1024**3))} GB")
    print(f"Free : {round(disk.free/(1024**3))} GB")
