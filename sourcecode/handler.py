from db import *

class Handler():
    def __init__(self):
        self.db = Database()
        self.charLimit = 64
        self.QcharLimit = 128

    def modInput(self, n, var):
        if len(str(var)) < n:
            return str(var)
        else:
            return False

    def signUp(self, username, password, secQ, secA):
        # Check size of inputs and ensure they are strings
        cleanName, cleanPass, cleanSecA = map(modInput, self.charLimit, (username, password, secA))
        cleanSecQ  = modInput(self.QcharLimit, secQ)

        # Check the output of the modifications
        badStr = ""
        for i,n in enumerate([cleanName, cleanPass, cleanSecQ, cleanSecA]):
            if n:
                pass
            else:
                badStr = badStr + str("Your "+vars[i]+" is beyond the characer limit\n")
        # If an input is beyond the character limit, return an error message
        if(len(badStr) > 0):
            return badStr
        
        # If all is good, register user
        rtn = self.db.registeruser(
            cleanName, cleanPass, cleanSecQ, cleanSecA)
        # If registration occurs correctly, return True,
        # else, return an error message
        if(rtn):
            return True
        else:
            return "That Username Already Exists\n"

    def login(self, username, password):
        cleanName, cleanPass = map(modInput, self.charLimit, (username, password))
        for i,n in enumerate([cleanName, cleanPass]):
            if n:
                pass
            else:
                return "Incorrect Username or Password\n"
        rtn = self.db.login(cleanName, cleanPass)
        if(rtn):
            return True
        else:
            return "Incorrect Username or Password\n"

    def store(self, username, password, tag):
        cleanName, cleanPass, cleanTag = map(modInput, self.charLimit, (username, password, tag))
        badStr = ""
        for i,n in enumerate([cleanName, cleanPass, cleanTag]):
            if n:
                pass
            else:
                if(i == 2):
                    badStr = badStr + str("Your Password Nickname is beyond the characer limit\n")
                else:
                    badStr = badStr + str("Your "+vars[i]+" is beyond the characer limit\n")
        if(len(badStr) > 0):
            return badStr

        rtn = db.insert(cleanTag, cleanName, cleanPass)
        if(rtn):
            return True
        else:
            return "Unexpected Error in Storing Record\n"

    def request(self, tag):
        cleanTag  = modInput(self.QcharLimit, tag)
        if cleanTag:
            pass
        else:
            return "Incorrect Password Nickname\n"
        rtn = self.db.get(cleanTag)
        if(rtn[0]==None):
            return "No Record Found\n"
        else:
            return rtn
    
    def delete(self, tag):
        cleanTag  = modInput(self.QcharLimit, tag)
        if cleanTag:
            pass
        else:
            return "Incorrect Password Nickname\n"
        rtn = self.db.delete(cleanTag)
        if(rtn):
            return True
        else:
            return "Unexpected Error in Deleting Record\n"

    def getSecQ(self, username):
        cleanName = modInput(self.charLimit, username)
        if cleanName:
            return self.db.fetchSQ(cleanName)
        else:
            return "Incorrect Username\n"
    
    def checkSecQ(self, username, seqA):
        # by this point, we know the username is correct
        cleanName, cleanSecA = map(modInput, self.charLimit, (username, secA))
        if cleanSecA:
            pass
        else:
            return "Incorrect Security Question Answer\n"
        return self.db.checkSA(cleanName, cleanSecA)


    def resetPass(self, username, newPass):
        cleanName, cleanPass = map(modInput, self.charLimit, (username, password))
        if n:
            pass
        else:
            return "Your Password Nickname is beyond the characer limit\n"
        # self.db.resetpassword()
        pass

    vars = {
        0 : "User Name",
        1 : "Password",
        2 : "Security Question",
        3 : "Security Question Answer",
    }

