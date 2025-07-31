import smtplib
from email.mime.text import MIMEText#email.mime.text.MIMEText(_text[, _subtype[, _charset]])
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase#email.mime.base.MIMEBase(_maintype(e.g. text or image), _subtype(e.g. plain or gif), **_params(e.g.key/value dictionary))
from email import encoders
import os.path
import serial
import time

from time import sleep

arduino = serial.Serial("COM4", 9600)
arduino.timeout=3
time.sleep(3)

def sendmail1():
    
    email = 'divyasrisaritha2002@gmail.com'
    password = 'mwchilygfqivzokm'
    send_to_email = 'sowmyasri806@gmail.com'
    subject = 'SMART IRRIGATION ALERT'
    message = 'MOTOR ON. SOIL IS DRY'

    msg = MIMEMultipart()#Create the container (outer) email message.
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    '''as.string()  
     |
     +------------MIMEMultipart  
                  |                                                |---content-type  
                  |                                   +---header---+---content disposition  
                  +----.attach()-----+----MIMEBase----|  
                                     |                +---payload (to be encoded in Base64)
                                     +----MIMEText'''
    msg.attach(MIMEText(message, 'plain'))#attach new  message by using the Message.attach


    server = smtplib.SMTP('smtp.gmail.com', 587)# Send the message via local SMTP server.
    server.starttls()# sendmail function takes 3 arguments: sender's address, recipient's address and message to send 
    server.login(email, password)
    print("mail accessed")
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    print("Mail sent")

def sendmail2():
    email = 'divyasrisaritha2002@gmail.com'
    password = 'mwchilygfqivzokm'
    send_to_email = 'sowmyasri806@gmail.com'
    subject1 = 'SMART IRRIGATION ALERT'
    message1  = 'MOTOR ON. TEMPERATURE IS HIGH'

    msg = MIMEMultipart()#Create the container (outer) email message.
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject1
    '''as.string()  
     |
     +------------MIMEMultipart  
                  |                                                |---content-type  
                  |                                   +---header---+---content disposition  
                  +----.attach()-----+----MIMEBase----|  
                                     |                +---payload (to be encoded in Base64)
                                     +----MIMEText'''
    msg.attach(MIMEText(message1, 'plain'))#attach new  message by using the Message.attach


    server = smtplib.SMTP('smtp.gmail.com', 587)# Send the message via local SMTP server.
    server.starttls()# sendmail function takes 3 arguments: sender's address, recipient's address and message to send 
    server.login(email, password)
    print("mail accessed")
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    print("Mail sent")
    

while True:
    r=arduino.read()
    time.sleep(1)
    print("Data from Arduino")
    print(r)
    time.sleep(1)
    if r==b'A':
        sendmail1()
    elif r==b'B':
        sendmail2()
        
