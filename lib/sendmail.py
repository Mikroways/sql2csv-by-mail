#!/usr/bin/env python3
import email, smtplib, os, sys, traceback
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = os.getenv('SMTP_PORT', 25)
host = os.getenv('SMTP_HOST')
username = os.getenv('SMTP_USERNAME')
password = os.getenv('SMTP_PASSWORD')
sender = os.getenv('MAIL_FROM')
receiver = os.getenv('MAIL_TO')
subject = os.getenv('MAIL_SUBJECT', 'Mail query')
body = os.getenv('MAIL_BODY', 'Results are attached, have a nice day!')

if not sender and not receiver:
    sys.exit('MAIL_FROM and MAIL_TO must be set')

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError as e:
        sys.exit('Must send a file to be attached')


try:
    server = smtplib.SMTP(host,port)
    server.login(username, password) if username else None

    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    message.attach(MIMEText(body, "plain"))

    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(filename)}"
    )

    message.attach(part)
    server.sendmail(sender, receiver, message.as_string())


except Exception as e:
    print(traceback.format_exc())
finally:
    server.quit()
