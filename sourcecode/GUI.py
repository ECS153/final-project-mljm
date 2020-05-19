import Tkinter
import tkMessageBox
from Tkinter import *

# Global variable for inputs
'''def values():
    global answer
    answer = float(AnswerEntry.get())'''

# Main Window layout
MainWindow = Tkinter.Tk()
MainWindow.title('THE VAULT')
MainWindow.geometry("400x150+10+20")

# Labels for entries
AccountNameLabel = Label(MainWindow, text = "Account \nName:", font = ("TimesRoman", 14))
AccountNameLabel.place(x=20, y=30)
MasterPasswordLabel = Label(MainWindow, text = "Master \nPassword:", font = ("TimesRoman", 14))
MasterPasswordLabel.place(x=20, y=80)

# User and password entry boxes
AccountNameEntry = Entry(MainWindow, bd = 5)
AccountNameEntry.place(x=100, y=30)
MasterPasswordEntry = Entry(MainWindow, bd = 5, show ='*')
MasterPasswordEntry.place(x=100, y=80)

# Function that retrieves password for user
def retrievePassword(tag):
    print("username:", username.get())
    print("password:", password.get())
    return

# Window that pops up after clicking login button
def welcome():
    # Answer Window layout
    welcomeWindow = Tkinter.Tk()
    welcomeWindow.title('Welcome')
    welcomeWindow.geometry("400x100+10+20")

    # Label for entry box
    AnswerLabel = Label(welcomeWindow, text = "Retrieve or \n store password?:", font = ("TimesRoman", 14))
    AnswerLabel.place(x=20, y=30)

    # Answer entry box
    AnswerEntry = Entry(welcomeWindow, bd = 5)
    AnswerEntry.place(x=150, y=30)

    def answerf():
        if AnswerEntry.get().strip().lower == "retrieve":
            # Retrieve Window layout
            RetrieveWindow = Tkinter.Tk()
            RetrieveWindow.title('Retrieve Passwords')
            RetrieveWindow.geometry("400x150+10+20")

            #retrievePassword(tag)

            # Passwords
            PasswordLabel = Label(RetrieveWindow, text = "Passwords:", font = ("TimesRoman", 14))
            PasswordLabel.place(x=20, y=30)

    # Enter button
    EnterButton = Tkinter.Button(welcomeWindow, text ="Enter")
    EnterButton.pack(side = BOTTOM)
    EnterButton.configure(command=answerf)
    EnterButton.pack()


    '''def answer()
    if AnswerEntry.get().strip().lower == "retrieve":
        # Retrieve Window layout
        RetrieveWindow = Tkinter.Tk()
        RetrieveWindow.title('Retrieve Passwords')
        RetrieveWindow.geometry("400x150+10+20")

        # Passwords
        PasswordLabel = Label(RetrieveWindow, text = "Passwords:", font = ("TimesRoman", 14))
        PasswordLabel.place(x=20, y=30)

        retrievePassword(tag)

        End app
        button_quit = Tkinter.Button(retrieveWindow, text = "Exit", command = retrieveWindow.quit)
        button_quit.pack()'''

# Login button
LoginButton = Tkinter.Button(MainWindow, text ="Login", command = welcome)
LoginButton.pack(side = BOTTOM)
LoginButton.pack()

MainWindow.mainloop()
