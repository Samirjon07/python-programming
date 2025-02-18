def factorial(a):
    try:
        
        if a>0:
            if a == 1:
                return 1
            else:
                return a * factorial(a-1)

        else:
            print("Factorial is not defined for negative numbers.")
        

    except ValueError:
        print("Entered value is wrong")