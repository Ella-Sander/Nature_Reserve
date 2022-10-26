import Users
from tkinter import *
from functools import partial

def get_user_name(username, password):
    while validateLogin(username, password) == "Login fail":
        username = input("Enter username: ")
        password = input("Enter password: ")
    return username

USER_NAME = ""
PASSWORD = ""

def validateLogin(username, password):
    user1 = username.get()
    password1 = password.get()
    exists = Users.user_name_taken(user1)
    if not exists:
        Users.add_new_user(user1, password1)
        USER_NAME = user1
        print("Sign up success")
        Users.update_users_csv()
        tkWindow.quit()

    else:
        if Users.check_user_and_password(user1, password1):
            print("Login success")
            USER_NAME = user1
            tkWindow.quit()
        else:
            print("Login fail")
            return "Login fail"



#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()
