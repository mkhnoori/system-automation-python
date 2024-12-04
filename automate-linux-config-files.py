import os
import shutil

# Backup Linux Config Files
def backup_configs(configs, backup_dir):
    os.makedirs(backup_dir, exist_ok=True)
    for config in configs:
        if os.path.exists(config):
            dest = os.path.join(backup_dir, os.path.basename(config))
            shutil.copy(config, dest)
            print(f"Backed up {config} to {dest}")
        else:
            print(f"Config {config} does not exist.")

# Example usage
backup_configs(["/etc/hosts", "/etc/fstab"], "/backup/configs")

# Restore Files from Backup
def restore_configs(backup_dir, destination_dir):
    for file in os.listdir(backup_dir):
        src = os.path.join(backup_dir, file)
        dest = os.path.join(destination_dir, file)
        shutil.copy(src, dest)
        print(f"Restored {src} to {dest}")

# Example usage
restore_configs("/backup/configs", "/etc")

