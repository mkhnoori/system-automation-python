import socket

def check_open_ports(host, ports):
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open on {host}")
            else:
                print(f"Port {port} is closed on {host}")

# Example usage
check_open_ports("127.0.0.1", [22, 80, 443])
