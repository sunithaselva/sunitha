
# python
# 1234
# \
# def login_success():
	# match
	  # message box
      
from tkinter import *
import tkinter.messagebox as tm
import pandas
import os

import pyodbc
# DATABASE##
db =pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\Users\User\Documents\atmData.mdb')
cur=db.cursor()
def show(uservalue,userpass):
     cur.execute("SELECT username,pass FROM atmdata1")
     myresult = cur.fetchall()
##     print(myresult)
     for i in range(len(myresult)):
          
          if(uservalue in myresult[i] ):
##              print(myresult[i])
              if (uservalue in myresult[i][0] and userpass in myresult[i][1]):
                   print("login sucess")
              else:
                   print("login unsucessful")
              
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)
        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()
        
    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        # print(username, password)

        show(username,password)


root = Tk()
lf = LoginFrame(root)
root.mainloop()
