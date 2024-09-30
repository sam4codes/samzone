from tkinter import *
from tkinter.ttk import Labelframe
from tkinter import filedialog,messagebox
import random
import time
#functions

def reset():
    textreceipt.delete(1.0,END)
    e_rice.set('0')
    e_ghorme.set('0')
    e_gheime.set('0')
    e_ash.set('0')
    e_sabzi.set('0')
    e_tah.set('0')
    e_ghali.set('0')
    e_fes.set('0')
    e_chelo.set('0')
    
    e_tea.set('0')
    e_khak.set('0')
    e_tokhm.set('0')
    e_doogh.set('0')
    e_khiar.set('0')
    e_dam.set('0')
    e_aragh.set('0')
    e_bahar.set('0')
    e_ab.set('0')
    
    e_shole.set('0')
    e_yazdi.set('0')
    e_halva.set('0')
    e_faloode.set('0')
    e_koolooch.set('0')
    e_baghlava.set('0')
    e_rangin.set('0')
    e_gaz.set('0')
    e_sohan.set('0')
    textrice.config(state=DISABLED)
    textchelo.config(state=DISABLED)
    textghorme.config(state=DISABLED)
    textgheime.config(state=DISABLED)
    textash.config(state=DISABLED)
    textsabzi.config(state=DISABLED)
    texttah.config(state=DISABLED)
    textghali.config(state=DISABLED)
    textfes.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textkhak.config(state=DISABLED)
    textkhiar.config(state=DISABLED)
    textdoogh.config(state=DISABLED)
    textaragh.config(state=DISABLED)
    textbahar.config(state=DISABLED)
    texttokhm.config(state=DISABLED)
    textdam.config(state=DISABLED)
    textab.config(state=DISABLED)
    textshole.config(state=DISABLED)
    textyazdi.config(state=DISABLED)
    texthalva.config(state=DISABLED)
    textbaghlava.config(state=DISABLED)
    textrangin.config(state=DISABLED)
    textgaz.config(state=DISABLED)
    textsohan.config(state=DISABLED)
    textkoolooch.config(state=DISABLED)
    textfaloode.config(state=DISABLED)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    resvar.set(0)
    costoffoodvar.set('')
    costofdrinkvar.set('')
    costofdesertvar.set('')
    subtotalvar.set('')
    totalcostvar.set('')
    servicetaxvar.set('')
    
    
    
     
def send_msg():
    messagetext=textarea.get(1.0,END)
    phonenumber=numberfield.get()
def send():
    global textarea,numberfield
    root2=Toplevel()
    root2.title('Send Bill')
    root2.config(bg='red4')
    root2.geometry('485x620+50+50')
    logoimage=PhotoImage(file='gol3.png')
    label0=Label(root2,image=logoimage,bg='red4',fg='red4')
    label0.pack(pady=5)
    numberlabel=Label(root2,text='Phone Number',font=('arial',18,'bold underline'),bg='red4',fg='black')
    numberlabel.pack(pady=5)
    numberfield=Entry(root2,font=('arial',22),bd=3,width=24)
    numberfield.pack(pady=5)

    billlabel=Label(root2,text='Bill Details',font=('arial',18,'bold underline'),bg='red4',fg='black')
    billlabel.pack(pady=5)
    textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textarea.pack(pady=5)
    sendbutton=Button(root2,text="Send",font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief='groove',command=send_msg)
    sendbutton.pack(pady=5)
    textarea.insert(END,'Receipt Rf:\t\t'+str(billnumber)+'\t\t'+str(date)+'\n\n')
    if costoffoodvar.get()!='0 Toman':
        textarea.insert(END,'Cost of Food: \t\t'+str(priceoffood)+' Toman\n')
    if costofdrinkvar.get()!='0 Toman':
        textarea.insert(END,'Cost of Drink(s): \t\t'+str(priceofdrink)+' Toman\n')
    if costofdesertvar.get()!='0 Toman':
        textarea.insert(END,'Cost of Desert(s): \t\t'+str(priceofdesert)+' Toman\n\n')
    textarea.insert(END,'Sub Total: \t\t'+str(subttotalofitems)+' Toman\n')
    textarea.insert(END,'Service Tax: \t\t'+str(int(servicetaxprice))+' Toman\n')
    if resvar.get()==1:
        textarea.insert(END,'Reservation Cost: \t\t'+str(int(res(subttotalofitems)))+' Toman\n')
    textarea.insert(END,'Total Cost: \t\t'+str(int(totalprice))+' Toman\n')
    root2.mainloop()



