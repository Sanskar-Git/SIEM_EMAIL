import smtplib
from email.mime.text import MIMEText

smtp_server = "localhost"
smtp_port = 1025


# -----------------------------
# SAFE EMAIL
# -----------------------------

safe_body = """
Hello Team,

This is a reminder that we have a meeting tomorrow at 10 AM.

Regards,
HR Department
"""

safe_msg = MIMEText(safe_body)

safe_msg["Subject"] = "Meeting Reminder"
safe_msg["From"] = "hr@company.com"
safe_msg["To"] = "employee@company.com"



# -----------------------------
# SUSPICIOUS EMAIL
# -----------------------------

phishing_body = """
URGENT: Your bank account will be suspended!

Click below to verify immediately:

http://localhost:5000/track?id=001

Or visit:
http://malicious-site.com/login
"""

phishing_msg = MIMEText(phishing_body)

phishing_msg["Subject"] = "Verify Your Bank Account Immediately"
phishing_msg["From"] = "attacker@evil.com"
phishing_msg["To"] = "victim@company.com"



# -----------------------------
# SEND EMAILS
# -----------------------------

server = smtplib.SMTP(smtp_server, smtp_port)

server.send_message(safe_msg)
print("Safe email sent")

server.send_message(phishing_msg)
print("Phishing email sent")

server.quit()