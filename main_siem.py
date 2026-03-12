
import time
from log_parser import parse_logs
from threat_detector import detect_threats
from alert_generator import generate_alerts

def run_siem():

    print("Email SIEM System Started...")

    while True:

        parsed_emails = parse_logs()

        threats = detect_threats(parsed_emails)

        if threats:
            generate_alerts(threats)

        time.sleep(5)

if __name__ == "__main__":
    run_siem()