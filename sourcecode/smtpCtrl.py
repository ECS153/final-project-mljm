import smtplib

class SMTPctrl():

    def __init__(self):
        self.account = "thevault.mljm@gmail.com"
        self.mpass = "%67w2^*sF#kdK1jY@WZAxIJihWMbBiCM6MNOX4by"
    
    def sendMail(self, recip, msg):
        with smtplib.SMTP('smtp.gmail.com:587') as server:
            server.starttls()
            server.login(self.account, self.mpass)
            server.sendmail(self.account, recip, msg)
            server.quit()

    def resetPass(self, user):
        message = (F"\nYour Vault app account, {user} has requested a password reset. \n" 
        "Please follow the instructions below to begin. If you believe this this notification is an error, " 
        F"please feel free to contact us at {self.account} and we will be sure to immediately delete your " 
        "email withou ever reading it! \n \n Thank you for choosing The Vault.")
        return message


mail = SMTPctrl()
user = 'bobRoberts'
addr = 'someEmail'
msg = mail.resetPass(user)

mail.sendMail(addr, msg)

