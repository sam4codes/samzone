from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win=Tk()
win.geometry("600x600")
win.config(bg='#11192c')
win.title('Training')

# -------- Def

def lightmode():
    win.config(bg='white')
    l1.config(fg='#11192c',bg='white')
    messagebox.showinfo('Light Mode','Theme Changed Successfully')

def darkmode():
    win.config(bg='#11192c')
    l1.config(fg='white', bg='#11192c')
    messagebox.showinfo('Dark Mode','Theme Changed Successfully')

def Close():
    top1.destroy()
    win.destroy()

#---------
    
def Simple_Calc():

    global top1
    top1=Toplevel()
    top1.geometry('500x360')
    top1.title('Calc')

    separator = ttk.Separator(top1, orient='vertical')
    separator.place(relx=0.33, rely=0, relwidth=0.2, relheight=1)

    def lighttmode():
        top1.config(bg='white')
    def darkkmode():
        top1.config(bg='#11192c')

    menubar= Menu(top1)
    top1.config(menu=menubar)

    view= Menu(menubar, tearoff=0)
    view.add_command(label='Light Mode',command=lighttmode)
    view.add_command(label='Dark Mode',command=darkkmode)
    menubar.add_cascade(label='View',menu=view)

    
    l1=Label(top1,text='+')
    l1.place(x=30,y=40)

    l3=Label(top1,text='-')
    l3.place(x=250,y=40)

    l3=Label(top1,text='x')
    l3.place(x=30,y=180)

    l3=Label(top1,text='/')
    l3.place(x=250,y=180)

    global l2
    
    l2=Label(top1,text='')
    l2.place(x=10,y=130)

    global e1
    global e2
    global e3
    global e4
    
    e1=Entry(top1)
    e2=Entry(top1)
    e3=Entry(top1)
    e4=Entry(top1)
    e5=Entry(top1)
    e6=Entry(top1)
    e7=Entry(top1)
    e8=Entry(top1)
    
    e1.place(x=10,y=20)
    e2.place(x=10,y=60)
    e3.place(x=230,y=20)
    e4.place(x=230,y=60)
    e5.place(x=10,y=160)
    e6.place(x=10,y=200)
    e7.place(x=230,y=160)
    e8.place(x=230,y=200)


    def Mosbat():
        o=int(e1.get())
        p=int(e2.get())
        l2.config(text="{} + {} = {}".format(o,p,o+p))
    b2=Button(top1,text='Answer',command=Mosbat)
    b2.place(x=10,y=100)

    def Menha():
        l1=Label(top1,text="")
        o=int(e3.get())
        p=int(e4.get())
        l1.config(text="{} - {} = {}".format(o,p,o-p))
        l1.place(x=230,y=130)
    b3=Button(top1,text='Answer',command=Menha)
    b3.place(x=230,y=100)

    def Zarb():
        l1=Label(top1,text="")
        o=int(e5.get())
        p=int(e6.get())
        l1.config(text="{} x {} = {}".format(o,p,o*p))
        l1.place(x=10,y=270)
    b4=Button(top1,text='Answer',command=Zarb)
    b4.place(x=10,y=240)

    def Taqsim():
        l1=Label(top1,text="")
        o=int(e7.get())
        p=int(e8.get())
        l1.config(text="{} / {} = {}".format(o,p,o/p))
        l1.place(x=230,y=270)
    b5=Button(top1,text='Answer',command=Taqsim)
    b5.place(x=230,y=240)
    
#---------

#def MajmuE():
#    
#    top1=Toplevel()
#    top1.geometry('500x360')
#    top1.title('MajmuE')
#    
#    def lighttmode():
#        top1.config(bg='white')
#        
#    def darkkmode():
#        top1.config(bg='#11192c')
#
#    menubar= Menu(top1)
#    top1.config(menu=menubar)
#
#    view= Menu(menubar, tearoff=0)
#    view.add_command(label='Light Mode',command=lighttmode)
#    view.add_command(label='Dark Mode',command=darkkmode)
#    menubar.add_cascade(label='View',menu=view)
#
#    e1=Entry(top1)
#    e2=Entry(top1)
#    e3=Entry(top1)
#    e4=Entry(top1)
#    e5=Entry(top1)
#    e6=Entry(top1)
#    e7=Entry(top1)
#    e8=Entry(top1)
#
#    e1.place(x=10,y=20)
#    e2.place(x=10,y=60)
#    e3.place(x=230,y=20)
#    e4.place(x=230,y=60)
#    e5.place(x=10,y=180)
#    e6.place(x=10,y=220)
#    e7.place(x=230,y=180)
#    e8.place(x=230,y=220)


    
# -------- Labels & Buttons ....

l1=Label(win,text='Py Training',fg='white',bg='#11192c',font=('arial',16, 'bold'))
l1.place(x=30,y=30)

b1=Button(win,text='Calc',font=('arial', 15),command=Simple_Calc)
b1.place(x=20,y=70)

#b2=Button(win,text='MajmuE',font=('arial', 15),command=MajmuE)
#b2.place(x=20,y=130)

# -------- File Menu

menubar= Menu(win)
win.config(menu=menubar)

filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=win.destroy)
menubar.add_cascade(label='File',menu=filemenu)


newmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit')
newmenu.add_command(label='Undo')
newmenu.add_command(label='Redo')
newmenu.add_separator()
newmenu.add_command(label='Cut')
newmenu.add_command(label='Copy')
newmenu.add_command(label='Paste')

view= Menu(menubar, tearoff=0)
view.add_command(label='Light Mode',command=lightmode)
view.add_command(label='Dark Mode',command=darkmode)
menubar.add_cascade(label='View',menu=view)

# --------  
