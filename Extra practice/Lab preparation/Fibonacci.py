num=int(input("Enter a number: "))

def fibonacci(num):
    if num<=1:
        return num
    else:
        return(fibonacci(num-1)+fibonacci(num-2))
    
for i in range(num):
    print(f"fibonacci({i})={fibonacci(i)}")