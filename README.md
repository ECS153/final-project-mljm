# ECS 153 Final Project: The Vault
A desktop password manager that stores passwords safely.

+ Project proposal: https://github.com/ECS153/final-project-mljm/blob/master/proposal.md
+ Milestone1: https://github.com/ECS153/final-project-mljm/blob/master/Milestone1.md
+ Milestone2: https://github.com/ECS153/final-project-mljm/blob/master/Milestone2.md
+ Milestone3: https://github.com/ECS153/final-project-mljm/blob/master/Milestone3.md
+ Final presentation: https://docs.google.com/presentation/d/1I_jjfSIMo8-8sW3r55dnOay3Vr6HPytVIziSXpQbRmQ/edit#slide=id.g87da6e7ecf_2_1

## Code Structure in sourcecode
-------------------------------------
|- **GUI.py**: Implement a graphical Interface for users to use the application.

|- **handler.py**: Handle the interaction between the User Interface and the Database.

|----- **smtpCtrl.py**: Provide SMTP service for the handler to send emails.

|- **db.py**: Maintain a Database and corresponding operations, including storing, retrieving and resetting.

|----- **crypt.py**: Provide encryption and decryption function for database operations.


## Installs needed for The Vault
+ Crypto: For encryption
  + _pip install pycryptodome_
+ Pillow: For images in GUI
  + [Found Here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow)
