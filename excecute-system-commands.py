import subprocess

def update_packages():
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        print("System packages updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating packages: {e}")

update_packages()
