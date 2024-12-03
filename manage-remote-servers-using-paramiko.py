import paramiko

def run_remote_command(host, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, username=user, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        print("Output:", stdout.read().decode())
        print("Error:", stderr.read().decode())
    finally:
        client.close()

# Example usage
run_remote_command("192.168.1.100", "user", "password", "uptime")