def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    bill_data=textreceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Info','Your bill has been successfully saved!')

def freceipt():
    global billnumber,date
    textreceipt.delete(1.0,END)
    x=random.randint(100,10000)
    billnumber="BILL"+str(x)
    date=time.strftime('%d/%m/%Y')
    textreceipt.insert(END,'Receipt Ref:  \t'+billnumber+'\t\t    '+date+'\n')
    textreceipt.insert(END,'************************************\n')
    textreceipt.insert(END,'Items \t\t    Cost of Items(Toman)\n')
    textreceipt.insert(END,'------------------------------------------------------\n')
    if e_rice.get()!='0':
        textreceipt.insert(END,'Rice and Tahdig\t\t\t'+str(int(e_rice.get())*50000)+'\n')
    if e_chelo.get()!='0':
        textreceipt.insert(END,'Chelo Kebab\t\t\t'+str(int(e_chelo.get())*120000)+'\n')
    if e_ghorme.get()!='0':
        textreceipt.insert(END,'Ghormeh Sabzi\t\t\t'+str(int(e_ghorme.get())*60000)+'\n')
    if e_gheime.get()!='0':
        textreceipt.insert(END,'Gheimeh\t\t\t'+str(int(e_gheime.get())*60000)+'\n')
    if e_ash.get()!='0':
        textreceipt.insert(END,'Ash Reshteh\t\t\t'+str(int(e_ash.get())*30000)+'\n')
    if e_sabzi.get()!='0':
        textreceipt.insert(END,'Koo Koo Sabzi\t\t\t'+str(int(e_sabzi.get())*40000)+'\n')
    if e_tah.get()!='0':
        textreceipt.insert(END,'Tahchin\t\t\t'+str(int(e_tah.get())*70000)+'\n')
    if e_ghali.get()!='0':
        textreceipt.insert(END,'Ghalie Mahi\t\t\t'+str(int(e_ghali.get())*100000)+'\n')
    if e_fes.get()!='0':
        textreceipt.insert(END,'Khoresh-e Fesenjan\t\t\t'+str(int(e_fes.get())*120000)+'\n')
    if e_tea.get()!='0':
        textreceipt.insert(END,'Persian Tea\t\t\t'+str(int(e_tea.get())*15000)+'\n')
    if e_khak.get()!='0':
        textreceipt.insert(END,'Khakshir\t\t\t'+str(int(e_khak.get())*12000)+'\n')
    if e_tokhm.get()!='0':
        textreceipt.insert(END,'Tokhme-Sharbati\t\t\t'+str(int(e_tokhm.get())*12000)+'\n')
    if e_doogh.get()!='0':
        textreceipt.insert(END,'Doogh\t\t\t'+str(int(e_doogh.get())*15000)+'\n')
    if e_khiar.get()!='0':
        textreceipt.insert(END,'Khiar-Sekanjabin\t\t\t'+str(int(e_khiar.get())*15000)+'\n')
    if e_dam.get()!='0':
        textreceipt.insert(END,'Damnoosh\t\t\t'+str(int(e_dam.get())*20000)+'\n')
    if e_aragh.get()!='0':
        textreceipt.insert(END,'Araghijat\t\t\t'+str(int(e_aragh.get())*20000)+'\n')
    if e_bahar.get()!='0':
        textreceipt.insert(END,'Bahar-Narenj\t\t\t'+str(int(e_bahar.get())*30000)+'\n')
    if e_ab.get()!='0':
        textreceipt.insert(END,'Water\t\t\t'+str(int(e_ab.get())*5000)+'\n')
    if e_shole.get()!='0':
        textreceipt.insert(END,'Sholeh Zard\t\t\t'+str(int(e_shole.get())*30000)+'\n')
    if e_yazdi.get()!='0':
        textreceipt.insert(END,'Shirini Yazdi\t\t\t'+str(int(e_yazdi.get())*12000)+'\n')
    if e_halva.get()!='0':
        textreceipt.insert(END,'Halva\t\t\t'+str(int(e_halva.get())*25000)+'\n')
    if e_faloode.get()!='0':
        textreceipt.insert(END,'Faloodeh Shirazi\t\t\t'+str(int(e_faloode.get())*15000)+'\n')
    if e_koolooch.get()!='0':
        textreceipt.insert(END,'Kooloocheh\t\t\t'+str(int(e_koolooch.get())*10000)+'\n')
    if e_baghlava.get()!='0':
        textreceipt.insert(END,'Baghlava\t\t\t'+str(int(e_baghlava.get())*30000)+'\n')
    if e_rangin.get()!='0':
        textreceipt.insert(END,'Ranginak\t\t\t'+str(int(e_rangin.get())*20000)+'\n')
    if e_gaz.get()!='0':
        textreceipt.insert(END,'Gaz\t\t\t'+str(int(e_gaz.get())*15000)+'\n')
    if e_sohan.get()!='0':
        textreceipt.insert(END,'Sohan\t\t\t'+str(int(e_sohan.get())*20000)+'\n')
    textreceipt.insert(END,'------------------------------------------------------\n\n')
    if costoffoodvar.get()!='0 Toman':
        textreceipt.insert(END,'Cost of Food: \t\t'+str(priceoffood)+' Toman\n')
    if costofdrinkvar.get()!='0 Toman':
        textreceipt.insert(END,'Cost of Drink(s): \t\t'+str(priceofdrink)+' Toman\n')
    if costofdesertvar.get()!='0 Toman':
        textreceipt.insert(END,'Cost of Desert(s): \t\t'+str(priceofdesert)+' Toman\n\n')
    textreceipt.insert(END,'Sub Total: \t\t'+str(subttotalofitems)+' Toman\n')
    textreceipt.insert(END,'Service Tax: \t\t'+str(int(servicetaxprice))+' Toman\n')
    if resvar.get()==1:
        textreceipt.insert(END,'Reservation Cost: \t\t'+str(int(res(subttotalofitems)))+' Toman\n')
    textreceipt.insert(END,'Total Cost: \t\t'+str(int(totalprice))+' Toman\n')
