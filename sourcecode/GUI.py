# for use on python3, use this import:
# import tkinter as Tkinter
# from tkinter import *

# for use on python2, use this import:
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

        mainFrame = Frame(self.MainWindow)
        mainFrame.pack(fill="none", expand=True)

        upperFrame = Frame(mainFrame)
        upperFrame.pack(side=TOP, fill="none", expand=False)

        lowerFrame = Frame(mainFrame)
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False)

        labelFrame = Frame(upperFrame)
        labelFrame.pack(side=LEFT)

        boxFrame = Frame(upperFrame)
        boxFrame.pack(side=RIGHT)

        # Labels for entries
        accountNameLabel = Label(labelFrame, text="Account Name:", font=("TimesNewRoman", 14))
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Master Password:", font=("TimesNewRoman", 14))
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes
        accountNameEntry = Entry(boxFrame, bd=5)
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordEntry = Entry(boxFrame, bd=5, show='*')
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)

        # Login button
        loginButton = Tkinter.Button(lowerFrame, text="Login", command=self.welcome)
        loginButton.pack(side=BOTTOM, expand=YES, pady=5)
        loginButton.pack()

        self.MainWindow.mainloop()

    # Window that pops up after clicking login button
    def welcome(self):
        # Welcome window layout
        welcomeWindow = Tkinter.Tk()
        welcomeWindow.title('WELCOME')
        welcomeWindow.geometry("300x100")


        # backgroundImage= Tkinter.tk.PhotoImage(file"{}")
        # imageLabel= Label(welcomeWindow, image=backgroundImage)
        # imageLabel.pack()

        # Create frame for buttons
        frame = Frame(welcomeWindow)
        frame.pack(fill="none", expand=True)

        # Retrieve button
        retrieveButton = Button(frame, text="Retrieve", height="5", width="10")
        retrieveButton.pack(side=LEFT)

        # Store button
        storeButton = Button(frame, text="Store", height="5", width="10")
        storeButton.pack(side=RIGHT)

        welcomeWindow.mainloop()


start = LoginWindow()
start.FirstWindow()
