# Imports SMTP Library
import smtplib

# Sender and Receiver
sender = 'sender@example.com'
receivers = ['receiver@example.com']

# Message
message = 'Welcome Guest!!'

try:
    smtpObj = smtplib.SMTP('localhost', 1025)

    smtpObj.sendmail(sender, receivers, message)

print("Email sent")

except smtplib.SMTPException:

print("Error sending email")

finally:

    smtpObj.quit()
