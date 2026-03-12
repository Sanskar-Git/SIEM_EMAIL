import requests
import time
import json

MAILHOG_API = "http://localhost:8025/api/v2/messages"

def fetch_logs():
    try:
        response = requests.get(MAILHOG_API)
        data = response.json()
        return data["items"]
    except Exception as e:
        print("Error collecting logs:", e)
        return []

def save_logs(logs):
    with open("email_logs.json", "w") as f:
        json.dump(logs, f, indent=4)

def run_collector():
    print("Log Collector Running...")

    while True:
        logs = fetch_logs()

        if logs:
            save_logs(logs)
            print(f"Collected {len(logs)} emails")

        time.sleep(5)

if __name__ == "__main__":
    run_collector()