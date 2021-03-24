import smtplib
from email.message import EmailMessage
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEXT_PATH = os.path.join(BASE_DIR, 'email.txt')

msg = EmailMessage()
msg['To'] = 'receiver@domain'
msg['From'] = 'sender@domain'
msg['Subject'] = 'Testing largetext from python'

with open(TEXT_PATH) as fp:
    msg.set_content(fp.read())

with smtplib.SMTP('localhost', 1025) as server:
    server.send_message(msg)
