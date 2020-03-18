import pyrebase
import string
import random

config = {
  "apiKey": "AIzaSyCmuYk0aioP-O_6z_kF4xzLk6yD9eY3xTc",
  "authDomain": "tinovationtestpy.firebaseapp.com",
  "databaseURL": "https://tinovationtestpy.firebaseio.com",
  "storageBucket": "tinovationtestpy.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

num_test_users = 100
uploadType = "requests"

def uploadTestData():
    for x in range(num_test_users):
        uid = random_generator()
        #arbitrary names used here, based on google form
        robotics = random.randint(1,5)
        photography = random.randint(1,5)
        scientology = random.randint(1,5)
        technology = random.randint(1,5)
        pokemon = random.randint(1,5)

        data = {"name": random_generator(6), "robotics": robotics, "photography": photography, "scientology": scientology, "technology": technology, "pokemon": pokemon}
        db.child(uploadType).child(uid).set(data)
        print("Uploaded User " + str(x))
    print("Completed uploading")
#used as a fake user id
def random_generator(size = 32, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

if __name__ == "__main__":
    # execute only if run as a script
    uploadTestData()
