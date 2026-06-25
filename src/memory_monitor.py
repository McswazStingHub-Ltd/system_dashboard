import psutil

def show_memory_info():
    mem = psutil.virtual_memory()

    print("\n=== Memory Information ===")
    print(f"Total RAM: {round(mem.total/(1024**3),2)} GB")
    print(f"Used RAM : {round(mem.used/(1024**3),2)} GB")
    print(f"Usage    : {mem.percent}%")
