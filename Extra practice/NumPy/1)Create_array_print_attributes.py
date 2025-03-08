'''
Create a 4X2 integer array and Prints its attributes
Note: The element must be a type of unsigned int16. And print the following Attributes: –

The shape of an array.
Array dimensions.
The Length of each element of the array in bytes.
Expected Output:

Printing Array

[[64392 31655]
 [32579     0]
 [49248   462]
 [    0     0]]

Printing NumPy array Attributes

Array Shape is:  (4, 2)
Array dimensions are  2
Length of each element of array in bytes is  2
'''
import numpy as np
arrayis=np.array([[64392,31655],[32579,0],[49248,462],[0,0]],dtype=np.uint16)

print(arrayis)
print(arrayis.shape)
print(arrayis.ndim)
print(arrayis.itemsize)



"""
import numpy

firstArray = numpy.empty([4,2], dtype = numpy.uint16) 
print("Printing Array")
print(firstArray)

print("Printing numpy array Attributes")
print("1> Array Shape is: ", firstArray.shape)
print("2>. Array dimensions are ", firstArray.ndim)
print("3>. Length of each element of array in bytes is ", firstArray.itemsize)
"""