from tkinter import *
from functools import partial
import Users


def validateLogin(username, password, points):
    print("username entered :", username.get())
    print("password entered :", password.get())
    print("points entered :", points.get())
    return


# window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form - pythonexamples.org')

# username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

# points
pointsLabel = Label(tkWindow, text="Points").grid(row=2, column=0)
points = StringVar()
pointsEntry = Entry(tkWindow, textvariable=points).grid(row=2, column=1)

validateLogin = partial(validateLogin, username, password, points)

# login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()
