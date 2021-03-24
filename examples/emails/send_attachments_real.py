import smtplib, ssl
from email.message import EmailMessage
import imghdr
import os
import mimetypes



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE_DIR, 'meme.jpg')

sender = os.getenv('EMAIL_SENDER')

msg = EmailMessage()
msg['to'] = os.getenv('EMAIL_RECEIVER')
msg['from'] = sender
msg['subject'] = 'Test sending attachments through python'
msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
msg.set_content('Please find the image attached below.')


with open(PATH, 'rb') as fp:
    img_data = fp.read()

# Guess the content type based on the file's extension.  Encoding
# will be ignored, although we should check for simple things like
# gzip'd or compressed files.
ctype, encoding = mimetypes.guess_type(PATH)
if ctype is None or encoding is not None:
    # No guess could be made, or the file is encoded (compressed), so
    # use a generic bag-of-bits type.
    ctype = 'application/octet-stream'
maintype, subtype = ctype.split('/', 1)

msg.add_attachment(img_data, maintype=maintype, subtype=subtype)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    try:
        server.login(sender, os.getenv('EMAIL_PASS'))
        server.send_message(msg)

    except smtplib.SMTPResponseException as exc:
        print('Exception occured during sending of email:', exc)
