'''
Accept a list of 5 float numbers as an input from the user

Expected Output:

[78.6, 78.6, 85.3, 1.2, 3.5]
'''
list=[]#create an empty list
for i in range(0,5):#looping until 5 numbers are entered
    number=float(input())#takes floating number as input
    list.append(number)#will add number to the end of the list
print(list)

'''ANSWER:

numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)
'''