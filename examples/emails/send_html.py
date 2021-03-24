import smtplib
from email.message import EmailMessage
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, 'email.html')

msg = EmailMessage()
msg['To'] = 'receiver@domain'
msg['From'] = 'sender@domain'
msg['Subject'] = 'Testing large HTML email'
msg.set_content('This is the text portion')

with open(HTML_PATH) as fp:
    msg.add_alternative(fp.read(), subtype='html')


with smtplib.SMTP('localhost', 1025) as server:
    server.send_message(msg)
