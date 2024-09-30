from tkinter import *
import pickle
import tkinter.messagebox
import datetime
#import os


BG='pink'

root=Tk()
root.geometry('482x500')
root.title('To Do!')
root.configure(bg=BG)
root.resizable(0,0)

def time():
    t=datetime.datetime.now().strftime("%Y %b %H:%M:%S %p")
    timel.config(text=t)
    root.after(500,time)
def add_task():
    listbox.insert(END,e.get())
       
def delete_task():
   
    x = listbox.curselection()
    listbox.delete(x)
def load_tasks():
      tasks = pickle.load(open("C:\\Users\\vira\\Desktop\\d.dat", "rb"))
      listbox.delete(0, END)
      for task in tasks:
            listbox.insert(END, task)  
def save_tasks():
    tasks = listbox.get(0, listbox.size())
    pickle.dump(tasks, open("C:\\Users\\vira\\Desktop\\d.dat", "wb"))
listbox = Listbox(root, height=10, width=40,bd=0,font=('Candara',15,'bold'),activestyle=NONE)
listbox.place(x=20,y=50)
e = Entry(root, width=40,font=('Arial',15,'bold'),bd=2)
e.place(x=20,y=320)
b1 = Button(root, text="Add", width=5,bd=2, command=add_task,activebackground=BG)
b1.place(x=20,y=360)
b2 = Button(root, text="Delete",bd=2, width=5, command=delete_task,activebackground=BG)
b2.place(x=150,y=360)
b3 =Button(root, text="Load",bd=2,width=5, command=load_tasks,activebackground=BG)
b3.place(x=280,y=360)
b4 = Button(root, text="Save", bd=2,width=5, command=save_tasks,activebackground=BG)
b4.place(x=400,y=360)
timel=Label(root,font='calibri',bd=2,bg=BG,fg='white')
timel.pack()
label=Label(root,bg=BG,fg='white',bd=2,font=('Calibri',17,'bold'))
label.place(x=220,y=425)


time()
mainloop()
