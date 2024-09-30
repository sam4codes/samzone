from tkinter import *
name=[]
passw=[]
def r():
    if b2["state"]=="disabled":
        b2["state"]="normal"
    l3.config(text="Registerd")
    name.append(str(e))
    passw.append(str(e2))
def login():
    a=-1
    for item in name:
        a+=1
        if e==item:
            b=a
    if b!=0 and e2==passw[b]:
        l3.config(text="Hello "+str(e)+" !")
    else :
        l3.config(text="sorry username isn't registerd or incorrect password is enterd")
    print(name)
    print(passw)
win=Tk()
win.title("register form")
win.geometry("400x300")
win.config(bg="powder blue")
l=Label(win,text="Username",font=("Dubai",11,"bold"),bg="powder blue")
l.place(x=30,y=40)
e=Entry(win)
e.place(x=150,y=40)
l2=Label(win,text="Password",font=("Dubai",11,"bold"),bg="powder blue")
l2.place(x=30,y=60)
e2=Entry(win)
e2.place(x=150,y=60)
b1=Button(win,text="register",command=r)
b1.place(x=185,y=80)
b2=Button(win,text="login",command=login)
b2.place(x=150,y=80)
b2["state"]="disabled"
l3=Label(win,text="  ",bg="powder blue")
l3.place(x=35,y=120)
