import Advanced_python.add as add
import Advanced_python.sub as sub
import Advanced_python.div as div
import Advanced_python.mul as mul

def oper():
    operations={
        1:add.addition,
        2:sub.substaction,
        3:mul.multiplication,
        4:div.division
        }
    print("Choose any option:\n")
    for key, values in operations.items():
        print(f"{key}. {values.__name__}\n")
    return operations



def choose(operations,choice,a,b):
    if choice in operations:
        result = operations[choice](a, b)
        print(f"Result: {result}")
    else:
        print("\nInvalid operation!!!,Try again!!!!!!!!!!!!\n")
       
        

operations = oper()
choice=int(input("\nChoose which operation you want: "))
a=int(input("Enter you first value: "))
b=int(input("Enter you second value: "))

choose(operations, choice,a,b)

    