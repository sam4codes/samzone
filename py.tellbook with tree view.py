from tkinter import ttk
# import tkinter as tk
from tkinter import *
def add_customer():
    name_and_surname = d.get()
    phone_number = f.get()
    ID = h.get()
    tree.insert(parent='', index= 'end', values=(ID, name_and_surname,phone_number))
def delete_selected():
    x=tree.selection()[0]
    tree.delete(x)
win=Tk()
win.geometry("550x300")
win.title("contact Book")
win.config(bg="gray")
lblTitle=Label(win, text="Adress Book:",bg="black",fg="white",font=("calibri",20,"bold"))
lblTitle.place(x=0, y=0, width= 250)
b=Label(win, text="date:",bg="black", fg="white")
b.place(x=250, y=0, width= 120)
e2=Entry(win)
e2.place(x=370, y=0, width= 160)


# label Name And Surname
lblName=Label(win, text="name and surname:", bg="dark blue", fg="yellow")
lblName.place(x=5, y=50, width= 125)
d=Entry(win)
d.place(x=140, y=50, width=400)
 

# label entry phone
lblPhone=Label(win, text="Phone Number:", bg="dark blue", fg="yellow")
lblPhone.place(x=5, y=80, width= 125)
f=Entry(win)
f.place(x=140, y=80, width=400)


# label ID
lblID=Label(win, text="ID:", bg="dark blue", fg="yellow")
lblID.place(x=5, y=110, width= 125)
h=Entry(win)
h.place(x=140, y=110, width=400)


# Command Button
bAdd= Button(win, text="Add Customer", bg="dark blue", fg="yellow", command = add_customer)
bAdd.place(x=5, y=140, width= 255)

bDelete= Button(win, text="Delete selected", bg="dark blue", fg="yellow", command = delete_selected)
bDelete.place(x=5, y=160, width= 255)

bExit= Button(win, text="Exit App", bg="dark blue", fg="yellow", command = quit)
bExit.place(x=5, y=180, width= 255)

# add TreeView
tree= ttk.Treeview(win, columns =(1, 2, 3), height= 5 , show= "headings")
tree.place(x= 260, y=140, width= 290, height= 70)

#add headings

tree.heading(1, text="ID")
tree.heading(2, text="Name")
tree.heading(3, text="phone")
# define column widht
tree.column(1, width=50)
tree.column(2, width=100)
mainloop()










