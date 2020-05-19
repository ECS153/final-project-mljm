import json
from sourcecode.db import *

class Handler():
    def __init__(self):
        self.db = Database()

    def signUp(self, username, password, secQ, secA):
        cleanName = str(username)
        cleanPass = str(password)
        cleanSecQ = str(secQ)
        cleanSecA = str(secA)
        rtn = self.db.registeruser(
            cleanName, cleanPass,cleanSecQ,cleanSecA)
        if(rtn):
            return True
        else:
            return "Username Already Exists"

    def login(self, username, password):
        cleanName = str(username)
        cleanPass = str(password)
        rtn = self.db.login(cleanName, cleanPass)
        if(rtn == 0):
            return True
        else:
            if(rtn == 1):
                return "User Does Not Exist"
            else:
                return "Incorrect Password"

    def store(self, tag, username, password):
        cleanTag = str(tag)
        cleanName = str(username)
        cleanPass = str(password)
        rtn = db.insert(cleanTag, cleanName, cleanPass)
        if(rtn):
            return True
        else:
            return "Unexpected Error"

    def request(self, tag):
        cleanTag = str(tag)
        rtn = self.db.get(cleanTag)
        if(rtn[0]==None):
            return "No Record Found"
        else:
            return rtn
    
    def delete(self, tag):
        cleanTag = str(tag)
        rtn = self.db.delete(cleanTag)
        if(rtn):
            return True
        else:
            return "Unexpected Error"

    def seqCheck(self, username, secA):
        cleanName = str(username)
        cleanSecA = str(secA)
        # TODO
        pass

    def resetPass(self, username, oldPass, newPass):
        cleanName = str(username)
        cleanOldPass = str(oldPass)
        cleanNewPass = str(newPass)
        # TODO
        pass


## NOTES
# for login, it needs to return either 0=success, 1=not a user, 2=incorrect pass
# for resetPass, user should input oldpass again so db can check it to make sure
    # incase a user leaves his window open
# window should close after 5 min of non-use