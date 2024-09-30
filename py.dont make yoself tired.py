from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

move_count=0

def move_cancel_button():
    global move_count
    move_count +=1
    if move_count>=5:
        messagebox.showinfo("پيام","خودتو خسته نکن الکي")
        move_count=0
    else:
        new_x=random.randint(10, 200)
        new_y=random.randint(10, 200)
        cancel_button.place(x=new_x, y=new_y)

def show_seconed_message():
    messagebox.showinfo("پيام","کلا موافقم")

#create the mian window
root=Tk()
root.geometry("700x700")
root.title("mister programmer")

header_label=Label(root,text="قبول داري خيلي خري",font=("Lalezar",22))
header_label.pack()


ok_button=Button(root,text="آره،معلومه",bg="green",fg="#fff",command=show_seconed_message)
ok_button.pack()

cancel_button=Button(root,text="نه،اصلا",bg="red",fg="#fff")
cancel_button.pack()

cancel_button.bind("<Enter>",lambda e:move_cancel_button())
#root.mianloop()