def res(A):
    b=A/10**4
    A0=str(A)
    A1=len(A0)
    t=(1/b)*10**A1
    return t

def ftotal():
    
    global priceoffood,priceofdrink,priceofdesert,subttotalofitems,servicetaxprice,totalprice
    item1=int(e_rice.get())
    item2=int(e_chelo.get())
    item3=int(e_ghorme.get())
    item4=int(e_gheime.get())
    item5=int(e_ash.get())
    item6=int(e_sabzi.get())
    item7=int(e_tah.get())
    item8=int(e_ghali.get())
    item9=int(e_fes.get())
    
    item10=int(e_tea.get())
    item11=int(e_khak.get())
    item12=int(e_tokhm.get())
    item13=int(e_doogh.get())
    item14=int(e_khiar.get())
    item15=int(e_dam.get())
    item16=int(e_aragh.get())
    item17=int(e_bahar.get())
    item18=int(e_ab.get())
    
    item19=int(e_shole.get())
    item20=int(e_yazdi.get())
    item21=int(e_halva.get())
    item22=int(e_faloode.get())
    item23=int(e_koolooch.get())
    item24=int(e_baghlava.get())
    item25=int(e_rangin.get())
    item26=int(e_gaz.get())
    item27=int(e_sohan.get())
    
    priceoffood=(item1*50000)+(item2*120000)+(item3*60000)+(item4*60000)+(item5*30000)+(item6*40000)+(item7*70000)+(item8*100000)+(item9*120000)
    priceofdrink=(item10*15000)+(item11*12000)+(item12*12000)+(item13*15000)+(item14*15000)+(item15*20000)+(item16*20000)+(item17*30000)+(item18*5000)
    priceofdesert=(item19*30000)+(item20*12000)+(item21*25000)+(item22*15000)+(item23*10000)+(item24*30000)+(item25*20000)+(item26*15000)+(item27*20000)

    costoffoodvar.set(str(priceoffood)+' Toman')
    costofdrinkvar.set(str(priceofdrink)+' Toman')
    costofdesertvar.set(str(priceofdesert)+' Toman')

    subttotalofitems=priceoffood+priceofdrink+priceofdesert
    subtotalvar.set(str(subttotalofitems)+' Toman')

    servicetaxprice=0.1*subttotalofitems
    servicetaxvar.set(str(int(servicetaxprice))+" Toman")
    if resvar.get()==1:
       totalprice= subttotalofitems+servicetaxprice+res(subttotalofitems)
    else:
        totalprice=subttotalofitems+servicetaxprice

    totalcostvar.set(str(int(totalprice))+' Toman')

