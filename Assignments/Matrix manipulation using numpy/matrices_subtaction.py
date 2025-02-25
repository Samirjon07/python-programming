import numpy as np

mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])

mat2=np.array([[0,1,2],[3,4,5],[6,7,8]])


#First method .zeroes will create matrix of zeros where after all values there is dot
sub=np.zeros((3,3))

if (mat1.shape[1]==mat2.shape[1]) & (mat1.shape[0]==mat2.shape[0]):
    for i in range(mat1.shape[1]):
        for j in range(mat1.shape[0]):
            sub[i,j]=mat1[i,j]-mat2[i,j]
print("\n",sub)            



#Second method .full will create 3*3 matrix where  all values are 0 (no dot)
sub=np.full((3,3),0)

if (mat1.shape[1]==mat2.shape[1]) & (mat1.shape[0]==mat2.shape[0]):
    for i in range(mat1.shape[1]):
        for j in range(mat1.shape[0]):
            sub[i,j]=mat1[i,j]-mat2[i,j]
print("\n",sub)
