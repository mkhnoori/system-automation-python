import paramiko

def deploy_ssh_key(server_ip, username, password, public_key):
    """
    Deploys an SSH public key to a remote server.

    :param server_ip: Server IP address.
    :param username: SSH username.
    :param password: SSH password.
    :param public_key: Path to the public key file.
    """
    try:
        key = open(public_key).read()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, username=username, password=password)

        command = f'echo "{key}" >> ~/.ssh/authorized_keys'
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        ssh.close()
        print(f"SSH key deployed to {server_ip}.")
    except Exception as e:
        print(f"Failed to deploy SSH key: {e}")

# Example usage
deploy_ssh_key("192.168.1.100", "root", "password", "/path/to/id_rsa.pub")
