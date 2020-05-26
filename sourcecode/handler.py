from db import *

class Handler():
    def __init__(self):
        self.db = Database("./vaultdb")
        self.charLimit = 64
        self.charMin = 4


    def modInput(self, var):
        if (len(str(var)) < self.charLimit) and (len(str(var)) >= self.charMin):
            return str(var)
        else:
            return False
    
    def getProvider(self, prov):
        if prov == "AT&T":
            return 1
        elif prov == "Sprint":
            return 2
        elif prov == "TMobile":
            return 3
        elif prov == "Verizon":
            return 4
        elif prov == "Boost":
            return 5
        elif prov == "Cricket":
            return 6
        elif prov == "MetroPCS":
            return 7
        elif prov == "Virgin Mobile":
            return 8
        else:
            return 0

    def closeDB(self):
        self.db.close()

    def signUp(self, username, password, email, phone, provider):
        # Check size of inputs and ensure they are strings

        cleanName, cleanPass, cleanEmail, cleanPhone= map(self.modInput, (username, password, email, phone))
        # Check the output of the modifications
        for n in enumerate([cleanName, cleanPass, cleanEmail, cleanPhone]):
            if n:
                pass
            else:
                return "One or more inputs excede the 64-characer limit"
        
        # If all is good, register user
        rtn = self.db.registeruser(cleanName, cleanPass, cleanEmail, cleanPhone, self.getProvider(provider))
        # If registration occurs correctly, return True,
        if(rtn):
            return True
        # else, return an error message
        else:
            return "Please Choose a different Account Name"

    def login(self, username, password):
        cleanName, cleanPass = map(self.modInput, (username, password))
        for n in enumerate([cleanName, cleanPass]):
            if n:
                pass
            else:
                return "Incorrect Username or Password"
        rtn = self.db.login(cleanName, cleanPass)
        if(rtn):
            return True
        else:
            return "Incorrect Username or Password"

    def store(self, tag, username, password):
        cleanName, cleanPass, cleanTag = map(self.modInput, (username, password, tag))
        for n in enumerate([cleanName, cleanPass, cleanTag]):
            if n:
                pass
            else:
                return "One or more inputs excede the 64-characer limit"

        rtn = self.db.insert(cleanTag, cleanName, cleanPass)
        if(rtn):
            return True
        else:
            return "Unexpected Error in Storing Record"

    def request(self, tag):
        cleanTag  = self.modInput(tag)
        if cleanTag:
            pass
        else:
            return "Incorrect Password Nickname"
        rtn = self.db.get(cleanTag)
        if(rtn[0]==None):
            return "No Record Found"
        else:
            return rtn
    
    def delete(self, tag):
        cleanTag  = self.modInput(tag)
        if cleanTag:
            pass
        else:
            return "Incorrect Password Nickname"
        rtn = self.db.delete(cleanTag)
        if(rtn):
            return True
        else:
            return "Unexpected Error in Deleting Record"

    def getEmail(self, user):
        cleanUser  = self.modInput(user)
        if cleanUser:
            pass
        else:
            return "Incorrect Password Username"
        rtn = self.db.fetchEmail(cleanUser)
        if rtn == "":
            return "Could Not Find Username"
        else:
            return rtn

    def resetPass(self, username, newPass):
        cleanName, cleanPass = map(self.modInput, (username, newPass))
        for n in enumerate([cleanName, cleanPass]):
            if n:
                pass
            else:
                return "Your Password Nickname is beyond the characer limit"
            if self.db.resetpassword(cleanName, cleanPass):
                return True
            else:
                return "Unexpected Error in Password Reset"
