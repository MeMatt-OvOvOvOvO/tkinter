from tkinter import *
import requests
import json

root = Tk()
root.title("Air quality")

# centrowanie okna na ekranie
appWidth = 350
appHeight = 200

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = (screenWidth / 2) - (appWidth / 2)
y = (screenHeight / 2) - (appHeight / 2)

root.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

root.configure(background='white')

pizza = StringVar()
pizza.set("400")


co2LabelName = Label(root, font=('Helvetica', 20))
co2LabelName.grid(column=0, row=2, sticky=NS)
co2LabelValue = Label(root, font=('Helvetica', 20))
co2LabelValue.grid(column=1, row=2, sticky=NS)


pm10LabelName = Label(root, font=('Helvetica', 20))
pm10LabelName.grid(column=0, row=3, sticky=NS)
pm10LabelValue = Label(root, font=('Helvetica', 20))
pm10LabelValue.grid(column=1, row=3, sticky=NS)


pm25LabelName = Label(root, font=('Helvetica', 20))
pm25LabelName.grid(column=0, row=4, sticky=NS)
pm25LabelValue = Label(root, font=('Helvetica', 20))
pm25LabelValue.grid(column=1, row=4, sticky=NS)

def showSelection():
    zmienna()

options = [
     ("Kraków, Aleja Krasińskiego"),
     ("Kraków, ul. Bujaka"),
     ("Kraków, ul. Bulwarowa"),
     ("Kraków, ul. Złoty Róg")
     ]
# for text, option in options:
#     myRadiobutton = Radiobutton(root, text=text, variable=pizza, value=option)
#     myRadiobutton.grid(column=1, row=0)
#     drop = OptionMenu(root, clicked, *options)  # pokazuje DropDownMEnu
#     drop.grid(column=0, row=0)

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options) #pokazuje DropDownMEnu
drop.grid(column=0, row=0)


myButton = Button(root, text="Submit", command=showSelection)
myButton.grid(column=1, row=0)


def zmienna():
    id = "0"
    global pizza
    try:

        if clicked.get() == "Kraków, Aleja Krasińskiego":
            id = "400"
            city = "Kraków, Aleja Krasińskiego"
        elif clicked.get() == "Kraków, ul. Bujaka":
            id = "401"
            city = "Kraków, ul. Bujaka"
        elif clicked.get() == "Kraków, ul. Bulwarowa":
            id = "402"
            city = "Kraków, ul. Bulwarowa"
        elif clicked.get() == "Kraków, ul. Złoty Róg":
            id = "10123"
            city = "Kraków, ul. Złoty Róg"

        co2 = "co2"
        pm10 = "pm10"
        pm25 = "pm25"

        apiValue = requests.get("http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/" + id)
        apiValue = json.loads(apiValue.content)

        try:
            co2Value = apiValue['coIndexLevel']['indexLevelName']
        except Exception as apiError:
            co2Value = "brak parametru"

        try:
            pm10Value = apiValue['pm10IndexLevel']['indexLevelName']
        except Exception as apiError:
            pm10Value = "brak parametru"

        try:
            pm25Value = apiValue['pm25IndexLevel']['indexLevelName']
        except Exception as apiError:
            pm25Value = "brak parametru"

        cityLabel = Label(root, text=city, background='white', font=('Helvetica', 20))
        cityLabel.grid(column=0, row=1, columnspan=2, sticky=EW)

        if co2Value == 'Bardzo dobry':
            color = 'green'
        elif co2Value == 'Dobry':
            color = 'orange'
        else:
            color = '#000000'

        co2LabelName = Label(root, text=co2, font=('Helvetica', 20))
        co2LabelName.grid(column=0, row=2, sticky=NS)
        co2LabelValue["text"] = co2Value
        co2LabelValue["fg"] = color
        co2LabelValue.grid(column=1, row=2, sticky=NS)

        if pm10Value == 'Bardzo dobry':
            color = 'green'
        elif pm10Value == 'Dobry':
            color = 'orange'
        else:
            color = '#000000'

        pm10LabelName = Label(root, text=pm10, font=('Helvetica', 20))
        pm10LabelName.grid(column=0, row=3, sticky=NS)
        pm10LabelValue["text"] = pm10Value
        pm10LabelValue["fg"] = color
        pm10LabelValue.grid(column=1, row=3, sticky=NS)

        if pm25Value == 'Bardzo dobry':
            color = 'green'
        elif pm25Value == 'Dobry':
            color = 'orange'
        else:
            color = '#000000'

        pm25LabelName = Label(root, text=pm25, font=('Helvetica', 20))
        pm25LabelName.grid(column=0, row=4, sticky=NS)
        pm25LabelValue["text"] = pm25Value
        pm25LabelValue["fg"] = color
        pm25LabelValue.grid(column=1, row=4, sticky=NS)

    except Exception as apiError:
        api = "Error..."

zmienna()
root.mainloop()