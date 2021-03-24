import smtplib, ssl
from email.message import EmailMessage
import imghdr
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_PATH = os.path.join(BASE_DIR, 'meme.jpg')


msg = EmailMessage()
msg['to'] = os.getenv('EMAIL_RECEIVER')
msg['from'] = sender = os.getenv('EMAIL_SENDER')
msg['subject'] = 'Test sending attachments through python'
msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
msg.set_content('Please find the image attached below.')

with open(IMG_PATH, 'rb') as fp:
    img_data = fp.read()

msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    try:
        server.login(sender, os.getenv('EMAIL_PASS'))
        server.send_message(msg)

    except smtplib.SMTPResponseException as exc:
        print('Exception occured during sending of email:', exc)
