def multiplication():
    try:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        c = a*b
        print("The answer of multiplication :", c)
    except ValueError:
        print("Entered value is wrong")