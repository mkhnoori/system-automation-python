# - Integrate multiple automation tasks into a single, modular tool using argument parsing.



import argparse
import os
import psutil
import subprocess

def list_files(directory):
    print(os.listdir(directory))

def check_system():
    print(f"CPU: {psutil.cpu_percent()}%")
    print(f"Memory: {psutil.virtual_memory().percent}%")

def update_system():
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linux System Automation Tool")
    parser.add_argument("--list-files", help="List files in a directory")
    parser.add_argument("--check-system", action="store_true", help="Check system health")
    parser.add_argument("--update-system", action="store_true", help="Update system packages")

    args = parser.parse_args()

    if args.list_files:
        list_files(args.list_files)
    if args.check_system:
        check_system()
    if args.update_system:
        update_system()
