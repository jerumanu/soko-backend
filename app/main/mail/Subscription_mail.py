import os
from flask_mail import Mail, Message


mail = Mail()




def send_email(email):
    msg      = Message()
    msg.body = ""
    mail.send(msg)