try:
    print(x)
except NameError:
    print("Variable x is not defined")
finally: # finally will run no matter whether there is an error or not
    print("The try block is finished")