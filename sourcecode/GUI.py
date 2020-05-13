import Tkinter
import tkMessageBox
from Tkinter import *

# Window layout
window = Tkinter.Tk()
window.title('VAULT')
window.geometry("400x150+10+20")

# Labels for entries
UsernameLabel = Label(window, text = "Username:", font = ("TimesRoman", 14))
UsernameLabel.place(x=20, y=30)
PasswordLabel = Label(window, text = "Password:", font = ("TimesRoman", 14))
PasswordLabel.place(x=20, y=80)

# User and password entry boxes
UsernameEntry = Entry(window, bd = 5)
UsernameEntry.place(x=100, y=30)
PasswordEntry = Entry(window, bd = 5, show ='*')
PasswordEntry.place(x=100, y=80)

# Window that pops up after clicking login button
# This is where it will prompt user to either enter vault or deny access and try again
def welcome():
   tkMessageBox.showinfo( "Welcome to the Vault", "ACCESS ACCEPTED")

# Login button
LoginButton = Tkinter.Button(window, text ="Login", command = welcome)
LoginButton.pack(side = BOTTOM)

LoginButton.pack()
window.mainloop()
