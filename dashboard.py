from flask import Flask, render_template_string
import requests
from threat_detector import detect_threats

app = Flask(__name__)

MAILHOG_API = "http://localhost:8025/api/v2/messages"

HTML_TEMPLATE = """
<html>

<head>
<title>Email SIEM Dashboard</title>

<script>
function showAlert(){
    alert("⚠ WARNING: Suspicious Email Detected!");
}
</script>

</head>

<body>

<h1>Email SIEM Monitoring Dashboard</h1>

{% for email in emails %}

<div style="border:1px solid black; padding:10px; margin:10px;">

<b>From:</b> {{email.from}} <br>
<b>Subject:</b> {{email.subject}} <br>

{% if email.threat %}
<button onclick="showAlert()">Open Email ⚠</button>
</a>
{% else %}
<a href="http://localhost:8025/#/{{email.id}}" target="_blank">
<button>Open Email</button>
</a>
{% endif %}

<p>{{email.body}}</p>


</div>

{% endfor %}

</body>
</html>
"""

@app.route("/")
def dashboard():

    response = requests.get(MAILHOG_API)
    data = response.json()["items"]

    emails = []

    for email in data:

        headers = email["Content"]["Headers"]

        parsed = {
            "id": email["ID"],
            "from": headers.get("From", [""])[0],
            "subject": headers.get("Subject", [""])[0],
            "body": email["Content"]["Body"]
        }

        threat = detect_threats([parsed])

        parsed["threat"] = True if threat else False

        emails.append(parsed)

    return render_template_string(HTML_TEMPLATE, emails=emails)

app.run(port=5001)