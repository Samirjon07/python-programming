'''
Write a Python code to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''

#Using list
number=[] 
for i in range(1,6):
    number.append(i) #I made it usind a list
    print(number)
    
#Using nested loop    
for i in range(1,6):
    for j in range (1,i+1):
        print(j,end=" ")
    print()
    
'''
print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")

'''