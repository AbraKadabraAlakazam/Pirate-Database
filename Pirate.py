import json
from tkinter import *
from random import randint
from firebase import firebase as fb
class Pirate:
    name  = ""
    ship = ""
    fic = False
    
    def getDict(self):
        d = {
            "name": self.name,
            "ship": self.ship,
            "fic": self.fic
            }
        return d

    def loadFromDict(self, d):
        self.name = d["name"]
        self.ship = d["ship"]
        self.fic = d["fic"]

class FirebaseManager:
    app = fb.FirebaseApplication("https://pirate-db-ab58b.firebaseio.com/", None)

    def writeToFile(self, idNum, obj):
        results = self.app.put("", idNum, obj)

# Functions for the windows
def addNew():
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

root = Tk()

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

# The Grid
title.grid(row = 0, column = 0, columnspan = 3)
name.grid(row = 1, column = 0)
ship.grid(row = 2, column = 0)
Fictional.grid(row = 3, column  = 0)
nText.grid(row = 1, column = 1)
nShip.grid(row = 2, column = 1)
save.grid(row = 4, column = 0, columnspan = 3)

# The Dropdown menus 
optionString = StringVar(root)
optionString.set("")
dropdown = OptionMenu(root, optionString, "True", "False", "Unknown")
dropdown.config(font = "Arial 12", width = "10", bg = "LightGreen")
dropdown.nametowidget(dropdown.menuname).config(font  = "Arial 12", bg = "LightGreen")
dropdown.grid(row = 3, column = 1)

root.mainloop()        
