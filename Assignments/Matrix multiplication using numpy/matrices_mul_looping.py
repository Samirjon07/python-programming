import numpy as np

mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])

mat2=np.array([[0,1,2],[3,4,5],[6,7,8]])

mul=np.zeros((3,3))

if mat1.shape[1]==mat2.shape[0]:
    
    #First method: this method is not efficient
    for i in range(3):
        for j in range(3):
            result=0
            for k in range(3):
                result +=mat1[i,k]*mat2[k,j]
            mul[i,j] = result    
            
    print("\n",mul)   


    #Second method: this is built in function
    mul = np.dot(mat1, mat2)
    print("\n",mul)


    #Third method: this method is efficient
    for i in range(len(mat1)):# len(mat1)= it means how many rows in mat1
        for j in range(mat2.shape[1]):
            result=0
            for k in range(mat1.shape[1]):
                result +=mat1[i,k]*mat2[k,j]
            mul[i,j] = result    
            
    print("\n",mul)
else:
    print("Matrices cannot be multiplied")
    print("Rows of first matrix should be equal to columns of second matrix")