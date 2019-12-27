# Import SMTP Library
import smtplib

# Import email modules
from email.message import EmailMessage

# Sender and Receiver
sender = 'sender@example.com'
receivers = ['receiver@example.com']

# Message
message = EmailMessage()

message['Subject'] = 'Welcome'
message['From'] = sender
message['To'] = receivers

message.set_content('Welcome Guest !!')

# Send email
try:

smtpObj = smtplib.SMTP('localhost', 1025)

smtpObj.send_message(message)

print("Email sent")

except smtplib.SMTPException:

print("Error sending email")

finally:

    smtpObj.quit()
