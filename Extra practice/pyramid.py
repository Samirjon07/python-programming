num =int(input("Enter num pf pyramid: "))

for i in range (1,2*num-1,6):
    print(" "*(num-3),"*"*i)
    num-=3
    
 