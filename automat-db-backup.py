import subprocess

def backup_database(user, password, database, backup_file):
    try:
        command = f"mysqldump -u {user} -p{password} {database} > {backup_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"Database {database} backed up to {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error backing up database: {e}")

# Example usage
backup_database("root", "password", "mydb", "/backup/mydb_backup.sql")
