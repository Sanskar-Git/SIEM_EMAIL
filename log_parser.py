import json

def parse_logs():

    with open("email_logs.json", "r") as f:
        logs = json.load(f)

    parsed_emails = []

    for email in logs:

        headers = email["Content"]["Headers"]

        parsed_email = {
            "from": headers.get("From", [""])[0],
            "to": headers.get("To", [""])[0],
            "subject": headers.get("Subject", [""])[0],
            "body": email["Content"]["Body"]
        }

        parsed_emails.append(parsed_email)

    return parsed_emails
