from tkinter import *
from tkinter import ttk
from prettytable import PrettyTable
win=Tk()



win.config(bg="pink")
win.geometry("600x600")
win.title("انتشارات")



pt=PrettyTable(["name","code"])

pt.add_row(["python","01"])
pt.add_row(["c++","02"])

pt1=PrettyTable(["name","code"])

pt1.add_row(["تاريخ بيهقي","03"])
pt1.add_row(["تاريخ ايران","04"])

pt2=PrettyTable(["name","code"])

pt2.add_row(["خيلي سبز","05"])
pt2.add_row(["رياضي1","06"])


l=Label(win,text="به انتشاراتي خوش آمديد",font="bold")
l.pack()
l1=Label(win,text="گروه کتاب")
l1.place(x=100,y=100)

        
        
        
        
def delete():
    n=gbook.get()
    global sel
    global x
    if n=="programming":
        l2.config(text="چه کتابي  را حذف کنم؟ ")
        sel=ttk.Combobox(win,textvariable=book,values=('{}'.format(pt.rows[0][0]),'{}'.format(pt.rows[1][0])),state='readonly')
        sel.place(x=150,y=300)
        x=sel.get()
        

def display():

    n=gbook.get()
    if n=="programming":
        l2.config(text=pt)
    if n=="historical":
        l2.config(text=pt1)
    if n=="math":
        l2.config(text=pt2)
def done():
    if sel.get()=='{}'.format(pt.rows[0][0]):
            del_pt.rows[0]
    l3.config(text="کتاب حذف شد")
    
    
    
        

    
        
gbook=StringVar()
book=StringVar()
combo=ttk.Combobox(win,textvariable=gbook,values=('programming','historical','math'),state='readonly')
combo.place(x=200,y=100)
b=Button(win,text="نمايش کتاب",command=display)
b.place(x=200,y=200)
b1=Button(win,text="ويرايش")
b1.place(x=250,y=130)
b2=Button(win,text="حذف",command=delete)
b2.place(x=210,y=130)
b3=Button(win,text="انجام",command=done)
b3.place(x=290,y=130)





b3.place(x=200,y=500)
l3=Label(win,text=" ")
l3.place(x=300,y=400)
l2=Label(win,text=" ")
l2.place(x=300,y=300)
