from tkinter import *
from PIL import ImageTk, Image, ImageFilter

root = Tk()
root.title("Images viewer")

img1 = Image.open("Images/hah.jpg")
myImage1 = ImageTk.PhotoImage(img1)
img2 = Image.open("Images/haha.jpg")
myImage2 = ImageTk.PhotoImage(img2)
img3 = Image.open("Images/hahah.jpg")
myImage3 = ImageTk.PhotoImage(img3)
img4 = Image.open("Images/hahaha.jpg")
myImage4 = ImageTk.PhotoImage(img4)
img5 = Image.open("Images/hahahah.jpg")
myImage5 = ImageTk.PhotoImage(img5)

imageList = [myImage1, myImage2, myImage3, myImage4, myImage5]

status = Label(root, text="Image 1 of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)

myLabel = Label(image=myImage1)
myLabel.grid(row=1, column=0, columnspan=3)

current_filter = ''

def nextImage(imageNumber):
    global myLabel
    global nextButton
    global backButton
    global current_filter
    global blur
    global contour
    global find_edges

    myLabel.grid_forget()
    myLabel = Label(image=imageList[imageNumber-1])
    nextButton = Button(root, text=">>", command=lambda: nextImage(imageNumber+1))
    backButton = Button(root, text="<<", command=lambda: backImage(imageNumber-1))
    blur = Button(root, text='blur', command=lambda: _filter(imageNumber - 1, 'BLUR'))
    contour = Button(root, text='contour', command=lambda: _filter(imageNumber - 1, 'CONTOUR'))
    find_edges = Button(root, text='find_edges', command=lambda: _filter(imageNumber - 1, 'FIND_EDGES'))

    if imageNumber == 5:
        nextButton = Button(root, text=">>", state=DISABLED)

    myLabel.grid(row=1, column=0, columnspan=3)
    backButton.grid(row=2, column=0)
    nextButton.grid(row=2, column=2)
    blur.grid(row=0, column=0)
    contour.grid(row=0, column=1)
    find_edges.grid(row=0, column=2)

    status = Label(root, text="Image " + str(imageNumber) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)

def backImage(imageNumber):
    global myLabel
    global nextButton
    global backButton
    global current_filter
    global blur
    global contour
    global find_edges

    myLabel.grid_forget()
    myLabel = Label(image=imageList[imageNumber - 1])
    nextButton = Button(root, text=">>", command=lambda: nextImage(imageNumber + 1))
    backButton = Button(root, text="<<", command=lambda: backImage(imageNumber - 1))
    blur = Button(root, text='blur', command=lambda: _filter(imageNumber - 1, 'BLUR'))
    contour = Button(root, text='contour', command=lambda: _filter(imageNumber - 1, 'CONTOUR'))
    find_edges = Button(root, text='find_edges', command=lambda: _filter(imageNumber - 1, 'FIND_EDGES'))

    if imageNumber == 1:
        backButton = Button(root, text="<<", state=DISABLED)

    myLabel.grid(row=1, column=0, columnspan=3)
    backButton.grid(row=2, column=0)
    nextButton.grid(row=2, column=2)
    blur.grid(row=0, column=0)
    contour.grid(row=0, column=1)
    find_edges.grid(row=0, column=2)

    status = Label(root, text="Image " + str(imageNumber) + " of " + str(len(imageList)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W + E)

def _filter(imageNumber, x):
    global myLabel
    global current_filter

    print(current_filter == x)
    print(imageNumber)
    if current_filter == x:
        current_filter = ''
        if imageNumber == 0:
            imageList[imageNumber] = myImage1
        if imageNumber == 1:
            imageList[imageNumber] = myImage2
        if imageNumber == 2:
            imageList[imageNumber] = myImage3
        if imageNumber == 3:
            imageList[imageNumber] = myImage4
        if imageNumber == 4:
            imageList[imageNumber] = myImage5
    else:
        if x == 'BLUR':
            filtr = ImageFilter.BLUR
            current_filter = 'BLUR'
        elif x == 'CONTOUR':
            filtr = ImageFilter.CONTOUR
            current_filter = 'CONTOUR'
        elif x == 'FIND_EDGES':
            filtr = ImageFilter.FIND_EDGES
            current_filter = 'FIND_EDGES'

        if imageNumber == 0:
            img = img1.filter(filtr)
        if imageNumber == 1:
            img = img2.filter(filtr)
        if imageNumber == 2:
            img = img3.filter(filtr)
        if imageNumber == 3:
            img = img4.filter(filtr)
        if imageNumber == 4:
            img = img5.filter(filtr)
        imageList[imageNumber] = ImageTk.PhotoImage(img)

    myLabel.grid_forget()
    myLabel = Label(image=imageList[imageNumber])
    myLabel.grid(row=1, column=0, columnspan=3)

backButton = Button(root, text='<<', command=backImage, state=DISABLED)
exitButton = Button(root, text='Exit', command=root.quit)
nextButton = Button(root, text='>>', command=lambda: nextImage(2))

blur = Button(root, text='blur', command=lambda: _filter(0, 'BLUR'))
contour = Button(root, text='contour', command=lambda: _filter(0, 'CONTOUR'))
find_edges = Button(root, text='find_edges', command=lambda: _filter(0, 'FIND_EDGES'))

blur.grid(row=0, column=0)
contour.grid(row=0, column=1)
find_edges.grid(row=0, column=2)

backButton.grid(row=2, column=0)
exitButton.grid(row=2, column=1)
nextButton.grid(row=2, column=2)
status.grid(row=3, column=0, columnspan=3, sticky=W+E)

root.mainloop()