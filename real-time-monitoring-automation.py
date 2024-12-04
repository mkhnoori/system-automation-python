import psutil
import smtplib
from email.mime.text import MIMEText

def send_alert(subject, message):
    sender = "admin@example.com"
    recipient = "alerts@example.com"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender, "password")
        server.sendmail(sender, recipient, msg.as_string())
        print("Alert email sent.")

def monitor_system():
    cpu_usage = psutil.cpu_percent(interval=5)
    if cpu_usage > 80:
        send_alert("High CPU Usage Alert", f"CPU usage is at {cpu_usage}%")

# Example usage
monitor_system()
