import smtplib
from email.mime.text import MIMEText

smtp_server = "localhost"
smtp_port = 1025

msg = MIMEText("This is a test email with suspicious link http://malicious-site.com")
msg["Subject"] = "Urgent: Click this now"
msg["From"] = "attacker@evil.com"
msg["To"] = "victim@company.com"

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.send_message(msg)

print("Email sent successfully!")