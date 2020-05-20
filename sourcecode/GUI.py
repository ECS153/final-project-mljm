import tkinter.font as tkFont
import tkinter
from tkinter import *
# pip install pillow
from PIL import Image, ImageTk

class VaultApp():

    def __init__(self):
        # Main Window layout
        self.MainWindow = tkinter.Tk()

    def LoginWindow(self):

        # Main Window layout
        self.MainWindow.title('THE VAULT')
        self.MainWindow.geometry("450x200+300+200")
        self.MainWindow.configure(bg="#66CC00")

        # Frames for the main login window
        mainFrame = Frame(self.MainWindow, bg="#66CC00")
        mainFrame.pack(fill="none", expand=True)
        upperFrame = Frame(mainFrame, bg="#66CC00")
        upperFrame.pack(side=TOP, fill="none", expand=False)
        lowerFrame = Frame(mainFrame, bg="#66CC00")
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False)
        labelFrame = Frame(upperFrame, bg="#66CC00")
        labelFrame.pack(side=LEFT)
        boxFrame = Frame(upperFrame, bg="#66CC00")
        boxFrame.pack(side=RIGHT)

        # Labels for entries for main login window
        times = tkFont.Font(family="TimesNewRoman", size=14)
        accountNameLabel = Label(labelFrame, text="Account Name:", bg="#66CC00", font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Master Password:", bg="#66CC00", font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes for main login window
        accountNameEntry = Entry(boxFrame, bd=5, bg="#3399FF")
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordEntry = Entry(boxFrame, bd=5, bg="#3399FF", show='*')
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)


        def Reset(self):

            # Reset Window layout
            ResetWindow = tkinter.Tk()
            ResetWindow.title('Settings')
            ResetWindow.geometry("700x700")

            # Reset Window frames
            mainFrame = Frame(ResetWindow)
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
            loginButton = tkinter.Button(lowerFrame, text="Login", command=self.welcome)
            loginButton.pack(side=BOTTOM, expand=YES, pady=20)
            loginButton.pack()

        # Login button in main login window
        loginButton = tkinter.Button(lowerFrame, text="Login", bg="#66CC00", height=1, width=6, command=self.welcome)
        loginButton.pack(side=TOP, expand=YES, pady=10)
        loginButton.pack()

        # Link to reset the user's Account Name and Password in main login window
        link = Label(lowerFrame, text="Forgot Master Password?", bg="#66CC00", fg="blue", cursor="arrow")
        link.pack(side=BOTTOM, expand=YES)
        link.bind("<Button-1>", Reset)

        self.MainWindow.mainloop()

    # Create a settings window
    def Settings(self):
        settingsWindow = tkinter.Tk()
        settingsWindow.title('Settings')
        settingsWindow.geometry("700x700")

        # Create a menu bar in settings window
        menu_bar = Menu(settingsWindow)
        settingsWindow.config(menu=menu_bar)

        # Create a File drop down menu in settings window
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Close settings window
        filemenu.add_command(label="Log Out", command=settingsWindow.destroy)
        # Exit out of whole app
        filemenu.add_command(label="Exit", command=settingsWindow.quit)

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
        enterButton = tkinter.Button(lowerFrame, text="Login")
        enterButton.pack(side=BOTTOM, expand=YES, pady=5)
        enterButton.pack()

        settingsWindow.mainloop()


    def welcome(self):
        # Welcome window layout
        welcomeWindow = tkinter.Tk()
        welcomeWindow.title('WELCOME')
        welcomeWindow.geometry("700x700+300+150")

        # Create a menu bar in welcome window
        menu_bar = Menu(welcomeWindow)
        welcomeWindow.config(menu=menu_bar, bg="#856ff8")

        # Create a File drop down menu in welcome window
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Settings should take you to another window
        filemenu.add_command(label="Settings", command=self.Settings)
        # Close welcome window
        filemenu.add_command(label="Log Out", command=welcomeWindow.destroy)
        # Exit out of whole app
        filemenu.add_command(label="Exit", command=welcomeWindow.quit)

        # Create an Action drop down menu in welcome window
        actionMenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Action", menu=actionMenu)
        # Store should take you to a window to store passwords
        actionMenu.add_command(label="Store")
        # Retrieve should take you to window that retrieves password
        actionMenu.add_command(label="Retrieve")

        # image = Image.open("vault.jpg")
        # #img_copy = image.copy()
        # background_image = self.ImageTk(image)
        # image_label = Label(welcomeWindow, image=background_image)
        # image_label.pack(fill=BOTH, expand=YES)

        # backgroundImage= tkinter.tk.PhotoImage("vault.jpg")
        # imageLabel= Label(welcomeWindow, image=backgroundImage)
        # imageLabel.pack()

        # v = Canvas(welcomeWindow, width=400, height=300)
        # v.pack(fill=BOTH, expand=True)
        # # img = PhotoImage(file='vault.jpg')
        # img= ImageTk.PhotoImage(Image.open("vault.jpg"))
        # v.create_image(20,20, image=img, anchor=NW)

        # imageFrame = Frame(welcomeWindow)
        # imageFrame.pack(fill=BOTH, expand=True)
        #
        # load = Image.open("vault.jpg")
        # photo = ImageTk.PhotoImage(load)
        # img = Label(self, image=photo)
        # img.image = photo
        # img.place(x=0, y=0)

        # Create frame for buttons in welcome window
        frame = Frame(welcomeWindow)
        frame.pack(fill="none", expand=True)

        # Retrieve button in welcome window
        retrieveButton = Button(frame, text="Retrieve", height="2", width="10")
        retrieveButton.pack(side=LEFT, padx=2)

        # Store button in welcome window
        storeButton = Button(frame, text="Store", height="2", width="10")
        storeButton.pack(side=RIGHT, padx=2)

        # welcomeWindow.mainloop()


start = VaultApp()
start.LoginWindow()

