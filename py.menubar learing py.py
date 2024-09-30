from tkinter import *
import turtle
win=Tk()
win.title("Python Training")
win.geometry("600x600")
win.config(bg="#cefcae")
####functionssss
def for_training():
    top1=Toplevel()
    top1.title("For Training")
    Label(top1,text="We will try to explain the ""FOR").pack()
def turtle_training():
    
   
    s=turtle.Screen()
    turtle.title("Colorful Shapes")
    turtle.screensize(500,600,bg="yellow")
    p=turtle.Pen()
    turtle.pensize(3)
    turtle.shape("turtle")
    turtle.pencolor("red")
#draw a triangle
    turtle.penup()
    turtle.goto(-200,-50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    turtle.circle(40,steps=3)
    turtle.end_fill()
#draw a square
    turtle.penup()
    turtle.goto(-100,-50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("brown")
    turtle.circle(40,steps=4)
    turtle.end_fill()
#draw a penta...
    turtle.penup()
    turtle.goto(0,-50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("green")
    for x in range(1,9):
        p.fd(50)
    
        p.left(225)
    turtle.end_fill()
#draw a hexagon
    turtle.penup()
    turtle.goto(100,-50)
    turtle.pendown()
    turtle.pen(fillcolor="green",pencolor="red",pensize=20)
    turtle.begin_fill()
    turtle.color("cyan")
    turtle.circle(40,steps=6)
    turtle.end_fill()
#draw a circle
    turtle.penup()
    turtle.goto(200,-50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("purple")
    turtle.circle(40)
    turtle.end_fill()
#header
    turtle.penup()
    turtle.goto(-100,50)
    turtle.pencolor("red")
    turtle.write("python is great",font=("tahoma",20,"bold"))
    turtle.hideturtle()
 
def vorood():
    top=Toplevel()
    top.title("Learning python in English")
    
    menubar=Menu(top)
    filemenu=Menu(menubar)
    filemenu.add_command(label="for training",command=for_training)
    filemenu.add_command(label="list training")
    filemenu.add_command(label="turtle training",command=turtle_training)
    menubar.add_cascade(label="primary education",menu=filemenu)
    top.config(menu=menubar)
########LABEL
LB1=Label(win,text="PYTHON TRAINING",font=("arial",20,"bold"),bd=30,bg="#fff993")
LB2=Label(win,text="We want to learn python together in this article",font=("arial",16,"bold"),bd=30,bg="#fff993")
LB3=Label(win,text="Choose your language to learn",font=("arial",14,"bold"),bd=30,bg="#fff993")
####BUTTON
b1=Button(win,text="English",font=("arial",16,"bold"),bd=10,command=vorood)
b2=Button(win,text=" فارسي ",font=("B Nazanin",14,"bold"),bd=10)
######  PLACE
LB1.place(x=500,y=30)
LB2.place(x=400,y=200)         
LB3.place(x=500,y=300)
b1.place(x=500,y=400)
b2.place(x=700,y=400)
