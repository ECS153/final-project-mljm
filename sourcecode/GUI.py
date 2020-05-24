import tkinter.font as tkFont
import tkinter
from tkinter import *
from handler import *

class VaultApp():

    def __init__(self):
        # Main Window layout
        self.handler = Handler()
        self.loginWindow = tkinter.Tk()
        self.welcomeWindow = None
        self.registerWindow = None
        self.settingsWindow = None
        self.resetWindow = None
        self.storeWindow = None
        self.retrieve = None

    def closeWindow(self, win):
        if (win == "self.loginWindow") and (self.welcomeWindow != None):
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
        if(self.storeWindow == None):
            pass
        else:
            self.storeWindow.destroy()
            self.storeWindow = None
        if(self.retrieve == None):
            pass
        else:
            self.retrieve.destroy()
            self.retrieve = None
        if(self.resetWindow == None):
            pass
        else:
            self.resetWindow.destroy()
            self.resetWindow = None

    def openWindow(self, winType):
        if winType == "welcome":
            if(self.welcomeWindow == None):
                self.Welcome()
            else:
                pass
        if winType == "settings":
            if(self.settingsWindow == None):
                self.Settings()
            else:
                pass
        elif winType == "reset":
            if(self.resetWindow == None):
                self.Reset()
            else:
                pass
        elif winType == "store":
            if(self.storeWindow == None):
                self.Store()
            else:
                pass
        elif winType == "retrieve":
            if(self.retrieve == None):
                self.Retrieve()
            else:
                pass
        elif winType == "register":
            if(self.registerWindow == None):
                self.Register()
            else:
                pass

    def login(self, aName, mPass, erro):
        if (not aName) or (not mPass):
            erro.set("Enter an Account Name and Password")
        else:
            rtn = self.handler.login(aName, mPass)
            if isinstance(rtn, bool):
                self.openWindow("welcome")
            else:
                erro.set(rtn)

    def reg(self, aName, mPass, erro, secQ, seqA):
        if (not aName) or (not mPass) or (not secQ) or (not seqA):
            erro.set("Enter all required fields")
        else:
            rtn = self.handler.signup(aName, mPass, secQ, seqA)
            if isinstance(rtn, bool):
                self.openWindow("Welcome")
            else:
                erro.set(rtn)

    def Login(self):
        bgColorMain = "#4CA7B2"
        bgColorSub = "#4697A1"

        # Login Window layout
        self.loginWindow.title('THE VAULT')
        self.loginWindow.geometry("500x225+300+200")
        self.loginWindow.configure(bg=bgColorMain)

        # Frames for login window
        mainFrame = Frame(self.loginWindow, bg=bgColorMain)
        mainFrame.pack(fill="none", expand=True)
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=15)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT)
        boxFrame = Frame(upperFrame, bg=bgColorMain)
        boxFrame.pack(side=RIGHT)
        lowerFrame = Frame(mainFrame, bg=bgColorMain)
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False, pady=5)
        buttonFrame = Frame(mainFrame, bg=bgColorMain)
        buttonFrame.pack(side=BOTTOM, fill="none", expand=False)

        err = tkFont.Font(family="Arial", weight=tkFont.BOLD, size=14)
        errorText = tkinter.StringVar()
        errorText.set("")
        errorLabel = Label(errorFrame, textvariable=errorText, bg=bgColorMain, fg="#D32600", font=err )
        errorLabel.pack()

        # Labels for entries for login window
        times = tkFont.Font(family="TimesNewRoman", size=14)
        accountNameLabel = Label(labelFrame, text="Account Name:", bg=bgColorMain, font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Master Password:", bg=bgColorMain, font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes for login window
        accountNameEntry = Entry(boxFrame, bd=4, bg=bgColorSub, fg="#FFFFFF")
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        accountNameEntry.configure(highlightbackground=bgColorSub)
        masterPasswordEntry = Entry(boxFrame, bd=4, bg=bgColorSub, show='*', fg="#FFFFFF")
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)
        masterPasswordEntry.configure(highlightbackground= bgColorSub)

        # Login button for login window
        loginButton = tkinter.Button(buttonFrame, text="Login", bg=bgColorSub, height=1, width=6,
                      command=lambda: self.login(accountNameEntry.get(),masterPasswordEntry.get(), errorText))
        loginButton.pack(side=LEFT, expand=YES, pady=5, padx=5)
        loginButton.configure(relief=RAISED)
        loginButton.pack()

        # Register button for login window
        registerButton = tkinter.Button(buttonFrame, text="Register", bg=bgColorSub, height=1, width=8,
                      command= lambda: self.openWindow("register"))
        registerButton.pack(side=RIGHT, expand=YES, pady=5, padx=5)
        registerButton.configure(relief=RAISED)
        registerButton.pack()

        # Link to reset the user's Account Name and Password
        link = Label(lowerFrame, text="Forgot Master Password?", bg=bgColorMain, fg="blue", cursor="arrow")
        link.pack(side=BOTTOM, expand=YES)
        link.bind("<Button-1>", lambda r: self.openWindow("reset"))

        # Closes window using x button
        self.loginWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("self.loginWindow"))
        self.loginWindow.mainloop()

    def Welcome(self):
        bgColorMain = "#856ff8"
        bgColorSub = "#765EEF"

        # Welcome window layout
        self.welcomeWindow = tkinter.Tk()
        self.welcomeWindow.title('WELCOME')
        self.welcomeWindow.geometry("600x500+300+150")

        # Create a menu bar
        menu_bar = Menu(self.welcomeWindow)
        self.welcomeWindow.config(menu=menu_bar, bg=bgColorMain)

        # Create a File drop down menu
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Settings option
        filemenu.add_command(label="Settings", command=lambda: self.openWindow("settings"))
        filemenu.add_separator()
        # Close welcome window
        filemenu.add_command(label="Log Out", command=self.cascadeDestroy)
        # Exit out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWindow("self.loginWindow"))

        # Create an Action drop down menu
        actionMenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Action", menu=actionMenu)
        # Store should take you to a window to store passwords
        actionMenu.add_command(label="Store", command=lambda: self.openWindow("store"))
        # Retrieve should take you to window that retrieves password
        actionMenu.add_command(label="Retrieve", command=lambda: self.openWindow("retrieve"))

        # Create frame for buttons
        buttonFrame = Frame(self.welcomeWindow)
        buttonFrame.pack(fill="none", expand=True)
        buttonFrame.configure(bg=bgColorMain)
        buttonFrame.pack()

        # Retrieve button
        retrieveButton = Button(buttonFrame, text="Retrieve", height="2", width="10", command=lambda: self.openWindow("retrieve"))
        retrieveButton.pack(side=LEFT, padx=10)
        retrieveButton.configure(bg=bgColorSub, relief=RAISED, state=ACTIVE)
        retrieveButton.pack()

        # Store button
        storeButton = Button(buttonFrame, text="Store", height="2", width="10", command=lambda: self.openWindow("store"))
        storeButton.pack(side=RIGHT, padx=10)
        storeButton.configure(bg=bgColorSub, relief=RAISED, state=ACTIVE)
        storeButton.pack()

        # Closes window using x button
        self.welcomeWindow.protocol("WM_DELETE_WINDOW", self.cascadeDestroy)
        self.welcomeWindow.mainloop()

    def Register(self):
        bgColorMain = "#009900"
        bgColorSub = "#259C44"

        # Register window layout
        self.registerWindow = Toplevel()
        self.registerWindow.title('REGISTER')
        self.registerWindow.geometry("600x500+300+150")

        # Create a menu bar
        menu_bar = Menu(self.registerWindow)
        self.registerWindow.config(menu=menu_bar, bg=bgColorMain)

        # Create a File drop down menu
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Register information
        filemenu.add_command(label="Register", command=lambda: self.openWindow("Register"))
        filemenu.add_separator()
        # Close welcome window
        filemenu.add_command(label="Close", command=lambda: self.closeWindow("self.registerWindow"))
        # Exit out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWindow("self.loginWindow"))

        # Create frames
        mainFrame = Frame(self.registerWindow, bg=bgColorMain)
        mainFrame.pack(fill="none", expand=True)
        mainFrame.pack()
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False, pady=5)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=20)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT, fill="none", expand=False, padx=5)
        entryFrame = Frame(upperFrame, bg=bgColorMain)
        entryFrame.pack(side=RIGHT, fill="none", expand=False, padx=5)
        buttonFrame = Frame(mainFrame, bg=bgColorMain, pady=20)
        buttonFrame.pack(side=BOTTOM, fill="none", expand=False)

        err = tkFont.Font(family="TimesNewRoman", weight=tkFont.BOLD, size=20)
        errorText = tkinter.StringVar()
        errorText.set("ERROR")
        errorLabel = Label(errorFrame, textvariable=errorText, bg=bgColorMain, fg="#FFFFFF", font=err )
        errorLabel.pack(side=TOP, fill=BOTH, pady=10)

        # Labels for entries
        times = tkFont.Font(family="TimesNewRoman", size=18)
        userNameLabel = Label(labelFrame, text="User Name:", bg=bgColorMain, font=times)
        userNameLabel.pack(side=TOP, fill=BOTH, pady=10)
        PasswordLabel = Label(labelFrame, text="Password:", bg=bgColorMain, font=times)
        PasswordLabel.pack(side=TOP, fill=BOTH, pady=10)
        securityQLabel = Label(labelFrame, text="Security Question:", bg=bgColorMain, font=times)
        securityQLabel.pack(side=TOP, fill=BOTH, pady=10)
        securityALabel = Label(labelFrame, text="Answer:", bg=bgColorMain, font=times)
        securityALabel.pack(side=TOP, fill=BOTH, pady=10)

        # User,password, security question, and security answer entry boxes
        userNameEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#FFFFFF")
        userNameEntry.pack(side=TOP, fill=BOTH, pady=10)
        userNameEntry.configure(highlightbackground=bgColorSub)
        passwordEntry = Entry(entryFrame, bd=4, bg=bgColorSub, show='*', fg="#FFFFFF")
        passwordEntry.pack(side=TOP, fill=BOTH, pady=10)
        passwordEntry.configure(highlightbackground= bgColorSub)
        securityQEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#FFFFFF")
        securityQEntry.pack(side=TOP, fill=BOTH, pady=10)
        securityQEntry.configure(highlightbackground=bgColorSub)
        securityAEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#FFFFFF")
        securityAEntry.pack(side=TOP, fill=BOTH, pady=10)
        securityAEntry.configure(highlightbackground=bgColorSub)

        # Register button
        registerButton = Button(buttonFrame, text="Register", height="2", width="10")
        registerButton.pack(side=RIGHT, padx=10)
        registerButton.configure(bg=bgColorSub, relief=RAISED, state=ACTIVE)
        registerButton.pack()

        # Cancel button
        cancelButton = Button(buttonFrame, text="Cancel", height="2", width="10", command=lambda: self.closeWindow("self.registerWindow"))
        cancelButton.pack(side=LEFT, padx=10)
        cancelButton.configure(bg=bgColorSub, relief=RAISED, state=ACTIVE)
        cancelButton.pack()

        # Closes window using x button
        self.registerWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("self.registerWindow"))
        self.registerWindow.mainloop()

    def Reset(self):
        bgColorMain = "#FFF9C4"
        bgColorSub = "#FFF176"

        # Reset Window layout
        self.resetWindow = Toplevel()
        self.resetWindow.title('RESET')
        self.resetWindow.geometry("400x300")

        # Create a menu bar
        menu_bar = Menu(self.resetWindow)
        self.resetWindow.config(menu=menu_bar, bg=bgColorMain)

        # Create a File drop down menu
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)

        # Close welcome window
        filemenu.add_command(label="Close", command=lambda: self.closeWindow("self.resetWindow"))
        # Exit out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWindow("self.loginWindow"))

        # Reset Window frames
        mainFrame = Frame(self.resetWindow, bg=bgColorMain)
        mainFrame.pack(fill="none", expand=True)
        mainFrame.pack()
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=10)
        lowerFrame = Frame(mainFrame, bg=bgColorMain)
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False, pady=5)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT)
        boxFrame = Frame(upperFrame, bg=bgColorMain)
        boxFrame.pack(side=RIGHT)

        # Label for entry
        times = tkFont.Font(family="TimesNewRoman", size=16)
        accountNameLabel = Label(labelFrame, text="Account Name:", font=times, bg=bgColorMain)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)

        # Account name entry box
        accountNameEntry = Entry(boxFrame, bd=5, bg=bgColorMain)
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        accountNameEntry.configure(highlightbackground=bgColorMain)

        # Enter button
        enterButton = tkinter.Button(lowerFrame, text="Enter", height="2", width="10")
        enterButton.pack(side=BOTTOM, expand=YES, pady=5)
        enterButton.configure(bg=bgColorSub)
        enterButton.pack()

        # Close window using x button
        self.resetWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("self.resetWindow"))
        self.resetWindow.mainloop()

    def Store(self):
        bgColorMain = "#BBDEFB"
        bgColorSub = "#4FC3F7"

        # Store Window layout
        self.storeWindow = Toplevel()
        self.storeWindow.title("STORE")
        self.storeWindow.geometry("500x300+400+150")

        # Reset Window frames
        mainFrame = Frame(self.storeWindow, bg=bgColorMain)
        mainFrame.pack(fill=BOTH, expand=True)
        mainFrame.pack()
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False, pady=5)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=20)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT, fill="none", expand=False, padx=5)
        entryFrame = Frame(upperFrame, bg=bgColorMain)
        entryFrame.pack(side=RIGHT, fill="none", expand=False, padx=5)
        buttonFrame = Frame(mainFrame, bg=bgColorMain, pady=20)
        buttonFrame.pack(side=BOTTOM, fill="none", expand=False)

        # Labels
        times = tkFont.Font(family="TimesNewRoman", size=16)
        nickNameLabel = Label(labelFrame, text="Nickname:", bg=bgColorMain, font=times)
        nickNameLabel.pack(side=TOP, fill=BOTH, pady=10)
        userNameLabel = Label(labelFrame, text="Username:", bg=bgColorMain, font=times)
        userNameLabel.pack(side=TOP, fill=BOTH, pady=10)
        PasswordLabel = Label(labelFrame, text="Password:", bg=bgColorMain, font=times)
        PasswordLabel.pack(side=TOP, fill=BOTH, pady=10)

        # Entry boxes
        nickNameEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#FFFFFF")
        nickNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        nickNameEntry.configure(highlightbackground=bgColorSub)
        userNameEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#FFFFFF")
        userNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        userNameEntry.configure(highlightbackground=bgColorSub)
        passwordEntry = Entry(entryFrame, bd=4, bg=bgColorSub, show='*', fg="#FFFFFF")
        passwordEntry.pack(side=TOP, fill=BOTH, pady=5)
        passwordEntry.configure(highlightbackground= bgColorSub)

        # Buttons
        storebutton = Button(buttonFrame, text="Store", bg=bgColorSub, height="2", width="10")
        storebutton.pack(side=RIGHT, padx=10)
        exitbutton = Button(buttonFrame, text="Exit", height="2", width="10",
                            command=lambda: self.closeWindow("self.loginWindow"))
        exitbutton.pack(side=RIGHT, padx=10)

        # Close window using x button
        self.storeWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("self.storeWindow"))
        self.storeWindow.mainloop()

    def Retrieve(self):
        bgColorMain = "#FFAB91"
        bgColorSub = "#FFAB91"

        # Store Window layout
        self.retrieveWindow = Toplevel()
        self.retrieveWindow.title("RETRIEVE")
        self.retrieveWindow.geometry("500x200+400+150")

        # Frames
        mainFrame = Frame(self.retrieveWindow, bg=bgColorMain)
        mainFrame.pack(fill=BOTH, expand=True)
        mainFrame.pack()
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False, pady=5)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=20)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT, fill="none", expand=False, padx=5)
        entryFrame = Frame(upperFrame, bg=bgColorMain)
        entryFrame.pack(side=RIGHT, fill="none", expand=False, padx=5)
        buttonFrame = Frame(mainFrame, bg=bgColorMain, pady=20)
        buttonFrame.pack(side=BOTTOM, fill="none", expand=False)

        # Labels
        times = tkFont.Font(family="TimesNewRoman", size=16)
        nickNameLabel = Label(labelFrame, text= "Nickname:", bg=bgColorMain, font=times)
        nickNameLabel.pack(side=TOP, fill=BOTH, pady=10)

        # Entry boxes
        nickNameEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#FFFFFF")
        nickNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        nickNameEntry.configure(highlightbackground=bgColorSub)

        # Buttons
        backButton = Button(buttonFrame, text="Back", bg=bgColorSub, height="2", width="10")
        backButton.pack(side=LEFT, padx=10)
        addButton = Button(buttonFrame, text="Add", height="2", width="10")
        addButton.pack(side=RIGHT, padx=10)

        # Close window using x button
        self.storeWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("self.retrieveWindow"))
        self.storeWindow.mainloop()

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
        filemenu.add_command(label="Exit", command=lambda: self.closeWindow("self.loginWindow"))

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

        # Close window using x button
        self.settingsWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("self.settingsWindow"))
        self.settingsWindow.mainloop()


start = VaultApp()
start.Login()
