import psutil

def check_system_health():
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Memory usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

    # Disk usage
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}%")

check_system_health()
