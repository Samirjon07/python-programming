try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:   #else will run if there is no error
    print("Variable x is defined")