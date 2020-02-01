import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
nArr=np.array([])
oArr=[]
for x in arr:
    if x%2!=0:
        oArr.append(x)
        nArr=np.append(nArr,-1)
    else:
        nArr=np.append(nArr,x)


oneDarr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
twoDarr = np.reshape(oneDarr, (-1,2))

a=np.array([0,1,2,3,4,5])
b=np.array([3,4,5,6,7,8])

for x in a:
    for y in b:
        if (x==y):
            print(x)
            a=np.delete(a, np.where(a==x))

print(a)
print(twoDarr)
print(oArr)
print(nArr)
