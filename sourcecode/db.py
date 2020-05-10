import json
import os

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
            self.db[str(nickname)] = (username,password)
            return True
        except:
            print("error happen when inserting ")
            return False
    
    def get(self, nickname):
        try:
            return self.db[nickname]
        except:
            print("error getting data")
            pass

    def delete(self, nickname):
        if not nickname in self.db:
            return False
        del self.db[nickname]
        return True


        
        
