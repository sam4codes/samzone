from prettytable import PrettyTable
import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
win=Tk()
win.geometry("1500x1500")
win.configure(bg="green")
def insert2():
    global t1
    global s1
    global u1
    global db
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "0441558062",
    database = "pooya"
    )
    cursor = db.cursor()
    sql="INSERT INTO entesharat(book_name,code) VALUES (%s,%s)"
    ####chand record
    n=int(input("Enter n:"))
    print("1- programing                    2- math                3-historical")
    m=int(input("Subject book : "))
    list1=[]
    v=PrettyTable(["book_name","code"])
    for i in range(0,n):
        book_name=input("book_name : ")
        code=input("code : ")
    val=(book_name,code)
    cursor.execute(sql,val)
    db.commit()
    print(cursor.rowcount,"record inserted")
    ##نشون دادن اطلاعات جدول
    cursor.execute("SELECT * FROM entesharat")
    myresult=cursor.fetchall()
    for x in myresult:
        if m==1:
            t1.add_row(x)
            L2.config(text=t1)
    for y in myresult:
        if m==2:
          u1.add_row(x)
          L2.config(text=u1)
    for z in myresult:
        if m==3:
          s1.add_row(x)
          L2.config(text=s1)
#        v.add_row(x)
  #  L2.config(text=v)
def update():
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "0441558062",
    database = "pooya"
          )
    cursor = db.cursor()
    n1=int(input("How many books do you want to change?"))
    for i in range(0,n1):
        b=int(input("Enter the name of the book to change : "))
    print(b)
def display2():
    n=gbook.get()
    if n=="programming":
        L2.config(text=L1)
    if n=="historical":
        L2.config(text=s1)
    if n=="math":
        L2.config(text=u1)
def display():
    n=gbook.get()
    if n=="programming":
        L2.config(text="چه کتابي  را حذف کنم؟ ")
        b6=Button(win,text="c++",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=del2).place(x=200,y=200)
        b7=Button(win,text="C",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=del3).place(x=300,y=200)
    if n=="historical":
        L2.config(text="چه کتابي  را حذف کنم؟ ")
        b8=Button(win,text="هخامنشيان",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=del4).place(x=200,y=200)
        b9=Button(win,text="ساسانيان",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=del5).place(x=320,y=200)
    if n=="math":
        L2.config(text="چه کتابي  را حذف کنم؟ ")
        b10=Button(win,text="ضرب",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=del6).place(x=200,y=200)
        b11=Button(win,text="   راديکال   ",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=del7).place(x=300,y=200)
def del2():
    L2.config(text=t3)
def del3():
    L2.config(text=t2)
def del4():
    L2.config(text=s3)
def del5():
    L2.config(text=s2)
def del6():
    L2.config(text=u3)
def del7():
    L2.config(text=u2)
#prettytable##
#t
t1= PrettyTable(["book_name","code"])
t1.add_row(["C","01"])
t1.add_row(["c++","02"])
t2= PrettyTable(["book_name","code"])
t2.add_row(["c++","02"])
t3= PrettyTable(["book_name","code"])
t3.add_row(["C","01"])
#s
s1=PrettyTable(["book_name","code"])
s1.add_row(["هخامنشيان","03"])
s1.add_row(["ساسانيان","04"])
s2=PrettyTable(["book_name","code"])
s2.add_row(["هخامنشيان","03"])
s3=PrettyTable(["book_name","code"])
s3.add_row(["ساسانيان","04"])
#u
u1=PrettyTable(["book_name","code"])
u1.add_row(["ضرب","05"])
u1.add_row(["راديکال","06"])
u2=PrettyTable(["book_name","code"])
u2.add_row(["ضرب","05"])
u3=PrettyTable(["book_name","code"])
u3.add_row(["راديکال","06"])
#label
L1=Label(win,text="انتشارات پويا",font=("B Koodak",50,'bold'),fg="green",bg="#d2d23d")
L2=Label(win,text=" ",bg="orange")
#Button
b1=Button(win,text="اضافه کردن کتاب",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=insert2)
b2=Button(win,text="نمايش کتاب",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=display2)
b3=Button(win,text="به روز رساني کتاب",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=update)
b4=Button(win,text=" خروج ",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=exit)
b5=Button(win,text="پاک کردن کتاب",font=('B Koodak',20,'bold'),fg="red",bg="#d2d23d",command=display)
#pack()پاک کردن کتاب
L1.place(x=651,y=5)
L2.place(x=100,y=100)
b1.place(x=600,y=250)
b2.place(x=900,y=250)
b3.place(x=600,y=400)
b4.place(x=900,y=400)
b5.place(x=600,y=550)
############################from prettytable import PrettyTable
gbook=StringVar()
birth=ttk.Combobox(win,textvariable=gbook,values=('programming','historical','math',"other"),state='readonly')
birth.place(x=250,y=100)
