import subprocess

def format_and_mount_disk(disk, mount_point):
    """
    Formats a disk with ext4 and mounts it.

    :param disk: Disk device (e.g., '/dev/sdb').
    :param mount_point: Directory to mount the disk.
    """
    try:
        subprocess.run(["sudo", "mkfs.ext4", disk], check=True)
        subprocess.run(["sudo", "mkdir", "-p", mount_point], check=True)
        subprocess.run(["sudo", "mount", disk, mount_point], check=True)
        print(f"Disk {disk} formatted and mounted at {mount_point}.")
    except subprocess.CalledProcessError as e:
        print(f"Error during disk formatting or mounting: {e}")

# Example usage
format_and_mount_disk("/dev/sdb", "/mnt/newdisk")
