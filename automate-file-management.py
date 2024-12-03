import shutil
import os

def backup_file(source, destination):
    if os.path.exists(source):
        shutil.copy(source, destination)
        print(f"File {source} backed up to {destination}")
    else:
        print(f"Source file {source} does not exist.")

# Example usage
backup_file("/etc/hosts", "/backup/hosts_backup")
