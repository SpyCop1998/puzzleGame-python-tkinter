from tkinter import *
import random
from tkinter import messagebox

class MainPuzzle:
    global i
    global w
    global name
    global score
    global que

    def __init__(self):
        self.i=0
        self.que=0
        global rootDisp
        rootDisp=Tk()
        rootDisp.title("Main Puzzle")
        rootDisp.geometry("500x500")
        rootDisp.resizable(False, False)
        #--
        photo = PhotoImage(file="spider.png")
        pic = Label(rootDisp, image=photo)
        pic.pack()
        #--

        lName=Label(rootDisp,text="NAME",font="Times 20",bg="pink")
        lName.place(x=50,y=200)

        entryName=Entry(rootDisp,font="Times 20",bg="pink")
        entryName.place(x=200,y=200)


        def mainGame():
            self.name = entryName.get()
            rootDisp.destroy()
            self.mainDisplay()

        #--
        btn1=Button(rootDisp,text="Submit",font="Times 20",bg="pink",command=mainGame)
        btn1.place(x=200,y=300)
        #--


        rootDisp.mainloop()

    Word=[
        "HEY",
        "MAN",
        "YEP",
        "HELLO",
        "WELCOME",
        "HI",
        "LPU",
        "CSE",
        "LAPTOP",
        "COMPUTER",
        "ENGINEERING",
        "MBA",
        "INDIA",
        "AMERICA",
        "GOA",
        "PUNJAB",
        "NEWYORK",
        "DELHI",
        "LOVELY",
        ]

    def mainDisplay(self):
        global finalScore
        global dispMain
        dispMain=Tk()
        #--
        #--
        back = PhotoImage(file="b.png")
        photoLabel = Label(dispMain, image=back)
        photoLabel.pack()
        #--

        dispMain.title("Main Puzzle")
        dispMain.geometry("800x600")
        dispMain.resizable(False,False)

        #--
        canvas = Canvas(dispMain, width=200, height=100)
        canvas.create_line(630, 0, 630, 500,fill="red")
        canvas.pack(fill=BOTH, expand=1)
        #
        canvas.create_line(0, 500, 630, 500,fill="red")
        canvas.pack(fill=BOTH, expand=1)
        #--
        finalScore=Label(dispMain,text="0",font="Times 20",bg="pink")
        finalScore.place(x=690, y=90)
        #--
        def ins():
            messagebox.showinfo("Instruction", "Chutia ho tum :(")
        def about():
            messagebox.showinfo("About", "Aukat ke bahar :(")
        def contact():
            messagebox.showinfo("Contact", "Haweli pr milo")
        #--
        Button(dispMain, text="INSTRUCTION",bg="pink", font="Times 15",command=ins).place(x=645, y=200)#-----------------------
        Button(dispMain,text="ABOUT",bg="pink",font="Times 15",command=about).place(x=675, y=340)
        Button(dispMain, text="CONTACT US",bg="pink", font="Times 15",command=contact).place(x=650,y=270)
        #--
        Label(dispMain,text="Enter Word : : ",font="Times 20",bg="pink").place(x=100,y=230)
        entry=Entry(dispMain,font="Times 20",bg="pink")
        entry.place(x=310,y=230)
        #--

        #--
        playerName=Label(dispMain,text="Welcome ",font="Times 20",bg="pink")
        playerName.place(x=200,y=0)
        Label(dispMain, text=self.name, font="Times 20", bg="pink").place(x=400, y=0)

        def newGame():
            self.w=Label(dispMain, font="Times 20", text=self.Word[self.i],bg="pink")
            self.w.place(x=350, y=110)
        #----

        def randomWord():
            l=len(self.Word)-1
            self.i=random.randint(0,l)
            self.w.config(text=self.Word[self.i])
        #--


        def submitWord():
            txt=entry.get()
            if txt==self.Word[self.i]:
                self.que=self.que+1
                messagebox.showinfo("INFO", "Right Answer")
                clear()
            else:
                messagebox.showinfo("INFO", "Wrong Answer")
                self.que = self.que - 1
                clear()
            self.score=10*self.que
            finalScore.config(text=self.score,bg="pink")

                #--
            randomWord()

        #--
        def clear():
            entry.delete(first=0,last=1000)
        #--
        def quit1():
            #a=self.score
            #txt= "Your Score : : "+a
            #messagebox.showinfo("",)
            dispMain.destroy()
        #--


        Label(dispMain,font="Times 20",text="Score",bg="pink").place(x=675,y=40)

        Button(dispMain, text="NEW GAME", font="Times 20",bg="pink",command=newGame).place(x=50, y=520)
        Label(dispMain,font="Times 20",text="Word : :",bg="pink").place(x=180,y=110)

        Button(dispMain, text="NEXT", font="Times 20",bg="pink",command=submitWord).place(x=300, y=520)
        Button(dispMain,text="QUIT",font="Times 20",bg="pink",command=quit1).place(x=500,y=520)


        dispMain.mainloop()

obj=MainPuzzle()