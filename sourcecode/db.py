import json
import os

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

#store and retrive functionality using simple json
class Database():
    def __init__(self, disk):
        #disk is the path of the file we store the data in
        self.disk = os.path.expanduser(disk)
        self.load(self.disk)
        pass
    
    def open(self, user, phrase):
        #open database 
        #user is the user who run the app
        #phrase is the master password
        self.load(self.disk)
        self.user = user
        self.phrase = phrase
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
            return True
        except:
            return False

    def insert(self, nickname, username, password):
        try:
            nickname = addchar(nickname,1)
            username = addchar(username,2)
            password = addchar(password,3)
            self.db[nickname] = (username,password)
            print("stored a record")
            return True
        except:
            print("error happen when inserting ")
            return False
    
    def get(self, nickname):
        try:
            nickname = addchar(nickname,1)
            (username, password) = self.db[nickname]
            username = removechar(username,2)
            password = removechar(password,3)
            print("got a record")
            return (username,password)
        except:
            print("error getting data")
            return (None, None)

    def delete(self, nickname):
        nickname = addchar(nickname,1)
        if not nickname in self.db:
            return False
        del self.db[nickname]
        print("deleted a record")
        return True


        
        
