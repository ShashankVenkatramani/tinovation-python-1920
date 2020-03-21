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
    dataUID = []
    users = db.child("users").get().val()
    requests = db.child("requests").get().val()
    for userUID in users:
        user = users[userUID]
        data.append([user["photography"], user["pokemon"], user["robotics"], user["scientology"], user["technology"]])
        dataUID.append(userUID)
    for requestUID in requests:
        request = requests[requestUID]
        data.append([request["photography"], request["pokemon"], request["robotics"], request["scientology"], request["technology"]])
        dataUID.append(requestUID)
    df_cluster_data = pd.DataFrame(data, columns = ["photography", "pokemon", "robotics", "scientology", "technology"])
    print(df_cluster_data)
    print(data[197])
    print(dataUID[197])
    pca = PCA(n_components = 2, random_state=1)
    df_cluster_pca = pca.fit_transform(df_cluster_data)
    print("Explained Variance Ratio: " + str(df_cluster_pca.explained_variance_ratio_.cumsum()[1]))

    distortions = []
    K_count_range = range(1,10)

    for i in K_to_try:
        model = KMeans(n_clusters=i, init='k-means++', random_state=1)
        model.fit(df_cluster_pca)
        distortions.append(model.inertia_)

    plt.plot(K_to_try, distortions, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Distortion Amount')
    plt.show()

def random_generator(size = 32, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

if __name__ == "__main__":
    # execute only if run as a script
    downloadTrainingData()
