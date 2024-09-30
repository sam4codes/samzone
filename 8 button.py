from tkinter import *
from tkinter import ttk
a=Tk()
a.geometry("600x600")

def exitd():
    quit()

b1=Button(a,text="exit",padx=30,pady=40,bg="yellow",command=exitd)
b1.grid(row=0,column=0)

def blist():
    e=[]
    print(e)
    y=input("enter your :")
    e.append(y)
    print(e)
b2=Button(a,text="create list",padx=30,pady=40,bg="green",command=blist)
b2.grid(row=0,column=1)

def lbox():
    t=Tk()
    t.geometry("600x600")
    listbox = Listbox(t, height = 10, width = 15, bg = "green",activestyle = 'dotbox', font = "Helvetica",fg = "yellow")
    listbox.insert(1, "radin")
    listbox.insert(2, "alivazeri")
    listbox.insert(3, "homan")
    listbox.insert(4, "parsa")
    listbox.insert(5, "mahdyar")
    listbox.insert(6, "parham")
    listbox.grid(row=0,column=5)
b3=Button(a,text="listbox",padx=30,pady=40,bg="red",command=lbox)
b3.grid(row=1,column=0)

def menu():
    a=Tk()
    a.geometry("600x600")
    menubar = Menu(a)
    a.config(menu = menubar)
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='part1', command = None)
    file.add_command(label ='part2', command = None)
b4=Button(a,text="menu",padx=30,pady=40,bg="brown",command=menu)
b4.grid(row=1,column=1)

def meangin():
    for i in range(5):
        a=input ("لطفا يک عدد را وارد کنيد:")
        a=int(a)
        if a<0:
            print ("خطا")
        d=0
    b=a+d
    c=b/5
    print ("ميانگين",c)

b5=Button(a,text="meangin",padx=30,pady=40,bg="gold",command=meangin)
b5.grid(row=2,column=0)

def hrof():
    a=input ("يک رشته وارد کنيد:")
    sound=("iouae")
    r=0
    r=int(r)
    for w in a:
        for e in sound:
            if w==e:
                r=r+1
    print (r)
        

b6=Button(a,text="horof",padx=30,pady=40,bg="red",command=hrof)
b6.grid(row=2,column=1)

def circle():
    import turtle
    t = turtle.Turtle()
    r = 50
    t.circle(r)
b7=Button(a,text="circle",padx=30,pady=40,bg="green",command=circle)
b7.grid(row=3,column=0)

def froml():
    g=Tk()
    g.geometry("600x600")
    l=Label(g,text="نام")
    l.grid(row=0,column=0)
    e=Entry(g)
    e.grid(row=0,column=1)
    l=Label(g,text="نام خانوادگي")
    l.grid(row=1,column=0)
    o=Entry(g)
    o.grid(row=1,column=1)
    def sabt():
        Label(g,text="نام"+"    "+e.get()).grid(row=3,column=0)
        Label(g,text="نام خانوادگي"+"    "+o.get()).grid(row=4,column=0)
    b=Button(g,text="sabt",padx=30,pady=40,command=sabt).grid(row=2,column=0)
b8=Button(a,text="form",padx=30,pady=40,bg="blue",command=froml)
b8.grid(row=3,column=1)
















