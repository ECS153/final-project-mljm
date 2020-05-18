import os
import json

# records {tag: [(username, password)]}

class dbData:
    def __init__(self):
        self.dbPath = self.openDBData()

    def openDBData(self):
        dirPath =  'db_data.txt'
        try:
            _db = open(dirPath, "xb")
            _db.close()
            return dirPath
        except OSError:
            if(os.path.exists(dirPath)):
                return dirPath
    
    def addUser(self, user, password, secQest):
        self.editPass(user, password)
        # editSecQuest()
        return

    def getPass(self, user):
        with open(self.dbPath, 'r') as dbFile:
            dbDat = json.load(dbFile)
            password = dbDat[user]['masterPass']
            del dbDat
            dbFile.close()   
        return password

    def editPass(self, user, password):
        with open(self.dbPath, 'w') as dbFile:
            if os.path.getsize(self.dbPath) == 0:
                dbDat = {}
                dbDat[user]={}
                dbDat[user]['masterPass'] = password
            else:
                dbDat = json.load(dbFile)
                try:
                    dbDat[user][masterPass] = password
                except KeyError:
                    dbDat[user] = {}
                    dbDat[user]['masterPass'] = password
            json.dump(dbDat, dbFile)
            dbFile.close()    
        return

    def editSecQuest(self, user, secQuest):
        pass

    def deleteUser(self, user):
        # find user account
        # delete all data in userData
        # delete user account from dbData
        pass

class userData:
    def __init__(self):
        self.userPath = self.openUserData()

    def openUserData(self):
        dirPath = "user_data.txt"
        try:
            _user = open(dirPath, 'xb')
            _user.close()
            return dirPath
        except OSError:
            if(os.path.exists(dirPath)):
                return dirPath
    
    def readData(self, user, tag):
        with open(self.userPath, 'r') as userFile:
            userDat = json.load(userFile)
            record = userDat[user][tag]
            del dbDat
            dbFile.close()   
        return record

    def writeData(self, user, record):
        with open(self.userPath, 'w') as userFile:
            if os.path.getsize(self.userPath) == 0:
                userDat = {}
                userDat[user] = {}
            else:
                userDat = json.load(userFile)
            for key,val in record.items():
                userDat[user][key] = val
            json.dump(userDat, userFile)
            userFile.close()   
            del userDat
        return record
    
    def deleteData(self, user, record):
        # find data
        # remove and reposition remaining records
        # return when completed
        pass


### TEST SCRIPT ###
data = {}
data['johnsmith']= {}
data['johnsmith']['amazon'] = '((jmna@gmailcom, ksh3h95bd),(heihf@gmailcom, htge4356),(iejtsx@gmailcom, nmzx.48))'
data['johnsmith']['gmail']= '((jmna, 23shyhy43d),(heihf, 234nt5985))'
data['johnsmith']['netflix'] = '((jmna@gmailcom, maown2o%92fkn))'

user = 'johnsmith'

rec1 = {'amazon':'(jmna@gmailcom, ksh3h95bd)'}
rec2 = {'netfilx': '(jmna@gmailcom, maown2o%92fkn)'}


dbf = dbData()
dbf.addUser('johnsmith', 'f5d16h4b68451b684', [])

userf = userData()

userf.writeData(user, rec1)

