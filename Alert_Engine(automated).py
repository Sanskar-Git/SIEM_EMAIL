import time
import datetime


# ---------------------------------
# Alert Class
# ---------------------------------
class Alert:

    def __init__(self, alert_type, severity, description, sender):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.alert_type = alert_type
        self.severity = severity
        self.description = description
        self.sender = sender

    def display(self):

        print("\n--------------------------------")
        print("Timestamp :", self.timestamp)
        print("Alert Type:", self.alert_type)
        print("Severity  :", self.severity)
        print("Description:", self.description)
        print("Sender    :", self.sender)
        print("--------------------------------")

    def log_alert(self):

        with open("email_ids_log.txt", "a") as file:
            file.write(
                f"{self.timestamp} | {self.alert_type} | {self.severity} | {self.description} | {self.sender}\n"
            )


# ---------------------------------
# Detection Engine
# ---------------------------------
class DetectionEngine:

    spam_keywords = ["free", "lottery", "win money"]
    phishing_keywords = ["verify account", "update password"]
    malware_files = [".exe", ".bat", ".js"]
    suspicious_links = ["bit.ly", "tinyurl"]

    def analyze(self, sender, subject, content, link, attachment):

        # Normal Email
        alert = Alert("Normal Alert", "Low", "Email detected", sender)
        alert.display()
        alert.log_alert()

        # Spam
        for word in self.spam_keywords:
            if word in content.lower():
                alert = Alert("Spam Alert", "Medium", "Spam keyword detected", sender)
                alert.display()
                alert.log_alert()

        # Phishing
        for word in self.phishing_keywords:
            if word in content.lower():
                alert = Alert("Phishing Alert", "High", "Phishing attempt detected", sender)
                alert.display()
                alert.log_alert()

        # Malware attachment
        for ext in self.malware_files:
            if attachment.endswith(ext):
                alert = Alert("Malware Attachment Alert", "Critical", "Malicious attachment detected", sender)
                alert.display()
                alert.log_alert()

        # Suspicious link
        for badlink in self.suspicious_links:
            if badlink in link:
                alert = Alert("Suspicious Link Alert", "High", "Suspicious URL detected", sender)
                alert.display()
                alert.log_alert()


# ---------------------------------
# IDS Monitor
# ---------------------------------
class IDSMonitor:

    def __init__(self):

        self.engine = DetectionEngine()
        self.processed_lines = 0

    def monitor_log(self):

        print("Email IDS Monitoring Started...\n")

        while True:

            try:

                with open("incoming_email_log.txt", "r") as file:

                    lines = file.readlines()

                    new_logs = lines[self.processed_lines:]

                    for log in new_logs:

                        parts = log.strip().split("|")

                        if len(parts) == 5:

                            sender = parts[0]
                            subject = parts[1]
                            content = parts[2]
                            link = parts[3]
                            attachment = parts[4]

                            print("\nNew Email Log Detected\n")

                            self.engine.analyze(
                                sender,
                                subject,
                                content,
                                link,
                                attachment
                            )

                    self.processed_lines = len(lines)

            except FileNotFoundError:
                print("Waiting for incoming_email_log.txt ...")

            time.sleep(5)


# ---------------------------------
# Start IDS Monitoring
# ---------------------------------

monitor = IDSMonitor()
monitor.monitor_log()