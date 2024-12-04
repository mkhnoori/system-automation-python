import subprocess


def configure_static_ip(ip_address, gateway, dns):
    network_config = f"""
    [Match]
    Name=eth0

    [Network]
    Address={ip_address}
    Gateway={gateway}
    DNS={dns}
    """
    try:
        # Write to a network configuration file
        with open("/etc/systemd/network/10-static-en.network", "w") as f:
            f.write(network_config)
        subprocess.run(["sudo", "systemctl", "restart", "systemd-networkd"], check=True)
        print("Static IP configuration applied.")
    except Exception as e:
        print(f"Failed to configure static IP: {e}")

# Example usage
configure_static_ip("192.168.1.100/24", "192.168.1.1", "8.8.8.8")
