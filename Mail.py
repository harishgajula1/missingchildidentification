import os,sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def mailsend(toaddr,msgbody):

    fromadrs="aliincloudtechnologies@gmail.com"
    password = "iamali21."

    msg = MIMEMultipart()
    msg['From'] = fromadrs
    msg['To'] = toaddr
    msg['Subject'] = "Missing Child Alert"
    body = msgbody
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.login(fromadrs, password)
    text = msg.as_string()
    server.sendmail(fromadrs, toaddr, text)
    server.quit()
    print("sent email")

#mailsend("alinowinhyd@gmail.com","hai")