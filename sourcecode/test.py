from db import *
from crypt import *

db = Database("./vaultdb")

# print(db.fetchEmail("admin"))
# db.resetpassword("admin", "pwd123456")

# db.registeruser("admin", "password", "admin@ucdavis.edu")
if not db.login("admin", "pwd123456"):
    exit()

key = "11364592315"
mycry = MyCrypt

db.insert(mycry.AES_Encrypt(key, "boa"), mycry.AES_Encrypt(key, "bsdux333"), mycry.AES_Encrypt(key, "dasxc32156dv"))
db.insert(mycry.AES_Encrypt(key, "boa2"), mycry.AES_Encrypt(key, "asdfdvcxv"), mycry.AES_Encrypt(key, "32dxcd622165"))
db.insert(mycry.AES_Encrypt(key, "google"), mycry.AES_Encrypt(key, "baxcxcz"), mycry.AES_Encrypt(key, "d15165649595dv"))
db.insert(mycry.AES_Encrypt(key, "amazon"), mycry.AES_Encrypt(key, "adgfhjtfd"), mycry.AES_Encrypt(key, "das51c54vd46asds"))

# (a,b) = db.get(mycry.AES_Encrypt(key, "boa"))
# if a != None and b != None:
#     print(mycry.AES_Decrypt(key,a),mycry.AES_Decrypt(key,b))
# (a,b) = db.get(mycry.AES_Encrypt(key, "google"))
# if a != None and b != None:
#     print(mycry.AES_Decrypt(key,a),mycry.AES_Decrypt(key,b))
# db.delete(mycry.AES_Encrypt(key, "boa"))
# print(db.get(mycry.AES_Encrypt(key, "boa")))
db.close()
