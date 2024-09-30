from prettytable import PrettyTable
import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
win=Tk()
win.geometry("1000x1000")
def insert():
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "0441558062",
    database = "publishers"
    )
    cursor = db.cursor()
    sql="INSERT INTO groupbook(groupid,groupname) VALUES (%s,%s)"
    ####chand record
    n=int(input("Enter n:"))
    list1=[]
    v= PrettyTable(["groupid","groupname"])
    for i in range(0,n):
        groupid=input("groupid : ")
        groupname=input("groupname : ")
        v.add_row([groupid,groupname])
    val=(groupid,groupname)
    cursor.execute(sql,val)
    db.commit()
    print(cursor.rowcount,"record inserted")
    print(v)
    ##نشون دادن اطلاعات جدول
    cursor.execute("SELECT * FROM groupbook")
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)
        v.add_row(x)
    print(v)
    L2.config(text=v)
def update():
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "0441558062",
    database = "publishers"
          )
    cursor = db.cursor()
    n1=int(input("How many changes do you want to change?"))
    for i in range(0,n1):
        b=int(input("enter the ? to update"))
    print(b)
def display():
    n=gbook.get()
    if n=="programming":
        L2.config(text=t)
    if n=="historical":
        L2.config(text=s)
    if n=="math":
        L2.config(text=u)
#prettytable
t= PrettyTable(["name","code"])
s=PrettyTable(["name","code"])
u=PrettyTable(["name","code"])
t.add_row(["c++","22"])
s.add_row(["Iran","05"])
s.add_row(["sasanian","06"])
u.add_row(["zarb","05"])
u.add_row(["radikal","06"])
#label
L1=Label(win,text="انتشارات پويا",font=("B Koodak",50,'bold'),fg="green",bg="#d2d23d")
L2=Label(win,text=" ",bg="orange")
#Button
b1=Button(win,text="اضافه کردن کتاب",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=insert)
b2=Button(win,text="نمايش کتاب",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=display)
b3=Button(win,text="به روز رساني کتاب",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=update)
b4=Button(win,text=" خروج ",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=exit)
#pack()
L1.place(x=651,y=5)
L2.place(x=100,y=100)
b1.place(x=600,y=350)
b2.place(x=900,y=350)
b3.place(x=600,y=500)
b4.place(x=900,y=500)
############################from prettytable import PrettyTable
gbook=StringVar()
birth=ttk.Combobox(win,textvariable=gbook,values=('programming','historical','math'),state='readonly')
birth.place(x=200,y=100)
