from tkinter import *
from tkinter import messagebox
win=Tk()
win.config(bg="#ecc5f3")
win.geometry("600x600")
telbook={}
list1=[]
#def______________________
def add():  
    f=open("telbook.txt","a+")
    telbook[e1.get()]=e2.get()
    a=e1.get()
    b=e2.get()
    if e1.get()=="":
        messagebox.showerror("خطا!","لطفا نام را وارد کنيد.")
    if e2.get()=="":
        messagebox.showerror("!خطا","لطفا شماره تلفن را وارد کنيد.")
    txt=f"{a}:{b}"
    lbox.insert(0,txt)
    list1.append(txt)
    txt="\n"+txt
    f.write(txt)
    f.close()
    return telbook
    return list1
def delete():
    l3.config(text="which number do you want remove?")        
    del telbook[e1.get()]
    lbox.delete(0,END)
    for i in list1:
    
        lbox.insert(0,i)
    return telbook
    return list1
    
   
    
    
    
def search() :
    a=telbook[e1.get()]
    l3.config(text="the phone number is {}".format(a))
def edit():
  
   telbook[e1.get()]=e2.get()
   lbox.insert(0,telbook)
    
    
    
#__________________________________________________
l=Label(text="NotBook",font=("arial",20),fg="blue")
l.pack()
l1=Label(text="Name",font=("arial",14),fg="blue")
l1.place(x=20,y=100)
l2=Label(text="Number",font=("arial",14),fg="blue")
l2.place(x=20,y=150)
l3=Label(text="",font=("arial",10),fg="blue")
l3.place(x=10,y=200)
lbox=Listbox(win,width=50,height=10,bg="#f8e8fb",bd=5)
lbox.place(x=250,y=100)
e1=Entry(win,bd=3)
e1.place(x=100,y=100)
e2=Entry(win,bd=3)
e2.place(x=100,y=150)
b1=Button(win,text="ADD Number",bd=3,command=add)
b1.place(x=150,y=300)
b2=Button(win,text="Delete",bd=3,bg="#aa2ec2",fg="white",command=delete)
b2.place(x=400,y=300)
b3=Button(win,text="Search",bd=3,command=search)
b3.place(x=150,y=350)
b4=Button(win,text="Edit",bd=3,command=edit)
b4.place(x=400,y=350)
#___________________
