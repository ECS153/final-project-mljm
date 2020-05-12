import os
from sourcecode.db import *

class userdata:
    def __init__(self, user_name):
        self.user = userName
        self.dataFile = self.load_data()

    def loadData(self):
        dirPath = os.getcwd() + "\\userdata\\" + self.user + ".txt"
        try:
            userFile = open(dirPath, "xb")
        except OSError:
            if(not(os.path.exists(dirPath))):
                os.makedirs(dirPath)
        else:
            return userFile

    def readData(self, record):
        # find data
        # convert from binary to unicode
        #return data to db
        pass

    def writeData(self, record):
        # convert encoded data to binary
        # store in userdata file
        # return true when completed
        pass
    
    def deleteData(self, record):
        # find data
        # remove and reposition remaining records
        # return true when completed
        pass
