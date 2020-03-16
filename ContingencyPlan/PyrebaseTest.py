import pyrebase

config = {
  "apiKey": "AIzaSyCmuYk0aioP-O_6z_kF4xzLk6yD9eY3xTc",
  "authDomain": "tinovationtestpy.firebaseapp.com",
  "databaseURL": "https://tinovationtestpy.firebaseio.com",
  "storageBucket": "tinovationtestpy.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

users = db.child("users").get()

print(users.val())
