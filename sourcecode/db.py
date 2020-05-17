import json
import os
from crypt import *

#functions that may be useful to manipulate string before storing
def addchar(string, mode):
    result = ""
    length = len(string)
    char_code = 97
    for i in range(length):
        #for every fixed number of character add a character
        #I can't make the character random right now because I can't easily get the same key again
        if i % mode == 0:
            result += chr(char_code)
            char_code += 1
            if char_code > 122:
                char_code = 64
        result += string[i]
    return result

def removechar(string, mode):
    result = ""
    length = len(string)
    count = 0
    for i in range(1,length):
        if count != mode:
            result += string[i]
            count += 1
        else:
            count = 0
    return result

def adduserprefix(user, nickname):
    #make sure uniqueness of nickname for each user
    #allowing different user to have same nickname for their own password
    result = ""
    result += user + "_" + nickname
    return result

def removeprefix(user, nickname):
    result = ""
    prefix = "" + user + "_" 
    if not nickname.startwith(prefix):
        print("error: this nickname doesn't belong to this user")
        return None
    length = len(prefix)
    result = nickname[length:]
    return result

#store and retrive functionality using simple json
class Database():
    def __init__(self, disk):
        #disk is the path of the file we store the data in
        self.disk = os.path.expanduser(disk)
        self.mycry = MyCrypt()
        self.load(self.disk)
        pass
    
    def open(self, user, phrase):
        #open database 
        #user is string of the username for the user who is using the app
        #phrase is string of the master password
        self.load(self.disk)
        self.user = user
        self.phrase = phrase
        #calculate encryption/decryption key based on user and phrase here
        self.key = calculatekey(self.user, self.phrase)
        return True

    def calculatekey(self, user, phrase):
        #calculate encryption/decryption key based on user and phrase
        pass

    def load(self, disk):
        if os.path.exists(disk):
            self.db = json.load(open(self.disk, "r"))
        else:
            self.db = {}
        return True
    
    def close(self):
        #write back to disk
        try:
            json.dump(self.db, open(self.disk, "w+"))
            return True
        except:
            return False

    def insert(self, nickname, username, password):
        try:
            nickname = adduserprefix(self.user, nickname)
            nickname = addchar(nickname,1)
            username = addchar(username,2)
            password = addchar(password,3)
            #nickname = self.mycry.AES_Encrypt(self.key, nickname)
            #username = self.mycry.AES_Encrypt(self.key, username)
            #password = self.mycry.AES_Encrypt(self.key, password)
            self.db[nickname] = (username,password)
            print("stored a record")
            return True
        except:
            print("error happen when inserting ")
            return False
    
    def get(self, nickname):
        try:
            nickname = adduserprefix(self.user, nickname)
            nickname = addchar(nickname,1)
            #nickname = self.mycry.AES_Encrypt(self.key, nickname)
            (username, password) = self.db[nickname]
            #username = self.mycry.AES_Decrypt(self.key, username)
            #password = self.mycry.AES_Decrypt(self.key, password)
            username = removechar(username,2)
            password = removechar(password,3)
            print("got a record")
            return (username,password)
        except:
            print("error getting data")
            return (None, None)

    def delete(self, nickname):
        nickname = adduserprefix(self.user, nickname)
        nickname = addchar(nickname,1)
        #nickname = self.mycry.AES_Encrypt(key, nickname)
        if not nickname in self.db:
            return False
        del self.db[nickname]
        print("deleted a record")
        return True

    def resetpassword(self, new_phrase):
        #reset master password
        #need to delete all old record for the user that was using the old password
        #and restore them with the new key defined by the new password
        old_password = self.phrase
        old_key = self.key
        new_key = calculatekey(self.user, new_phrase)
        prefix = ""
        prefix += self.user + "_"
        for nickname in self.db:
            #for each nickname in the file
            #if it starts with the current username then it belongs to the user
            if nickname.startwith('prefix'):
                #decrypt to get original record data
                (old_username,old_password) = self.db[nickname]
                old_nickname = self.mycry.AES_Decrypt(old_key, nickname)
                old_username = self.mycry.AES_Decrypt(old_key, old_username)
                old_password = self.mycry.AES_Decrypt(old_key, old_password)
                #adding prefix and character are skipped because they are already there 
                #encrypt record data with new key
                new_nickname = self.mycry.AES_Encrypt(new_key, old_nickname)
                new_username = self.mycry.AES_Encrypt(new_key, old_username)
                new_password = self.mycry.AES_Encrypt(new_key, old_password)
                #store the new record and delete the old one 
                self.db[new_nickname] = (new_username, new_password)
                del self.db[nickname]
        self.phrase = new_phrase
        self.key = new_key







        
        
