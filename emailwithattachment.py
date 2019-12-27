# Import SMTP Library
import smtplib
import ssl
import base64

# Import email modules
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP Server
server = 'tls://smtp.gmail.com'
port = 587
user = 'yourname@gmail.com'
password = 'password'

# Sender and Receiver
sender = 'yourname@gmail.com'
receivers = ['receiver@gmail.com']

# Attachment
filename = 'hello.txt'

# Read and encode into base64 format
with open(filename, 'rb') as attachment:
   encodedPart = MIMEBase('application', 'octet-stream')
   encodedPart.set_payload(attachment.read())

encoders.encode_base64(encodedPart)

encodedPart.add_header(
"Content-Disposition",
    f"attachment; filename= {filename}",
)

# Message
message = MIMEMultipart()

message['From'] = sender
message['To'] = receiver
message['MIME-Version'] = '1.0'
message['Content-type']: 'text/html'
message['Subject'] = 'Welcome'

message.attach(MIMEText('Welcome Guest !!', "plain"))
message.attach(encodedPart)

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
