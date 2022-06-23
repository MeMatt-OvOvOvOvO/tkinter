import math, tkinter

window = tkinter.Tk()
window.title("Simplest calculator")

screen = tkinter.Entry(window, text="asdfMovie", borderwidth=5, font=("Helvetica Neue", 28), bg="black", fg="white")
screen.grid(row=0, column=0, columnspan=5, rowspan=2, padx=1, pady=10, ipady=40)

for i in range(1, 10):
    rowNumber = math.floor((i - 1) / 3) + 2
    columnNumber = ((i + 2) % 3)
    btn = tkinter.Button(window, text=str(i), height=3, width=6, font=("Helvetica Neue", 20), bg="black", fg="orange")
    btn.grid(row=rowNumber, column=columnNumber, padx=1, pady=1)

specialSigns = [["+", 1, 4], ["-", 2, 4], ["*", 3, 4], ["/", 4, 4], ["0", 4, 0], ["C", 4, 1], ["=", 4, 2]]

for x in specialSigns:
    btn = tkinter.Button(window, text=x[0], height=3, width=6, font=("Helvetica Neue", 20), bg="orange", fg="black")
    if x[0] == "0":
        btn.config(bg="black", fg="orange")

    btn.grid(row=x[1] + 1, column=x[2], padx=1, pady=1)

window.mainloop()