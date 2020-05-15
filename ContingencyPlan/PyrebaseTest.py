import pyrebase

config = {
  "apiKey": "",
  "authDomain": "tinovationtestpy.firebaseapp.com",
  "databaseURL": "https://tinovationtestpy.firebaseio.com",
  "storageBucket": "tinovationtestpy.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

users = db.child("users").get()

print(users.val())
