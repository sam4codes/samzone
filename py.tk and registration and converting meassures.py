from tkinter import *
from tkinter import ttk
maneli = Tk()
maneli.geometry("700x600")
maneli.resizable(width=False,height=False)
maneli.title("تبديل واحد")
maneli.config(bg="#89e5d4")
cn = Canvas(width=200,height=200,bg="#89e5d4")
cn.pack(expand=YES,fill=BOTH)
def hajm():
    def metr():
        def e9():
            l13.insert(1,int(e14.get())*1000000)
        t14 = Toplevel()
        t14.geometry("250x300")
        t14.config(bg="#cbc6ff")
        l10 = Label(t14,text="cm",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l10.place(x=30,y=100)
        l11 = Label(t14,text="ml",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l11.place(x=150,y=100)
        e14 = Entry(t14,bg="white")
        e14.place(x=20,y=150)
        l13 = Listbox(t14,width=10,height=5)
        l13.place(x=150,y=150)
        b24 = Button(t14,text="تبديل",font=("Courier New",9,"bold"),command=e9)
        b24.place(x=100,y=200)
    def lit():
        def e8():
            l12.insert(1,int(e13.get())*1000)
        t13 = Toplevel()
        t13.geometry("250x300")
        t13.config(bg="#cbc6ff")
        l9 = Label(t13,text="cm",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l9.place(x=30,y=100)
        l10 = Label(t13,text="L",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l10.place(x=150,y=100)
        e13 = Entry(t13,bg="white")
        e13.place(x=20,y=150)
        l12 = Listbox(t13,width=10,height=5)
        l12.place(x=150,y=150)
        b23 = Button(t13,text="تبديل",font=("Courier New",9,"bold"),command=e8)
        b23.place(x=100,y=200)
    def mili():
        def e7():
            l11.insert(1,int(e12.get())*1000)
        t12 = Toplevel()
        t12.geometry("250x300")
        t12.config(bg="#cbc6ff")
        l8 = Label(t12,text="L",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l8.place(x=30,y=100)
        l9 = Label(t12,text="ml",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l9.place(x=150,y=100)
        e12 = Entry(t12,bg="white")
        e12.place(x=20,y=150)
        l11 = Listbox(t12,width=10,height=5)
        l11.place(x=150,y=150)
        b22 = Button(t12,text="تبديل",font=("Courier New",9,"bold"),command=e7)
        b22.place(x=100,y=200)
    t11 = Toplevel()
    t11.geometry("250x300")
    t11.config(bg="#efd76e")
    b19=Button(t11,text="ليتر به ميلي ليتر",font=("Courier New",7,"bold"),command=mili)
    b19.place(x=30,y=100)
    b20=Button(t11,text="مترمکعب به ليتر",font=("Courier New",7,"bold"),command=lit)
    b20.place(x=150,y=100)
    b21=Button(t11,text="مترمکعب به ميلي ليتر",font=("Courier New",7,"bold"),command=metr)
    b21.place(x=80,y=200)
def jerm():
    def g():
        def e6():
            l10.insert(1,int(e11.get())*1000000)
        t10 = Toplevel()
        t10.geometry("250x300")
        t10.config(bg="#cbc6ff")
        l7 = Label(t10,text="ton",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l7.place(x=30,y=100)
        l8 = Label(t10,text="g",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l8.place(x=150,y=100)
        e11 = Entry(t10,bg="white")
        e11.place(x=20,y=150)
        l10 = Listbox(t10,width=10,height=5)
        l10.place(x=150,y=150)
        b18 = Button(t10,text="تبديل",font=("Courier New",9,"bold"),command=e6)
        b18.place(x=100,y=200)
    def kg():
        def e5():
            l9.insert(1,int(e10.get())*1000)
        t9 = Toplevel()
        t9.geometry("250x300")
        t9.config(bg="#cbc6ff")
        l7 = Label(t9,text="kg",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l7.place(x=30,y=100)
        l8 = Label(t9,text="g",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l8.place(x=150,y=100)
        e10 = Entry(t9,bg="white")
        e10.place(x=20,y=150)
        l9 = Listbox(t9,width=10,height=5)
        l9.place(x=150,y=150)
        b17 = Button(t9,text="تبديل",font=("Courier New",9,"bold"),command=e5)
        b17.place(x=100,y=200)
    def ton():
        def e4():
            l8.insert(1,int(e9.get())*1000)
        t8 = Toplevel()
        t8.geometry("250x300")
        t8.config(bg="#cbc6ff")
        l6 = Label(t8,text="ton",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l6.place(x=30,y=100)
        l7 = Label(t8,text="kg",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l7.place(x=150,y=100)
        e9 = Entry(t8,bg="white")
        e9.place(x=20,y=150)
        l8 = Listbox(t8,width=10,height=5)
        l8.place(x=150,y=150)
        b16 = Button(t8,text="تبديل",font=("Courier New",9,"bold"),command=e4)
        b16.place(x=100,y=200)
    t7 = Toplevel()
    t7.geometry("250x300")
    t7.config(bg="#fcffda")
    b13=Button(t7,text="ton -> kg",font=("Courier New",9,"bold"),command=ton)
    b13.place(x=30,y=100)
    b14=Button(t7,text="kg -> g",font=("Courier New",9,"bold"),command=kg)
    b14.place(x=150,y=100)
    b15=Button(t7,text="ton -> g",font=("Courier New",9,"bold"),command=g)
    b15.place(x=80,y=200)
def tool():
    def km():
        def e3():
            l7.insert(1,int(e8.get())//10000)
        t6 = Toplevel()
        t6.geometry("250x300")
        t6.config(bg="#cbc6ff")
        l5 = Label(t6,text="cm",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l5.place(x=30,y=100)
        l6 = Label(t6,text="m",bg="#cbc6ff",font=("Courier New",15,"bold"))
        l6.place(x=150,y=100)
        e8 = Entry(t6,bg="white")
        e8.place(x=20,y=150)
        l7 = Listbox(t6,width=10,height=5)
        l7.place(x=150,y=150)
        b12 = Button(t6,text="تبديل",font=("Courier New",9,"bold"),command=e3)
        b12.place(x=100,y=200)
    def m():
        def e2():
            l6.insert(1,int(e7.get())//1000)
        t5 = Toplevel()
        t5.geometry("250x300")
        t5.config(bg="#d9f9ff")
        l4 = Label(t5,text="m",bg="#d9f9ff",font=("Courier New",15,"bold"))
        l4.place(x=30,y=100)
        l5 = Label(t5,text="km",bg="#d9f9ff",font=("Courier New",15,"bold"))
        l5.place(x=150,y=100)
        e7 = Entry(t5,bg="white")
        e7.place(x=20,y=150)
        l6 = Listbox(t5,width=10,height=5)
        l6.place(x=150,y=150)
        b11 = Button(t5,text="تبديل",font=("Courier New",9,"bold"),command=e2)
        b11.place(x=100,y=200)
    def cm():
        def e1():
            l5.insert(1,int(e6.get())//100)
        t4 = Toplevel()
        t4.geometry("250x300")
        t4.config(bg="#ffa393")
        l3 = Label(t4,text="cm",bg="#ffa393",font=("Courier New",15,"bold"))
        l3.place(x=30,y=100)
        l4 = Label(t4,text="m",bg="#ffa393",font=("Courier New",15,"bold"))
        l4.place(x=150,y=100)
        e6 = Entry(t4,bg="white")
        e6.place(x=20,y=150)
        l5 = Listbox(t4,width=10,height=5)
        l5.place(x=150,y=150)
        b10 = Button(t4,text="تبديل",font=("Courier New",9,"bold"),command=e1)
        b10.place(x=100,y=200)
    t3 = Toplevel()
    t3.geometry("250x300")
    t3.config(bg="#e0bffc")
    b7 = Button(t3,text="cm -> m",font=("Courier New",9,"bold"),command=cm)
    b7.place(x=30,y=100)
    b8 = Button(t3,text="m -> km",font=("Courier New",9,"bold"),command=m)
    b8.place(x=150,y=100)
    b9 = Button(t3,text="cm -> km",font=("Courier New",11,"bold"),command=km)
    b9.place(x=80,y=200)
def new():
    def add():
        a.insert(1,e1.get(),e2.get(),e3.get(),e4.get(),e5.get())
    t1 = Toplevel()
    t1.title("ثبت نام")
    t1.geometry("700x700")
    t1.config(bg="#5551ba")
    month=StringVar()
    grade=StringVar()
    year=StringVar()
    x=Spinbox(t1,from_=1330,to=1401,textvariable=year,state="readonly")
    x.place(x=175,y=460)
    l2 = Label(t1,text="Information",fg="#ffbfd8",font=("Courier New",25,"bold")
      ,bg="#5551ba")
    l2.place(x=250,y=0)
    l3 = Label(t1,text="Name: ",fg="#e23617",font=("Courier New",25,"bold")
          ,bg="#5551ba")
    l3.place(x=50,y=100)
    l4 = Label(t1,text="Last name: ",fg="#FF4500",font=("Courier New",25,"bold")
          ,bg="#5551ba")
    l4.place(x=50,y=150)
    l5 = Label(t1,text="Phone number: ",fg="#f7f97c",font=("Courier New",25,"bold")
          ,bg="#5551ba")
    l5.place(x=50,y=200)
    l6 = Label(t1,text="Address: ",fg="#2bc47a",font=("Courier New",25,"bold")
          ,bg="#5551ba")
    l6.place(x=50,y=250)
    l7 = Label(t1,text="Code: ",fg="#33a4f4",font=("Courier New",25,"bold")
          ,bg="#5551ba")
    l7.place(x=50,y=300)
    e1 = Entry(t1,bg="white")
    e1.place(x=175,y=115)
    e2 = Entry(t1,bg="white")
    e2.place(x=275,y=165)
    e3 = Entry(t1,bg="white")
    e3.place(x=340,y=215)
    e4 = Entry(t1,bg="white")
    e4.place(x=235,y=263)
    e5 = Entry(t1,bg="white")
    e5.place(x=175,y=310)
    n7 = Label(t1,text="Month: ",fg="#6f24b5",font=("Courier New",25,"bold")
      ,bg="#5551ba").place(x=50,y=350)
    birth=ttk.Combobox(t1,textvariable=month,values=("January","February","March","April",
                   "May","June","July","August","September","October","November","December"),state="readonly").place(x=185,y=360)
    n8 = Label(t1,text="Grade: ",fg="#ec08d8",font=("Courier New",25,"bold")
          ,bg="#5551ba")
    n8.place(x=50,y=400)
    grade=ttk.Combobox(t1,textvariable=grade,values=("1st","2nd","3rd","4th",
                       "5th","6th","7th","8th","9th","10th","11th","12th","University","Graduated"),state="readonly").place(x=185,y=410)
    n9 = Label(t1,text="Year: ",fg="#e23617",font=("Courier New",25,"bold")
          ,bg="#5551ba")
    n9.place(x=50,y=450)
    a = Listbox(t1,width=15,height=15,font=("Courier New",15,"bold"))
    a.place(x=500,y=110)
    b2 = Button(t1,text="صفحه اصلي",width=10,height=2,
            font=("Courier New",12,"bold"),bg="#d6edbe",command=bad)
    b2.place(x=270,y=500)
    b3 = Button(t1,text="اضافه کردن",width=10,height=2,font=("Courier New",12,"bold"),bg="#d6edbe",command=add)
    b3.place(x=150,y=500)
def bad():
    t2 = Toplevel()
    t2.geometry("250x300")
    t2.config(bg="#86f28c")
    b3 = Button(t2,text="تبديل طول",width=9,height=3,font=("Courier New",10,"bold"),
                command=tool)
    b3.place(x=30,y=100)
    b4 = Button(t2,text="تبديل جرم",width=9,height=3,font=("Courier New",10,"bold"),
                command=jerm)
    b4.place(x=150,y=100)
    b6 = Button(t2,text="تبديل حجم",width=9,height=3,font=("Courier New",10,"bold"),
                command=hajm)
    b6.place(x=90,y=200)
l1 = Label(maneli,text="!سلام",bg="#89e5d4",font=("Courier New",25,"bold"))
l1.place(x=320,y=5)
b1 = Button(maneli,text="ثبت نام",bg="#f7d4d9",font=("Courier New",25,"bold"),
            command=new)
b1.place(x=280,y=350)
#p1 = PhotoImage(file="hello.png")
#cn.create_image(355,200,image=p1)

