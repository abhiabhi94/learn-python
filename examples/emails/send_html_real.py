import smtplib
from email.message import EmailMessage
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, 'email.html')


msg = EmailMessage()
msg['To'] = os.getenv('EMAIL_RECEIVER')
msg['From'] = sender = os.getenv('EMAIL_SENDER')
msg['Subject'] = 'Testing large HTML email'

with open(HTML_PATH) as fp:
    msg.add_alternative(fp.read(), subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender, os.getenv('EMAIL_PASS'))
    server.send_message(msg)
