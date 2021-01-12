from tkinter import*
from functools import  partial
import  tkinter as tk
import  time
def validateLogin(username, password):
	print("username entered :", username)
	print("password entered :", password)




def Login_test():
    LoginScreen =Tk()
    LoginScreen.title("Login")
    LoginScreen.geometry("300x300")
    bolean=False
    if(bolean == False):
        Label(LoginScreen, text="User Name").grid(row=0, column=0)
        username = tk.StringVar()
        Entry(LoginScreen, textvariable=username).grid(row=0, column=1)

        Label(LoginScreen, text="Password").grid(row=1, column=0)
        password =tk.StringVar()
        Entry(LoginScreen, textvariable=password, show='*').grid(row=1, column=1)
    else:
        print("Enter the values in Entry box")
    if (username.get() == "" and password.get() == ""):
        bolean = True
    if(bolean==True):
        #validateLogin = partial(validateLogin, username, password)
        Button(LoginScreen, text="Loginto", command=validateLogin(username.get(),password.get())).grid(row=4, column=0)

    print("******")
def register_test():
    register_screen =Tk()
    register_screen.title("Register")
    register_screen.geometry("500x500")
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter your details", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue").pack()
    print("******")




if __name__=="__main__":
    userCred={}
    #*************************#
    tkwindow=Tk()
    tkwindow.geometry("350x300")
    tkwindow.title("ATM")

    Label(tkwindow, text="User Name").grid(row=0, column=0)
    username = tk.StringVar()
    Entry(tkwindow, textvariable=username).grid(row=0, column=1)

    Label(tkwindow, text="Password").grid(row=1, column=0)
    password = tk.StringVar()
    Entry(tkwindow, textvariable=password, show='*').grid(row=1, column=1)




    Login =tk.Button(tkwindow, text="Login",bg="blue", width="30", height="2", font=("Calibri", 13))
    # Login.pack()

    Login.grid(row=0, column=1, padx=40, pady=20)
    # btn=tk.Button(tkwindow,text="Register",bg="blue", width="30", height="2", font=("Calibri", 13), command=register_test)
    # btn.grid(row=3, column=1, padx=40, pady=40)
    tkwindow.mainloop()

