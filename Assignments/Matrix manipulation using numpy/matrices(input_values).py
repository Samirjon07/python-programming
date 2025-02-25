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
    
    
def multip(matrix1,matrix2):
    mult=np.dot(matrix1,matrix2)
    print(f"\n\nThe multiplication of \n\n{matrix1} \nand \n\n{matrix2} is : \t\n\n {mult} ")
multip(matrix1,matrix2)




'''CHATGPT WRITTEN:
import numpy as np

def get_matrix(name):
    """Function to take user input and return a NumPy matrix."""
    try:
        rows = int(input(f"\nEnter number of rows for {name}: "))
        cols = int(input(f"Enter number of columns for {name}: "))
        
        print(f"\nEnter values for {name} ({rows}x{cols}):")
        matrix = np.array([[int(input(f"Element [{r+1},{c+1}]: ")) for c in range(cols)] for r in range(rows)])
        
        print(f"\n{name}:")
        print(matrix)
        return matrix

    except ValueError:
        print("\n❌ Invalid input! Please enter integers only.")
        return get_matrix(name)  # Retry input in case of invalid values

def multiply_matrices(matrix1, matrix2):
    """Function to multiply two matrices with validation."""
    if matrix1.shape[1] != matrix2.shape[0]:  # Validate multiplication condition
        print("\n❌ Error: Cannot multiply! Columns of Matrix1 must match Rows of Matrix2.")
        return None
    
    result = np.dot(matrix1, matrix2)
    print(f"\n✅ The multiplication of \n\n{matrix1} \nand \n\n{matrix2} \nis:\n\n{result}")
    return result

# Main execution
matrix1 = get_matrix("Matrix1")
matrix2 = get_matrix("Matrix2")

multiply_matrices(matrix1, matrix2)


'''