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

#Frame1 items
label1 = Label(frame1, text = "Pirate DB", font = ("Comic Sans MS",30), bg = "salmon", fg="black
               ")
label1.pack()

#Frame2 items
label2 = Label(frame2, text = "Search", font = ("Comic Sans MS",20), bg = "salmon", fg="white")
entry = Entry(frame2, font = ("Comic Sans MS",20), bg = "olive", fg="white")
searchButton = Button(frame2, text = "Go", font = ("Comic Sans MS",20), bg = "salmon", fg="white")

#Frame3 items
label3 = Label(frame3, text = "Frame 3", font = ("Comic Sans MS",20), bg = "salmon", fg="white")
label3.pack()

#Frame4 items
listbox = Listbox(frame4, font = ("Comic Sans MS",20), bg = "olive", fg="white")
listbox.pack()
listDict = {"Jerry":"1", "Gerry":"2", "Jeri":"3", "Gerri":"4"}
deleteButton = Button(frame4, text="Delete", font = ("Comic Sans MS", 20), command=listDelete, bg = "Olive", fg="white")
deleteButton.pack()
extButton = Button(frame4, text="Exit", font = ("Comic Sans MS", 20), command=ext, bg = "Olive", fg="white")
extButton.pack()
for item in listDict:
    listbox.insert(END, item)
    
#The grid
label2.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)
searchButton.grid(row = 0, column = 2)

#The Frames
frame1.grid(row = 0, column = 0)
frame2.grid(row = 0, column = 1)
frame3.grid(row = 1, column = 0)
frame4.grid(row = 1, column = 1)

window1.mainloop()
