try:
    print(x)
except NameError:
    print("Variable x is not defined")
finally:
    print("The try block is finished")