# a=[1,2,3,4.5]

# print(a[0])

# b=[[1,2,3],[4,5,6]]
# print(b[0][0])

# userdata=[[user1,password],[user2,password],[user3,password]]
# for i in range(len(userdata)):
	# print(userdata(i))
	# if "user1" in userdata [i]:
		# if "user1" in userdata [i][0] and "password" in userdata[i][1]
			# return True
		# else:
			# return False
			
			
from tkinter import*

import pyodbc
# DATABASE##
db =pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=C:\Users\User\Documents\atmData.mdb')
cur=db.cursor()

cur.execute("SELECT username,Balance FROM atmdata1")
data=cur.fetchone()
print(data)
def updatetable(balance,Name):
    try:
        cur.execute("UPDATE atmdata1 SET Balance=? WHERE username=?",(balance,Name))
        db.commit()
        
    except Exception as e:
        print("update failed",e)
class DepositFrame(Frame):
    def __init__(self, master,data):
        super().__init__(master)
        self.data=data
        self.depositLabel=Label(self,text="enter the amount")
        self.depositLabel.grid(columnspan=1)
        self.depositentry = Entry(self)
        self.depositentry.grid(row=2, columnspan=1, sticky=W)
        self.depositButton=Button(self,text="submit",command=self.deposit,bg="pink",fg="purple")
        self.depositButton.grid(columnspan=2)
        self.pack()
        
    def deposit(self):
        depositvalue= self.depositentry.get()
        balance=int(self.data[1])+int(depositvalue)
        updatetable(balance,data[0])
        # root2.deiconify()   #makes the root window visible again
    master.destroy()
        
class WithdrawFrame(Frame):
    def __init__(self, master,data):
        super().__init__(master)
        self.data=data
        self.WithdrawButton=Button(self,text="1000",command=self.withdraw1000,bg="grey",fg="red")
        self.WithdrawButton.grid(row=0, columnspan=2, sticky=W)
        self.WithdrawButton=Button(self,text="500",command=self.withdraw500,bg="grey",fg="red")
        self.WithdrawButton.grid(row=1, columnspan=2, sticky=W)
        self.WithdrawButton=Button(self,text="100",command=self.withdraw100,bg="grey",fg="red")
        self.WithdrawButton.grid(row=2, columnspan=2, sticky=W)
        self.pack()
    def withdraw1000(self):
        balance=int(self.data[1])-1000
        updatetable(balance,data[0])
    def withdraw500(self):
        balance=int(self.data[1])-500
        updatetable(balance,data[0])
    def withdraw100(self):
        balance=int(self.data[1])-100
        updatetable(balance,data[0])
        
        
class AccountFrame(Frame):
    def __init__(self, master,data):
        super().__init__(master)
        self.data=data
        self.mainLabel=Label(self,text="welcome "+self.data[0])
        self.mainLabel.grid(columnspan=2)
        self.Viewbalancebtn = Button(self, text="Viewbalance", command=self.viewbalance,fg="blue",bg="pink")
        self.Viewbalancebtn.grid(columnspan=4)
        self.withdrawbtn= Button(self, text="withdraw", command=self.Withdraw,fg="blue",bg="pink")
        self.withdrawbtn.grid(columnspan=6)
        self.depositbtn= Button(self, text="deposit", command=self.deposit,fg="blue",bg="pink")
        self.depositbtn.grid(columnspan=8)
        self.pack()
    def viewbalance(self):
        BLLabel=Label(root,text="available balance"+data[1])
        BLLabel.pack()
        
    def Withdraw(self):
        root1=Tk()
        WithdrawFrame(root1,data)
    
    def deposit(self):
        root2=Tk()
        DepositFrame(root2,data)
        
        
root=Tk()
root.geometry('500x500')
AccountFrame(root,data)



root.mainloop()
			