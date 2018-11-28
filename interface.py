#Imports
from tkinter import *
import FirebaseManager

#Main window
window1 = Tk()
window1.config(bg="salmon")

#Functions
def listDelete():
    listbox.delete(ANCHOR)
def ext():
    
    window1.destroy()
    
def doFilter():
    filt = entry.get()
    listbox.delete(0, "end")
    for pirate in d:
        if (filt.lower() in d[pirate]["name"].lower() or
        filt.lower() in d[pirate]["ship"].lower()):
            listbox.insert(END, d[pirate]["name"])

def searchUpdate(e):
    doFilter()
    
def display(pirateId):
    pirateName.config(text =d[pirateId]["name"])
    shipLabel.config(text = "Ship: " + d[pirateId]["ship"])
    if d[pirateId]["fic"] == "True":
        ficLabel.config(text = "This pirate is fictional!")
    else:
        ficLabel.config(text = "This pirate was/is real!")

def onselect(e):
    w = e.widget
    index  = int(w.curselection()[0])
    piratename = w.get(index)
    for pirate in d:
        if piratename.lower() == d[pirate]["name"].lower():
            display(pirate)

def scrollRight():
    index = int(listbox.curselection()[0])
    listbox.selection_clear(index)
    if index == len(d)-1:
        index  = 0
    else:
        index += 1
    updateListbox(index)

def scrollLeft():
    index = int(listbox.curselection()[0])
    listbox.selection_clear(index)
    if index == 0:
        index  = len(d)-1
    else:
        index -= 1
    updateListbox(index)

def updateListbox(index):
    listbox.selection_set(index)
    piratename = listbox.get(index)
    for pirate in d:
        if piratename.lower() == d[pirate]["name"].lower():
            display(pirate)
            
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
entry.bind("<KeyRelease>", searchUpdate)
label2.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)

#Frame3 items
leftImg = PhotoImage(file = "bloot.gif")
rightImg = PhotoImage(file = "right.gif")
rightImg = rightImg.subsample(2)
leftImg = leftImg.subsample(2)
leftBtn = Button(frame3, image = leftImg, bg = "olive", command = scrollLeft)
rightBtn = Button(frame3, image = rightImg, bg = "olive", command = scrollRight)
pirateName = Label(frame3, text = "Example Pirate", bg  = "salmon", font = ("Comic Sans MS", 30), fg = "white")
leftBtn.grid(row = 1, column = 0, rowspan = 4)
rightBtn.grid(row = 1, column = 2, rowspan = 4)
pirateName.grid(row = 0, column = 1)
fillerImg = PhotoImage(file = "knoi.gif")
pirateLabel = Label(frame3, image = fillerImg, bg = "salmon")
pirateLabel.grid(row = 1, column = 1)
shipLabel = Label(frame3, text = "Ship: The Example Ship", bg = "salmon", fg = "white", font = cm)
ficLabel = Label(frame3, text = "Fictional: True", bg = "salmon", fg = "white", font = cm)
shipLabel.grid(row = 2, column = 1)
ficLabel.grid(row = 3, column = 1)

#Frame4 items
label4 = Label(frame4, text = "View Pirate", font = cm, bg = "salmon", fg = "white")
label4.pack() 
listbox = Listbox(frame4, font = cm, bg = "Olive", fg="white")
listbox.bind("<<ListboxSelect>>", onselect)
listbox.pack()
fm = FirebaseManager.FirebaseManager()
d = fm.getAll()
for item in d:
    pirate = d[item]
    listbox.insert(END, pirate["name"])
deleteButton = Button(frame4, text="Delete", font = cm, command=listDelete, bg = "Olive", fg="white")
deleteButton.pack()
extButton = Button(frame4, text="Exit", font = cm, command=ext, bg = "Olive", fg="white")
extButton.pack()
    
#The Frames
frame1.grid(row = 0, column = 0)
frame2.grid(row = 0, column = 1)
frame3.grid(row = 1, column = 0)
frame4.grid(row = 1, column = 1)

window1.mainloop()
