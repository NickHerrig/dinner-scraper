import os
import smtplib
import ssl


sender_email = "nickherrigdeveloper@gmail.com"
password = os.environ['DEV_EMAIL_PASS']
port = 465


def send_message(send_to, subject, message):
    """
    Send an text or email from nickherrigdeveloper@gmail.com.

    Keyword arguments:
    send_to -- the receiver, can be an email or phone number w/ carrier gateway address
    subject -- the subject line
    message -- the message body 

    Carrier gateway addresses:
    'AT&T: number@txt.att.net'
    'Verizon: number@vtext.com'
    'Sprint PCS: number@messaging.sprintpcs.com'
    'T-Mobile: number@tmomail.net'
    'Virgin Mobile: number@vmobl.com'

    """

    email = 'Subject: {}\n\n{}'.format(subject, message)
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, send_to, email)
