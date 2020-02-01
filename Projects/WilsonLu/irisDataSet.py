# Load libaries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal_length', 'sepal_width', 'petal length', 'petal width', 'class']
dataset = pandas.read_csv(url, names=names)

# Dimensions of a dataset (instances, attributes)
# instances (rows), attributes (columns)
print(dataset.shape)

# head (first # of rows)
print(dataset.head(20)) # prints first 20 rows

# descriptions (Statistical Summary)
# includes count, mean, standard deviation, min, 25%, 50% (median), 75%, max
print(dataset.describe())

# class distribution (# of instances that belong to each class)
# species of iris in this case
print(dataset.groupby('class').size())

# 2 types of plots, univariate and multivariate
# univariate: better understand each attribute (focus on different trends in the specific attribute)
    # box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
    # histogram
dataset.hist()
plt.show()
# Gaussian distribution is normal distribution

# multivariate: better understand relationship between attributes (track trends with each other)
    # Scatter Plot Matrix
scatter_matrix(dataset)
plt.show()

# Split-out validation dataset
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, train_size = validation_size, random_state = seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# Evaluate each method in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits = 10, random_state = seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv = kfold, scoring = scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()


# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
# precision is the percentage that the class has predicted correctly
# support is the number of samples in the true response that lie in that class
# weighted average is the weighted average of precision, recall and f1-score where the weights are the support values.
# precision and recall wiki https://en.wikipedia.org/wiki/Precision_and_recall
# f1-score is the harmonic mean of precision adn recall. The scores corresponding to every calss will tell you the accuracy of the classifier in classifying the data points in that particular class comapred to all other classes

# the columns are the predicted iris-setosa, versicolor, and virginica
# [what is Iris-setosa[num, num, num]
# what is Iris-versicolor[num, num, num]
# what is virginica[num, num, num]]
