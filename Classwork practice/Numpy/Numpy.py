# Before importing numpy you should numpy from command prompt or powershell 
# Write Install numpy -- it will automatically install it 

import numpy as np


x=np.array([10,11,12,13,14])
print(x)


y=np.array((10,20,30,40))
print(y)


print(x[1]) #accessing elements of array called x by using array
print(y[1]) #accessing elements of array called y by using array

# zero dimensional array -- which has 0, 0 address in matrix
zero=np.array(10)
print(zero)


# one dimensional array -- which consists of multiple zero dimensional arrays
one=np.array([10,20,30,40])
print(one)


# two dimensional array -- which consists of multiple one dimensional arrays
two=np.array([[1,2,3],[4,5,6]])
print("\n",two)

# three dimensional array -- which consists of multiple two dimensional arrays
three=np.array([[[1,2,3],[4,5,6]]+[[1,2,3],[4,5,6]]])
print("\n",three)

# addition of two dimensional matrices
sum =two+two
print("\n",sum)

# method to know dimension of matrix : name.ndim
print(f"The number of dimensions in \n {one} is {one.ndim}")
print(f"The number of dimensions in \n {two} is {two.ndim}")
print(f"The number of dimensions in \n {three} is {three.ndim}")