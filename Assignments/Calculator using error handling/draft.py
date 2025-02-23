import numpy as np

try:
    print("***** FIRST MATRIX *****")
    row = int(input("Enter number of rows: "))
    column = int(input("Enter number of columns: "))

    matrix1 = np.zeros((row, column), dtype=int)

    # Display initial matrix format
    print("\nEnter values inside the matrix format:")
    print("[")
    for _ in range(row):
        print(" [", " ".join("_" for _ in range(column)), "]")
    print("]")

    # Taking input row by row
    print("\nNow enter values row by row:")
    print("[")
    for i in range(row):
        print(" [ ", end="")  # Start row bracket
        for j in range(column):
            matrix1[i, j] = int(input())  # Take input one by one
            if j < column - 1:
                print("", end=" ")  # Keep cursor in the same row
        print("]")  # Close row bracket
    print("]")  # Close full matrix

    # Display the first matrix
    print("\nMatrix1:")
    print("[")
    for i in range(row):
        print(" [", " ".join(map(str, matrix1[i])), "]")
    print("]")

    print("\n***** SECOND MATRIX *****")
    row = int(input("Enter number of rows: "))
    column = int(input("Enter number of columns: "))

    matrix2 = np.zeros((row, column), dtype=int)

    # Display initial matrix format
    print("\nEnter values inside the matrix format:")
    print("[")
    for _ in range(row):
        print(" [", " ".join("_" for _ in range(column)), "]")
    print("]")

    # Taking input row by row
    print("\nNow enter values row by row:")
    print("[")
    for i in range(row):
        print(" [ ", end="")  # Start row bracket
        for j in range(column):
            matrix2[i, j] = int(input())  # Take input one by one
            if j < column - 1:
                print("", end=" ")  # Keep cursor in the same row
        print("]")  # Close row bracket
    print("]")  # Close full matrix

    # Display the second matrix
    print("\nMatrix2:")
    print("[")
    for i in range(row):
        print(" [", " ".join(map(str, matrix2[i])), "]")
    print("]")

except ValueError:
    print("Invalid value! Please enter numbers only.")

    
def multip(matrix1,matrix2):
    mult=np.dot(matrix1,matrix2)
    print( mult)
multip(matrix1,matrix2)