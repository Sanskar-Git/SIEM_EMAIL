from flask import Flask, request

app = Flask(__name__)

@app.route("/track")
def track_click():

    email_id = request.args.get("id")

    print("\n================================")
    print("🚨 ALERT: PHISHING LINK CLICKED")
    print("================================")

    print("Email ID:", email_id)
    print("User IP:", request.remote_addr)

    return "Security Alert Logged"

app.run(port=5000)