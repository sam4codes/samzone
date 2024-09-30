from tkinter import *
from tkinter import ttk
win=Tk()
win.geometry("1300x650")
win.resizable(width=False, height=False)
win.title("Periodic table")
#win.icon(
win.config(bg="#212121")
#win.attributes('-fullscreen', True)

global dark_on
dark_on=True


bg="black"
fg="white"

def d_l():
   global dark_on

   if dark_on==True:
       bg="white"
       fg="black"
       print(bg,fg)
       dark_on=False
   else:
       bg="black"
       fg="white"
       
    
       dark_on=True
bt=Button(win,text="rad",command=d_l)
bt.place(x=200,y=300)


#msg for tommarow stick the VIIs to the table (close)
"""
darkslate

#212121
#3d3d3d


"""

#bg="#121212"




############################################





def newwin():
    win2 = Toplevel()
    window.geometry('100x100')
    newlabel = Label(window, text = "Settings Window")
    
    newlabel.pack()



###############################################################labels###############################################################

bg="#121212"
#fg="white"

G1=Label(text="IA    ",font=("Times",12,"bold"),bg=bg,fg=fg)
G2=Label(text="IIA   ",font=("Times",12,"bold"),bg=bg,fg=fg)
G3=Label(text="IIIB  ",font=("Times",12,"bold"),bg=bg,fg=fg)
G4=Label(text="IVB   ",font=("Times",12,"bold"),bg=bg,fg=fg)
G5=Label(text="VB    ",font=("Times",12,"bold"),bg=bg,fg=fg)
G6=Label(text="VIB   ",font=("Times",12,"bold"),bg=bg,fg=fg)
G7=Label(text="VIIB  ",font=("Times",12,"bold"),bg=bg,fg=fg)
G8=Label(text="VIII  ",font=("Times",12,"bold"),bg=bg,fg=fg)
G9=Label(text="VIII  ",font=("Times",12,"bold"),bg=bg,fg=fg)
G10=Label(text="VIII ",font=("Times",12,"bold"),bg=bg,fg=fg)
G11=Label(text="IB   ",font=("Times",12,"bold"),bg=bg,fg=fg)
G12=Label(text="IIB  ",font=("Times",12,"bold"),bg=bg,fg=fg)
G13=Label(text="IIIA ",font=("Times",12,"bold"),bg=bg,fg=fg)
G14=Label(text="IVA  ",font=("Times",12,"bold"),bg=bg,fg=fg)
G15=Label(text="VA   ",font=("Times",12,"bold"),bg=bg,fg=fg)
G16=Label(text="VIA  ",font=("Times",12,"bold"),bg=bg,fg=fg)
G17=Label(text="VIIA ",font=("Times",12,"bold"),bg=bg,fg=fg)
G18=Label(text="VIIIA",font=("Times",12,"bold"),bg=bg,fg=fg)
####_________
n1=Label(text="n=1",font=("Times",15,"bold"),bg=bg,fg=fg)
n2=Label(text="n=2",font=("Times",15,"bold"),bg=bg,fg=fg)
n3=Label(text="n=3",font=("Times",15,"bold"),bg=bg,fg=fg)
n4=Label(text="n=4",font=("Times",15,"bold"),bg=bg,fg=fg)
n5=Label(text="n=5",font=("Times",15,"bold"),bg=bg,fg=fg)
n6=Label(text="n=6",font=("Times",15,"bold"),bg=bg,fg=fg)
n7=Label(text="n=7",font=("Times",15,"bold"),bg=bg,fg=fg)


