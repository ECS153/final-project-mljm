import smtplib
import secrets

class SMTPctrl():

    def __init__(self):
        self.account = "thevault.mljm@gmail.com"
        self.mpass = "%67w2^*sF#kdK1jY@WZAxIJihWMbBiCM6MNOX4by"
        self.resetCode = secrets.token_urlsafe(20)
    
    def sendMail(self, recip, user):
        msg = self.resetPass(user)
        with smtplib.SMTP('smtp.gmail.com:587') as server:
            server.starttls()
            server.login(self.account, self.mpass)
            server.sendmail(self.account, recip, msg)
            server.quit()

    def resetPass(self, user):
        message = (F"\nYour Vault app account, {user} has requested a password reset. \n" 
        "Please follow the instructions below to begin.\n" + \
        "Type the code below into the RESET window on the Vault app and enter a new password to reset\n"+ \
        F"Reset Code: {self.resetCode} \n\n"
        "If you believe this this notification is an error, "+ \
        F"please feel free to contact us at {self.account} and we will be sure to immediately delete your "+\
        "email withou ever reading it! \n\n Thank you for choosing The Vault.\n\n")
        return message

    def getResetCode(self):
        return self.resetCode
