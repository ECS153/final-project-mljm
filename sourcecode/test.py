from db import *

db = Database("./ourdb")
db.open("username", "password")

db.insert("boa", "bsdux333", "dasxc32156dv")
db.insert("boa2", "czxzcvc", "24sf84yr33r")
db.insert("amazon", "dvuxdsafvi", "123456")
db.insert("google", "username", "password")

print(db.get("amazon"))
print(db.get("google"))
db.delete("boa")
print(db.get("boa"))

db.close()