###############################################################buttons###############################################################    
#G1
H=Button(win, text="H",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Li=Button(win, text="Li",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Na=Button(win, text="Na",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
K=Button(win, text="K",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Rb=Button(win, text="Rb",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Cs=Button(win, text="Cs",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Fr=Button(win, text="Fr",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G2
Be=Button(win, text="Be",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Mg=Button(win, text="Mg",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ca=Button(win, text="Ca",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Sr=Button(win, text="Sr",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ba=Button(win, text="Ba",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ra=Button(win, text="Ra",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G3
Sc=Button(win, text="Sc",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Y=Button(win, text="Y",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Lu=Button(win, text="Lu",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Lr=Button(win, text="Lr",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G4
Ti=Button(win, text="Ti",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Zr=Button(win, text="Zr",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Hf=Button(win, text="Hf",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Rf=Button(win, text="Rf",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G5
V=Button(win, text="V",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Nb=Button(win, text="Nb",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ta=Button(win, text="Ta",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Db=Button(win, text="Db",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G6
Cr=Button(win, text="Cr",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Mo=Button(win, text="Mo",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
W=Button(win, text="W",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Sg=Button(win, text="Sg",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G7
Mn=Button(win, text="Mn",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Tc=Button(win, text="Tc",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Re=Button(win, text="Re",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Bh=Button(win, text="Bh",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G8
Fe=Button(win, text="Fe",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ru=Button(win, text="Ru",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Os=Button(win, text="Os",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Hs=Button(win, text="Hs",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G9
Co=Button(win, text="Co",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Rh=Button(win, text="Rh",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ir=Button(win, text="Ir",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Mt=Button(win, text="Mt",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G10
Ni=Button(win, text="Ni",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Pd=Button(win, text="Pd",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Pt=Button(win, text="Pt",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ds=Button(win, text="Ds",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G11
Cu=Button(win, text="Cu",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ag=Button(win, text="Ag",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Au=Button(win, text="Au",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Rg=Button(win, text="Rg",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G12
Zn=Button(win, text="Zn",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Cd=Button(win, text="Cd",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Hg=Button(win, text="Hg",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Cn=Button(win, text="Cn",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G13
B=Button(win, text="B",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Al=Button(win, text="Al",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ga=Button(win, text="Ga",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
In=Button(win, text="In",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Tl=Button(win, text="Tl",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Nh=Button(win, text="Nh",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G14
C=Button(win, text="C",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Si=Button(win, text="Si",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ge=Button(win, text="Ge",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Sn=Button(win, text="Sn",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Pb=Button(win, text="Pb",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Fl=Button(win, text="Fl",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G15
N=Button(win, text="N",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
P=Button(win, text="P",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
As=Button(win, text="As",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Sb=Button(win, text="Sb",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Bi=Button(win, text="Bi",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Mc=Button(win, text="Mc",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G16
O=Button(win, text="O",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
S=Button(win, text="S",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Se=Button(win, text="Se",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Te=Button(win, text="Te",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Po=Button(win, text="Po",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Lv=Button(win, text="Lv",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G17
F=Button(win, text="F",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Cl=Button(win, text="Cl",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Br=Button(win, text="Br",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
I=Button(win, text="I",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
At=Button(win, text="At",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ts=Button(win, text="Ts",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#G18
He=Button(win, text="He",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ne=Button(win, text="Ne",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ar=Button(win, text="Ar",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Kr=Button(win, text="Kr",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Xe=Button(win, text="Xe",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Rn=Button(win, text="Rn",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Og=Button(win, text="Og",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
####################################################F1
La=Button(win, text="La",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ce=Button(win, text="Ce",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Pr=Button(win, text="Pr",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Nd=Button(win, text="Nd",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Pm=Button(win, text="Pm",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Sm=Button(win, text="Sm",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Eu=Button(win, text="Eu",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Gd=Button(win, text="Gd",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Tb=Button(win, text="Tb",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Dy=Button(win, text="Dy",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Ho=Button(win, text="Ho",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Er=Button(win, text="Er",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Tm=Button(win, text="Tm",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Yb=Button(win, text="Yb",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
#####################################################F2
Ac=Button(win, text="Ac",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Th=Button(win, text="Th",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Pa=Button(win, text="Pa",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
U=Button(win, text="U",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Np=Button(win, text="Np",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Pu=Button(win, text="Pu",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Am=Button(win, text="Am",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Cm=Button(win, text="Cm",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Bk=Button(win, text="Bk",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Cf=Button(win, text="Cf",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Es=Button(win, text="Es",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Fm=Button(win, text="Fm",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
Md=Button(win, text="Md",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,pady=1.3,borderwidth=0)
No=Button(win, text="No",font=("Helvatica",19,"bold"), bg="#00c80c", fg="white", justify="center",width=1,height=1,padx=11.7,borderwidth=0)
###############################################################places#################################################################
n=60#xseed60 for entire pos
z=110#yseed110 for entire pos
#the point is to make developing easier and fasgter with more efficency
i=47
#i is 48 (x cordination multiplier) space between groups
j=54#j is 54 (y cordination multiplier)
f=-40#the f block distance from the table (neg)40

nd=-52 #d stands for distance and is the distance till G1
gd=-50  #distance till n+1
####labels
G1.place(x=n,y=z+gd)
G2.place(x=n+i,y=z+gd)
G3.place(x=n+2*i,y=z+gd)
G4.place(x=n+3*i,y=z+gd)
G5.place(x=n+4*i,y=z+gd)
G6.place(x=n+5*i,y=z+gd)
G7.place(x=n+6*i,y=z+gd)
G8.place(x=n+7*i,y=z+gd)
G9.place(x=n+8*i,y=z+gd)
G10.place(x=n+9*i,y=z+gd)
G11.place(x=n+10*i,y=z+gd)
G12.place(x=n+11*i,y=z+gd)
G13.place(x=n+12*i,y=z+gd)
G14.place(x=n+13*i,y=z+gd)
G15.place(x=n+14*i,y=z+gd)
G16.place(x=n+15*i,y=z+gd)
G17.place(x=n+16*i,y=z+gd)
G18.place(x=n+17*i,y=z+gd)
#===============
n1.place(x=n+nd,y=z+10)
n2.place(x=n+nd,y=z+j+10)
n3.place(x=n+nd,y=z+2*j+10)
n4.place(x=n+nd,y=z+3*j+10)
n5.place(x=n+nd,y=z+4*j+10)
n6.place(x=n+nd,y=z+5*j+10)
n7.place(x=n+nd,y=z+6*j+10)
#G1
H.place(x=n,y=z)
Li.place(x=n,y=z+j)
Na.place(x=n,y=z+2*j)
K.place(x=n,y=z+3*j)
Rb.place(x=n,y=z+4*j)
Cs.place(x=n,y=z+5*j)
Fr.place(x=n,y=z+6*j)
#G2
Be.place(x=n+i,y=z+j)
Mg.place(x=n+i,y=z+2*j)
Ca.place(x=n+i,y=z+3*j)
Sr.place(x=n+i,y=z+4*j)
Ba.place(x=n+i,y=z+5*j)
Ra.place(x=n+i,y=z+6*j)
#G3
Sc.place(x=n+2*i,y=z+3*j)
Y.place(x=n+2*i,y=z+4*j)
Lu.place(x=n+2*i,y=z+5*j)
Lr.place(x=n+2*i,y=z+6*j)
#G4
Ti.place(x=n+3*i,y=z+3*j)
Zr.place(x=n+3*i,y=z+4*j)
Hf.place(x=n+3*i,y=z+5*j)
Rf.place(x=n+3*i,y=z+6*j)
#G5
V.place(x=n+4*i,y=z+3*j)
Nb.place(x=n+4*i,y=z+4*j)
Ta.place(x=n+4*i,y=z+5*j)
Db.place(x=n+4*i,y=z+6*j)
#G6
Cr.place(x=n+5*i,y=z+3*j)
Mo.place(x=n+5*i,y=z+4*j)
W.place(x=n+5*i,y=z+5*j)
Sg.place(x=n+5*i,y=z+6*j)
#G7
Mn.place(x=n+6*i,y=z+3*j)
Tc.place(x=n+6*i,y=z+4*j)
Re.place(x=n+6*i,y=z+5*j)
Bh.place(x=n+6*i,y=z+6*j)
#G8
Fe.place(x=n+7*i,y=z+3*j)
Ru.place(x=n+7*i,y=z+4*j)
Os.place(x=n+7*i,y=z+5*j)
Hs.place(x=n+7*i,y=z+6*j)
#G9
Co.place(x=n+8*i,y=z+3*j)
Rh.place(x=n+8*i,y=z+4*j)
Ir.place(x=n+8*i,y=z+5*j)
Mt.place(x=n+8*i,y=z+6*j)
#G10
Ni.place(x=n+9*i,y=z+3*j)
Pd.place(x=n+9*i,y=z+4*j)
Pt.place(x=n+9*i,y=z+5*j)
Ds.place(x=n+9*i,y=z+6*j)
#G11
Cu.place(x=n+10*i,y=z+3*j)
Ag.place(x=n+10*i,y=z+4*j)
Au.place(x=n+10*i,y=z+5*j)
Rg.place(x=n+10*i,y=z+6*j)
#G12
Zn.place(x=n+11*i,y=z+3*j)
Cd.place(x=n+11*i,y=z+4*j)
Hg.place(x=n+11*i,y=z+5*j)
Cn.place(x=n+11*i,y=z+6*j)
#G13
B.place(x=n+12*i,y=z+j)
Al.place(x=n+12*i,y=z+2*j)
Ga.place(x=n+12*i,y=z+3*j)
In.place(x=n+12*i,y=z+4*j)
Tl.place(x=n+12*i,y=z+5*j)
Nh.place(x=n+12*i,y=z+6*j)
#G14
C.place(x=n+13*i,y=z+j)
Si.place(x=n+13*i,y=z+2*j)
Ge.place(x=n+13*i,y=z+3*j)
Sn.place(x=n+13*i,y=z+4*j)
Pb.place(x=n+13*i,y=z+5*j)
Fl.place(x=n+13*i,y=z+6*j)
#G15
N.place(x=n+14*i,y=z+j)
P.place(x=n+14*i,y=z+2*j)
As.place(x=n+14*i,y=z+3*j)
Sb.place(x=n+14*i,y=z+4*j)
Bi.place(x=n+14*i,y=z+5*j)
Mc.place(x=n+14*i,y=z+6*j)
#G16
O.place(x=n+15*i,y=z+j)
S.place(x=n+15*i,y=z+2*j)
Se.place(x=n+15*i,y=z+3*j)
Te.place(x=n+15*i,y=z+4*j)
Po.place(x=n+15*i,y=z+5*j)
Lv.place(x=n+15*i,y=z+6*j)
#G17
F.place(x=n+16*i,y=z+j)
Cl.place(x=n+16*i,y=z+2*j)
Br.place(x=n+16*i,y=z+3*j)
I.place(x=n+16*i,y=z+4*j)
At.place(x=n+16*i,y=z+5*j)
Ts.place(x=n+16*i,y=z+6*j)
#G18
He.place(x=n+17*i,y=z)
Ne.place(x=n+17*i,y=z+j)
Ar.place(x=n+17*i,y=z+2*j)
Kr.place(x=n+17*i,y=z+3*j)
Xe.place(x=n+17*i,y=z+4*j)
Rn.place(x=n+17*i,y=z+5*j)
Og.place(x=n+17*i,y=z+6
         *j)
#F1#########
La.place(x=n+2*i,y=z+8*j+f)
Ce.place(x=n+3*i,y=z+8*j+f)
Pr.place(x=n+4*i,y=z+8*j+f)
Nd.place(x=n+5*i,y=z+8*j+f)
Pm.place(x=n+6*i,y=z+8*j+f)
Sm.place(x=n+7*i,y=z+8*j+f)
Eu.place(x=n+8*i,y=z+8*j+f)
Gd.place(x=n+9*i,y=z+8*j+f)
Tb.place(x=n+10*i,y=z+8*j+f)
Dy.place(x=n+11*i,y=z+8*j+f)
Ho.place(x=n+12*i,y=z+8*j+f)
Er.place(x=n+13*i,y=z+8*j+f)
Tm.place(x=n+14*i,y=z+8*j+f)
Yb.place(x=n+15*i,y=z+8*j+f)
#F2
Ac.place(x=n+2*i,y=z+9*j+f)
Th.place(x=n+3*i,y=z+9*j+f)
Pa.place(x=n+4*i,y=z+9*j+f)
U.place(x=n+5*i,y=z+9*j+f)
Np.place(x=n+6*i,y=z+9*j+f)
Pu.place(x=n+7*i,y=z+9*j+f)
Am.place(x=n+8*i,y=z+9*j+f)
Cm.place(x=n+9*i,y=z+9*j+f)
Bk.place(x=n+10*i,y=z+9*j+f)
Cf.place(x=n+11*i,y=z+9*j+f)
Es.place(x=n+12*i,y=z+9*j+f)
Fm.place(x=n+13*i,y=z+9*j+f)
Md.place(x=n+14*i,y=z+9*j+f)
No.place(x=n+15*i,y=z+9*j+f)












