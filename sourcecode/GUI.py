import tkinter.font as tkFont
import tkinter
from tkinter import *

class VaultApp():

    def __init__(self):
        # Main Window layout
        self.MainWindow = tkinter.Tk()
        self.welcomeWindow = None
        self.settingsWindow = None
        self.ResetWindow = None
        self.st = None
        self.retrieve = None


    def closeWin(self, win):
        if (win == "self.MainWindow") and (self.welcomeWindow != None):
            self.cascadeDestroy()
        exec(win +".destroy()")
        exec(win+" = None")


    def cascadeDestroy(self):
        self.welcomeWindow.destroy()
        self.welcomeWindow = None
        if(self.settingsWindow == None):
            pass
        else:
            self.settingsWindow.destroy()
            self.settingsWindow = None
        if(self.st == None):
            pass
        else:
            self.st.destroy()
            self.st = None
        if(self.retrieve == None):
            pass
        else:
            self.retrieve.destroy()
            self.retrieve = None
        # if(self.ResetWindow == None):
        #     pass
        # else:
        #     self.ResetWindow.destroy()
        #     self.ResetWindow = None


    def openWindow(self, winType):
        if winType == "welcome":
            if(self.welcomeWindow == None):
                self.welcome()
            else:
                pass
        if winType == "settings":
            if(self.settingsWindow == None):
                self.Settings()
            else:
                pass
        elif winType == "reset":
            if(self.ResetWindow == None):
                self.Reset()
            else:
                pass
        elif winType == "store":
            if(self.st == None):
                self.open_Store()
            else:
                pass
        elif winType == "retrieve":
            if(self.retrieve == None):
                self.open_Retrieve()
            else:
                pass


    def LoginWindow(self):
        # Main Window layout
        self.MainWindow.title('THE VAULT')
        self.MainWindow.geometry("450x200+300+200")
        self.MainWindow.configure(bg="#FFB266")

        # Frames for the main login window
        mainFrame = Frame(self.MainWindow, bg="#FFB266")
        mainFrame.pack(fill="none", expand=True)
        upperFrame = Frame(mainFrame, bg="#FFB266")
        upperFrame.pack(side=TOP, fill="none", expand=False)
        lowerFrame = Frame(mainFrame, bg="#FFB266")
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False)
        labelFrame = Frame(upperFrame, bg="#FFB266")
        labelFrame.pack(side=LEFT)
        boxFrame = Frame(upperFrame, bg="#FFB266")
        boxFrame.pack(side=RIGHT)

        # Labels for entries for main login window
        times = tkFont.Font(family="TimesNewRoman", size=14)
        accountNameLabel = Label(labelFrame, text="Account Name:", bg="#FFB266", font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Master Password:", bg="#FFB266", font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes for main login window
        accountNameEntry = Entry(boxFrame, bd=5, bg="#FFB266")
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        accountNameEntry.configure(highlightbackground="#FFB266")
        masterPasswordEntry = Entry(boxFrame, bd=5, bg="#FFB266", show='*')
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)
        masterPasswordEntry.configure(highlightbackground= "#FFB266")

        # Login button in main login window
        loginButton = tkinter.Button(lowerFrame, text="Login", bg='#FFB266', height=1, width=6, command=lambda: self.openWindow("welcome"))
        loginButton.pack(side=TOP, expand=YES, pady=10)
        loginButton.configure(relief=RAISED)
        loginButton.pack()

        # Link to reset the user's Account Name and Password in main login window
        link = Label(lowerFrame, text="Forgot Master Password?", bg="#FFB266", fg="blue", cursor="arrow")
        link.pack(side=BOTTOM, expand=YES)
        link.bind("<Button-1>", lambda r: self.openWindow("reset"))

        self.MainWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWin("self.MainWindow"))
        self.MainWindow.mainloop()


    def Reset(self):
        # Reset Window layout
        self.ResetWindow = tkinter.Tk()
        self.ResetWindow.title('Reset')
        self.ResetWindow.geometry("400x300")

        # Reset Window frames
        mainFrame = Frame(self.ResetWindow)
        mainFrame.pack(fill="none", expand=True)
        upperFrame = Frame(mainFrame)
        upperFrame.pack(side=TOP, fill="none", expand=False)
        lowerFrame = Frame(mainFrame)
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False)
        labelFrame = Frame(upperFrame)
        labelFrame.pack(side=LEFT)
        boxFrame = Frame(upperFrame)
        boxFrame.pack(side=RIGHT)

        # Labels for entries in reset window
        times = tkFont.Font(family="TimesNewRoman", size=14)
        accountNameLabel = Label(labelFrame, text="Account Name:", font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Master Password:", font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes in reset window
        accountNameEntry = Entry(boxFrame, bd=5)
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordEntry = Entry(boxFrame, bd=5, show='*')
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)

        # Login button in reset window
        EnterButton = tkinter.Button(lowerFrame, text="Login", command=lambda: self.openWindow("welcome"))
        EnterButton.pack(side=BOTTOM, expand=YES, pady=20)
        EnterButton.pack()

        self.MainWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWin("self.ResetWindow"))


    # Create a settings window
    def Settings(self):
        self.settingsWindow = tkinter.Tk()
        self.settingsWindow.title('Settings')
        self.settingsWindow.geometry("600x500")

        # Create a menu bar in settings window
        menu_bar = Menu(self.settingsWindow)
        self.settingsWindow.config(menu=menu_bar)

        # Create a File drop down menu in settings window
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Close settings window
        filemenu.add_command(label="Log Out", command=self.cascadeDestroy)
        # Exit out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWin("self.MainWindow"))

        # Frames for the settings window
        mainFrame = Frame(self.settingsWindow)
        mainFrame.pack(fill="none", expand=True)
        upperFrame = Frame(mainFrame)
        upperFrame.pack(side=TOP, fill="none", expand=False)
        lowerFrame = Frame(mainFrame)
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False)
        labelFrame = Frame(upperFrame)
        labelFrame.pack(side=LEFT)
        boxFrame = Frame(upperFrame)
        boxFrame.pack(side=RIGHT)

        # Labels for entries in settings window
        times = tkFont.Font(family="TimesNewRoman", size=14)
        accountNameLabel = Label(labelFrame, text="Enter new Account Name:", font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Enter new Master Password:", font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes in settings window
        accountNameEntry = Entry(boxFrame, bd=5)
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordEntry = Entry(boxFrame, bd=5, show='*')
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)

        # Login button in settings window
        enterButton = tkinter.Button(lowerFrame, text="Enter")
        enterButton.pack(side=BOTTOM, expand=YES, pady=5)
        enterButton.pack()

        self.settingsWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWin("self.settingsWindow"))
        #settingsWindow.mainloop()


    def welcome(self):
        # Welcome window layout
        self.welcomeWindow = tkinter.Tk()
        self.welcomeWindow.title('WELCOME')
        self.welcomeWindow.geometry("600x500+300+150")

        # Create a menu bar in welcome window
        menu_bar = Menu(self.welcomeWindow)
        self.welcomeWindow.config(menu=menu_bar, bg="#856ff8")

        # Create a File drop down menu in welcome window
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Settings should take you to another window
        filemenu.add_command(label="Settings", command=lambda: self.openWindow("settings"))
        filemenu.add_separator()
        # Close welcome window
        filemenu.add_command(label="Log Out", command=self.cascadeDestroy)
        # Exit out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWin("self.MainWindow"))

        # Create an Action drop down menu in welcome window
        actionMenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Action", menu=actionMenu)
        # Store should take you to a window to store passwords
        actionMenu.add_command(label="Store", command=lambda: self.openWindow("store"))
        # Retrieve should take you to window that retrieves password
        actionMenu.add_command(label="Retrieve", command=lambda: self.openWindow("retrieve"))

        # Create frame for buttons in welcome window
        frame = Frame(self.welcomeWindow)
        frame.pack(fill="none", expand=True)
        frame.configure(bg="#856ff8")
        frame.pack()

        # Retrieve button in welcome window
        retrieveButton = Button(frame, text="Retrieve", height="2", width="10", command=lambda: self.openWindow("retrieve"))
        retrieveButton.pack(side=LEFT, padx=10)
        retrieveButton.configure(bg="#856ff8", relief=RAISED, state=ACTIVE)
        retrieveButton.pack()

        # Store button in welcome window
        storeButton = Button(frame, text="Store", height="2", width="10", command=lambda: self.openWindow("store"))
        storeButton.pack(side=RIGHT, padx=10)
        storeButton.configure(bg="#856ff8", relief=RAISED, state=ACTIVE)
        storeButton.pack()

        self.welcomeWindow.protocol("WM_DELETE_WINDOW", self.cascadeDestroy)
        self.welcomeWindow.mainloop()


    def open_Store(self):
        self.st = Toplevel()
        self.st.title("Store Passwords")
        self.st.geometry("400x150")

        # Create label
        label = Label(self.st, text="Enter passwords to store")
        label.pack()

        # Create exit button.
        exit_button = Button(self.st, text="Close", command=lambda: self.closeWin("self.st"))
        exit_button.pack()

        # Create quit button.
        quit_button = Button(self.st, text="Exit", command=lambda: self.closeWin("self.MainWindow"))
        quit_button.pack()

        self.st.protocol("WM_DELETE_WINDOW", lambda: self.closeWin("self.st"))
        self.st.mainloop()


    def open_Retrieve(self):
        self.retrieve = Toplevel()
        self.retrieve.title("Retrieve Passwords")
        self.retrieve.geometry("400x150")

        # Create label
        label = Label(self.retrieve, text = "Select Passwords to Retrieve")
        label.pack()

        # Create exit button
        exit_button = Button(self.retrieve, text = "Close", command = lambda: self.closeWin("self.retrieve"))
        exit_button.pack()

        # Create quit button.
        quit_button = Button(self.retrieve, text = "Exit", command = lambda: self.closeWin("self.MainWindow"))
        quit_button.pack()

        self.retrieve.protocol("WM_DELETE_WINDOW", lambda: self.closeWin("self.retrieve"))
        self.retrieve.mainloop()


start = VaultApp()
start.LoginWindow()
