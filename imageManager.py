from google.cloud import storage
import os
import datetime

class ImageManager:
    
    #Use these credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

    client = storage.Client()
    bucket = client.get_bucket('pirate-db-ab58b.appspot.com')
    url = ''
    imagepath = "knoi.gif"

    def uploadImage(self):
        imageBlob = self.bucket.blob("images/" + self.imagepath)
        imageBlob.upload_from_filename(self.imagepath)
        d = datetime.datetime(2040, 1, 1)
        self.url = imageBlob.generator_signed_url(d)


