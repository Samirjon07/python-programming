
from numpy import random
import numpy as np

print("\nThe random integer number from 1 to 100: \n",random.randint(100)) # there is no logic- it will generate random integer number up to 100


#randint method can take size parameter
x=random.randint(100,size=5)
print("\nThe random matrix with 1 row and 5 columns: \n",x) #it will generate one dimentional array with 5 elements
print(type(x))# it is <class 'numpy.ndarray'>



#size can take two or more parameters to show size of the array
x=random.randint(100,size=(5,2)) #size(rows,columns)
print("\nThe random matrix with 5 rows and 2 columns: \n",x) #it will generate two dimentional array with 5 rows and 2 columns


#randint-rand integer, but rand is without integer it means: it will generate floating number up to 1
x=random.rand(3,5)
print("\nThe random matrix with 3 rows and 5 columns with up to 1 in each element:\n",x)


#choice[] you write numbers it will choose one randomly
x=random.choice([1,3,5,7,9])
print("\nFrom [1,3,5,7,9] these numbers it will choose one randomly :\n",x)


#choice([numbers],size=(rows,columns))
x=(random.choice([1,3,5,7,9],size=(3,3)))
print("\nThe random matrix with 3 rows and 3 columns whih will choose only [1,3,5,7,9]:\n",x)


#randint(starting point, ending point,)
x=np.random.randint(1,20,10)
print("\nThe random matrix with 10 random numbers from 1 and 10:\n",x)



