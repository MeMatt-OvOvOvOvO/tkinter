from tkinter import *

root = Tk()
root.title("Dropdown Menu")
root.geometry("300x300")

def showSelection():
    myLabel = Label(root, text=clicked.get()).pack()

days = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]

clicked = StringVar()
clicked.set(days[0])

drop = OptionMenu(root, clicked, *days)
drop.pack()

myButton = Button(root, text="Pokaż wybrane", command=showSelection).pack()

root.mainloop()