def frice():
    if var1.get()==1:
        textrice.config(state=NORMAL)
        textrice.delete(0,END)
        textrice.focus()
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')


def fchelo():
    if var2.get()==1:
        textchelo.config(state=NORMAL)
        textchelo.delete(0,END)
        textchelo.focus()
    else:
        textchelo.config(state=DISABLED)
        e_chelo.set('0')

def fghorme():
    if var3.get()==1:
        textghorme.config(state=NORMAL)
        textghorme.delete(0,END)
        textghorme.focus()
    else:
        textghorme.config(state=DISABLED)
        e_ghorme.set('0')

def fgheime():
    if var4.get()==1:
        textgheime.config(state=NORMAL)
        textgheime.delete(0,END)
        textgheime.focus()
    else:
        textgheime.config(state=DISABLED)
        e_gheime.set('0')

def fash():
    if var5.get()==1:
        textash.config(state=NORMAL)
        textash.delete(0,END)
        textash.focus()
    else:
        textash.config(state=DISABLED)
        e_ash.set('0')

def fsabzi():
    if var6.get()==1:
        textsabzi.config(state=NORMAL)
        textsabzi.delete(0,END)
        textsabzi.focus()
    else:
        textsabzi.config(state=DISABLED)
        e_sabzi.set('0')

def ftah():
    if var7.get()==1:
        texttah.config(state=NORMAL)
        texttah.delete(0,END)
        texttah.focus()
    else:
        texttah.config(state=DISABLED)
        e_tah.set('0')

def fghali():
    if var8.get()==1:
        textghali.config(state=NORMAL)
        textghali.delete(0,END)
        textghali.focus()
    else:
        textghali.config(state=DISABLED)
        e_ghali.set('0')

def ffes():
    if var9.get()==1:
        textfes.config(state=NORMAL)
        textfes.delete(0,END)
        textfes.focus()
    else:
        textfes.config(state=DISABLED)
        e_fes.set('0')

def ftea():
    if var10.get()==1:
        texttea.config(state=NORMAL)
        texttea.delete(0,END)
        texttea.focus()
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')

def fkhak():
    if var11.get()==1:
        textkhak.config(state=NORMAL)
        textkhak.delete(0,END)
        textkhak.focus()
    else:
        textkhak.config(state=DISABLED)
        e_khak.set('0')

def ftokhm():
    if var12.get()==1:
        texttokhm.config(state=NORMAL)
        texttokhm.delete(0,END)
        texttokhm.focus()
    else:
        texttokhm.config(state=DISABLED)
        e_tokhm.set('0')

def fdoogh():
    if var13.get()==1:
        textdoogh.config(state=NORMAL)
        textdoogh.delete(0,END)
        textdoogh.focus()
    else:
        textdoogh.config(state=DISABLED)
        e_doogh.set('0')

def fkhiar():
    if var14.get()==1:
        textkhiar.config(state=NORMAL)
        textkhiar.delete(0,END)
        textkhiar.focus()
    else:
        textkhiar.config(state=DISABLED)
        e_khiar.set('0')

def fdam():
    if var15.get()==1:
        textdam.config(state=NORMAL)
        textdam.delete(0,END)
        textdam.focus()
    else:
        textdam.config(state=DISABLED)
        e_dam.set('0')

def faragh():
    if var16.get()==1:
        textaragh.config(state=NORMAL)
        textaragh.delete(0,END)
        textaragh.focus()
    else:
        textaragh.config(state=DISABLED)
        e_aragh.set('0')

def fbahar():
    if var17.get()==1:
        textbahar.config(state=NORMAL)
        textbahar.delete(0,END)
        textbahar.focus()
    else:
        textbahar.config(state=DISABLED)
        e_bahar.set('0')

def fab():
    if var18.get()==1:
        textab.config(state=NORMAL)
        textab.delete(0,END)
        textab.focus()
    else:
        textab.config(state=DISABLED)
        e_ab.set('0')       

def fshole():
    if var19.get()==1:
        textshole.config(state=NORMAL)
        textshole.delete(0,END)
        textshole.focus()
    else:
        textshole.config(state=DISABLED)
        e_shole.set('0')

