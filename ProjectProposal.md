# *The Vault* by MLJM 
---
## Project Proposal

### Purpose
For many web sites and applications, the use of high-entropy passwords is usually one of the first levels of defense from attackers. Because of this, having a unique and intricate password for each of these is extremely important, however, remembering numerous long or complicated strings can be difficult for many users. The idea of having a centralized location of all of your passwords is appealing, assuming that they are safe from any outside attacks.

### Our Design
We plan to build an encrypted password manager to store usernames and passwords locally for websites. It will be a desktop-based application and will be able to provide the correct password for each input pair of website and username from the user. There are three attributes stored for each record, including nickname for the website, username, and password. Once stored, the records will be encrypted and shuffled so that the attacker is not able to determine the corresponding attribute pairs, even if they have access to the database's raw files.

**Possible Implementations**
- Adding random characters into the password (before or after encryption), we can put this noise in random positions so if attackers just look into the data file they can't determine the structure of the password. 
	- Our system would need to figure out where the real characters are, maybe saving them as another field or determining them by some calculation based on metadata of the website or username (like RID or even the website or username itself).
- Adding some indirection to the password that is encrypted in a different way (maybe a different key or different algorithm), this should do the shuffling as we can put the password anywhere instead of paired with the website and username.


### Expected Results
We expect the Vault to achieve the following goals:
- Perform basic functions of storing and retrieving records containting the correct password given a specific website nickname and username.
- Generate a non-descript and ultimately unreadable records datafile, that will not reveal the users information regardless of access to The Vault's source code. 

