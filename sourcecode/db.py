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
        self.mycry = MyCrypt
        self.disk = os.path.expanduser(disk)
        #load userinfo file
        self.userinfo = os.path.expanduser("./userinfo")
        self.loaduserinfo(self.userinfo)
        self.load(self.disk)
        self.user = ""
        pass
    
    def loaduserinfo(self, userinfo):
        if os.path.exists(userinfo):
            self.users = json.load(open(self.userinfo, "r"))
        else:
            self.users = {}
        return True

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
            json.dump(self.users, open(self.userinfo, "w+"))
            return True
        except:
            return False

    def registeruser(self, user, phrase, email, phone, provider):
        if user in self.users:
            print("same username existed")
            return False
        sha1_phrase = self.mycry.SHA1(phrase)
        epKey = self.calculatekey(sha1_phrase[::-1])
        email = self.mycry.AES_Encrypt(epKey, email)
        phone = self.mycry.AES_Encrypt(epKey, phone)

        self.users[user] = (sha1_phrase, email, phone, provider)
        json.dump(self.users, open(self.userinfo, "w+"))
        return True

    def login(self, user, phrase):
        #open database and check if the input master password is correct
        #user is string of the username for the user who is using the app
        #phrase is string of the master password user enter for login
        if user not in self.users:
            print("User not exist!")
            return False

        # self.load(self.disk)
        self.user = user
        (sha1_phrase, email, phone, provider) = self.users[user]
        #calculate encryption/decryption key based on user and phrase here
        self.key = self.calculatekey(sha1_phrase)
        
        #check login here
        #do sha1 to phrase and check it with stored sha1_phrase
        hashed = self.mycry.SHA1(phrase)
        if hashed == sha1_phrase:
            print("Login successfully")
            return True
        else:
            print("Wrong master password")
            return False

    def calculatekey(self, phrase):
        #calculate encryption/decryption key based on user's sha1_phrase
        #do whatever to make the key based on sha1_phrase
        # the key's length is 16 chars
        raw = self.mycry.SHA1(phrase)
        h0 = int(raw[0:8], 16)
        h1 = int(raw[8:16], 16)
        h2 = int(raw[16:24], 16)
        h3 = int(raw[24:32], 16)
        h4 = int(raw[32:40], 16)

        h0 = h0 & h1
        h2 = h2 & h3 | h4        
        key = "%08x%08x" % (h0, h2)

        return key

    def insert(self, nickname, username, password):
        try:
            nickname = adduserprefix(self.user, nickname)
            # nickname = addchar(nickname,1)
            username = addchar(username,2)
            password = addchar(password,3)
            nickname = self.mycry.AES_Encrypt(self.key, nickname)
            username = self.mycry.AES_Encrypt(self.key, username)
            password = self.mycry.AES_Encrypt(self.key, password)
            self.db[nickname] = (username,password)
            print("stored a record")
            json.dump(self.db, open(self.disk, "w+"))
            return True
        except:
            print("error happen when inserting ")
            return False
    
    def get(self, nickname):
        # Given a nickname for a website
        # Return the username and password for that website 
        try:
            nickname = adduserprefix(self.user, nickname)
            #nickname = addchar(nickname,1)
            nickname = self.mycry.AES_Encrypt(self.key, nickname)
            (username, password) = self.db[nickname]
            username = self.mycry.AES_Decrypt(self.key, username)
            password = self.mycry.AES_Decrypt(self.key, password)
            username = removechar(username,2)
            password = removechar(password,3)
            print("got a record")
            return (username,password)
        except:
            print("error getting data")
            return (None, None)

    def delete(self, nickname):
        nickname = adduserprefix(self.user, nickname)
        # nickname = addchar(nickname,1)
        nickname = self.mycry.AES_Encrypt(self.key, nickname)
        if not nickname in self.db:
            return False
        del self.db[nickname]
        print("deleted a record")
        json.dump(self.db, open(self.disk, "w+"))
        return True
    
    def fetchEmail(self, user):
        # Use email to reset master password
        # self.user = user
        if user not in self.users:
            return None
        (sha1_phrase, email, phone, provider) = self.users[user]
        epKey = self.calculatekey(sha1_phrase[::-1])
        try:
            email = self.mycry.AES_Decrypt(epKey, email)
            return email
        except:
            return None

    def fetchPhone(self, user):
        # Use phone number to reset master password
        # Return: phone number and service provider
        if user not in self.users:
            return (None, None)
        (sha1_phrase, email, phone, provider) = self.users[user]
        epKey = self.calculatekey(sha1_phrase[::-1])
        try:
            phone = self.mycry.AES_Decrypt(epKey, phone)
            return (phone, provider)
        except:
            return (None, None)

    def fetchSQ(self, user):
        # The user who forget master password should ask for answering security questions
        # There should be an interaction: return the question to user and get an answer back from user
        # Should it be implemented in two functions? 
        self.user = user
        if user not in self.users:
            print("User not exist")
            return False
        (sha1_phrase, secQ, secA) = self.users[user]
        self.tempsecA = secA
        return secQ
    
    def checkSA(self, answer):
        # Check if the security answer is correct
        hashed = self.mycry.SHA1(answer)
        if hashed == self.tempsecA:
            self.tempsecA = None
            print("Identity checked")
            return True
        else:
            print("Wrong security answer")
            return False


    def resetpassword(self, user, new_phrase):
        #reset master password
        #need to delete all old records for the user that was using the old password to encrypt
        #and restore them with the new key defined by the new password
        
        # old_key = self.key
        (old_sha1phrase, email, phone, provider) = self.users[user]
        old_key = self.calculatekey(old_sha1phrase)
        old_epKey = self.calculatekey(old_sha1phrase[::-1])

        new_sha1phrase = self.mycry.SHA1(new_phrase)
        new_key = self.calculatekey(new_sha1phrase)
        new_epKey = self.calculatekey(new_sha1phrase[::-1])

        # update encrypted email and phone number
        email = self.mycry.AES_Decrypt(old_epKey, email)
        phone = self.mycry.AES_Decrypt(old_epKey, phone)
        email = self.mycry.AES_Encrypt(new_epKey, email)
        phone = self.mycry.AES_Encrypt(new_epKey, phone)


        prefix = ""
        prefix += user + "_"
        password_nicknames = []
        for nickname in self.db:
            #for each nickname in the file
            #if it starts with the current username then it belongs to the user
            print("nickname = ", nickname)
            old_nickname = self.mycry.AES_Decrypt(old_key, nickname)
            if old_nickname.startswith(prefix):
                print("this password belong to the user")
                password_nicknames.append(nickname)
        for nickname in password_nicknames:
            print("change dictionary")
            # decrypt to get original record data
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
            print("added entry, deleted old entry")
            #self.db[nickname] = (old_username, old_password)
        #edit sha1_phrase in userinfo
        self.users[user] = (new_sha1phrase, email, phone, provider)
        
        self.key = new_key
        return True

    def resetEmail(self, new_email):
        # Change the email after logged in
        (sha1phrase, email, phone, provider) = self.users[self.user]
        epKey = self.calculatekey(sha1phrase[::-1])
        new_email = self.mycry.AES_Encrypt(epKey, new_email)
        self.users[self.user] = (sha1phrase, new_email, phone, provider)
        return True
    
    def resetPhone(self, new_phone, new_provider):
        # Change the phone number and service provider after logged in
        (sha1phrase, email, phone, provider) = self.users[self.user]
        epKey = self.calculatekey(sha1phrase[::-1])
        new_phone = self.mycry.AES_Encrypt(epKey, new_phone)
        self.users[self.user] = (sha1phrase, email, new_phone, new_provider)
        return True

    







        
        
