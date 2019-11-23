# Numpy Practice
import numpy as np
# 1
arr = np.arange(10)
print(arr)

#2
arr = arr[arr % 2 == 1]
print(arr)

#3
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(out)

#4
arr = arr.reshape(2, -1)
print(arr)

#5
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.intersect1d(a, b)
print(c)

#6
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
a = np.setdiff1d(a, b)
print(a)

#7
