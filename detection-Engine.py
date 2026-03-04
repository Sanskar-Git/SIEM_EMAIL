from collections import defaultdict
import time 

email_counter = defaultdict(list)

def detect(parsed_data):
    alerts = []

    sender = parsed_data.get("from")

    if not sender: 
        return alerts
    
    current_time = time.time()
    email_counter[sender].append(current_time)
 
    # removing timestamps older than 10 seconds
    email_counter[sender] = [
        t for t in email_counter[sender]
        if current_time - t < 10
    ]

    # Spam Detection Rule
    if len(email_counter[sender]) > 5:
        alerts.append(f"Spam detected from {sender}")
    
    return alerts

if __name__ == "__main__":
    test_data = {"from": "attacker@test.com"}

    for i in range(7):
        alerts = detect(test_data)
        print(f"Attempt {i+1}: ", alerts)
        time.sleep(1)