import json
from tkinter import *
from random import randint
from firebase import firebase as fb
class Pirate:
    name  = ""
    ship = ""
    fic = False
    image = ""
    
    def getDict(self):
        d = {
            "name": self.name,
            "ship": self.ship,
            "fic": self.fic,
            "image": self.image
            }
        return d

    def loadFromDict(self, d):
        self.name = d["name"]
        self.ship = d["ship"]
        self.fic = d["fic"]
        sefl.image = d["image"]

class FirebaseManager:
    app = fb.FirebaseApplication("https://pirate-db-ab58b.firebaseio.com/", None)

    def writeToFile(self, idNum, obj):
        results = self.app.put("", idNum, obj)

# Functions for the windows
def addNew():
    global win, nText, nShip, optionString
    p = Pirate()
    p.name = nText.get()
    p.ship = nShip.get()
    p.fictional = optionString.get()

    nText.delete("end", 0)
    nShip.delete("end", 0)
    optionString.set("")
    
    d = p.getDict()
    fm = FirebaseManager()
    idNum = randint(11111, 99999)
    fm.writeToFile(idNum, d)

    win.destroy()

def Canc():
    global win
    win.destroy()

def browseImage():
    x=0
    
def loadwindow(root):
    global win, nText, nShip, optionString,lbImage 
    win = root
    
    # Configure the window
    root.title("Pirate Database")
    root.config(bg="LightBlue")

    # The Objects
    title = Label(root, text = "Pirate Database", font = "Arial 25 bold", bg ="LightBlue")
    name = Label(root, text = "Name", font = "Arial 20", bg ="LightGreen")
    ship = Label(root, text = "Ship", font = "Arial 20", bg ="LightGreen")
    Fictional = Label(root, text = "Fictional", font = "Arial 20", bg ="LightGreen")
    nText = Entry(root, font = "Arial 15", bg ="LightGreen")
    nShip = Entry(root, font = "Arial 15", bg ="LightGreen")
    save = Button(root, font = "Arial 20", text = "Save", bg ="LightGreen", command = addNew)
    cancel = Button(root, font = "Arial 20", text = "Cancel", bg ="LightGreen", command = Canc)
    imgSelect = Button(root, font = "Arial 20", text = "Select an Image", bg = "LightGreen", command = browseImage)
    lbImage = Label(root, text="", font="Arial 20", bg="LightBlue")

    # The Grid
    title.grid(row = 0, column = 0, columnspan = 3)
    name.grid(row = 1, column = 0)
    ship.grid(row = 2, column = 0)
    Fictional.grid(row = 3, column  = 0)
    nText.grid(row = 1, column = 1)
    nShip.grid(row = 2, column = 1)
    save.grid(row = 5, column = 0)
    cancel.grid(row = 5, column = 1)
    imgSelect.grid(row=4, column = 0)
    lbImage.grid(row=4, column=1)

    # The Dropdown menus 
    optionString = StringVar(root)
    optionString.set("True")
    dropdown = OptionMenu(root, optionString, "True", "False")
    dropdown.config(font = "Arial 12", width = "10", bg = "LightGreen")
    dropdown.nametowidget(dropdown.menuname).config(font  = "Arial 12", bg = "LightGreen")
    dropdown.grid(row = 3, column = 1)

    root.mainloop()        
