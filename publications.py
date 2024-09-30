from tkinter import *
from tkinter import messagebox
#============================
def mainPage00():
    #========================
    def calculate00():
        #====================
        def confirmBtn00():
            #================
            def purchase00():
                calWin.destroy()
                mainWin00()
            #================
            finishWin = Toplevel()
            finishWin.title("calculate")
            finishWin.state("zoomed")
            finishWin.resizable(width=False, height=False)
            finishWin.config(bg="#fff")
            #================
            purchaseImg = PhotoImage(file="purchase.png")
            purchase = Button(finishWin, image=purchaseImg, bd=0, bg="#fff", fg="#fff", command=purchase00)
            purchase.place(x=350, y=0)
            #================
            finishWin.mainloop()
        #====================
        calWin = Tk()
        calWin.title("calculate")
        calWin.state("zoomed")
        calWin.resizable(width=False, height=False)
        calWin.config(bg="#2167de")
        #====================
        # calculate label
        calculateLbl = Label(calWin, text="Calculate", font=("impact", 100, "bold"), bg="#2167de", fg="#fff")
        calculateLbl.pack()
        #====================
        # line
        lb1 = Label(calWin, text="------------", font=("impact", 80, "bold"), bg="#2167de", fg="#17499d")
        lb1.place(x=565, y=245)
        #---------------
        lb2 = Label(calWin, text="------------", font=("impact", 80, "bold"), bg="#2167de", fg="#17499d")
        lb2.place(x=565, y=395)
        #====================
        # entries
        etr1 = Entry(calWin, font=("airal", 25, "bold"), bd=1, bg="#fff", fg="#000", width=4)
        etr1.place(x=505, y=220)
        #---------------
        etr2 = Entry(calWin, font=("airal", 25, "bold"), bd=1, bg="#fff", fg="#000", width=4)
        etr2.place(x=655, y=220)
        #---------------
        etr3 = Entry(calWin, font=("airal", 25, "bold"), bd=1, bg="#fff", fg="#000", width=4)
        etr3.place(x=805, y=220)
        #---------------
        etr4 = Entry(calWin, font=("airal", 25, "bold"), bd=1, bg="#fff", fg="#000", width=4)
        etr4.place(x=955, y=220)
        #====================
        # one line
        l1 = Label(calWin, text="-", font=("impact", 28, "bold"), bg="#2167de", fg="#17499d")
        l1.place(x=608, y=213)
        #---------------
        l2 = Label(calWin, text="-", font=("impact", 28, "bold"), bg="#2167de", fg="#17499d")
        l2.place(x=760, y=213)
        #---------------
        l3 = Label(calWin, text="-", font=("impact", 28, "bold"), bg="#2167de", fg="#17499d")
        l3.place(x=912, y=213)
        #====================
        # year label and entry
        yearL = Label(calWin, text="Year :", font=("impact", 28, "bold"), bg="#2167de", fg="#17499d")
        yearL.place(x=585, y=370)
        #---------------
        yearE = Entry(calWin, font=("airal", 25, "bold"), bd=1, bg="#fff", fg="#000", width=2)
        yearE.place(x=690, y=375)
        #====================
        # month label and entry
        monthL = Label(calWin, text="Month :", font=("impact", 28, "bold"), bg="#2167de", fg="#17499d")
        monthL.place(x=785, y=370)
        #---------------
        monthE = Entry(calWin, font=("airal", 25, "bold"), bd=1, bg="#fff", fg="#000", width=2)
        monthE.place(x=915, y=375)
        #====================
        # CVV2 label and entry
        cvv2L = Label(calWin, text="CVV2 :", font=("impact", 28, "bold"), bg="#2167de", fg="#17499d")
        cvv2L.place(x=555, y=527)
        #---------------
        cvv2E = Entry(calWin, font=("airal", 25, "bold"), bd=1, bg="#fff", fg="#000", width=3)
        cvv2E.place(x=562, y=600)
        #====================
        # second pass label and entry
        secondPassL = Label(calWin, text="Second Pass :", font=("impact", 28, "bold"), bg="#2167de", fg="#17499d")
        secondPassL.place(x=755, y=527)
        #---------------
        secondPassE = Entry(calWin, font=("airal", 25, "bold"), bd=1, bg="#fff", fg="#000", width=5)
        secondPassE.place(x=762, y=600)
        #====================
        # confirm button
        confirmBtn = Button(calWin, text="Confirm", font=("impact", 28, "bold"), bd=1, bg="#fff", fg="#2167de", command=confirmBtn00)
        confirmBtn.place(x=670, y=720)
        #====================
        calWin.mainloop()
    #========================
    # my defs
    # all button work
    def allBtn00():
        #====================
        # my defs
        # next button work
        def nextBtn00():
            #================
            # my defs
            # next button 2 work
            def nextBtn200():
                #============
                # first page button work
                def firstPageL00():
                    page3.destroy()
                    page2.destroy()
                #============
                page3 = Toplevel()
                page3.title("Entesharat")
                page3.resizable(0, 0) 
                page3.state("zoomed")
                page3.config(bg="#fff")
                #============
                # my background
                backAllL3 = Label(page3, image=backAllp2)
                backAllL3.place(x=-10, y=-10)
                #============
                price13 = Label(page3, text="7$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
                price13.place(x=551, y=452)
                #---------------
                price14 = Label(page3, text="7$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
                price14.place(x=885, y=452)
                #---------------
                price15 = Label(page3, text="9$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
                price15.place(x=1215, y=452)
                #====================
                # books
                bookL13 = Button(page3, image=book13, bd=0, command=book1300)
                bookL13.place(x=500, y=220)
                #-------
                bookL14 = Button(page3, image=book14, bd=0, command=book1400)
                bookL14.place(x=835, y=220)
                #-------
                bookL15 = Button(page3, image=book15, bd=0, command=book1500)
                bookL15.place(x=1160, y=220)
                #============
                # first page button
                firstPage = PhotoImage(file="firstPage.png")
                firstPageL = Button(page3, image=firstPage, bd=0, bg="#fff", command=firstPageL00)
                firstPageL.place(x=775, y=580)
                #============
                # main buttons
                # next page button
                # nextBtn = Button(page1, image=nextB, bd=0, bg="#3B92AD")
                # nextBtn.place(x=30, y=580)
                #-------
                # # previouse page button
                preBtn2 = Button(page3, image=previouseB, bd=0, bg="#3B92AD", command=lambda: page3.destroy())
                preBtn2.place(x=110, y=680)
                #============
                page3.mainloop()
            #================
            page2 = Toplevel()
            page2.title("Entesharat")
            page2.resizable(0, 0) 
            page2.state("zoomed")
            page2.config(bg="#fff")
            #================
            # my background
            backAllL2 = Label(page2, image=backAll)
            backAllL2.place(x=-10, y=-10)
            #================
            # price of books
            price7 = Label(page2, text="2$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
            price7.place(x=541, y=295)
            #---------------
            price8 = Label(page2, text="4$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
            price8.place(x=875, y=295)
            #---------------
            price9 = Label(page2, text="9$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
            price9.place(x=1200, y=295)
            #---------------
            price10 = Label(page2, text="4$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
            price10.place(x=541, y=665)
            #---------------
            price11 = Label(page2, text="5$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
            price11.place(x=880, y=665)
            #---------------
            price12 = Label(page2, text="5$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
            price12.place(x=1200, y=665)
            #====================
            # books
            bookL7 = Button(page2, image=book7, bd=0, bg="#fff", command=book700)
            bookL7.place(x=490, y=65)
            #-----------
            bookL8 = Button(page2, image=book8, bd=0, bg="#fff", command=book800)
            bookL8.place(x=800, y=65)
            #-----------
            bookL9 = Button(page2, image=book9, bd=0, command=book900)
            bookL9.place(x=1155, y=65)
            #-----------
            bookL10 = Button(page2, image=book10, bd=0, command=book1000)
            bookL10.place(x=499, y=440)
            #-----------
            bookL11 = Button(page2, image=book11, bd=0, command=book1100)
            bookL11.place(x=835, y=440)
            #-----------
            bookL12 = Button(page2, image=book12, bd=0, command=book1200)
            bookL12.place(x=1145, y=440)
            #================
            # main buttons
            # next page button
            nextBtn2 = Button(page2, image=nextB, bd=0, bg="#3B92AD", command=nextBtn200)
            nextBtn2.place(x=30, y=580)
            #-----------
            # # previouse page button
            preBtn = Button(page2, image=previouseB, bd=0, bg="#3B92AD", command=lambda: page2.destroy())
            preBtn.place(x=110, y=680)
            #================
            page2.mainloop()
        #====================
        page1 = Toplevel()
        page1.title("Entesharat")
        page1.resizable(0, 0) 
        page1.state("zoomed")
        page1.config(bg="#fff")
        #====================
        # main buttons images
        backAll = PhotoImage(file="win1.png")
        backAllp2 = PhotoImage(file="win2.png")
        nextB = PhotoImage(file="np.png")
        previouseB = PhotoImage(file="pp.png")
        #====================
        # my background
        backAllL = Label(page1, image=backAll)
        backAllL.place(x=-10, y=-10)
        #====================
        # price of books
        price1 = Label(page1, text="2$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        price1.place(x=541, y=295)
        #---------------
        price2 = Label(page1, text="8$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        price2.place(x=875, y=295)
        #---------------
        price3 = Label(page1, text="5$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        price3.place(x=1200, y=295)
        #---------------
        price4 = Label(page1, text="2$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        price4.place(x=541, y=665)
        #---------------
        price5 = Label(page1, text="3$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        price5.place(x=880, y=665)
        #---------------
        price6 = Label(page1, text="7$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        price6.place(x=1200, y=665)
        #====================
        # books
        bookL1 = Button(page1, image=book1, bd=0, command=book100)
        bookL1.place(x=485, y=70)
        #---------------
        bookL2 = Button(page1, image=book2, bd=0, command=book200)
        bookL2.place(x=810, y=70)
        #---------------
        bookL3 = Button(page1, image=book3, bd=0, command=book300)
        bookL3.place(x=1115, y=70)
        #---------------
        bookL4 = Button(page1, image=book4, bd=0, command=book400)
        bookL4.place(x=475, y=440)
        #---------------
        bookL5 = Button(page1, image=book5, bd=0, command=book500)
        bookL5.place(x=815, y=440)
        #---------------
        bookL6 = Button(page1, image=book6, bd=0, command=book600)
        bookL6.place(x=1102, y=445)
        #====================
        # main buttons
        # next page button
        nextBtn = Button(page1, image=nextB, bd=0, bg="#3B92AD", command=nextBtn00)
        nextBtn.place(x=30, y=580)
        #---------------
        # # previouse page button
        # preBtn = Button(page1, image=previouseB, bd=0, bg="#3B92AD")
        # preBtn.place(x=110, y=680)
        #====================
        page1.mainloop()
        #====================
    #========================
    # horror button work
    def horrorB00():
        #====================
        win0 = Toplevel()
        win0.title("Entesharat")
        win0.resizable(0, 0)
        win0.state("zoomed")
        win0.config(bg="#fff")
        #====================
        # my background
        backHorror = PhotoImage(file="backHorror.png")
        backHorrorL = Button(win0, image=backHorror)
        backHorrorL.place(x=-10, y=-10)
        #====================
        # back button
        backBtn = PhotoImage(file="btnBack.png")
        backBtnL = Button(win0, image=backBtn, bd=0, command=lambda: win0.destroy())
        backBtnL.place(x=822, y=600)
        #====================
        # my books
        # book3
        hbook3 = Label(win0, text="7$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        hbook3.place(x=610, y=460)
        hbookImgL3 = Button(win0, image=book6, bd=0, bg="#fff", command=book600)
        hbookImgL3.place(x=513, y=250)
        #-------------------
        # book4
        hbook4 = Label(win0, text="8$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        hbook4.place(x=936, y=460)
        hbookImgL4 = Button(win0, image=book13, bd=0, command=book1300)
        hbookImgL4.place(x=890, y=235)
        #-------------------
        # book5
        hbook5 = Label(win0, text="7$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        hbook5.place(x=1270, y=465)
        hbookImgL5 = Button(win0, image=book14, bd=0, command=book1400)
        hbookImgL5.place(x=1224, y=235)
        #====================
        win0.mainloop()
    #========================
    # comedy buttton work
    def comedyB00():
        #====================
        win0 = Toplevel()
        win0.title("Entesharat")
        win0.resizable(0, 0)
        win0.state("zoomed")
        win0.config(bg="#fff")
        #====================
        # my background
        backComedy = PhotoImage(file="backComedy.png")
        backComedyL = Button(win0, image=backComedy)
        backComedyL.place(x=-10, y=-10)
        #====================
        # back button
        backBtn = PhotoImage(file="btnBack.png")
        backBtnL = Button(win0, image=backBtn, bd=0, command=lambda: win0.destroy())
        backBtnL.place(x=822, y=600)
        #====================
        # my books
        # book3
        cbook3 = Label(win0, text="7$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        cbook3.place(x=610, y=470)
        cbookImgL3 = Button(win0, image=book2, bd=0, command=book200)
        cbookImgL3.place(x=545, y=240)
        #-------------------
        # book4
        cbook4 = Label(win0, text="8$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        cbook4.place(x=936, y=470)
        cbookImgL4 = Button(win0, image=book12, bd=0, command=book1200)
        cbookImgL4.place(x=885, y=235)
        #-------------------
        # book5
        cbook5 = Label(win0, text="7$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        cbook5.place(x=1270, y=470)
        cbookImgL5 = Button(win0, image=book15, bd=0, command=book1500)
        cbookImgL5.place(x=1215, y=235)
        #====================
        win0.mainloop()
        #====================
    #========================
    # action button work
    def actionB00():
        #====================
        win0 = Toplevel()
        win0.title("Entesharat")
        win0.resizable(0, 0)
        win0.state("zoomed")
        win0.config(bg="#fff")
        #====================
        # my background
        backAction = PhotoImage(file="backAction.png")
        backActionL = Button(win0, image=backAction)
        backActionL.place(x=-10, y=-10)
        #====================
        # back button
        backBtn = PhotoImage(file="btnBack.png")
        backBtnL = Button(win0, image=backBtn, bd=0, command=lambda: win0.destroy())
        backBtnL.place(x=822, y=600)
        #====================
        # my books
        # book3
        abook3 = Label(win0, text="7$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        abook3.place(x=610, y=460)
        abookImgL3 = Button(win0, image=book1, bd=0, command=book100)
        abookImgL3.place(x=555, y=245)
        #-------------------
        # book4
        abook4 = Label(win0, text="8$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        abook4.place(x=936, y=460)
        abookImgL4 = Button(win0, image=book9, bd=0, command=book900)
        abookImgL4.place(x=895, y=245)
        #-------------------
        # book5        
        abook5 = Label(win0, text="7$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
        abook5.place(x=1270, y=460)
        abookImgL5 = Button(win0, image=book10, bd=0, command=book1000)
        abookImgL5.place(x=1227, y=245)
        #====================
        win0.mainloop()
        #====================
    #========================
    # option button work
    def opImgB00():
        opImgB.config(image=opImg2, command=opImgB00_)
        developerBtn.place(x=1380, y=175)
        aboutBtn.place(x=1380, y=225)
        favBtn.place(x=1380, y=275)
    #-------------------
    def opImgB00_():
        opImgB.config(image=opImg, command=opImgB00)
        developerBtn.place(x=5380, y=175)
        aboutBtn.place(x=5380, y=225)
        favBtn.place(x=5380, y=275)
    #========================
    # books
    def book100():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back1.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book200():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back2.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book300():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back3.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book400():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back4.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book500():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back5.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book600():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back6.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book700():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back7.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book800():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back8.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book900():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back9.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book1000():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back10.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book1100():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back11.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book1200():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back12.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book1300():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back13.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book1400():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back14.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #-------------------
    def book1500():
        #====================
        # wishList button work
        def wishList00():
            listBtn.config(image=listImg2, command=wishList00_)
        #---------------
        def wishList00_():
            listBtn.config(image=listImg, command=wishList00)
        #====================
        page = Tk()
        page.title("Entesharat")
        page.resizable(0, 0) 
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        back1 = PhotoImage(file="back15.png", master=page)
        back1L = Label(page, image=back1)
        back1L.place(x=-10, y=-80)
        #====================
        # buy button
        buyImg = PhotoImage(file="buy.png", master=page)
        buyBtn = Button(page, image=buyImg, bd=0, bg="#fff", command=calculate00)
        buyBtn.place(x=230, y=630)
        #====================
        # wishList button
        listImg = PhotoImage(file="wishList.png", master=page)
        listImg2 = PhotoImage(file="wishList2.png", master=page)
        listBtn = Button(page, image=listImg, bd=0, bg="#fff", command=wishList00)
        listBtn.place(x=730, y=630)
        #====================
        page.mainloop()
    #========================
    # options buttons work
    # developer
    def developerBtn00():
        page = Toplevel()
        page.title("Entesharat")
        page.resizable(0, 0)
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        # background
        devImg = PhotoImage(file="developerPage.png")
        dev = Label(page, image=devImg)
        dev.place(x=-10, y=-10)
        #====================
        page.mainloop()
    #-------------------
    # about
    def aboutBtn00():
        page = Toplevel()
        page.title("Entesharat")
        page.resizable(0, 0)
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        # background
        devImg = PhotoImage(file="aboutPage.png")
        dev = Label(page, image=devImg)
        dev.place(x=-10, y=-10)
        #====================
        page.mainloop()
    #-------------------
    # favorites
    def favBtn00():
        page = Toplevel()
        page.title("Entesharat")
        page.resizable(0, 0)
        page.state("zoomed")
        page.config(bg="#fff")
        #====================
        # state label
        favImg = PhotoImage(file="fav.png")
        state = Label(page, image=favImg)
        state.place(x=-10, y=-20)
        #====================
        page.mainloop()
    #========================
    # search button work
    def seaBtn00():
        userSearch = myEntry.get()
        if userSearch in myLibrary:
            myEntry.delete(0, END)
            if userSearch == "nagofte-haye enghelab":
                book100()
            if userSearch == "a kite for moon":
                book200()
            if userSearch == "kalaka":
                book300()
            if userSearch == "darhaye movazi":
                book400()
            if userSearch == "empty home":
                book500()
            if userSearch == "salib-e ghahve-ee":
                book600()
            if userSearch == "exercise book":
                book700()
            if userSearch == "the book of mormon":
                book800()
            if userSearch == "the edge of the unknown":
                book900()
            if userSearch == "take age of the strongman":
                book1000()
            if userSearch == "take back your time":
                book1100()
            if userSearch == "after midnight":
                book1200()
            if userSearch == "the book of chaos":
                book1300()
            if userSearch == "rock to die":
                book1400()
            if userSearch == "harry potter":
                book1500()
        #---------------
        elif userSearch in writers:
            myEntry.delete(0, END)
            if userSearch == "Abbas amir entezam":
                book100()
            if userSearch == "Martin palche":
                book200()
            if userSearch == "Mansor hashemi":
                book300()
            if userSearch == "Akbar sagpaz":
                book400()
            if userSearch == "Mammad":
                book500()
            if userSearch == "Mammad2":
                book600()
            if userSearch == "Apadana":
                book700()
            if userSearch == "Lionel messi":
                book800()
            if userSearch == "Lewan":
                book900()
            if userSearch == "Gideon raghman":
                book1000()
            if userSearch == "Caleb ulku":
                book1100()
            if userSearch == "Marial":
                book1200()
            if userSearch == "Jessica renwock":
                book1300()
            if userSearch == "Martines":
                book1400()
            if userSearch == "Rowlink":
                book1500()
        #---------------
        elif userSearch in ages:
            myEntry.delete(0, END)
            if userSearch == "+2":
                page = Tk()
                page.title("Entesharat")
                page.resizable(0, 0)
                page.state("zoomed")
                page.config(bg="#fff")
                #============
                # my books
                book01 = PhotoImage(file="book1.png", master=page)
                book02 = PhotoImage(file="book2.png", master=page)
                book03 = PhotoImage(file="book3.png", master=page)
                book04 = PhotoImage(file="book4.png", master=page)
                book05 = PhotoImage(file="book5.png", master=page)
                book06 = PhotoImage(file="book6.png", master=page)
                book07 = PhotoImage(file="book7.png", master=page)
                book08 = PhotoImage(file="book8.png", master=page)
                book09 = PhotoImage(file="book9.png", master=page)
                book010 = PhotoImage(file="book10.png", master=page)
                book011 = PhotoImage(file="book11.png", master=page)
                book012 = PhotoImage(file="book12.png", master=page)
                book013 = PhotoImage(file="book13.png", master=page)
                book014 = PhotoImage(file="book14.png", master=page)
                book015 = PhotoImage(file="book15.png", master=page)
                #============
                # b = Button(page, image=book09, bd=6)
                # b.place(x=50, y=40)
        #---------------
        elif userSearch in regions:
            myEntry.delete(0, END)
        else:
            messagebox.showerror(title="Oops!", message="I can't find anything")
    #========================
    win = Tk()
    win.title("Entesharat")
    win.resizable(0, 0)
    win.state("zoomed")
    win.config(bg="#fff")
    #========================
    # my library
    myLibrary = [
        "nagofte-haye enghelab", "a kite for moon", "kalaka", "darhaye movazi", "empty home", "salib-e ghahve-ee",
        "exercise book", "the book of mormon", "the edge of the unknown", "take age of the strongman",
        "take back your time", "after midnight", "the book of chaos", "rock to die", "harry potter"
    ]
    writers = [
        "Abbas amir entezam", "Martin palche", "Mansor hashemi", "Akbar sagpaz", "Mammad", "Mammad2", "Apadana",
        "Lionel messi", "Lewan", "Gideon raghman", "Caleb ulku", "Marial", "Jessica renwock", "Martines",
        "Rowlink"
    ]
    ages = [
        "+2", "+8", "+9", "+12", "+15", "+16", "+17", "+18", "+19"
    ]
    regions = [
        "IRanian", "ARgemtine", "AMerican", "GErman"
    ]
    #========================
    # my books
    book1 = PhotoImage(file="book1.png")
    book2 = PhotoImage(file="book2.png")
    book3 = PhotoImage(file="book3.png")
    book4 = PhotoImage(file="book4.png")
    book5 = PhotoImage(file="book5.png")
    book6 = PhotoImage(file="book6.png")
    book7 = PhotoImage(file="book7.png")
    book8 = PhotoImage(file="book8.png")
    book9 = PhotoImage(file="book9.png")
    book10 = PhotoImage(file="book10.png")
    book11 = PhotoImage(file="book11.png")
    book12 = PhotoImage(file="book12.png")
    book13 = PhotoImage(file="book13.png")
    book14 = PhotoImage(file="book14.png")
    book15 = PhotoImage(file="book15.png")
    #========================
    # my background
    Img = PhotoImage(file="back.png")
    ImgL = Label(win, image=Img)
    ImgL.place(x=-10, y=-10)
    #========================
    # search button
    seaImg = PhotoImage(file="search.png")
    seaBtn = Button(win, image=seaImg, bd=0, bg="#3B92AD", command=seaBtn00)
    seaBtn.place(x=530, y=70)
    #========================
    # option button
    opImg = PhotoImage(file="op1.png")
    opImg2 = PhotoImage(file="op2.png")
    opImgB = Button(win, image=opImg, bd=0, bg="#3B92AD", command=opImgB00)
    opImgB.place(x=1425, y=75)
    #-------------------
    # developer button
    developerBtn = Button(win, text="Developer", font=("calibri", 22, "bold"), bd=0, bg="#fff", fg="#3B92AD", command=developerBtn00)
    developerBtn.place(x=5380, y=175)
    #-------------------
    # about button
    aboutBtn = Button(win, text="About", font=("calibri", 22, "bold"), bd=0, bg="#fff", fg="#3B92AD", command=aboutBtn00)
    aboutBtn.place(x=5380, y=225)
    #-------------------
    # favorites button
    favBtn = Button(win, text="Favorites", font=("calibri", 22, "bold"), bd=0, bg="#fff", fg="#3B92AD", command=favBtn00)
    favBtn.place(x=5380, y=275)
    #========================
    # conform button
    btnImg = PhotoImage(file="btnCon.png")
    allBtn = Button(win, image=btnImg, bd=0, command=allBtn00)
    allBtn.place(x=300, y=360)
    #========================
    # Entry
    myEntry = Entry(win, font=("calibri", 40, "bold"), bd=0, bg="#fff", fg="#000")
    myEntry.place(x=600, y=70)
    #========================
    # books
    bookImgL1 = Button(win, image=book1, bd=0, command=book100)
    bookImgL1.place(x=720, y=250)
    #-------------------
    bookImgL2 = Button(win, image=book2, bd=0, command=book200)
    bookImgL2.place(x=1100, y=250)
    #========================
    # prices
    price01 = Label(win, text="2$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
    price01.place(x=776, y=485)
    #-------------------
    price02 = Label(win, text="8$", font=("calibri", 35, "bold"), bg="#fff", fg="#000")
    price02.place(x=1167, y=485)
    #========================
    # options
    horrorB = Button(win, text="Horror", font=("calibri", 37, "bold"), bd=0, bg="#fff", fg="#3B92AD", command=horrorB00)
    horrorB.place(x=700, y=620)
    #-------------------
    comedyB = Button(win, text="Comedy", font=("calibri", 37, "bold"), bd=0, bg="#fff", fg="#3B92AD", command=comedyB00)
    comedyB.place(x=885, y=620)
    #-------------------
    comedyB = Button(win, text="Action", font=("calibri", 37, "bold"), bd=0, bg="#fff", fg="#3B92AD", command=actionB00)
    comedyB.place(x=1110, y=620)
    #========================
    win.mainloop()
mainPage00()