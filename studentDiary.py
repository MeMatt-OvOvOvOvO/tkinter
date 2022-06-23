from tkinter import *
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("500x700")

allRecords = ''
# tworzenie bazy lub połaczenie z istniejącą bazą
myConnection = sqlite3.connect('studentDiary.db')

# tworzenie kursora do bazy
myCursor = myConnection.cursor()

# funkcja zapisująca dane w bazie
def saveData():
    # tworzenie bazy lub połaczenie z istniejącą bazą
    myConnection = sqlite3.connect('studentDiary.db')

    # tworzenie kursora do bazy
    myCursor = myConnection.cursor()

    try:
        # tworzenie tabeli
        myCursor.execute("""CREATE TABLE students (
                    subcjectName text,
                    firstSemesterGrade integer,
                    secondSemesterGrade integer,
                    finalGrade integer
                    )""")
    except Exception as apiError:
        api = "Error..."

    myCursor.execute("INSERT INTO students VALUES (:subcjectName, :firstSemesterGrade, :secondSemesterGrade, :finalGrade)",
        {
            'subcjectName': subcjectName.get(),
            'firstSemesterGrade': firstSemesterGrade.get(),
            'secondSemesterGrade': secondSemesterGrade.get(),
            'finalGrade': finalGrade.get(),
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

# funkcja odczytująca dane z bazy
def queryShow():
    # tworzenie bazy lub połaczenie z istniejącą bazą
    myConnection = sqlite3.connect('studentDiary.db')

    # tworzenie kursora do bazy
    myCursor = myConnection.cursor()

    myCursor.execute("SELECT *, oid FROM students")
    records = myCursor.fetchall()
    # print(records) # wyświetla dane pobrane z bazy w konsoli w postaci listy z krotkami
    showRecords = ''
    for record in records:
        showRecords += str(record) + "\n"
    allRecords = ''
    number = 0
    firstSemester = 0
    secondSemester = 0
    final = 0

    for record in records:
        number += 1
        firstSemester += record[1]
        secondSemester += record[2]
        final += record[3]
        allRecords += str(record) + '\n'
    if number != 0:
        firstSemesterAverage = firstSemester / number
        secondSemesterAverage = secondSemester / number
        finalAverage = final / number
        allRecords += 'First semester average: ' + str(firstSemesterAverage) + '\n' + 'Second semester average: ' + str(secondSemesterAverage) + '\n' + 'Final average: ' + str(finalAverage)
    else:
        allRecords = '...'

    allRecords = showRecords + allRecords
    # maybe needed
    # try:
    #     queryLabel.destroy()
    # except:
    #     pass
    queryLabel = Label(root, text=allRecords)
    queryLabel.grid(row=14, column=0, columnspan=2)

    # zapisz zmiany
    myConnection.commit()

    # rozłączenie z bazą
    myConnection.close()

# funkcja usuwająca rekordy z bazy
def deleteData():
    # tworzenie bazy lub połaczenie z istniejącą bazą
    myConnection = sqlite3.connect('studentDiary.db')

    # tworzenie kursora do bazy
    myCursor = myConnection.cursor()

    myCursor.execute("DELETE FROM students WHERE oid=" + deleteId.get())

    # zapisz zmiany
    myConnection.commit()

    # rozłączenie z bazą
    myConnection.close()

# pola tekstowe do wprowadzania danych
subcjectName = Entry(root, width=15, font=('Helvetica', 14))
subcjectName.grid(row=0, column=1, padx=5)
firstSemesterGrade = Entry(root, width=15, font=('Helvetica', 14))
firstSemesterGrade.grid(row=1, column=1)
secondSemesterGrade = Entry(root, width=15, font=('Helvetica', 14))
secondSemesterGrade.grid(row=2, column=1)
finalGrade = Entry(root, width=15, font=('Helvetica', 14))
finalGrade.grid(row=3, column=1)

# opisy pól tekstowych
subcjectNameLabel = Label(root, text="Nazwa przedmiotu:", font=('Helvetica', 14))
subcjectNameLabel.grid(row=0, column=0, sticky=E)
firstSemesterGradeLabel = Label(root, text="Ocena z pierwszego semestru:", font=('Helvetica', 14))
firstSemesterGradeLabel.grid(row=1, column=0, sticky=E)
secondSemesterGradeLabel = Label(root, text="Ocena z drugiego semestru:", font=('Helvetica', 14))
secondSemesterGradeLabel.grid(row=2, column=0, sticky=E)
finalGradeLabel = Label(root, text="Ocena roczna:", font=('Helvetica', 14))
finalGradeLabel.grid(row=3, column=0, sticky=E)

# przycisk usuwający dane z bazy
queryButton = Button(root, text="Usuń rekord", command=deleteData)
queryButton.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
queryButton1 = Button(root, text="Pokaż dane", command=queryShow)
queryButton1.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# przycisk odczytujący dane z bazy
sth = Label(root, text=allRecords, font=('Helvetica', 14))
sth.grid(row=14, column=0, columnspan = 2, sticky=E)

# przycisk zapisujący dane z pól tektowych w bazie
saveButton = Button(root, text="Zapisz dane", command=saveData)
saveButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# usuwanie
deleteId = Entry(root, width=15, font=('Helvetica', 14))
deleteId.grid(row=11, column=1)

deleteLabel = Label(root, text="Id rekordu:", font=('Helvetica', 14))
deleteLabel.grid(row=11, column=0, sticky=E)

# zapisz zmiany
myConnection.commit()

# rozłaczenie z bazą
myConnection.close()

root.mainloop()