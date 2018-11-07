from firebase import firebase as fb
app = fb.FirebaseApplication("https://pirate-db-ab58b.firebaseio.com/", None)
d = app.get("22666", None)
print(d)

newPirate = {"name": "Jack Sparrow", "ship": "Black Pearl", "fic": "True"}
result = app.put("", "BAKASHI", newPirate)
print(result)
