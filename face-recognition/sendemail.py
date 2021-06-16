"""
Allow less secure apps in the following link 

https://www.google.com/settings/security/lesssecureapps

then run this python program
"""
from private import uname, passwd 

class Sendemail:
    def __init__(self):
        send_email()

def send_email(sendto, subject, text):
    username =  uname # Change this!
    password =  passwd # Change this!
    for i in range(3):
        try:
            print("Sending Email to {} (trial {})...".format(sendto, i+1))
            import smtplib
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            msg = 'Subject: {}\n\n{}'.format(subject, text)
            server.sendmail(username, sendto, msg)
            server.quit()
            print("Email sent!")
            break
        except Exception as e:
            print("Failed to send email due to Exception:")
            print(e)