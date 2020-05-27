from db import *
from crypt import *

db = Database("./vaultdb")


db.registeruser("admin", "123456", "admin@ucdavis.edu", "5302207777", 1)
if not db.login("admin", "123456"):
    exit()


# db.insert("boa", "bsdux333", "dasxc32156dv")
# db.insert("boa2", "asdfdvcxv", "32dxcd622165")
# db.insert("google", "baxcxcz", "d15165649595dv")
# db.insert("amazon", "adgfhjtfd", "das51c54vd46asds")

# print(db.get("boa"))
# print(db.get("boa2"))
# print(db.get("google"))
# print(db.get("amazon"))
print(db.fetchEmail("admin"))
print(db.fetchPhone("admin"))
db.resetEmail("xxx@ucdavis.edu")
db.resetPhone("2331223456", 1)
# db.resetpassword("admin", "password")
# print("master password changed")
print(db.fetchEmail("admin"))
print(db.fetchPhone("admin"))
#db.close()
# if not db.login("admin", "password"):
#    exit()

# print(db.get("boa2"))
# print(db.get("google"))
# print(db.get("amazon"))


# (a,b) = db.get(mycry.AES_Encrypt(key, "boa"))
# if a != None and b != None:
#     print(mycry.AES_Decrypt(key,a),mycry.AES_Decrypt(key,b))
# (a,b) = db.get(mycry.AES_Encrypt(key, "google"))
# if a != None and b != None:
#     print(mycry.AES_Decrypt(key,a),mycry.AES_Decrypt(key,b))
# db.delete(mycry.AES_Encrypt(key, "boa"))
# print(db.get(mycry.AES_Encrypt(key, "boa")))
db.close()
