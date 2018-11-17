#Imports
from tkinter import *

#Main window
window1 = Tk()
window1.config(bg="salmon")

#Functions
def listDelete():
    listbox.delete(ANCHOR)
def ext():
    window1.destroy()

#The Frames
frame1 = Frame(window1)
frame1.config(bg="salmon")
frame2 = Frame(window1)
frame2.config(bg="salmon")
frame3 = Frame(window1)
frame3.config(bg="salmon")
frame4 = Frame(window1)
frame4.config(bg="salmon")

#Shortcuts
cm = ("Comic Sans MS", 20)

#Frame1 items
label1 = Label(frame1, text = "Pirate DB", font = ("Comic Sans MS", 30), bg = "salmon", fg="black")
label1.pack()

#Frame2 items
label2 = Label(frame2, text = "Search", font = cm, bg = "salmon", fg="white")
entry = Entry(frame2, font = cm, bg = "olive", fg="white")
label2.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)

#Frame3 items
leftImg = PhotoImage(file = "bloot.gif")
rightImg = PhotoImage(file = "right.gif")
rightImg = rightImg.subsample(2)
leftImg = leftImg.subsample(2)
leftBtn = Button(frame3, image = leftImg, bg = "olive")
rightBtn = Button(frame3, image = rightImg, bg = "olive")
pirateName = Label(frame3, text = "Pirate", bg  = "salmon", font = ("Comic Sans MS", 30), fg = "white")
leftBtn.grid(row = 1, column = 0, rowspan = 4)
rightBtn.grid(row = 1, column = 2, rowspan = 4)
pirateName.grid(row = 0, column = 1)
fillerImg = PhotoImage(file = "knoi.gif")
pirateLabel = Label(frame3, image = fillerImg, bg = "salmon")
pirateLabel.grid(row = 1, column = 1)
shipLabel = Label(frame3, text = "Ship: The Rugberry", bg = "salmon", fg = "white", font = cm)
ficLabel = Label(frame3, text = "Fictional: True", bg = "salmon", fg = "white", font = cm)
shipLabel.grid(row = 2, column = 1)
ficLabel.grid(row = 3, column = 1)

#Frame4 items
label4 = Label(frame4, text = "View Pirate", font = cm, bg = "salmon", fg = "white")
label4.pack() 
listbox = Listbox(frame4, font = cm, bg = "Olive", fg="white")
listbox.pack()
listDict = {"Jerry":"1", "Gerry":"2", "Jeri":"3", "Gerri":"4"}
deleteButton = Button(frame4, text="Delete", font = cm, command=listDelete, bg = "Olive", fg="white")
deleteButton.pack()
extButton = Button(frame4, text="Exit", font = cm, command=ext, bg = "Olive", fg="white")
extButton.pack()
for item in listDict:
    listbox.insert(END, item)
    
#The Frames
frame1.grid(row = 0, column = 0)
frame2.grid(row = 0, column = 1)
frame3.grid(row = 1, column = 0)
frame4.grid(row = 1, column = 1)

window1.mainloop()
