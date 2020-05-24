# The design

First time using, before any password is stored, ask user to set a master password.



## Database

+ Maintain two map:

  <tag, username, cipher password>

  <tag, username, key>, the key should be encrypted by master password



## Store(tag, username, password)

+ Generate a key to encrypt password, store the pair <tag, username, cipher password>

  **cipher password = Encrypt(password, key)**

+ Use master password to encrypt the key, store the pair <tag, username, encrypted key>

  **encrypted key = AES_Encrypt(master password, key)**



## Retrieve(tag, username)

* Access database to get cipher password and encrypted key.

  <tag, username> -> cipher password

  <tag, username> -> encrypted key

* Ask user to enter master password

* **key = AES_Decrypt(master password, encrypted key)**

+ **password = Decrypt(key, cipher password)**



## Problem

+ How to store master password? We can't store it directly in plaintext. Just remember it? Then each time storing a password, user need to enter a master password. 
