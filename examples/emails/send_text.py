import smtplib
from email.message import EmailMessage


msg = EmailMessage()
msg['to'] = 'receiver@domain'
msg['from'] = 'sender@domain'
msg['subject'] = 'Test sending text emails from python'
msg.set_content('Hi! just checking to see if this works')


with smtplib.SMTP('localhost', 1025) as server:
    server.send_message(msg)
