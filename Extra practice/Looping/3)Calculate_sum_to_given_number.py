'''
Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55
'''

i=1
sum=0
number=int(input("Enter a number: \n"))

'''
for i in range (1,number):
    for j in range (1,i+1):
        print(j,end="+") # it will show all the steps 
#it will put + at the end too        
    sum+=i
    print("=",sum)    
    
'''  
    

'''
for i in range(1, number):  
    for j in range(1, i + 1):  
        if j == i:  
            print(j, end="")  # Print last number without "+"
        else:
            print(j, end="+")  # Print numbers with "+"
    
    sum += i  # Add i to sum
    print(" =", sum)  # Print the sum
'''


# Loop to calculate sum
for i in range(1, number):
    sum += i  # Add i to sum

# Print only the last step
for j in range(1, number):
    if j == number - 1:
        print(j, end="")  # Print last number without "+"
    else:
        print(j, end="+")  # Print numbers with "+"

print(" =", sum)  # Print final sum
    
    
    

    
    
    
    
'''
# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)

'''
    
    