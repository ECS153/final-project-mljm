# Meeting 05/15

## Add more emphasis on UI
```
Log in
|->password management
|	|-> Store 
|	|-> Retrieve
|
|->account management
	|->change password
	|->change security questions
```

## idea

+ Add multiple security questions to give a hint to the master password.
+ If forget password, answer security questions correctly, reset the password.
+ when user changes password, it will have to decrypt all records with old master-password and re-encrypt with new master-password.



## Plan for next milestones

+ Lynn: Working on the hash function, generate key things.
+ Monica: 2 windows, one for login and one for after login.
+ Jiahao: Password recover and reset.
+ Mike: password storage system
