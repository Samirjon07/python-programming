import numpy as np
from numpy import random

#zeros((rows,columns))
x=np.zeros((1,2))
print("\nThe matrix with 1 row and 2 columns which has all 0:\n",x)


#full((rows,columns),number)
x=np.full((1,2),1)
print("\nThe matrix which has 1 row and 2 columns which has all 1:\n",x)


#create two matrix 2*2 which only should have numbers (5,10,15)
num=np.arange(5,20,5)
#size(rows,columns,number of matrices)
x=(random.choice(num,size=(2,2,2)))
print("\nThe 2*2 matrices which have only 5,10,15",x)


#arange(starting point, ending point, difference or increment)
x=np.arange(1,500,50)
print("\nThe matrix between 1 and 500 with difference 50:\n",x)

#shape - it will show number of rows and columns
x=np.array([[1,2,3,4],[5,6,7,8]])
print("\n",x.shape)

# this will add all numbers it is not matrix addtion
x=np.array([[1,2,3,4],[5,6,7,8]])
y=np.array([[0,1,2,3],[4,5,6,7]])
z=np.sum([x,y])
print("\nSum of all values:\n",z)


x=np.array([[1,2,3,4],[5,6,7,8]])
y=np.array([[0,1,2,3],[4,5,6,7]])
z=np.sum([x,y],axis=0)
print("\nSum of columns:\n",z)


z=np.sum([x,y],axis=1)
print("\nSum of rows:\n",z)


#joining two arrays -- it is not addition
x=np.array([[1,2,3,4],[5,6,7,8]])
y=np.array([[0,1,2,3],[4,5,6,7]])
z=np.vstack((x,y))
print("\nDimension of x array:\n",x.ndim)
print("\nDimension of x array:\n",y.ndim)
print("\nJoining two arrays:\n",z)
print("\nDimension of z array:\n",z.ndim)


#merging two arrays
x=np.array([[1,2,3,4],[5,6,7,8]])
y=np.array([[0,1,2,3],[4,5,6,7]])
z=np.hstack((x,y))
print("\nMerging two arrays:\n",z)


z=np.column_stack((x,y))
print("\n",z)