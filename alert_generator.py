
def generate_alerts(threats):

    for threat in threats:

        print("\n==============================")
        print("🚨 MALICIOUS EMAIL DETECTED")
        print("==============================")

        print("From:", threat["from"])
        print("To:", threat["to"])
        print("Subject:", threat["subject"])

        print("\nEmail Body:")
        print(threat["body"])

        print("\nAction: Investigate Immediately")