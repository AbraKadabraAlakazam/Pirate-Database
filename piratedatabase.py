class Pirate:
    name = ""
    ship = ""
    fictional = False

    def loadFromDict(self, d):
        self.name = d["name"]
        self.ship = d["ship"]
        self.fictional = d["fictional"]

    def getDict(self):
        d = {"name": self.name,
             "ship":self.ship,
             "fictional":self.fictional}
        return d
        
class FileManager:
    path = "pirates.json"
