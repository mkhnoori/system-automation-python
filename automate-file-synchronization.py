import paramiko

def sync_files(remote_host, username, password, local_file, remote_path):
    transport = paramiko.Transport((remote_host, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        sftp.put(local_file, remote_path)
        print(f"File {local_file} uploaded to {remote_host}:{remote_path}")
    except Exception as e:
        print(f"Failed to upload file: {e}")
    finally:
        sftp.close()
        transport.close()

# Example usage
sync_files("192.168.1.100", "user", "password", "/path/to/local/file.txt", "/remote/path/file.txt")
