import json
from tkinter import *
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

class FileManager:
    path = "pirateDB.json"


    def writeToFile(self, idNum, obj):
        try:
            f = open(self.path, "r")
            d = json.load(f)
            f.close()
        except:
            d = {}
        d[idNum] = obj
        f = open(self.path, "w")
        json.dump(d, f)
        f.close()

# Functions for the windows
def addNew():
    x=0

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
