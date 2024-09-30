from tkinter import *
import tkinter
import pickle
import tkinter.messagebox
import datetime
import os
newpath = f'C:\\Users\\{os.getlogin()}\\Todo' 
if not os.path.exists(newpath):
        os.makedirs(newpath)

BG='#121212'

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
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        pass        
def delete_task():
    try:
        
        if not listbox_tasks.get(ANCHOR):
            task_index = listbox_tasks.index(0)
            listbox_tasks.delete(task_index)
        else:
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(task_index)

    except:
        pass
def load_tasks():
    try:
        label.config(text='')

        tasks = pickle.load(open(f"C:\\Users\\{os.getlogin()}\\Todo\\Todocache1.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
        label.config(text='')
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find cache.dat you havn't saved anything!")
def save_tasks():
    label.config(text='')
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open(f"C:\\Users\\{os.getlogin()}\\Todo\\Todocache1.dat", "wb"))
    label.config(text='saved!')

listbox_tasks = tkinter.Listbox(root, height=10, width=40,bd=0,font=('Candara',15,'bold'),activestyle=NONE)
listbox_tasks.place(x=20,y=50)
entry_task = tkinter.Entry(root, width=40,font=('Arial',15,'bold'),bd=2)
entry_task.place(x=20,y=320)
button_add_task = tkinter.Button(root, text="Add", width=5,bd=2, command=add_task,activebackground=BG)
button_add_task.place(x=20,y=360)
button_delete_task = tkinter.Button(root, text="Delete",bd=2, width=5, command=delete_task,activebackground=BG)
button_delete_task.place(x=150,y=360)
button_load_tasks = tkinter.Button(root, text="Load",bd=2,width=5, command=load_tasks,activebackground=BG)
button_load_tasks.place(x=280,y=360)
button_save_tasks = tkinter.Button(root, text="Save", bd=2,width=5, command=save_tasks,activebackground=BG)
button_save_tasks.place(x=400,y=360)
timel=Label(root,font='calibri',bd=2,bg=BG,fg='white')
timel.pack()
label=Label(root,bg=BG,fg='white',bd=2,font=('Calibri',17,'bold'))
label.place(x=220,y=425)
root.bind('<Return>',add_task)
listbox_tasks.bind('<BackSpace>',delete_task)
root.bind('<Control-s>',save_tasks)
root.bind('<Control-l>', load_tasks)
root.bind('<Control-q>', quit)

time()
mainloop()
