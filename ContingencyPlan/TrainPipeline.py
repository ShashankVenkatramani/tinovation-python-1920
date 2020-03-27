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
    print("Data succesfully placed into Pandas Dataframe")



    pca = PCA().fit(df_cluster_data)
    cluster_pca = PCA(n_components = 2, random_state=0).fit_transform(df_cluster_data)

    plt.figure()
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('Number of Components')
    plt.xlabel('Variance')
    plt.show()

    pca = PCA(n_components = 2, random_state=0)
    cluster_pca = pca.fit_transform(df_cluster_data)
    print("PCA reduction succesfull")

    distortions = []
    K_count_range = range(1,10)

    for i in K_count_range:
        model = KMeans(n_clusters=i, random_state=0)
        model.fit(cluster_pca)
        distortions.append(model.inertia_)
    print("Plotting for optimal KCount")
    plt.plot(K_count_range, distortions, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Distortion Amount')
    plt.show()

    print("Creating final Model")
    model = KMeans(n_clusters=5, random_state=0)
    final_model = model.fit(cluster_pca)

    cluster_number = model.predict(cluster_pca)

    print("Plotting clusters")
    plt.scatter(cluster_pca[cluster_number == 0, 0], cluster_pca[cluster_number == 0, 1], s = 50, c = 'blue', label = 'Cluster 1')
    plt.scatter(cluster_pca[cluster_number == 1, 0], cluster_pca[cluster_number == 1, 1], s = 50, c = 'green', label = 'Cluster 2')
    plt.scatter(cluster_pca[cluster_number == 2, 0], cluster_pca[cluster_number == 2, 1], s = 50, c = 'purple', label = 'Cluster 3')
    plt.scatter(cluster_pca[cluster_number == 3, 0], cluster_pca[cluster_number == 3, 1], s = 50, c = 'yellow', label = 'Cluster 4')
    plt.scatter(cluster_pca[cluster_number == 4, 0], cluster_pca[cluster_number == 4, 1], s = 50, c = 'red', label = 'Cluster 5')

    plt.scatter(final_model.cluster_centers_[:, 0], final_model.cluster_centers_[:, 1], s=100, c = 'black', label = 'Centroids')
    plt.title('Clusters of Students')
    plt.xlabel('PCA 1')
    plt.ylabel('PCA 2')
    plt.legend()
    plt.grid()
    plt.show()




def random_generator(size = 32, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

if __name__ == "__main__":
    # execute only if run as a script
    downloadTrainingData()
