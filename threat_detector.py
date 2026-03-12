
import re

SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "password",
    "bank",
    "click"
]

SUSPICIOUS_DOMAINS = [
    "evil.com",
    "malicious-site.com"
]

def detect_threats(emails):

    threats = []

    for email in emails:

        score = 0

        subject = email["subject"].lower()
        body = email["body"].lower()
        sender = email["from"].lower()

        # keyword detection
        for word in SUSPICIOUS_KEYWORDS:
            if word in subject or word in body:
                score += 1

        # suspicious sender domain
        for domain in SUSPICIOUS_DOMAINS:
            if domain in sender:
                score += 2

        # detect urls
        urls = re.findall(r'(https?://\S+)', body)

        if urls:
            score += 1

        if score >= 3:
            threats.append(email)

    return threats