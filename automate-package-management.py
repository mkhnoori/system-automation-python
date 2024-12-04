import subprocess

def install_security_updates():
    """
    Installs only security updates on a Linux system.
    """
    try:
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "upgrade", "-y", "--with-new-pkgs"], check=True)
        print("Security updates installed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install updates: {e}")

install_security_updates()
