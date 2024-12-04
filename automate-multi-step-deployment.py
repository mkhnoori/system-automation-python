import subprocess

def deploy_django():
    try:
        subprocess.run(["git", "pull", "origin", "main"], check=True)
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        subprocess.run(["python3", "manage.py", "migrate"], check=True)
        subprocess.run(["sudo", "systemctl", "restart", "gunicorn"], check=True)
        print("Django application deployed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Deployment failed: {e}")

deploy_django()
