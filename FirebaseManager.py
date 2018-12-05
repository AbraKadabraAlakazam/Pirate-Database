from firebase import firebase as fb

class FirebaseManager:
    app = fb.FirebaseApplication("https://pirate-db-ab58b.firebaseio.com/", None)

    def writeToFile(self, idNum, obj):
        results = self.app.put("", idNum, obj)

    def getAll(self):
        d = self.app.get("", None)
        return d

    def DeletePirate(self, id):
        self.app.delete(id, None)
