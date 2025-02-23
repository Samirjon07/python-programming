import numpy as np

try:
    print("\n\n**** FIRST MATRIX *****\n")
    row=int(input("Enter number of rows: "))
    column=int(input("Enter number of columns: "))
    
    matrix1= np.zeros((row,column),dtype=int)
    
    print("\nEnter values inside the matrix format:")
    print("[")
    
    for x in range(row):
        print(" [",end=" ")
        for y in range(column):
            matrix1[x,y]=int(input())
        print("]")
    print("]")
    
    print("\nMatrix1:")
    print(matrix1)
    
   
   
    print("\n\n***** SECOND MATRIX *****\n")
    row=int(input("Enter number of rows: "))
    column=int(input("Enter number of columns: "))
    
    matrix2= np.zeros((row,column),dtype=int)
    
    print("\nEnter values inside the matrix format:")
    print("[")
    
    for x in range(row):
        print(" [",end=" ")
        for y in range(column):
            matrix2[x,y]=int(input())
        print("]")
    print("]")
    
    print("\nMatrix2:")
    print(matrix2)
    
    
except ValueError:
    print("Invalid value!!!")