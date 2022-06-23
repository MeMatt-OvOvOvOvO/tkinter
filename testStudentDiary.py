from tkinter import *
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("750x400")

# tworzenie bazy lub połaczenie z istniejącą bazą
myConnection = sqlite3.connect('addressBook.db')

# tworzenie kursora do bazy
myCursor = myConnection.cursor()

# pola tekstowe do wprowadzania danych
subcjectName = Entry(root, width=30, font=('Helvetica', 14))
subcjectName.grid(row=0, column=1, padx=5)
firstSemesterGrade = Entry(root, width=30, font=('Helvetica', 14))
firstSemesterGrade.grid(row=1, column=1)
secondSemesterGrade = Entry(root, width=30, font=('Helvetica', 14))
secondSemesterGrade.grid(row=2, column=1)
finalGrade = Entry(root, width=30, font=('Helvetica', 14))
finalGrade.grid(row=3, column=1)
zipcode = Entry(root, width=30, font=('Helvetica', 14))
zipcode.grid(row=4, column=1)

# opisy pól tekstowych
subcjectNameLabel = Label(root, text="Nazwa przedmiotu:", font=('Helvetica', 14))
subcjectNameLabel.grid(row=0, column=0, sticky=E)
firstSemesterGradeLabel = Label(root, text="Ocena z pierwszego semestru:", font=('Helvetica', 14))
firstSemesterGradeLabel.grid(row=1, column=0, sticky=E)
secondSemesterGradeLabel = Label(root, text="Ocena z drugiego semestru:", font=('Helvetica', 14))
secondSemesterGradeLabel.grid(row=2, column=0, sticky=E)
finalGradeLabel = Label(root, text="Ocena roczna:", font=('Helvetica', 14))
finalGradeLabel.grid(row=3, column=0, sticky=E)
zipcodeLabel = Label(root, text="costam:", font=('Helvetica', 14))
zipcodeLabel.grid(row=4, column=0, sticky=E)

# funkcja zapisująca dane w bazie
def saveData():
    # tworzenie bazy lub połaczenie z istniejącą bazą
    myConnection = sqlite3.connect('addressBook.db')

    # tworzenie kursora do bazy
    myCursor = myConnection.cursor()

    myCursor.execute("INSERT INTO addresses VALUES (:subcjectName, :firstSemesterGrade, :secondSemesterGrade, :finalGrade, :zipcode)",
                    {
                        'subcjectName': subcjectName.get(),
                        'firstSemesterGrade': firstSemesterGrade.get(),
                        'secondSemesterGrade': secondSemesterGrade.get(),
                        'finalGrade': finalGrade.get(),
                        'zipcode': zipcode.get()
                    })

    # zapisz zmiany
    myConnection.commit()

    # rozłączenie z bazą
    myConnection.close()

    # czyszczenie pól tekstowych
    subcjectName.delete(0, END)
    firstSemesterGrade.delete(0, END)
    secondSemesterGrade.delete(0, END)
    finalGrade.delete(0, END)
    zipcode.delete(0, END)

# przycisk zapisujący dane z pól tektowych w bazie
saveButton = Button(root, text="Zapisz dane", command=saveData)
saveButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# zapisz zmiany
myConnection.commit()

# rozłaczenie z bazą
myConnection.close()

root.mainloop()