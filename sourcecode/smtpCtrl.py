import smtplib
import secrets

class SMTPctrl():
    
    def __init__(self):
        self.account = "thevault.mljm@gmail.com"
        self.mpass = "mwshaewpwtaoapco"
    
    def sendMail(self, recip, user):
        resetCode = secrets.token_urlsafe(15)
        with smtplib.SMTP('smtp.gmail.com:587') as controller:
            controller.starttls()
            controller.login(self.account, self.mpass)
            controller.sendmail(self.account, recip, self.resetEmailMsg(user, resetCode))
            controller.quit()
        return resetCode

    def sendSMS(self, recip, user, carr):
        resetCode = secrets.token_urlsafe(15)
        sendAddr = str(recip) + self.getCarrier(carr)
        with smtplib.SMTP('smtp.gmail.com:587') as controller:
            controller.starttls()
            controller.login(self.account, self.mpass)
            controller.sendmail(self.account,sendAddr,self.resetSMSMsg(user, resetCode))
            controller.quit()
        return resetCode

    def resetEmailMsg(self, user, code):
        message = (F"\nFrom The Vault App\n\n Your Vault app account, {user}, has requested a password reset. \n"+ \
        "Please follow the instructions below to begin.\n" + \
        "Type the code below into the RESET window on the Vault app and enter a new password to reset\n"+ \
        F"Reset Code: {code} \n\n" + \
        "If you believe this this notification is an error, "+ \
        F"please feel free to contact us at {self.account} and we will be sure to immediately delete your "+ \
        "email withou ever reading it! \n\n Thank you for choosing The Vault.\n\n")
        return message

    def resetSMSMsg(self, user, code):
        message = "\nFrom The Vault App.\nYour account, " + user + \
            ", has requested a password reset. To continue, please use the following"+\
            "code in the app:\n "+ code
        return message

    def getResetCode(self):
        return self.resetCode

    def getCarrier(self,carr):
        carriers = {
            1 : '@txt.att.net', #At&t
            2 : '@pm.sprint.com', #Sprint
            3 : '@tmomail.net', #TMobile
            4 : '@vtext.com', #Verizon
            5 : '@myboostmobile.com', #Boost
            6 : '@sms.mycricket.com', #Cricket
            7 : '@mymetropcs.com', #MetroPCS
            8 : '@vmobl.com' #Virgin Mobile
        }
        return carriers[carr]
