'''
Write a Python program to print the reverse number pattern using a for loop.

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''


for j in range(5,0,-1):
    for i in range(j,0,-1):
        print(i,end=" ")
    print()
   

"""
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
"""

