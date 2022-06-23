from tkinter import *
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Checkboxes")
root.geometry("500x600")

win = None

# everytking about a
aUser = 0
def returnA(arg=None):
    global aUser
    aUser = float(a.get())
    result = a.get()
    aLabel.config(text=result)
    a.delete(0, END)

a = Entry(root, borderwidth=0, bg="#666666", fg="#eee", font=("Helvetica", 16), textvariable="")
a.place(height= 50,width= 450,y=0)
a.focus()
a.bind("<Return>", returnA)
a.pack()

aButton = Button(root, text="Entry a", command=returnA)
aButton.place(height= 50,width= 50,y=0,x=450)

aLabel = Label(root, text="")
aLabel.pack()


# everytking about b
bUser = 0
def returnB(arg=None):
    global bUser
    bUser = float(b.get())
    result = b.get()
    bLabel.config(text=result)
    b.delete(0, END)

b = Entry(root, borderwidth=0, bg="#666666", fg="#eee", font=("Helvetica", 16), textvariable="")
b.place(height= 50,width= 450,y=0)
b.focus()
b.bind("<Return>", returnB)
b.pack()

bButton = Button(root, text="Entry b", command=returnB)
bButton.place(height= 50,width= 50,y=50,x=450)

bLabel = Label(root, text="")
bLabel.pack()

# everytking about c
cUser = 0
def returnC(arg=None):
    global cUser
    cUser = float(c.get())
    result = c.get()
    cLabel.config(text=result)
    c.delete(0, END)

c = Entry(root, borderwidth=0, bg="#666666", fg="#eee", font=("Helvetica", 16), textvariable="")
c.place(height= 50,width= 450,y=0)
c.focus()
c.bind("<Return>",returnC)
c.pack()

cButton = Button(root, text="Entry c", command=returnC)
cButton.place(height= 50,width= 50,y=100,x=450)

cLabel = Label(root, text="")
cLabel.pack()

delta1 = 0
def delta():
    global delta1
    bToSecond = bUser * bUser
    anotherOne = 4 * aUser * cUser
    delta1 = bToSecond - anotherOne
    print(delta1)

deltaButton = Button(root, text="Get delta value", command=delta)
deltaButton.place(height= 50,width= 500,y=150,)


def x1():
    sth1 = - bUser - math.sqrt(delta1)
    sth2 = 2 * aUser
    sth3 = sth1/sth2
    print(sth3)



def x2():
    sth1 = - bUser + math.sqrt(delta1)
    sth2 = 2 * aUser
    sth3 = sth1/sth2
    print(sth3)



def drawSth(A,B,C):
    global win
    if win is not None:
        win.place_forget()
    a = []
    b = []
    for x in range(-15,15,1):
        y=(A * (x**2))+(B * x)+C
        a.append(x)
        b.append(y)
    hah = plt.figure()
    haha=hah.add_subplot(111)
    haha.grid()
    haha.plot(a, b)
    var = FigureCanvasTkAgg(hah, root)
    win=var.get_tk_widget()
    win.place(height= 250,width= 500,y=300)

showButton = Button(root, text="show", command=lambda:drawSth(aUser,bUser,cUser))
showButton.place(height= 50,width= 500,y=250)


root.mainloop()