def fyazdi():
    if var20.get()==1:
        textyazdi.config(state=NORMAL)
        textyazdi.delete(0,END)
        textyazdi.focus()
    else:
        textyazdi.config(state=DISABLED)
        e_yazdi.set('0')

def fhalva():
    if var21.get()==1:
        texthalva.config(state=NORMAL)
        texthalva.delete(0,END)
        texthalva.focus()
    else:
        texthalva.config(state=DISABLED)
        e_halva.set('0')

def ffaloode():
    if var22.get()==1:
        textfaloode.config(state=NORMAL)
        textfaloode.delete(0,END)
        textfaloode.focus()
    else:
        textfaloode.config(state=DISABLED)
        e_faloode.set('0') 

def fkoolooch():
    if var23.get()==1:
        textkoolooch.config(state=NORMAL)
        textkoolooch.delete(0,END)
        textkoolooch.focus()
    else:
        textkoolooch.config(state=DISABLED)
        e_koolooch.set('0')

def fbaghlava():
    if var24.get()==1:
        textbaghlava.config(state=NORMAL)
        textbaghlava.delete(0,END)
        textbaghlava.focus()
    else:
        textbaghlava.config(state=DISABLED)
        e_baghlava.set('0')

def frangin():
    if var25.get()==1:
        textrangin.config(state=NORMAL)
        textrangin.delete(0,END)
        textrangin.focus()
    else:
        textrangin.config(state=DISABLED)
        e_rangin.set('0')

def fgaz():
    if var26.get()==1:
        textgaz.config(state=NORMAL)
        textgaz.delete(0,END)
        textgaz.focus()
    else:
        textgaz.config(state=DISABLED)
        e_gaz.set('0')

def fsohan():
    if var27.get()==1:
        textsohan.config(state=NORMAL)
        textsohan.delete(0,END)
        textsohan.focus()
    else:
        textsohan.config(state=DISABLED)
        e_sohan.set('0')








#main window

r=Tk()
r.geometry('1375x690+0+5')
r.resizable(0,0)
r.title('Restaurant Management System')
r.config(bg='firebrick4')

#topframe

topframe=Frame(r,bd=10,relief='ridge',bg='firebrick4',padx=80)
topframe.pack(side=TOP)
LF=Label(topframe,text='Restaurant Management System',font=('Times New Roman',30,'bold'),fg='yellow',bg='firebrick4',bd=9,width=51)
LF.grid(row=0,column=0)

#menu frame

menuframe=Frame(r,relief='ridge',bd=10,bg='firebrick4')
menuframe.pack(side=LEFT)
costframe=Frame(menuframe,bd=4,relief='ridge',bg='firebrick4')
costframe.pack(side=BOTTOM,ipadx=60)
Foodframe=LabelFrame(menuframe,text="Food", font=('Harlow Solid Italic',20,'bold'),bd=10,relief='ridge',fg='red4',pady=40)
Foodframe.pack(side=LEFT)
Drinkframe=LabelFrame(menuframe,text="Drink", font=('Harlow Solid Italic',20,'bold'),bd=10,relief='ridge',fg='blue',pady=40)
Drinkframe.pack(side=LEFT)
Desertframe=LabelFrame(menuframe,text="Desert", font=('Harlow Solid Italic',20,'bold'),bd=10,relief='ridge',fg='deeppink',pady=40)
Desertframe.pack(side=LEFT)

#right frame

rightframe=Frame(r,relief='ridge',bd=15,bg='red4')
rightframe.pack(side=RIGHT)
cframe=Frame(rightframe,bd=1,relief='ridge',bg='red4')
cframe.pack()
receiptframe=Frame(rightframe,bd=4,relief='ridge',bg='red4')
receiptframe.pack()
buttonsframe=Frame(rightframe,bd=3,relief='ridge',bg='red4')
buttonsframe.pack()

#variables 

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_rice=StringVar()
e_chelo=StringVar()
e_ghorme=StringVar()
e_gheime=StringVar()
e_ash=StringVar()
e_sabzi=StringVar()
e_tah=StringVar()
e_ghali=StringVar()
e_fes=StringVar()

e_tea=StringVar()
e_khak=StringVar()
e_tokhm=StringVar()
e_doogh=StringVar()
e_khiar=StringVar()
e_dam=StringVar()
e_aragh=StringVar()
e_bahar=StringVar()
e_ab=StringVar()

