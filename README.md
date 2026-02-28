This Repo is all about SIEM for email 

the program will fetch email logs, segregate them and based on the rules and the logic provided it will generate an alert 

This repo has 5 modules 
1. log_collector.py
2. parser.py
3. detection_engine.py
4. alert_engine.py
5. main.py
   
The Log collector module will read the logs in real time.

The parser module will segregate the important feilds from log file.

The Detection Engine will consist of logic and rules based on which the alert will be generated 

The alert Engine will alert the user if the rules define is violated

Future scope - comnecting a dashboard for seamless user experience 

![SIEM_Flowchart](https://github.com/user-attachments/assets/ecef6b33-f914-4fe9-81e0-7d9f3b07d189)
