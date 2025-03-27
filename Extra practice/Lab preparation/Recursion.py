num = int(input("Enter a number: "))



def recursion(num):
    if (num==1):
        return 1
    else:
        return num*recursion(num-1 )
    
print(recursion(num))