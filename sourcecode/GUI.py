import tkinter.font as tkFont
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
# pip install pillow
from PIL import Image, ImageTk

class LoginWindow():

    def __init__(self):
        # Main Window layout
        self.MainWindow = tkinter.Tk()

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
        times = tkFont.Font(family="TimesNewRoman", size=14)
        accountNameLabel = Label(labelFrame, text="Account Name:", font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Master Password:", font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes
        accountNameEntry = Entry(boxFrame, bd=5)
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordEntry = Entry(boxFrame, bd=5, show='*')
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)

        # Login button
        loginButton = tkinter.Button(lowerFrame, text="Login", command=self.welcome)
        loginButton.pack(side=BOTTOM, expand=YES, pady=5)
        loginButton.pack()

        self.MainWindow.mainloop()


    # Create a settings window
    def Settings(self):
        settingsWindow = tkinter.Tk()
        settingsWindow.title('Settings')
        settingsWindow.geometry("700x700")

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

        # Labels for entries
        times = tkFont.Font(family="TimesNewRoman", size=14)
        accountNameLabel = Label(labelFrame, text="Enter new Account Name:", font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Enter new Master Password:", font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes
        accountNameEntry = Entry(boxFrame, bd=5)
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordEntry = Entry(boxFrame, bd=5, show='*')
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)

        # Login button
        enterButton = tkinter.Button(lowerFrame, text="Login")
        enterButton.pack(side=BOTTOM, expand=YES, pady=5)
        enterButton.pack()

        settingsWindow.mainloop()


    def welcome(self):

        # Welcome window layout
        welcomeWindow = tkinter.Tk()
        welcomeWindow.title('WELCOME')
        welcomeWindow.geometry("700x700")

        # Create a menu bar
        menu_bar = Menu(welcomeWindow)
        welcomeWindow.config(menu=menu_bar)
        filemenu = Menu(menu_bar)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Settings should take you to another window
        filemenu.add_command(label="Settings", command=self.Settings())
        #filemenu.add_cascade(label="Settings",menu= self.Settings())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=welcomeWindow.quit)

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

        # Create frame for buttons
        frame = Frame(welcomeWindow)
        frame.pack(fill="none", expand=True)

        # Retrieve button
        retrieveButton = Button(frame, text="Retrieve", height="2", width="10")
        retrieveButton.pack(side=LEFT, padx=2)

        # Store button
        storeButton = Button(frame, text="Store", height="2", width="10")
        storeButton.pack(side=RIGHT, padx=2)

        #welcomeWindow.mainloop()


start = LoginWindow()
start.FirstWindow()

