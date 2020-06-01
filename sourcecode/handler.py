from db import *

class Handler():
    def __init__(self):
        self.db = Database("./vaultdb")
        self.charLimit = 64
        self.charMin = 4
        self.phoneLimit = 10


    def modInput(self, var):
        if (len(str(var)) <= self.charLimit) and (len(str(var)) >= self.charMin):
            return str(var)
        else:
            return False
            
    def modPhone(self, var):
        try:
            int(var)
        except:
            return False
        if (len(var) == self.phoneLimit):
            return str(var)
        else:
            return False
    
    def modEmail(self, var):
        if ((len(str(var)) <= self.charLimit) and (str(var).find('@') != -1) and (str(var).find('.') != -1)):
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
        cleanName, cleanPass = map(self.modInput, (username, password))
        cleanEmail = self.modEmail(email)
        cleanPhone = self.modPhone(phone)
        # Check the output of the modifications
        for k,val in enumerate([cleanName, cleanPass, cleanEmail, cleanPhone]):
            if val:
                pass
            else:
                if k==0 or k==1:
                    return "Username and Password must be between 4 and 64 characters"
                elif k == 2:
                    return "Please enter a valid email"
                else:
                    return "Please enter a valid Phone Number"
        
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
                return "One or more inputs do not meet the 4-64 character range"

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
        if rtn == None:
            return "Could Not Find Username"
        else:
            return rtn
    
    def getPhone(self, user):
        cleanUser  = self.modInput(user)
        if cleanUser:
            pass
        else:
            return "Incorrect Password Username"
        rtn = self.db.fetchPhone(cleanUser)
        if rtn[0] == None:
            return "Could Not Find Username"
        else:
            return rtn

    def resetPass(self, username, newPass):
        cleanName, cleanPass = map(self.modInput, (username, newPass))
        for n in enumerate([cleanName, cleanPass]):
            if n:
                pass
            else:
                return "Your Password must be between 4 and 64 characters"
            if self.db.resetpassword(cleanName, cleanPass):
                return True
            else:
                return "Unexpected Error in Password Reset"
    
    def resetEmail(self, email):
        cleanEmail = self.modEmail(email)
        if cleanEmail:
            pass
        else:
            return "Please enter a valid email"
        if self.db.resetEmail(cleanEmail):
            return True
        else:
            return "Unexpected Error in Email Reset"
    
    def resetPhone(self, phone, prov):
        cleanPhone = self.modEmail(phone)
        if cleanPhone:
            pass
        else:
            return "Please enter valid Phone information"
        if self.db.resetPhone(cleanPhone, self.getProvider(prov)):
            return True
        else:
            return "Unexpected Error in Phone Number Reset"
