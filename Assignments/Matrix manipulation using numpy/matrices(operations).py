import numpy as np

mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n\n",mat1)

mat2=np.array([[0,1,2],[3,4,5],[6,7,8]])
print("\n\n",mat2)

sum=mat1+mat2
print("\n\n",sum)

sub=mat1-mat2
print("\n\n",sub)

mul=np.dot(mat1,mat2)
print("\n\n",mul)