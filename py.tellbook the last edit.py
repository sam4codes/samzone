from tkinter import *
from tkinter import messagebox
win=Tk()
win.config(bg="#2c302e")
win.geometry("750x650")
win.resizable(width=False, height=False)

###
def add():
    contact=e1.get()+":"+e2.get()
    if e1.get()=="" :
         messagebox.showerror("Error","pls,Enter Name")
    if e2.get()=="":
         messagebox.showerror("Error","pls,Enter Number")
    else:
        lbox.insert(END,contact)
        e1.delete(0,END)
        e2.delete(0,END)  
def delete():
    lbox.delete(ANCHOR)
    new_contact=lbox.get(0,END)
    f=open("telbook.txt","w")
    for item in new_contact:
        if item.endswith("\n"):
            f.write(item)
        else:

            f.write(item+'\n')
    f.close()
    
def search():
    a=e1.get()
    f=open("telbook.txt","r")
    for line in f:
        if a in line:
              
            l3.config(text="the phone number is {}".format(line))
def edit():
     #messagebox.showerror("Help","First click you name after that enter name and new number")
     x =lbox.curselection()
     lbox.delete(x)
     contact=e1.get()+":"+e2.get()
     lbox.insert(contact,0)
     e1.delete(0,END)
     e2.delete(0,END)  
def save():
    f=open("telbook.txt","w+")
    list_tuple = lbox.get(0,END)
    print(list_tuple)
    for item in list_tuple:
        if item.endswith("\n"):
            f.write(item)
        else:

            f.write(item+'\n')
    f.close()
def show():
    lbox.delete(0,END)
    f=open("telbook.txt","r")
    for line in f:
        lbox.insert(END, line)
mySelf = Label(win, text="made by mrTech", font=("mv boli", 20, "bold"), bg="#2c302e", fg="#fff")
mySelf.place(x=450, y=580)
l=Label(win, text="NoteBook", font=("calibri",45,"bold"),bg="#2c302e", fg="#fff")
l.place(x=80, y=20)
l1=Label(text="Name :", font=("calibri", 29,"bold"),bg="#2c302e", fg="#fff")
l1.place(x=20,y=150)
l2=Label(text="Number :",font=("calibri", 29,"bold"),bg="#2c302e", fg="#fff")
l2.place(x=20,y=250)
l3 = Label(win, text="", font=("calibri", 20), bg="#2c302e", fg="#fff")
l3.place(x=398, y=580)

lbox=Listbox(win, font=("calibri", 20), width=19, height=15, bg="#fff", fg="#000", bd=0)
lbox.place(x=440,y=40)

e1=Entry(win, font=("calibri", 27), bg="#fff", fg="#000", bd=0, width=13)
e1.place(x=150,y=154)
e2=Entry(win, font=("calibri", 27), bg="#fff", fg="#000", bd=0, width=11)
e2.place(x=186,y=254)

b1=Button(win,text="ADD", font=("calibri", 27, "bold"), bg="#3dc24d", fg="#fff", bd=0, width=7, height=1, command=add)
b1.place(x=40,y=350)

b2=Button(win,text="Delete", font=("calibri", 27, "bold"), bg="#df5968", fg="#fff", bd=0, width=7, height=1, command=delete)
b2.place(x=220,y=350)

b3=Button(win,text="Search", font=("calibri", 27, "bold"), bg="#2e8dd1", fg="#fff", bd=0, width=7, height=1, command=search)
b3.place(x=40,y=450)

b4=Button(win,text="Edit", font=("calibri", 27, "bold"), bg="#d7aa26", fg="#fff", bd=0, width=7, height=1, command=edit)
b4.place(x=220,y=450)

b5=Button(win,text="Save", font=("calibri", 27, "bold"), bg="#3dc24d", fg="#fff", bd=0, width=7, height=1, command=save)
b5.place(x=40,y=550)
b6=Button(win,text="Show", font=("calibri", 27, "bold"), bg="#8122dd", fg="#fff", bd=0, width=7, height=1, command=show)
b6.place(x=220,y=550)
win.mainloop()

