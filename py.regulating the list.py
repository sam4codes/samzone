from tkinter import *
a=Tk()
a.geometry("500x500")
a.title("app roham")
lis=[]
lism=[]
Label(a,text="Entry your number").pack()
vorodi1=Entry(a,width=40)
vorodi1.pack()

vorodi2=Entry(a,width=40)
vorodi2.pack()

vorodi3=Entry(a,width=40)
vorodi3.pack()

vorodi4=Entry(a,width=40)
vorodi4.pack()

vorodi5=Entry(a,width=40)
vorodi5.pack()

Label(a,text="Entry your number").pack()

vorodim=Entry(a,width=40)
vorodim.pack()

def yourlist():
    global v1
    global v2
    global v3
    global v4
    global v5
    global vm
    global lv
    global lss
    v1=vorodi1.get()
    v2=vorodi2.get()
    v3=vorodi3.get()
    v4=vorodi4.get()
    v5=vorodi5.get()
    vm=vorodim.get()
    lv=Label(a,text="_______________نتيجه______________",fg="blue").pack()
    if v1 == vm:
        Label(a,text="قسمت 1",fg="green").pack()
    if v2 == vm:
        Label(a,text="قسمت 2",fg="green").pack()
    if v3 == vm:
        Label(a,text="قسمت 3",fg="green").pack()
    if v4 == vm:
        Label(a,text="قسمت 4",fg="green").pack()
    if v5 == vm:
        Label(a,text="قسمت 5",fg="green").pack()
    lss=Label(a,text="_______________مرتب شده______________",fg="blue").pack()
    lis=[int(vorodi1.get()),int(vorodi2.get()),int(vorodi3.get()),int(vorodi4.get()),int(vorodi5.get())]
    lis.sort()
    Label(a,text=lis,fg="green",font="30").pack()
b=Button(a,text="ثبت",borderwidth=10,padx=100,command=yourlist).pack()

mainloop()





























