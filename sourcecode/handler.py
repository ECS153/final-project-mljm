from db import *

class Handler():
    def __init__(self):
        self.db = Database("./vautlDB")
        self.charLimit = 64


    def modInput(self, var):
        if len(str(var)) < self.charLimit:
            return str(var)
        else:
            return False

    def signUp(self, username, password, secQ, secA):
        # Check size of inputs and ensure they are strings
        cleanName, cleanPass, cleanSecA = map(modInput, (username, password, secA))
        cleanSecQ  = self.modInput(secQ)

        # Check the output of the modifications
        badStr = ""
        for i,n in enumerate([cleanName, cleanPass, cleanSecQ, cleanSecA]):
            if n:
                pass
            else:
                badStr = badStr + str("\nYour "+vars[i]+" is beyond the characer limit")
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
            return "That Username Already Exists"

    def login(self, username, password):
        cleanName, cleanPass = map(self.modInput, (username, password))
        for i,n in enumerate([cleanName, cleanPass]):
            if n:
                pass
            else:
                return "Incorrect Username or Password"
        rtn = self.db.login(cleanName, cleanPass)
        if(rtn):
            return True
        else:
            return "Incorrect Username or Password"

    def store(self, username, password, tag):
        cleanName, cleanPass, cleanTag = map(self.modInput, (username, password, tag))
        badStr = ""
        for i,n in enumerate([cleanName, cleanPass, cleanTag]):
            if n:
                pass
            else:
                if(i == 2):
                    badStr = badStr + str("\nYour Password Nickname is beyond the characer limit")
                else:
                    badStr = badStr + str("\nYour "+vars[i]+" is beyond the characer limit")
        if(len(badStr) > 0):
            return badStr

        rtn = db.insert(cleanTag, cleanName, cleanPass)
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

    def getSecQ(self, username):
        cleanName = self.modInput(username)
        if cleanName:
            return self.db.fetchSQ(cleanName)
        else:
            return "Incorrect Username"
    
    def checkSecQ(self, username, seqA):
        # by this point, we know the username is correct
        cleanName, cleanSecA = map(self.modInput,(username, secA))
        if cleanSecA:
            pass
        else:
            return "Incorrect Security Question Answer"
        return self.db.checkSA(cleanName, cleanSecA)


    def resetPass(self, username, newPass):
        cleanName, cleanPass = map(self.modInput, (username, password))
        if n:
            pass
        else:
            return "Your Password Nickname is beyond the characer limit"
        if self.db.resetpassword(cleanPass):
            return "Your password has been reset"
        else:
            return "Unexpected Error in Password Reset"


    vars = {
        0 : "User Name",
        1 : "Password",
        2 : "Security Question",
        3 : "Security Question Answer",
    }

