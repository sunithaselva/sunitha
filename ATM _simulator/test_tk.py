
from tkinter import*

import pyodbc
global username_db
# DATABASE##
db =pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\Users\User\Documents\atmData.mdb')
cur=db.cursor()
cur.execute("SELECT username,Balance,Pass FROM atmdata1")
data=cur.fetchall()
print(data)
def updatetable(balance,Name):
    try:
        cur.execute("UPDATE atmdata1 SET Balance=? WHERE username=?",(balance,Name))
        db.commit()
        
    except Exception as e:
        print("update failed",e)
def getbalance(Name):
    try:
        cur.execute("SELECT Balance FROM atmdata1  WHERE username=?", ( Name))
        balancedata = cur.fetchone()
        return balancedata

    except Exception as e:
        print("update failed", e)



def updatepin(pin, Name):
    try:
        cur.execute("UPDATE atmdata1 SET pass=? WHERE username=?", (pin, Name))
        db.commit()

    except Exception as e:
        print("update failed", e)

class changepinFrame(Frame):
    def __init__(self, master,data):
        super().__init__(master)
        self.data=data
        self.oldpinLabel=Label(self,text="enter oldpin")
        self.oldpinLabel.grid(columnspan=2)
        self.oldpinentry = Entry(self)
        self.oldpinentry.grid(row=2, columnspan=4, sticky=W)
        self.newpinLabel = Label(self, text="enter newpin")
        self.newpinLabel.grid(columnspan=4)
        self.newpinEntry= Entry(self)
        self.newpinEntry.grid(row=4, columnspan=8, sticky=W)
        self.newpinconfLabel = Label(self, text="enter confnewpin")
        self.newpinconfLabel.grid(columnspan=6)
        self.newpinconfEntry = Entry(self)
        self.newpinconfEntry.grid(row=6, columnspan=12, sticky=W)
        self.submitButton=Button(self,text="submit",command=self.changepin,bg="pink",fg="purple")
        self.submitButton.grid(columnspan=4)
        self.pack()
    def changepin(self):
        cur.execute("SELECT pass FROM atmdata1  WHERE username=?", (self.data[0]))
        balancedata = cur.fetchone()
        oldpin=balancedata[0]
        oldpinentry = self.oldpinentry.get()
        if (oldpin==oldpinentry):
            print("changepin")
            newpinentry = self.newpinEntry.get()
            newpinconfentry = self.newpinconfEntry.get()
            if (newpinentry==newpinconfentry):
                updatepin(newpinentry,self.data[0])
            else:
                print("password not match")
        else:
            print("old pin not match")
        self.master.destroy()


class DepositFrame(Frame):
    def __init__(self, master,data):
        self.data=data
        super().__init__(master)
        self.depositLabel=Label(self,text="enter the amount")
        self.depositLabel.grid(columnspan=1)
        self.depositentry = Entry(self)
        self.depositentry.grid(row=2, columnspan=1, sticky=W)
        self.depositButton=Button(self,text="submit",command=self.deposit,bg="pink",fg="purple")
        self.depositButton.grid(columnspan=2)
        self.pack()
        
    def deposit(self):
        depositvalue= self.depositentry.get()
        w_balnce = getbalance(self.data[0])
        balance=int(w_balnce[0])+int(depositvalue)
        updatetable(balance,self.data[0])
        self.master.destroy()
        # root2.deiconify()   #makes the root window visible again

        
class WithdrawFrame(Frame):
    def __init__(self, master,data):
        self.data=data
        super().__init__(master)
        self.WithdrawButton=Button(self,text="1000",command=self.withdraw1000,bg="grey",fg="red")
        self.WithdrawButton.grid(row=0, columnspan=2, sticky=W)
        self.WithdrawButton=Button(self,text="500",command=self.withdraw500,bg="grey",fg="red")
        self.WithdrawButton.grid(row=1, columnspan=4, sticky=W)
        self.WithdrawButton=Button(self,text="100",command=self.withdraw100,bg="grey",fg="red")
        self.WithdrawButton.grid(row=2, columnspan=6, sticky=W)
        self.pack()
    def withdraw1000(self):
        w_balnce=getbalance(self.data[0])
        balance=int(w_balnce[0])-1000
        updatetable(balance,self.data[0])
        self.master.destroy()
    def withdraw500(self):
        w_balnce = getbalance(self.data[0])
        balance=int(w_balnce[0])-500
        updatetable(balance,self.data[0])
        self.master.destroy()
    def withdraw100(self):
        w_balnce = getbalance(self.data[0])
        balance=int(w_balnce[0])-100
        updatetable(balance,self.data[0])
        self.master.destroy()
        
        
class AccountFrame(Frame):
    def __init__(self, master,data):
        super().__init__(master)
        self.data=data
        self.mainLabel=Label(self,text="Welcome ", bg="yellow", fg="black", width=26,height=5,font="ariel,14,bold"+self.data[0])
        self.mainLabel.grid(columnspan=2, padx=5, pady=5,sticky="e")
        self.Viewbalancebtn = Button(self, text="Viewbalance", command=self.viewbalance,fg="blue",bg="pink", width=25,height=5, font="italian,10,bold")
        self.Viewbalancebtn.grid(columnspan=4,sticky="e")
        self.withdrawbtn= Button(self, text="withdraw", command=self.Withdraw,fg="blue",bg="pink", width=25,height=5, font="italian,10,bold")
        self.withdrawbtn.grid(columnspan=6, sticky="e")
        self.depositbtn= Button(self, text="deposit", command=self.deposit,fg="blue",bg="pink", width=25,height=5, font="italian,10,bold")
        self.depositbtn.grid(columnspan=8, sticky="e")
        self.changepinbtn = Button(self, text="changepin", command=self.changepin, fg="blue", bg="pink", width=25,height=5, font="italian,10,bold")
        self.changepinbtn.grid(columnspan=8, sticky="e")
        self.pack()
    def viewbalance(self):
        w_balnce = getbalance(self.data[0])
        print(w_balnce,self.data[0])
        BLLabel=Label(self,text="available balance"+w_balnce[0])
        BLLabel.grid(columnspan=10,)
        BLLabel.after(1000, lambda: BLLabel.destroy())

    def Withdraw(self):
        root1=Tk()
        WithdrawFrame(root1,self.data)
    
    def deposit(self):
        root2=Tk()
        DepositFrame(root2,self.data)
    def changepin(self):
        root3=Tk()
        changepinFrame(root3, self.data)


def show(uservalue, userpass):
    cur.execute("SELECT username,pass FROM atmdata1")
    myresult = cur.fetchall()
    ##     print(myresult)
    for i in range(len(myresult)):

        if (uservalue in myresult[i]):
            ##              print(myresult[i])
            if (uservalue in myresult[i][0] and userpass in myresult[i][1]):
                print("login sucess")
                username_db=uservalue
                rootacc = Tk()
                rootacc.geometry('500x600')
                rootacc.title('MY ATM')
                rootacc.config(bg="sky blue")
                AccountFrame(rootacc, [uservalue])
                border_effects = RAISED
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
        show(username, password)
        
        
root=Tk()
root.geometry('300x300')
root.title('MY ATM')
root.config(bg="sky blue")
LoginFrame(root)



root.mainloop()