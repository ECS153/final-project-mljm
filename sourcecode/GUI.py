import tkinter.font as tkFont
import tkinter
from tkinter import *
from tkinter import Text
from handler import *
from smtpCtrl import *
from PIL import Image, ImageTk

class VaultApp():

    def __init__(self):
        # Main Window layout
        self.handler = Handler()
        self.currUser = None
        self.smtp = None
        self.resetCode = None
        self.loginWindow = tkinter.Tk()
        self.loginError = None
        self.welcomeWindow = None
        self.registerWindow = None
        self.settingsWindow = None
        self.resetWindow = None
        self.secresetWindow = None
        self.storeWindow = None
        self.retrieveWindow = None

    def openWindow(self, winType, msg=""):
        win = "self."+winType+"Window"
        if msg == "":
            func = "self."+winType.capitalize()+"()"
        else:
            func = "self."+winType.capitalize()+"(\""+msg+"\")"
        if (eval(win)==None):
            exec(func)
        else:
            pass

    def closeWindow(self, winType):
        win = "self."+winType+"Window"
        if (win == "self.loginWindow") and (self.welcomeWindow != None):
            self.cascadeDestroy()
        if (win == "self.loginWindow") and (self.registerWindow != None):
            self.registerWindow.destroy()
        if (win == "self.loginWindow") and (self.resetWindow != None):
            self.resetCascadeDestroy()
        if win == "self.loginWindow":
            self.currUser = None
            self.handler.closeDB()
        exec(win +".destroy()")
        exec(win+" = None")

    def cascadeDestroy(self):
        self.currUser = None
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
        if(self.retrieveWindow == None):
            pass
        else:
            self.retrieveWindow.destroy()
            self.retrieveWindow = None
        if(self.resetWindow == None):
            pass
        else:
            self.resetWindow.destroy()
            self.resetWindow = None
    
    def resetCascadeDestroy(self):
        self.currUser = None
        self.resetWindow.destroy()
        self.resetWindow = None
        if(self.secresetWindow == None):
            pass
        else:
            self.secresetWindow.destroy()
            self.secresetWindow = None

    def login(self, aName, mPass, erro):
        name = aName.get()
        pas = mPass.get()
        if (not name) or (not pas):
            erro.set("Enter an Account Name and Password")
        else:
            rtn = self.handler.login(name, pas)
            if isinstance(rtn, bool):
                if self.welcomeWindow != None:
                    self.cascadeDestroy()
                self.currUser = name
                aName.set("")
                mPass.set("")
                self.loginError.set("")
                self.openWindow("welcome", "Welcome To The Vault")
            else:
                erro.set(rtn)

    def reg(self, aName, mPass, email, phone, prov, erro):
        if (not aName) or (not mPass) or (not email) or (not phone) or (prov == "Select Phone Provider"):
            erro.set("Please Fill In All Required Fields")
        else:
            rtn = self.handler.signUp(aName, mPass, email, phone, prov)
            if isinstance(rtn, bool):
                self.currUser = aName
                self.handler.login(aName, mPass)
                self.closeWindow("register")
                self.openWindow("welcome", "Congratulations! Registration Complete!")
            else:
                erro.set(rtn)
    
    def getNewCode(self, user, byway):
        if byway == 'phone':
            phoneInfo = self.handler.getPhone(user)
            if isinstance(phoneInfo, str):
                return phoneInfo
            else:
                self.smtp = SMTPctrl()
                self.resetCode = self.smtp.sendSMS(phoneInfo[0], self.currUser, phoneInfo[1])
                return True
        else:    
            email = self.handler.getEmail(user)
            if str(email).find('@') < 0:
                return email
            else:
                self.smtp = SMTPctrl()
                self.resetCode = self.smtp.sendMail(email, self.currUser)
                return True
            
    def startPassReset(self, user, byway, erro):
        if len(user) < 4:
            erro.set("Invalid Username")
        else:
            self.currUser = user
            rtn = self.getNewCode(user, byway)
            if isinstance(rtn, bool):
                self.resetWindow.destroy()
                self.resetWindow=None
                self.secresetWindow = self.Secreset()
            else:
                erro.set(rtn)

    def resetPass(self, newpass, erro, code=None):
        if code == None:
            self.handler.resetPass(self.currUser, newpass)
            erro.set("Password has been reset!")
        else:    
            if code != self.resetCode:
                erro.set("Incorrect Reset Code")
            else:
                rtn = self.handler.resetPass(self.currUser, newpass)
                if rtn:
                    self.resetCode = None
                    self.secresetWindow.destroy()
                    self.secresetWindow = None
                    self.loginError.set("Password Reset!")
                else:
                    erro.set(rnt)

    def clearStore(self, tag, user, passw, erro):
        tag.set("")
        user.set("")
        passw.set("")
        erro.set("")

    def storeRec(self, tag, user, passw, erro):
        Tag, User, Passw = tag.get(), user.get(), passw.get()
        if (not Tag) or (not User) or (not Passw):
            erro.set("Please Fill All Required Fields")
            return
        else:
            rtn=self.handler.store(Tag,User,Passw)
            if isinstance(rtn, bool):
                tag.set("")
                user.set("")
                passw.set("")
                erro.set("Record Successfully Stored!")
            else:
                erro.set(rtn)

    def clearRet(self, tag, record, erro):
        tag.set("")
        record.delete('1.0', '5.0')
        erro.set("")

    def returnRet(self, tag, record, erro):
        if (not tag):
            erro.set("Please Enter a Nickname")
        else:
            rtn=self.handler.request(tag)
            if isinstance(rtn, str):
                erro.set(rtn)
            else:
                user=rtn[0]
                passw=rtn[1]
                rec = '\n' +str(user)+ '\n\n' +str(passw)
                record.insert('2.0', rec)

    def Login(self):
        bgColorMain = "#4CA7B2"
        bgColorSub = "#4697A1"

        # Login Window layout
        self.loginWindow.title('THE VAULT')
        self.loginWindow.geometry("650x300+800+300")
        self.loginWindow.configure(bg=bgColorMain)

        # Frames for Login window
        mainFrame = Frame(self.loginWindow, bg=bgColorMain)
        mainFrame.pack(fill="none", expand=True)
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=10)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT)
        entryFrame = Frame(upperFrame, bg=bgColorMain)
        entryFrame.pack(side=RIGHT)
        lowerFrame = Frame(mainFrame, bg=bgColorMain)
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False)
        buttonFrame = Frame(mainFrame, bg=bgColorMain)
        buttonFrame.pack(side=TOP, fill="none", expand=False)

        # Labels
        err = tkFont.Font(family="TimesNewRoman", size=18)
        self.loginError = tkinter.StringVar()
        self.loginError.set("")
        errorLabel = Label(errorFrame, textvariable=self.loginError, bg=bgColorMain, fg="#E8E8E8", font=err )
        errorLabel.pack()
        times = tkFont.Font(family="TimesNewRoman", size=18)
        accountNameLabel = Label(labelFrame, text="Account Name:", bg=bgColorMain, font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Master Password:", bg=bgColorMain, font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes
        large_font = ('times',16)
        nameText = tkinter.StringVar()
        nameText.set("")
        accountNameEntry = Entry(entryFrame, textvariable=nameText, font=large_font, bd=4, bg=bgColorSub, fg="#FFFFFF")
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        accountNameEntry.configure(highlightbackground=bgColorSub)
        passText = tkinter.StringVar()
        passText.set("")
        masterPasswordEntry = Entry(entryFrame, textvariable=passText, font=large_font, bd=4, bg=bgColorSub, show='*', fg="#FFFFFF")
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)
        masterPasswordEntry.configure(highlightbackground= bgColorSub)

        # Login button
        large_font = ('times',16)
        loginButton = tkinter.Button(buttonFrame, text="Login", font=large_font, height=1, width=6,
                      command=lambda: self.login(nameText,passText, self.loginError))
        loginButton.pack(side=LEFT, expand=YES, pady=5, padx=5)
        loginButton.configure(relief=RAISED)

        # Register button
        registerButton = tkinter.Button(buttonFrame, text="Register", font=large_font, height=1, width=8,
                      command= lambda: self.openWindow("register"))
        registerButton.pack(side=RIGHT, expand=YES, pady=5, padx=5)
        registerButton.configure(relief=RAISED)

        # Link to reset the user's Account Name and Password
        link = Label(lowerFrame, text="Forgot Master Password?", bg=bgColorMain, fg="blue", cursor="arrow")
        link.pack(side=BOTTOM, expand=YES)
        link.bind("<Button-1>", lambda r: self.openWindow("reset"))

        self.loginWindow.bind('<Return>', lambda event=None: loginButton.invoke())
        # Closes window using x button
        self.loginWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("login"))
        self.loginWindow.mainloop()

    def Welcome(self, msg=""):
        bgColorMain = "#dfbb3b"
        bgColorSub = "#765EEF"

        imgDat = Image.open("vault.jpg")
        img = ImageTk.PhotoImage(imgDat)


        # Welcome window layout
        self.welcomeWindow = Toplevel()
        self.welcomeWindow.title('WELCOME')
        self.welcomeWindow.geometry("1000x600+750+250")

        # Menu bar
        menu_bar = Menu(self.welcomeWindow)
        self.welcomeWindow.config(menu=menu_bar, bg=bgColorMain)

        # File drop down menu
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Settings option
        filemenu.add_command(label="Settings", command=lambda: self.openWindow("settings"))
        filemenu.add_separator()
        # Closes welcome window
        filemenu.add_command(label="Log Out", command=self.cascadeDestroy)
        # Exits out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWindow("login"))

        # Action drop down menu
        actionMenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Action", menu=actionMenu)
        # Store should take you to a window to store passwords
        actionMenu.add_command(label="Store", command=lambda: self.openWindow("store"))
        # Retrieve should take you to window that retrieves password
        actionMenu.add_command(label="Retrieve", command=lambda: self.openWindow("retrieve"))

        # Window frames
        mainFrame = Frame(self.welcomeWindow, bg=bgColorMain)
        mainFrame.pack(fill="none", expand=True)
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False, pady=10)
        buttonFrame = Frame(mainFrame, bg=bgColorMain)
        buttonFrame.pack(side=TOP, fill="none", expand=True, pady=10)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=TOP, fill="none", expand=False)

        # Labels
        times = tkFont.Font(family="TimesNewRoman", size=40, weight='bold')
        welcomeLabel = Label(mainFrame, image=img)
        welcomeLabel.pack(side=TOP, fill=BOTH)
        err = tkFont.Font(family="TimesNewRoman", size=30)
        errorText = tkinter.StringVar()
        errorText.set(msg)
        errorLabel = Label(errorFrame, textvariable=errorText, bg=bgColorMain, fg="#333333", font=err)
        errorLabel.pack(side=TOP, fill=BOTH, pady=10)

        # Retrieve button
        large_font = ('times',18)
        retrieveButton = Button(buttonFrame, text="Retrieve", font=large_font, height="2", width="10", command=lambda: self.openWindow("retrieve"))
        retrieveButton.pack(side=LEFT, padx=10)
        retrieveButton.configure(relief=RAISED, state=NORMAL)

        # Store button
        large_font = ('times',18)
        storeButton = Button(buttonFrame, text="Store", font=large_font, height="2", width="10", command=lambda: self.openWindow("store"))
        storeButton.pack(side=RIGHT, padx=10)
        storeButton.configure(relief=RAISED, state=NORMAL)

        # Closes window using x button
        self.welcomeWindow.protocol("WM_DELETE_WINDOW", self.cascadeDestroy)
        self.welcomeWindow.mainloop()

    def Register(self):
        bgColorMain = "#00BF00"
        bgColorSub = "#009E00"

        # Register window layout
        self.registerWindow = Toplevel()
        self.registerWindow.title('REGISTER')
        self.registerWindow.geometry("550x450+750+250")

        # Menu bar
        menu_bar = Menu(self.registerWindow)
        self.registerWindow.config(menu=menu_bar, bg=bgColorMain)

        # File drop down menu
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Registers information
        filemenu.add_command(label="Register", command=lambda: self.openWindow("register"))
        filemenu.add_separator()
        # Closes welcome window
        filemenu.add_command(label="Close", command=lambda: self.closeWindow("register"))
        # Exits out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWindow("login"))

        # Window frames
        mainFrame = Frame(self.registerWindow, bg=bgColorMain)
        mainFrame.pack(fill="none", expand=True)
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False, pady=5)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=20)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT, fill="none", expand=False, padx=20)
        entryFrame = Frame(upperFrame, bg=bgColorMain)
        entryFrame.pack(side=RIGHT, fill="none", expand=False, padx=15)
        buttonFrame = Frame(mainFrame, bg=bgColorMain, pady=20)
        buttonFrame.pack(side=BOTTOM, fill="none", expand=False)

        # Labels
        err = tkFont.Font(family="TimesNewRoman", size=18)
        errorText = tkinter.StringVar()
        errorText.set("")
        errorLabel = Label(errorFrame, textvariable=errorText, bg=bgColorMain, fg="#E8E8E8", font=err )
        errorLabel.pack(side=TOP, fill=BOTH, pady=10)

        labelpad = 9
        times = tkFont.Font(family="TimesNewRoman", size=18)
        userNameLabel = Label(labelFrame, text="User Name:", bg=bgColorMain, font=times)
        userNameLabel.pack(side=TOP, fill=BOTH, pady=labelpad)
        PasswordLabel = Label(labelFrame, text="Password:", bg=bgColorMain, font=times)
        PasswordLabel.pack(side=TOP, fill=BOTH, pady=labelpad)
        emailLabel = Label(labelFrame, text="Email Address:", bg=bgColorMain, font=times)
        emailLabel.pack(side=TOP, fill=BOTH, pady=labelpad)
        phoneLabel = Label(labelFrame, text="Phone Number:", bg=bgColorMain, font=times)
        phoneLabel.pack(side=TOP, fill=BOTH, pady=labelpad)
        providerLabel = Label(labelFrame, text="Provider:", bg=bgColorMain, font=times)
        providerLabel.pack(side=TOP, fill=BOTH, pady=labelpad)

        entrypad = 13
        # User information entry boxes
        userNameEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#FFFFFF", width=30)
        userNameEntry.pack(side=TOP, fill=BOTH, pady=entrypad)
        userNameEntry.configure(highlightbackground=bgColorSub)
        passwordEntry = Entry(entryFrame, bd=4, bg=bgColorSub, show='*', fg="#FFFFFF", width=30)
        passwordEntry.pack(side=TOP, fill=BOTH, pady=entrypad)
        passwordEntry.configure(highlightbackground= bgColorSub)
        emailEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#FFFFFF", width=30)
        emailEntry.pack(side=TOP, fill=BOTH, pady=entrypad)
        emailEntry.configure(highlightbackground=bgColorSub)
        phoneEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#FFFFFF", width=30)
        phoneEntry.pack(side=TOP, fill=BOTH, pady=entrypad)
        phoneEntry.configure(highlightbackground=bgColorSub)

        providerText = tkinter.StringVar()
        providerText.set("Select Phone Provider")
        providerEntry = Menubutton(entryFrame, textvariable=providerText, relief=FLAT)
        providerEntry.pack(side=TOP, fill=BOTH, pady=entrypad)
        providerEntry.menu = Menu(providerEntry, tearoff=0)
        providerEntry["menu"] = providerEntry.menu
        providerEntry.menu.add_checkbutton(label="AT&T", variable=IntVar(), command= lambda: providerText.set("AT&T"))
        providerEntry.menu.add_checkbutton(label="Sprint", variable=IntVar(), command= lambda: providerText.set("Sprint"))
        providerEntry.menu.add_checkbutton(label="TMobile", variable=IntVar(), command= lambda: providerText.set("TMobile"))
        providerEntry.menu.add_checkbutton(label="Verizon", variable=IntVar(), command= lambda: providerText.set("Verizon"))
        providerEntry.menu.add_checkbutton(label="Boost", variable=IntVar(), command= lambda: providerText.set("Boost"))
        providerEntry.menu.add_checkbutton(label="Cricket", variable=IntVar(), command= lambda: providerText.set("Cricket"))
        providerEntry.menu.add_checkbutton(label="MetroPCS", variable=IntVar(), command= lambda: providerText.set("MetroPCS"))
        providerEntry.menu.add_checkbutton(label="Virgin Mobile", variable=IntVar(), command= lambda: providerText.set("Virgin Mobile"))

        # Register button
        registerButton = Button(buttonFrame, text="Register", height="2", width="10",
            command=lambda: self.reg(userNameEntry.get(),passwordEntry.get(),emailEntry.get(),phoneEntry.get(),providerText.get(),errorText))
        registerButton.pack(side=RIGHT, padx=10)
        registerButton.configure(relief=RAISED, state=NORMAL)

        # Cancel button
        cancelButton = Button(buttonFrame, text="Cancel", height="2", width="10", command=lambda: self.closeWindow("register"))
        cancelButton.pack(side=LEFT, padx=10)
        cancelButton.configure(relief=RAISED, state=NORMAL)

        self.registerWindow.bind('<Return>', lambda event=None: registerButton.invoke())
        # Closes window using x button
        self.registerWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("register"))
        self.registerWindow.mainloop()

    def Reset(self):
        bgColorMain = "#F2D98C"
        bgColorSub = "#FFF176"

        # Reset Window layout
        self.resetWindow = Toplevel()
        self.resetWindow.title('RESET')
        self.resetWindow.geometry("450x300+800+300")

        # Menu bar
        menu_bar = Menu(self.resetWindow)
        self.resetWindow.config(menu=menu_bar, bg=bgColorMain)

        # File drop down menu
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)

        # Closes welcome window
        filemenu.add_command(label="Close", command=self.resetCascadeDestroy)
        # Exits out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWindow("login"))

        # Window frames
        mainFrame = Frame(self.resetWindow, bg=bgColorMain)
        mainFrame.pack(fill="none", expand=True)
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False, pady=10)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=10)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT)
        entryFrame = Frame(upperFrame, bg=bgColorMain)
        entryFrame.pack(side=RIGHT)
        buttonFrame = Frame(mainFrame, bg=bgColorMain, pady=5)
        buttonFrame.pack(side=BOTTOM, fill="none", expand=False, pady=5)

        err = tkFont.Font(family="TimesNewRoman", size=18)
        errorText = tkinter.StringVar()
        errorText.set("")
        errorLabel = Label(errorFrame, textvariable=errorText, bg=bgColorMain, fg="#333333", font=err )
        errorLabel.pack(side=TOP, fill=BOTH, pady=10)

        # Label for entry box
        times = tkFont.Font(family="TimesNewRoman", size=18)
        accountNameLabel = Label(labelFrame, text="Account Name:", font=times, bg=bgColorMain)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)

        # Account name entry box
        large_font = ('times',17)
        accountNameEntry = Entry(entryFrame, font=large_font, bd=5, bg=bgColorMain)
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        accountNameEntry.configure(highlightbackground=bgColorMain)

        # Enter button
        emailButton = tkinter.Button(buttonFrame, text="Reset via Email", height="2", width="14", 
            command=lambda: self.startPassReset(accountNameEntry.get(),'email', errorText))
        emailButton.pack(side=RIGHT, expand=YES, pady=5, padx=5)


        phoneButton = tkinter.Button(buttonFrame, text="Reset via SMS", height="2", width="14", 
            command=lambda: self.startPassReset(accountNameEntry.get(),'phone', errorText))
        phoneButton.pack(side=RIGHT, expand=YES, pady=5, padx=5)


        # Cancel button
        cancelButton = Button(buttonFrame, text="Cancel", height="2", width="8", 
            command=lambda: self.closeWindow("reset"))
        cancelButton.pack(side=LEFT, pady=5, padx=5)

        # Closes window using x button
        self.resetWindow.protocol("WM_DELETE_WINDOW", self.resetCascadeDestroy)
        self.resetWindow.mainloop()

    def Secreset(self):
        bgColorMain = "#FFF9C4"
        bgColorSub = "#FFF176"

        # Reset Window layout
        self.secresetWindow = Toplevel()
        self.secresetWindow.title('RESET')
        self.secresetWindow.geometry("500x350+800+300")

        # Menu bar
        menu_bar = Menu(self.secresetWindow)
        self.secresetWindow.config(menu=menu_bar, bg=bgColorMain)

        # File drop down menu
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)

        filemenu.add_command(label="Send New Code")
        # Closes welcome window
        filemenu.add_command(label="Close", command=lambda: self.closeWindow("reset"))
        # Exits out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWindow("login"))

        # Window frames
        mainFrame = Frame(self.secresetWindow, bg=bgColorMain)
        mainFrame.pack(fill="none", expand=True)
        mainFrame.pack()
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=10)
        lowerFrame = Frame(mainFrame, bg=bgColorMain)
        lowerFrame.pack(side=TOP, fill="none", expand=False, pady=5)    
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT)
        boxFrame = Frame(upperFrame, bg=bgColorMain)
        boxFrame.pack(side=RIGHT)

        # Labels
        err = tkFont.Font(family="TimesNewRoman", size=18)
        errorText = tkinter.StringVar()
        errorText.set("")
        errorLabel = Label(errorFrame, textvariable=errorText, bg=bgColorMain, fg="#333333", font=err )
        errorLabel.pack(side=TOP, fill=BOTH, pady=10)
        times = tkFont.Font(family="TimesNewRoman", size=16)
        codeLabel = Label(labelFrame, text="Enter Reset Code:", font=times, bg=bgColorMain)
        codeLabel.pack(side=TOP, fill=BOTH, pady=5)
        newpassLabel = Label(labelFrame, text="Enter New Password:", font=times, bg=bgColorMain)
        newpassLabel.pack(side=TOP, fill=BOTH, pady=5)

        # Account name entry box
        codeEntry = Entry(boxFrame, bd=5, bg=bgColorMain, width=30)
        codeEntry.pack(side=TOP, fill=BOTH, pady=5)
        codeEntry.configure(highlightbackground=bgColorMain)
        newpassEntry = Entry(boxFrame, bd=5, bg=bgColorMain, width=30)
        newpassEntry.pack(side=TOP, fill=BOTH, pady=5)
        newpassEntry.configure(highlightbackground=bgColorMain)

        # Enter button
        getnewButton = tkinter.Button(lowerFrame, text="Get New Code", height="2", width="15", command=lambda: self.getNewCode(self.user))
        getnewButton.pack(side=LEFT, expand=YES, pady=5, padx=10)

        resetButton = tkinter.Button(lowerFrame, text="Reset Password", height="2", width="15", command=lambda: self.resetPass(newpassEntry.get(),errorText,codeEntry.get()))
        resetButton.pack(side=RIGHT, expand=YES, pady=5, padx=10)


        # Closes window using x button
        self.secresetWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("secreset"))
        self.secresetWindow.mainloop()

    def Store(self):
        bgColorMain = "#89BFF5"
        bgColorSub = "#8FBFEF"

        # Store Window layout
        self.storeWindow = Toplevel()
        self.storeWindow.title("STORE")
        self.storeWindow.geometry("500x400+800+300")

        # Window frames
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
        err = tkFont.Font(family="TimesNewRoman", size=18)
        errorText = tkinter.StringVar()
        errorText.set("")
        errorLabel = Label(errorFrame, textvariable=errorText, bg=bgColorMain, fg="#E8E8E8", font=err )
        errorLabel.pack(side=TOP, fill=BOTH, pady=10)
        times = tkFont.Font(family="TimesNewRoman", size=16)
        nickNameLabel = Label(labelFrame, text="Nickname:", bg=bgColorMain, font=times)
        nickNameLabel.pack(side=TOP, fill=BOTH, pady=10)
        userNameLabel = Label(labelFrame, text="Username:", bg=bgColorMain, font=times)
        userNameLabel.pack(side=TOP, fill=BOTH, pady=10)
        PasswordLabel = Label(labelFrame, text="Password:", bg=bgColorMain, font=times)
        PasswordLabel.pack(side=TOP, fill=BOTH, pady=10)

        # Entry boxes
        nickNameText = tkinter.StringVar()
        nickNameText.set("")
        nickNameEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#000000", textvariable=nickNameText)
        nickNameEntry.pack(side=TOP, fill=BOTH, pady=10)
        nickNameEntry.configure(highlightbackground=bgColorSub)
        userNameText = tkinter.StringVar()
        userNameText.set("")
        userNameEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#000000", textvariable=userNameText)
        userNameEntry.pack(side=TOP, fill=BOTH, pady=10)
        userNameEntry.configure(highlightbackground=bgColorSub)
        passwordText = tkinter.StringVar()
        passwordText.set("")
        passwordEntry = Entry(entryFrame, bd=4, bg=bgColorSub, show='*', fg="#000000", textvariable=passwordText)
        passwordEntry.pack(side=TOP, fill=BOTH, pady=10)
        passwordEntry.configure(highlightbackground= bgColorSub)

         # Cancel button
        cancelbutton = Button(buttonFrame, text="Cancel", height="2", width="10",
            command=lambda: self.closeWindow("store"))
        cancelbutton.configure(state=NORMAL)
        cancelbutton.pack(side=LEFT, padx=10)

         # Clear button
        clearbutton = Button(buttonFrame, text="Clear", height="2", width="10",
            command=lambda: self.clearStore(nickNameText,userNameText,passwordText,errorText))
        clearbutton.configure(state=NORMAL)
        clearbutton.pack(side=LEFT, padx=10)

        # Store button
        storebutton = Button(buttonFrame, text="Store", height="2", width="10",
            command=lambda: self.storeRec(nickNameText,userNameText,passwordText, errorText))
        storebutton.configure(state=NORMAL)
        storebutton.pack(side=RIGHT, padx=10)

        self.storeWindow.bind('<Return>', lambda event=None: storebutton.invoke())
        # Closes window using x button
        self.storeWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("store"))
        self.storeWindow.mainloop()

    def Retrieve(self):
        bgColorMain = "#FFAB91"
        bgColorSub = "#FFAB91"

        # Store Window layout
        self.retrieveWindow = Toplevel()
        self.retrieveWindow.title("RETRIEVE")
        self.retrieveWindow.geometry("500x400+800+300")

        # Frames
        mainFrame = Frame(self.retrieveWindow, bg=bgColorMain)
        mainFrame.pack(fill=BOTH, expand=True)
        mainFrame.pack()
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False, pady=5)
        upperFrame = Frame(mainFrame, bg=bgColorMain)
        upperFrame.pack(side=TOP, fill="none", expand=False, pady=20)
        labelFrame = Frame(upperFrame, bg=bgColorMain)
        labelFrame.pack(side=LEFT, fill="none", expand=False, padx=5, pady=40)
        entryFrame = Frame(upperFrame, bg=bgColorMain)
        entryFrame.pack(side=RIGHT, fill="none", expand=False, padx=5)
        buttonFrame = Frame(mainFrame, bg=bgColorMain, pady=20)
        buttonFrame.pack(side=TOP, fill="none", expand=False)

        # Labels
        err = tkFont.Font(family="TimesNewRoman", size=18)
        errorText = tkinter.StringVar()
        errorText.set("")
        errorLabel = Label(errorFrame, textvariable=errorText, bg=bgColorMain, fg="#E8E8E8", font=err)
        errorLabel.pack(side=TOP, fill=BOTH, pady=10)
        times = tkFont.Font(family="TimesNewRoman", size=16)
        nickNameLabel = Label(labelFrame, text= "Nickname:", bg=bgColorMain, font=times)
        nickNameLabel.pack(side=TOP, fill="none", pady=20)
        recordLabel = Label(labelFrame, text= "Record:", bg=bgColorMain, font=times)
        recordLabel.pack(side=TOP, fill="none", pady=20)

        # Entry boxes
        nickNameText = tkinter.StringVar()
        nickNameText.set("")
        nickNameEntry = Entry(entryFrame, bd=4, bg=bgColorSub, fg="#000000", textvariable=nickNameText)
        nickNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        nickNameEntry.configure(highlightbackground=bgColorSub)

        recordScroll = Scrollbar(entryFrame)
        recordEntry = Text(entryFrame, bd=4, bg=bgColorSub, fg="#000000", state=NORMAL, wrap="word", height=10, width=40)
        recordEntry.pack(side=TOP, fill="none", pady=5)
        recordScroll.config(command=recordEntry.yview)
        recordEntry.config(yscrollcommand=recordScroll.set)

        # Cancel button
        cancelbutton = Button(buttonFrame, text="Cancel", height="2", width="10",
            command=lambda: self.closeWindow("retrieve"))
        cancelbutton.configure(state=NORMAL)
        cancelbutton.pack(side=LEFT, padx=10)

        # Clear button
        clearbutton = Button(buttonFrame, text="Clear", height="2", width="10",
            command=lambda: self.clearRet(nickNameText, recordEntry, errorText))
        clearbutton.configure(state=NORMAL)
        clearbutton.pack(side=LEFT, padx=10)

        # Retrieve button
        retrieveButton = Button(buttonFrame, text="Retrieve", height="2", width="10",
            command=lambda: self.returnRet(nickNameText.get(),recordEntry,errorText))
        retrieveButton.pack(side=LEFT, padx=10)
        retrieveButton.configure(state=NORMAL)

        self.retrieveWindow.bind('<Return>', lambda event=None: retrieveButton.invoke())
        # Closes window using x button
        self.retrieveWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("retrieve"))
        self.retrieveWindow.mainloop()


    def Settings(self):
        bgColorMain = "#B3DD88"
        bgColorSub = "#B3D98C"

        self.settingsWindow = Toplevel()
        self.settingsWindow.title('Settings')
        self.settingsWindow.geometry("580x550+770+270")
        framewidth = 50

        # Menu bar in settings window
        menu_bar = Menu(self.settingsWindow)
        self.settingsWindow.config(menu=menu_bar)

        # Creates a File drop down menu in settings window
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Closes settings window
        filemenu.add_command(label="Log Out", command=self.cascadeDestroy)
        # Exits out of whole app
        filemenu.add_command(label="Exit", command=lambda: self.closeWindow("login"))

        # Frames
        mainFrame = Frame(self.settingsWindow, bg=bgColorMain)
        mainFrame.pack(fill=BOTH, expand=True)
        errorFrame = Frame(mainFrame, bg=bgColorMain)
        errorFrame.pack(side=TOP, fill="none", expand=False)

        passFrame = LabelFrame(mainFrame, bg=bgColorMain)
        passFrame.pack(side=TOP, fill=BOTH, expand=True, ipady=15, ipadx=5)
        passbuttonFrame = Frame(passFrame, bg=bgColorMain)
        passbuttonFrame.pack(side=BOTTOM, fill="none", expand=True)

        emailFrame = LabelFrame(mainFrame, bg=bgColorMain)
        emailFrame.pack(side=TOP, fill=BOTH, expand=True, ipady=15, ipadx=5)
        mailbuttonFrame = Frame(emailFrame, bg=bgColorMain)
        mailbuttonFrame.pack(side=BOTTOM, fill="none", expand=True)

        phoneFrame = LabelFrame(mainFrame, bg=bgColorMain)
        phoneFrame.pack(side=TOP, fill=BOTH, expand=True, ipady=15, ipadx=5)
        phonebuttonFrame = Frame(phoneFrame, bg=bgColorMain)
        phonebuttonFrame.pack(side=BOTTOM, fill="none", expand=True)
        
        # Labels
        err = tkFont.Font(family="TimesNewRoman", size=18)
        errorText = tkinter.StringVar()
        errorText.set("")
        errorLabel = Label(errorFrame, textvariable=errorText, bg=bgColorMain, fg="#E8E8E8", font=err)
        errorLabel.pack(side=TOP, fill=BOTH, pady=10)

        times = tkFont.Font(family="TimesNewRoman", size=18)

        masterPasswordLabel = Label(passFrame, text="Enter new Master Password:", bg=bgColorMain, font=times)
        masterPasswordLabel.pack(side=LEFT, fill="none", expand=True, pady=5)

        newEmailLabel = Label(emailFrame, text="Enter New Email Address:", bg=bgColorMain, font=times)
        newEmailLabel.pack(side=LEFT, fill="none", expand=True, pady=5)

        phoneLabelFrame = Frame(phoneFrame, bg=bgColorMain)
        phoneLabelFrame.pack(side=LEFT, fill=BOTH, expand=True)
        phoneNumberLabel = Label(phoneLabelFrame, text="Enter New Phone Number:", bg=bgColorMain, font=times)
        phoneNumberLabel.pack(side=TOP, fill="none", pady=5)
        newProviderLabel = Label(phoneLabelFrame, text="Enter New Cell Provider:", bg=bgColorMain, font=times)
        newProviderLabel.pack(side=TOP, fill="none", pady=5)

        # Entry boxes
        mPassText = tkinter.StringVar()
        mPassText.set("")
        masterPasswordEntry = Entry(passFrame, bd=5, show='*', bg=bgColorSub, textvariable=mPassText, fg="#000000")
        masterPasswordEntry.configure(highlightbackground=bgColorSub)
        masterPasswordEntry.pack(side=RIGHT, fill="none", expand=True, pady=5)

        mailText = tkinter.StringVar()
        mailText.set("")
        newEmailEntry = Entry(emailFrame, bd=5, bg=bgColorSub, textvariable=mailText,fg="#000000")
        newEmailEntry.configure(highlightbackground=bgColorSub)
        newEmailEntry.pack(side=RIGHT, fill="none", expand=True, pady=5)

        numText = tkinter.StringVar()
        numText.set("")
        phoneEntryFrame = Frame(phoneFrame, bg=bgColorMain)
        phoneEntryFrame.pack(side=RIGHT, fill="none", expand=True)
        phoneNumberEntry = Entry(phoneEntryFrame, bd=5, bg=bgColorSub, textvariable=numText,fg="#000000")
        phoneNumberEntry.configure(highlightbackground=bgColorSub)
        phoneNumberEntry.pack(side=TOP, fill="none", expand=True, pady=5)
        providerText = tkinter.StringVar()
        providerText.set("Select Phone Provider")
        providerEntry = Menubutton(phoneEntryFrame, textvariable=providerText, relief=FLAT, width=20)
        providerEntry.pack(side=TOP, fill="none", expand=True, pady=5)
        providerEntry.menu = Menu(providerEntry, tearoff=0)
        providerEntry["menu"] = providerEntry.menu
        providerEntry.menu.add_checkbutton(label="AT&T", variable=IntVar(), command= lambda: providerText.set("AT&T"))
        providerEntry.menu.add_checkbutton(label="Sprint", variable=IntVar(), command= lambda: providerText.set("Sprint"))
        providerEntry.menu.add_checkbutton(label="TMobile", variable=IntVar(), command= lambda: providerText.set("TMobile"))
        providerEntry.menu.add_checkbutton(label="Verizon", variable=IntVar(), command= lambda: providerText.set("Verizon"))
        providerEntry.menu.add_checkbutton(label="Boost", variable=IntVar(), command= lambda: providerText.set("Boost"))
        providerEntry.menu.add_checkbutton(label="Cricket", variable=IntVar(), command= lambda: providerText.set("Cricket"))
        providerEntry.menu.add_checkbutton(label="MetroPCS", variable=IntVar(), command= lambda: providerText.set("MetroPCS"))
        providerEntry.menu.add_checkbutton(label="Virgin Mobile", variable=IntVar(), command= lambda: providerText.set("Virgin Mobile"))

        def changePass(npass, erro):  
            rtn = self.handler.resetPass(self.currUser, npass.get())
            if rtn:
                erro.set("Password Reset!")
            else:
                erro.set(rnt)
            npass.set("")

        def changeEmail(mail, erro):
            rtn = self.handler.resetEmail(mail.get())
            if rtn:
                erro.set("Email Reset!")
            else:
                erro.set(rnt)
            mail.set("")
        
        def changePhone(num, prov, erro):
            rtn = self.handler.resetPhone(num.get(), prov.get())
            if rtn:
                erro.set("Phone Information Reset!")
            else:
                erro.set(rnt)
            num.set("")
            prov.set("Select Phone Provider")

        # Change buttons
        changePasswordButton = tkinter.Button(passbuttonFrame, text="Change Password", height="1", width="15",
            command=lambda: changePass(mPassText,errorText))
        changePasswordButton.configure(relief=RAISED, state=NORMAL)
        changePasswordButton.pack(side=TOP, pady=5)

        changeEmailButton = tkinter.Button(mailbuttonFrame, text="Change Email", height="1", width="15",
            command=lambda: changeEmail(mailText,errorText))
        changeEmailButton.configure(relief=RAISED, state=NORMAL)
        changeEmailButton.pack(side=TOP, pady=5)

        changePhoneButton = tkinter.Button(phonebuttonFrame, text="Change Phone Info", height="1", width="15",
            command=lambda: changePhone(numText,providerText,errorText))
        changePhoneButton.configure(relief=RAISED, state=NORMAL)
        changePhoneButton.pack(side=TOP, pady=5)

        # Closes window using x button
        self.settingsWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow("settings"))
        self.settingsWindow.mainloop()


start = VaultApp()
start.Login()
