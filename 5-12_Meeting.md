#MEETING 5/12

**Last week:**   
	- We discussed the basic design implementation of our project  
	- A user will input a username, nick name of the website it is using, and a password  
	- We'll have an encrypted database to store password and username    
	- Not sure if we are going to create our own database or use an existing one  
	- Not sure how to do the encryption part   
	- Assigned a general task for each member of the group  
	- Came up with with the name of the project: Vault  

**This week:** 
	- We discussed in more detail the way each part of the project will be implemented  
	- A user will create an account name and master password in order to access the Vault   
	- The master password is store in a database file    
	- We will use a hash table to encrypt this master password, like the MD5 algorithm  
	- A database will be used to store the account, the hash function, the seed, and the encrypted password  
	- The user will use the account name and master password to log in   
	- The info the user inputs will then be check against the real master password and account name and if correct then user will be   allowed to log in    
	- When user is in the Vault, it can sore or retrieve passwords as desired  
	- The storing of a password works by generating a key to encrypt the password and using the master password to encrypt the key   
	- The database should store the account name, the tag, the encrypted key, and encrypted password  
	- To tag is the nickname of the website   
	- To retrieve a password, the database is accessed to get encrypted password and key  
	- Then the user enters the master password to decrypt the key   
	- Then the user uses the key to decrypt the password  
	- We decided to have two maps, one that has database file with the account name, hash function, the seed, encrypted master password and another database file with the account, tag, username, encrypted key, encrypted password  
	
  - **goal:** finish milestone, video and continue writing code. Prepare for Friday meeting 
