from tkinter import *
import os
from twilio.rest import Client
from tkinter import ttk 
master = Tk()
master.configure(bg="SkyBlue1")
master.geometry('739x415') 
Label(master, text="Please Select Your Bank ",font=("Times New Roman",30)).grid(row=0, column=100)
var1 = IntVar()
Checkbutton(master, text="State Bank of india ",font=("Times New Roman",10), variable=var1).grid(row=1,sticky=W ,column=100)
var2 = IntVar()
Checkbutton(master, text="Bank Of India ",font=("Times New Roman",10), variable=var2).grid(row=2,sticky=W ,column=100)
var3 = IntVar()
Checkbutton(master, text="Central Bank of India ",font=("Times New Roman",10), variable=var3).grid(row=3,sticky=W ,column=100)
var4 = IntVar()
Checkbutton(master, text="Punjab National Bank	 ",font=("Times New Roman",10), variable=var4).grid(row=4,sticky=W ,column=100)
var5 = IntVar()
Checkbutton(master, text="Oriental Bank of Commerce ",font=("Times New Roman",10), variable=var5).grid(row=5,sticky=W, column=100)
var6 = IntVar()
Checkbutton(master, text="Bhartiya Mahila Bank",font=("Times New Roman",10), variable=var6).grid(row=6,sticky=W ,column=100)
var7 = IntVar()
Checkbutton(master, text="State Bank of india ",font=("Times New Roman",10), variable=var7).grid(row=7,sticky=W, column=100)
var8 = IntVar()
Checkbutton(master, text="Andhra bank  ",font=("Times New Roman",10), variable=var8).grid(row=8,sticky=W, column=100)
def nnnn():
 window = Tk() 
 
 window.configure(bg="purple1")
 canvas = Canvas(width=739,height=415)
 canvas.grid()
 photo = PhotoImage(file='123.gif')
 canvas.create_image(0,0,image=photo,anchor=NW)
 window.title("Welcome to advance security system")
 window.geometry('739x415')
 lbl =Label(window,text="Advance ATM Security System",font=("Arial Bond",30))    
 Accountno = Label(window,text = "Enter your account No").place(x = 30,y = 50)  
 otp = Label(window,text = "Enter Your otp").place(x = 30,y = 90)  
 e1 = Entry(window)
 e1.place(x = 170, y = 50) 

 e2 = Entry(window)
 e2.place(x = 120, y = 90) 

 def otp(): 
    account_sid = "AC2fe06b193bff79b01adf92ddd387fa76"
    auth_token = "5e786068ce72d42e523de190ee5a4b76"
    client = Client(account_sid, auth_token)

    client.messages.create(
         body='The otp for authentication of atm banking system is 435779',
         from_='+12182315323',
         to='+918225886692'
       )





 def on_button():
    #e1 = Entry(window).place(x = 170, y = 50)
    print(type(e1))
    av=e1.get()
    print(type(av))
    if int(av) == 123456789:
        print("YOOO")
        slabel = Label(window, text="Otp  was sent to your Registered mobile no").place(x=400,y=50)
        otp()
        
    else:
        tlabel = Label(window, text="Your account no is incorrect").place(x=400,y=50)
 def on_button1():
    #e1 = Entry(window).place(x = 170, y = 50)
    print(type(e2))
    a=e2.get()
    print(type(a))
    if int(a) == 435779:
        slabel = Label(window, text="You Have Succesfully Authenticated").place(x=400,y=80)
        
    else:
        tlabel = Label(window, text="Sorry PLease re enter your otp ").place(x=400,y=80)      
        tlabel = Label(window, text="3 unsuccesfull try will Block your account !!!").place(x=400,y=100)      



 button = Button(window,text="Enter", command=on_button)
 button.place(x=300,y=50) 
 button = Button(window,text="Enter", command=on_button1)
 button.place(x=300,y=80)
 

 def clicked():

    lbl1=Label(text="Button was clicked !!")

 def withdrawal():
    withdrawal = Tk() 
    withdrawal.configure(bg="purple1")
    withdrawal.geometry('739x415')
    lbl2 = Label(withdrawal, text="Please enter your amount for withdrawal",font=("Arial Bond",10)).place(x=50,y=30)
    z = Entry(withdrawal)
    z.place(x=50,y=80)
    def on_button4():
        lbl2 = Label(withdrawal, text="Amount Succesfully Withdrawan",font=("Arial Bond",8)).place(x=50,y=110)
        
    but = Button(withdrawal,text="Enter", command=on_button4)
    but.place(x=50,y=130)
 
    
    withdrawal.mainloop()
    
    
 def balance():

    balance = Tk() 
    balance.configure(bg="purple1")
    balance.geometry('739x415')
    lbl3 = Label(balance, text="Your balance is 50000 rupees",font=("Arial Bond",10)).place(x=50,y=30)
    balance.mainloop()
    

 def Statement():
    Statement = Tk() 
    Statement.configure(bg="purple1")
    Statement.geometry('739x415')
    lbl2 = Label(Statement, text=" 5000  is withdrawal from your account on 10/10/19 ",font=("Arial Bond",10)).place(x=50,y=30)
    Statement.mainloop()
    
    
 def Fund_Transfer():
    Fund_Transfer = Tk() 
    Fund_Transfer.configure(bg="purple1")
    Fund_Transfer.geometry('739x415')
    lbl2 = Label(Fund_Transfer, text="Please enter your amount for Transfer",font=("Arial Bond",10)).place(x=50,y=30)
    z = Entry(Fund_Transfer)
    z.place(x=50,y=80)
    def on_button6():
        lbl3 = Label(Fund_Transfer, text="Amount Succesfully Transfer to another account",font=("Arial Bond",8)).place(x=50,y=110)
        
    but5 = Button(Fund_Transfer,text="Enter", command=on_button6)
    but5.place(x=50,y=130)
 
    Fund_Transfer.mainloop()

 def Deposit():
    Deposit = Tk()
    Deposit.configure(bg="purple1")
    Deposit.geometry('739x415')
    lbl2 = Label(Deposit, text="Please enter your amount for deposit",font=("Arial Bond",10)).place(x=50,y=30)
    x = Entry(Deposit)
    x.place(x=50,y=80)
    def on_button5():
        lbl2 = Label(Deposit, text="Amount Succesfully Deposit to your bank account",font=("Arial Bond",8)).place(x=50,y=110)
        
    but1 = Button(Deposit,text="Enter", command=on_button5)
    but1.place(x=50,y=130)
 
    Deposit.mainloop()

 btn =Button(window,text="Scan Your Fingerprint",font=("Arial Bond",18),bg="Cyan",fg="red",command=clicked)
 btn1 =Button(window,text="Withdrawal",font=("Arial Bond",18),bg="Cyan",fg="red",command=withdrawal)
 btn2 =Button(window,text="Balance",font=("Arial Bond",18),bg="Cyan",fg="red",command=balance)
 btn3 =Button(window,text="Mini statement",font=("Arial Bond",18),bg="Cyan",fg="red",command=Statement)
 btn4 =Button(window,text="Fund Transfer",font=("Arial Bond",18),bg="Cyan",fg="red",command=Fund_Transfer)
 btn5 =Button(window,text="Deposit",font=("Arial Bond",18),bg="Cyan",fg="red",command=Deposit)
 btn.place(x=30,y=180)
 btn1.place(x=30,y=240)
 btn2.place(x=30,y=300)
 btn3.place(x=500,y=180)
 btn4.place(x=500,y=240)
 btn5.place(x=500,y=300)

 window.mainloop()

def newwindow():
    nnnn()


btn = Button(master, text='Enter', command=newwindow).grid(row=5, column=200, pady=4)
master.mainloop()


 