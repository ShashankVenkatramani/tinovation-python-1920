import pyrebase
import string
import random

import pandas as pd
import numpy as np
import collections
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_samples
import matplotlib.pyplot as plt
from matplotlib import cm


config = {
  "apiKey": "AIzaSyCmuYk0aioP-O_6z_kF4xzLk6yD9eY3xTc",
  "authDomain": "tinovationtestpy.firebaseapp.com",
  "databaseURL": "https://tinovationtestpy.firebaseio.com",
  "storageBucket": "tinovationtestpy.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


def downloadTrainingData():
    data = []
    users = db.child("users").get().val()
    requests = db.child("requests").get().val()
    for userUID in users:
        user = users[userUID]
        data.append([userUID, user["photography"], user["pokemon"], user["robotics"], user["scientology"], user["technology"]])
    for requestUID in requests:
        request = requests[requestUID]
        data.append([requestUID, request["photography"], request["pokemon"], request["robotics"], request["scientology"], request["technology"]])
    print(data)

def random_generator(size = 32, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

if __name__ == "__main__":
    # execute only if run as a script
    downloadTrainingData()
