import smtplib

SENDER_EMAIL = 'YOUR_EMAIL@EMAIL.COM'  # replace with your email address
SENDER_PASSWORD = 'YOUR_PASSWORD'  # replace with your email password

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)
