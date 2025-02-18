def power():
    try:
        a = int(input("Enter value of a:"))
        power = int(input("Enter value of power:"))
        c = a**power
        print(f"The answer of a power {power}:", c)
    except ValueError:
        print("Entered value is wrong")