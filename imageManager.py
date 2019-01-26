from google.cloud import storage
from PIL import Image, ImageTk
import os, io, urllib
import datetime

class ImageManager:
    
    #Use these credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

    client = storage.Client()
    bucket = client.get_bucket('pirate-db-ab58b.appspot.com')
    url = ''
    imagepath = "knoi.gif"

    def uploadImage(self):
        imageBlob = self.bucket.blob("images/" + os.path.basename(self.imagepath))
        imageBlob.upload_from_filename(self.imagepath)
        d = datetime.datetime(2040, 1, 1)
        self.url = imageBlob.generate_signed_url(d)

    def downloadUrl(self):
        rawdata = urllib.request.urlopen(self.url).read()
        img = Image.open(io.BytesIO(rawdata))
        imgtk = ImageTk.PhotoImage(img)
        return(imgtk)

