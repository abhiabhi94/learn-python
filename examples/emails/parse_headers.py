import smtplib
import os
from email.parser import BytesParser
from email.policy import default


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS_PATH = os.path.join(BASE_DIR, 'email_headers.txt')

with open(HEADERS_PATH, 'rb') as fp:
    message = BytesParser(policy=default).parse(fp)

with smtplib.SMTP('localhost', 1025) as server:
    server.send_message(message)
