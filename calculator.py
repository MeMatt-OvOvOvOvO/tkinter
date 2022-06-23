from tkinter import *

window = Tk()
window.title("Calculator")

#rozmiar okna aplikacji
window.geometry('200x250')

def button_click(number):
    #entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def wyczysc():
    entry.delete(0, END)

#Pole wynikow
entry = Entry(window, borderwidth=0, bg="#666666", fg="#eeeeee", font=("Helvetica", 16))
entry.place(height= 50,width= 200)

#dodawanie
def button_add():
    firstNumber = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(firstNumber)
    entry.delete(0, END)

#odejmowanie
def button_subtract():
    firstNumber = entry.get()
    global f_num
    global math
    math = "subtract"
    f_num = float(firstNumber)
    entry.delete(0, END)

#mnozenie
def button_multiply():
    firstNumber = entry.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(firstNumber)
    entry.delete(0, END)

#dzielenie
def button_divide():
    firstNumber = entry.get()
    global f_num
    global math
    math = "divide"
    f_num = float(firstNumber)
    entry.delete(0, END)

#rowna sie
def button_equal():
    secondNumber = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, f_num + int(secondNumber))
    elif math == "subtract":
        entry.insert(0, f_num - int(secondNumber))
    elif math == "multiply":
        entry.insert(0, f_num * int(secondNumber))
    elif math ==  "divide":
        try:
            entry.insert(0, f_num / int(secondNumber))
        except ZeroDivisionError:
            entry.insert(0, "Nie dziel przez 0!")
        else:
            entry.insert(0, f_num / int(secondNumber))

btn7 = Button(window, text='7', command=lambda: button_click(7))
btn7.place(height= 50,width= 50,y=50)
btn4 = Button(window, text='4', command=lambda: button_click(4))
btn4.place(height= 50,width= 50,y=100)
btn1 = Button(window, text='1', command=lambda: button_click(1))
btn1.place(height= 50,width= 50,y=150)
btn0 = Button(window, text='0', command=lambda: button_click(0))
btn0.place(height= 50,width= 50,y=200)

#2st
btn8 = Button(window, text='8', command=lambda: button_click(8))
btn8.place(height= 50,width= 50,x=50,y=50)
btn5 = Button(window, text='5', command=lambda: button_click(5))
btn5.place(height= 50,width= 50,x=50,y=100)
btn2 = Button(window, text='2', command=lambda: button_click(2))
btn2.place(height= 50,width= 50,x=50,y=150)
btnC = Button(window, text='C', command=lambda: wyczysc())
btnC.place(height= 50,width= 50,x=50,y=200)

#3rd
btn9 = Button(window, text='9', command=lambda: button_click(9))
btn9.place(height= 50,width= 50,x=100,y=50)
btn6 = Button(window, text='6', command=lambda: button_click(6))
btn6.place(height= 50,width= 50,x=100,y=100)
btn3 = Button(window, text='3', command=lambda: button_click(3))
btn3.place(height= 50,width= 50,x=100,y=150)
btnRown = Button(window, text='=', command= button_equal)
btnRown.place(height= 50,width= 50,x=100,y=200)

#4th
btnPlus = Button(window, text='+', command= button_add)
btnPlus.place(height= 50,width= 50,x=150,y=50)
btnMinus = Button(window, text='-', command= button_subtract)
btnMinus.place(height= 50,width= 50,x=150,y=100)
btnMnoz = Button(window, text='*', command= button_multiply)
btnMnoz.place(height= 50,width= 50,x=150,y=150)
btnDziel = Button(window, text='/', command= button_divide)
btnDziel.place(height= 50,width= 50,x=150,y=200)

window.mainloop()