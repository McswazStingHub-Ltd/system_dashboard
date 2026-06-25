import shutil

def show_memory_info():
    total, used, free = shutil.disk_usage("/")

    print("\n=== Storage Information ===")
    print(f"Total: {total // (1024**3)} GB")
    print(f"Used : {used // (1024**3)} GB")
    print(f"Free : {free // (1024**3)} GB")