e_shole=StringVar()
e_yazdi=StringVar()
e_halva=StringVar()
e_faloode=StringVar()
e_koolooch=StringVar()
e_baghlava=StringVar()
e_rangin=StringVar()
e_gaz=StringVar()
e_sohan=StringVar()

costoffoodvar=StringVar()
costofdrinkvar=StringVar()
costofdesertvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

#set to zero entries

e_rice.set('0')
e_chelo.set('0')
e_ghorme.set('0')
e_gheime.set('0')
e_ash.set('0')
e_sabzi.set('0')
e_tah.set('0')
e_ghali.set('0')
e_fes.set('0')

e_tea.set('0')
e_khak.set('0')
e_tokhm.set('0')
e_doogh.set('0')
e_khiar.set('0')
e_dam.set('0')
e_aragh.set('0')
e_bahar.set('0')
e_ab.set('0')

e_shole.set('0')
e_yazdi.set('0')
e_halva.set('0')
e_faloode.set('0')
e_koolooch.set('0')
e_baghlava.set('0')
e_rangin.set('0')
e_gaz.set('0')
e_sohan.set('0')


#food

rice=Checkbutton(Foodframe,text='Rice and Tahdig',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var1,command=frice)
rice.grid(row=0,column=0,sticky=W)
chelo=Checkbutton(Foodframe,text='Chelo Kebab',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var2,command=fchelo)
chelo.grid(row=1,column=0,sticky=W)
ghorme=Checkbutton(Foodframe,text='Ghormeh Sabzi',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var3,command=fghorme)
ghorme.grid(row=2,column=0,sticky=W)
gheime=Checkbutton(Foodframe,text='Gheimeh',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var4,command=fgheime)
gheime.grid(row=3,column=0,sticky=W)
ash=Checkbutton(Foodframe,text='Ash Reshteh',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var5,command=fash)
ash.grid(row=4,column=0,sticky=W)
sabzi=Checkbutton(Foodframe,text='Koo Koo Sabzi ',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var6,command=fsabzi)
sabzi.grid(row=5,column=0,sticky=W)
tah=Checkbutton(Foodframe,text='Tahchin',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var7,command=ftah)
tah.grid(row=6,column=0,sticky=W)
ghali=Checkbutton(Foodframe,text='Ghalie Mahi',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var8,command=fghali)
ghali.grid(row=7,column=0,sticky=W)
fes=Checkbutton(Foodframe,text='Khoresh-e Fesenjan',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var9,command=ffes)
fes.grid(row=8,column=0,sticky=W)

#entry for foods

textrice=Entry(Foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rice)
textrice.grid(row=0,column=1)
textchelo=Entry(Foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chelo)
textchelo.grid(row=1,column=1)
textghorme=Entry(Foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ghorme)
textghorme.grid(row=2,column=1)
textgheime=Entry(Foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_gheime)
textgheime.grid(row=3,column=1)
textash=Entry(Foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ash)
textash.grid(row=4,column=1)
textsabzi=Entry(Foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sabzi)
textsabzi.grid(row=5,column=1)
texttah=Entry(Foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tah)
texttah.grid(row=6,column=1)
textghali=Entry(Foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ghali)
textghali.grid(row=7,column=1)
textfes=Entry(Foodframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fes)
textfes.grid(row=8,column=1)

#drink

tea=Checkbutton(Drinkframe,text='Persian Tea',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var10,command=ftea)
tea.grid(row=0,column=0,sticky=W)
khak=Checkbutton(Drinkframe,text='Khakshir',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var11,command=fkhak)
khak.grid(row=1,column=0,sticky=W)
tokhm=Checkbutton(Drinkframe,text='Tokhm-Sharbati',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var12,command=ftokhm)
tokhm.grid(row=2,column=0,sticky=W)
doogh=Checkbutton(Drinkframe,text='Doogh',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var13,command=fdoogh)
doogh.grid(row=3,column=0,sticky=W)
khiar=Checkbutton(Drinkframe,text='Khiar-Sekanjabin ',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var14,command=fkhiar)
khiar.grid(row=4,column=0,sticky=W)
dam=Checkbutton(Drinkframe,text='Damnoosh',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var15,command=fdam)
dam.grid(row=5,column=0,sticky=W)
aragh=Checkbutton(Drinkframe,text='Araghijat',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var16,command=faragh)
aragh.grid(row=6,column=0,sticky=W)
Bahar=Checkbutton(Drinkframe,text='Bahar-Narenj',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var17,command=fbahar)
Bahar.grid(row=7,column=0,sticky=W)
ab=Checkbutton(Drinkframe,text='Water',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var18,command=fab)
ab.grid(row=8,column=0,sticky=W)

