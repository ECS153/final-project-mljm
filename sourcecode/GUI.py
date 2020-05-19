import Tkinter
from Tkinter import *


class LoginWindow():
    def __init__(self):
        # Main Window layout
        self.MainWindow = Tkinter.Tk()

    def FirstWindow(self):
        # Main Window layout
        self.MainWindow.title('THE VAULT')
        self.MainWindow.geometry("400x150+10+20")

        # Labels for entries
        accountNameLabel = Label(self.MainWindow, text="Account \nName:", font=("TimesRoman", 14))
        accountNameLabel.place(x=20, y=30)
        masterPasswordLabel = Label(self.MainWindow, text="Master \nPassword:", font=("TimesRoman", 14))
        masterPasswordLabel.place(x=20, y=80)

        # User and password entry boxes
        accountNameEntry = Entry(self.MainWindow, bd=5)
        accountNameEntry.place(x=100, y=30)
        masterPasswordEntry = Entry(self.MainWindow, bd=5, show='*')
        masterPasswordEntry.place(x=100, y=80)

        # Login button
        loginButton = Tkinter.Button(self.MainWindow, text="Login", command=self.welcome)
        loginButton.pack(side=BOTTOM)
        loginButton.pack()

        self.MainWindow.mainloop()

    # Window that pops up after clicking login button
    def welcome(self):
        # Answer Window layout
        welcomeWindow = Tkinter.Tk()
        welcomeWindow.title('WELCOME')
        welcomeWindow.geometry("300x100")

        # Create frame for buttons
        frame = Frame(welcomeWindow)
        frame.pack()

        # Retrieve button
        retrieveButton = Button(frame, text="Retrieve", height="5", width="10")
        retrieveButton.pack(side=LEFT)

        # Store button
        storeButton = Button(frame, text="Store", height="5", width="10")
        storeButton.pack(side=RIGHT)

        welcomeWindow.mainloop()


start = LoginWindow()
start.FirstWindow()
