import smtplib
from email.message import EmailMessage
import os


msg = EmailMessage()
msg['from'] = sender = os.getenv('EMAIL_SENDER')
msg['to'] = os.getenv('EMAIL_RECEIVER')
msg['subject'] = 'Testing text email through python'
msg.set_content('Hi! let us hope this works.')

with smtplib.SMTP_SSL('smtp.gmail.com') as server:
    server.login(sender, os.getenv('EMAIL_PASS'))
    server.send_message(msg)