#entry for drink

texttea=Entry(Drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tea)
texttea.grid(row=0,column=1)
textkhak=Entry(Drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_khak)
textkhak.grid(row=1,column=1)
texttokhm=Entry(Drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tokhm)
texttokhm.grid(row=2,column=1)
textdoogh=Entry(Drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_doogh)
textdoogh.grid(row=3,column=1)
textkhiar=Entry(Drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_khiar)
textkhiar.grid(row=4,column=1)
textdam=Entry(Drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_dam)
textdam.grid(row=5,column=1)
textaragh=Entry(Drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_aragh)
textaragh.grid(row=6,column=1)
textbahar=Entry(Drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bahar)
textbahar.grid(row=7,column=1)
textab=Entry(Drinkframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ab)
textab.grid(row=8,column=1)

#desrts

shole=Checkbutton(Desertframe,text='Sholeh Zard',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var19,command=fshole)
shole.grid(row=0,column=0,sticky=W)
yazdi=Checkbutton(Desertframe,text='Shirini Yazdi',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var20,command=fyazdi)
yazdi.grid(row=1,column=0,sticky=W)
Halva=Checkbutton(Desertframe,text='Halva',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var21,command=fhalva)
Halva.grid(row=2,column=0,sticky=W)
Faloode=Checkbutton(Desertframe,text='Faloodeh Shirazi',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var22,command=ffaloode)
Faloode.grid(row=3,column=0,sticky=W)
kolooch=Checkbutton(Desertframe,text='Kooloocheh',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var23,command=fkoolooch)
kolooch.grid(row=4,column=0,sticky=W)
Baghlava=Checkbutton(Desertframe,text='Baghlava',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var24,command=fbaghlava)
Baghlava.grid(row=5,column=0,sticky=W)
Rangin=Checkbutton(Desertframe,text='Ranginak',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var25,command=frangin)
Rangin.grid(row=6,column=0,sticky=W)
gaz=Checkbutton(Desertframe,text='Gaz',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var26,command=fgaz)
gaz.grid(row=7,column=0,sticky=W)
sohan=Checkbutton(Desertframe,text='Sohan',font=('Matura MT Script Capitals',15,'bold'),offvalue=0,onvalue=1,variable=var27,command=fsohan)
sohan.grid(row=8,column=0,sticky=W)

#entry for desert

