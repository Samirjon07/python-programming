import numpy as np

try:
    row=int(input("Enter number of rows: "))
    column=int(input("Enter number of columns: "))
    
    matrix= np.zeros((row,column),dtype=int)
    
    for x in range(row):
        matrix[x]=list(map(int,input().split()))
    
    print("\nMatrix:")
    for row_values in matrix:
        print(" ".join(map(str,row_values)))
    
    
except ValueError:
    print("Invalid value!!!")