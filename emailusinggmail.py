# Import SMTP Library
import smtplib
import ssl

# Import email modules
from email.message import EmailMessage

# SMTP Server
server = 'tls://smtp.gmail.com'
port = 587
user = 'yourname@gmail.com'
password = 'password'

# Sender and Receiver
sender = 'yourname@gmail.com'
receivers = ['receiver@gmail.com']

# Message
message = EmailMessage()

message['From'] = sender
message['To'] = receivers
message['MIME-Version'] = '1.0'
message['Content-type']: 'text/html'
message['Subject'] = 'Welcome'

message.set_content('Welcome Guest !!')

# Create SSL context
context = ssl.create_default_context()

# Send email
try:

   smtpObj = smtplib.SMTP(server, port)

   smtpObj.ehlo()
   smtpObj.starttls(context=context)
   smtpObj.ehlo()
   smtpObj.login(user, password)

   smtpObj.send_message(message)

print("Email sent")

except smtplib.SMTPException as exc:

print("Error sending email")
print(exc)

finally:
    smtpObj.quit()