textshole=Entry(Desertframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shole)
textshole.grid(row=0,column=1)
textyazdi=Entry(Desertframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_yazdi)
textyazdi.grid(row=1,column=1)
texthalva=Entry(Desertframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_halva)
texthalva.grid(row=2,column=1)
textfaloode=Entry(Desertframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faloode)
textfaloode.grid(row=3,column=1)
textkoolooch=Entry(Desertframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_koolooch)
textkoolooch.grid(row=4,column=1)
textbaghlava=Entry(Desertframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_baghlava)
textbaghlava.grid(row=5,column=1)
textrangin=Entry(Desertframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rangin)
textrangin.grid(row=6,column=1)
textgaz=Entry(Desertframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_gaz)
textgaz.grid(row=7,column=1)
textsohan=Entry(Desertframe,font=('arial',15,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sohan)
textsohan.grid(row=8,column=1)

#costlabels and entry fields

labelcostofFood=Label(costframe,text ='Cost of Food',font=('Mongolian Baiti',20,'bold'),bg='firebrick4',fg='black')
labelcostofFood.grid(row=0,column=0)
textcostofFood=Entry(costframe,font=('Mongolian Baiti',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textcostofFood.grid(row=0,column=1,padx=41)

labelcostofDrink=Label(costframe,text ='Cost of Drink',font=('Mongolian Baiti',20,'bold'),bg='firebrick4',fg='black')
labelcostofDrink.grid(row=1,column=0)
textcostofDrink=Entry(costframe,font=('Mongolian Baiti',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinkvar)
textcostofDrink.grid(row=1,column=1,padx=41)

labelcostofDesert=Label(costframe,text ='Cost of Desert',font=('Mongolian Baiti',20,'bold'),bg='firebrick4',fg='black')
labelcostofDesert.grid(row=2,column=0)
textcostofDesert=Entry(costframe,font=('Mongolian Baiti',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdesertvar)
textcostofDesert.grid(row=2,column=1,padx=41)

labelsubTotal=Label(costframe,text ='Sub Total',font=('Mongolian Baiti',20,'bold'),bg='firebrick4',fg='black')
labelsubTotal.grid(row=0,column=2)
textsubTotal=Entry(costframe,font=('Mongolian Baiti',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textsubTotal.grid(row=0,column=3,padx=41)

labelserviceTax=Label(costframe,text ='Service Tax',font=('Mongolian Baiti',20,'bold'),bg='firebrick4',fg='black')
labelserviceTax.grid(row=1,column=2)
textserviceTax=Entry(costframe,font=('Mongolian Baiti',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textserviceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costframe,text ='Total Cost',font=('Mongolian Baiti',20,'bold'),bg='firebrick4',fg='black')
labelTotalCost.grid(row=2,column=2)
textTotalcost=Entry(costframe,font=('Mongolian Baiti',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalcost.grid(row=2,column=3,padx=41)
resvar=IntVar()
a=Checkbutton(costframe,text='Reservation',font=('Mongolian Baiti',16,'bold'),fg='black',offvalue=0,onvalue=1,variable=resvar,bg='firebrick4',activebackground='firebrick4')
a.place(x=825,y=42)

#buttons

buttontotal=Button(buttonsframe,text='Total',font=('Mongolian Baiti',14,'bold'),fg='black',bg='red4',bd=3,command=ftotal)
buttontotal.grid(row=0,column=0)

buttonreceipt=Button(buttonsframe,text='Receipt',font=('Mongolian Baiti',14,'bold'),fg='black',bg='red4',bd=3,command=freceipt)
buttonreceipt.grid(row=0,column=1)

buttonsave=Button(buttonsframe,text='Save',font=('Mongolian Baiti',14,'bold'),fg='black',bg='red4',bd=3,command=save)
buttonsave.grid(row=0,column=2)

buttonsend=Button(buttonsframe,text='Send',font=('Mongolian Baiti',14,'bold'),fg='black',bg='red4',bd=3,command=send)
buttonsend.grid(row=0,column=3)

buttonreset=Button(buttonsframe,text='Reset',font=('Mongolian Baiti',14,'bold'),fg='black',bg='red4',bd=3,command=reset)
buttonreset.grid(row=0,column=4)

#text area

textreceipt=Text(receiptframe,font=('Mongolian Baiti',12,'bold'),bd=3,width=36,height=18)
textreceipt.grid(row=0,column=0)



#calculator


operator='' #to show clicked buttons on entry part
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    #calculatorfield.delete(0,END)
    calculatorfield.insert(END,operator)
    
def clear():
    global operator
    operator=''
    calculatorfield.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorfield.delete(0,END)
    calculatorfield.insert(0,result)
    operator=''

calculatorfield=Entry(cframe,font=('arial',14,'bold'),width=30,bd=4)
calculatorfield.grid(row=0,column=0,columnspan=4)
button1=Button(cframe,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('1'))
button1.grid(row=1,column=0)
button2=Button(cframe,text='2',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('2'))
button2.grid(row=1,column=1)
button3=Button(cframe,text='3',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('3'))
button3.grid(row=1,column=2)
buttonplus=Button(cframe,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)
button4=Button(cframe,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)
button5=Button(cframe,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=5,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)
button6=Button(cframe,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=5,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)
buttonminus=Button(cframe,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('-'))
buttonminus.grid(row=2,column=3)
button7=Button(cframe,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('7'))
button7.grid(row=3,column=0)
button8=Button(cframe,text='8',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=5,command=lambda:buttonClick('8'))
button8.grid(row=3,column=1)
button9=Button(cframe,text='9',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=5,command=lambda:buttonClick('9'))
button9.grid(row=3,column=2)
buttonmltiply=Button(cframe,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('*'))
buttonmltiply.grid(row=3,column=3)
buttonans=Button(cframe,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=answer)
buttonans.grid(row=4,column=0)
buttonclear=Button(cframe,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=clear)
buttonclear.grid(row=4,column=1)
button0=Button(cframe,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)
buttondivison=Button(cframe,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=5,command=lambda:buttonClick('/'))
buttondivison.grid(row=4,column=3)
r.mainloop()
