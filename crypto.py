from PIL import Image,ImageTk
from tkinter import *
import requests
import json
import time
#.........................................
win=Tk()
win.title("canvency")
win.geometry("600x800+360+60")
#.........................................
#USDT
btcd="https://api.nobitex.ir/v2/orderbook/BTCUSDT"
btcd2="https://api.nobitex.ir/v2/orderbook/ETHUSDT"
btcd3="https://api.nobitex.ir/v2/orderbook/ETCUSDT"
btcd4="https://api.nobitex.ir/v2/orderbook/SHIBUSDT"
btcd5="https://api.nobitex.ir/v2/orderbook/BCHUSDT"
#IRT
btcr="https://api.nobitex.ir/v2/orderbook/BTCIRT"
btcr2="https://api.nobitex.ir/v2/orderbook/ETHIRT"
btcr3="https://api.nobitex.ir/v2/orderbook/ETCIRT"
btcr4="https://api.nobitex.ir/v2/orderbook/SHIBIRT"
btcr5="https://api.nobitex.ir/v2/orderbook/BCHIRT"
#.........................................
def wh():
    while 1:
        btcdsh=requests.get(btcd)
        btcdsh=btcdsh.json()
        btcdsh2=btcdsh['lastTradePrice']
        label_btcd.config(text=btcdsh2)
        #...
        btcd2sh=requests.get(btcd2)
        btcd2sh=btcd2sh.json()
        btcd2sh2=btcd2sh['lastTradePrice']
        label_btcd2.config(text=btcd2sh2)
        #...
        btcd3sh=requests.get(btcd3)
        btcd3sh=btcd3sh.json()
        btcd3sh2=btcd3sh['lastTradePrice']
        label_btcd3.config(text=btcd3sh2)
        #...
        btcd4sh=requests.get(btcd4)
        btcd4sh=btcd4sh.json()
        btcd4sh2=btcd4sh['lastTradePrice']
        label_btcd4.config(text=btcd4sh2)
        #...
        btcd5sh=requests.get(btcd5)
        btcd5sh=btcd5sh.json()
        btcd5sh2=btcd5sh['lastTradePrice']
        label_btcd5.config(text=btcd5sh2)
        #....................
        btcrsh=requests.get(btcr)
        btcrsh=btcrsh.json()
        btcrsh2=btcrsh['lastTradePrice']
        label_btcr.config(text=btcrsh2)
        #...
        btcr2sh=requests.get(btcr2)
        btcr2sh=btcr2sh.json()
        btcr2sh2=btcr2sh['lastTradePrice']
        label_btcr2.config(text=btcr2sh2)
        #...
        btcr3sh=requests.get(btcr3)
        btcr3sh=btcr3sh.json()
        btcr3sh2=btcr3sh['lastTradePrice']
        label_btcr3.config(text=btcr3sh2)
        #...
        btcr4sh=requests.get(btcr4)
        btcr4sh=btcr4sh.json()
        btcr4sh2=btcr4sh['lastTradePrice']
        label_btcr4.config(text=btcr4sh2)
        #...
        btcr5sh=requests.get(btcr5)
        btcr5sh=btcr5sh.json()
        btcr5sh2=btcr5sh['lastTradePrice']
        label_btcr5.config(text=btcr5sh2)
#.........................................
btc_im=PhotoImage(file="BTC.png")
eth_im=PhotoImage(file="ETH.png")
etc_im=PhotoImage(file="ETC.png")
shib_im=PhotoImage(file="SHIB.png")
bch_im=PhotoImage(file="BCH.png")
#.........................................
label_name=Label(win,text="نام:")
label_USDT=Label(win,text="USDT:")
label_IRT=Label(win,text="IRT:")
label=Label(win,text="بيت کوين(BTC):",font=("Input Mono", 15))
label2=Label(win,text="اتريوم(ETH):",font=("Input Mono", 15))
label3=Label(win,text="اتريوم کلاسيک(ETC):",font=("Input Mono", 15))
label4=Label(win,text="هزار شيبا(SHIB):",font=("Input Mono", 15))
label5=Label(win,text="بيت کوين کش(BCH):",font=("Input Mono", 15))
button=Button(win,text="start",command=wh,font=("Input Mono", 15))
label_im=Label(win,image=btc_im)
label_im2=Label(win,image=eth_im)
label_im3=Label(win,image=etc_im)
label_im4=Label(win,image=shib_im)
label_im5=Label(win,image=bch_im)
#....................
label_btcd=Label(win,text="",font=("Input Mono", 15))
label_btcd2=Label(win,text="",font=("Input Mono", 15))
label_btcd3=Label(win,text="",font=("Input Mono", 15))
label_btcd4=Label(win,text="",font=("Input Mono", 15))
label_btcd5=Label(win,text="",font=("Input Mono", 15))
#..........
label_btcr=Label(win,text="",font=("Input Mono", 15))
label_btcr2=Label(win,text="",font=("Input Mono", 15))
label_btcr3=Label(win,text="",font=("Input Mono", 15))
label_btcr4=Label(win,text="",font=("Input Mono", 15))
label_btcr5=Label(win,text="",font=("Input Mono", 15))
#....................
label_name.place(x=170,y=0)
label_USDT.place(x=270,y=0)
label_IRT.place(x=370,y=0)
label.place(x=100,y=100)
label2.place(x=100,y=200)
label3.place(x=100,y=300)
label4.place(x=100,y=400)
label5.place(x=100,y=500)
label_btcd.place(x=270,y=100)
label_btcd2.place(x=270,y=200)
label_btcd3.place(x=270,y=300)
label_btcd4.place(x=270,y=400)
label_btcd5.place(x=270,y=500)
label_btcr.place(x=370,y=100)
label_btcr2.place(x=370,y=200)
label_btcr3.place(x=370,y=300)
label_btcr4.place(x=370,y=400)
label_btcr5.place(x=370,y=500)
label_im.place(x=50,y=95)
label_im2.place(x=50,y=195)
label_im3.place(x=50,y=295)
label_im4.place(x=50,y=395)
label_im5.place(x=50,y=495)
button.place(x=400,y=600)
#.........................................
