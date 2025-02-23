import Division as D
import Multiplication as M
import Subtraction as S
import Addition as A
import Power as P
import Factorial as F



def oper():
    operations ={
        1: A.addition,
        2: S.subtraction,
        3: M.multiplication,
        4: D.division,
        5: P.power,
        6: F.factorial
    }
    print("\n******************************************************************************")
    print("\n********************   PLEASE CHOOSE ONE OPERATIONS   ************************")
    print("\n******************************************************************************")
    for key,values in operations.items():
        print(f"\n******* {key}--{values.__name__.upper()} \n")
    return operations 

def choose(operations):
    try:
        choice = int(input("Enter your choice from 1 to 6: "))

        if choice in operations:
            if choice == 6:
                a = int(input("Enter value of what factorial :"))  
                result = operations[choice](a)
            else:
                result = operations[choice]()
            print(f"Result: {result}")
        else :
            print("\n**********************************************************")
            print("\n****************   INVALID OPERATIONS!!!  ****************")
            print("\n**********************************************************\n")

            print("\n**********************************************************")
            print("\n********************   PLEASE RETRY  *********************\n")
            print("\n**********************************************************")
            choose(operations)


       
    except ValueError:
        print("\n****************************************************************")
        print("\n******************   ENTERED VALUE IS WRONG   ******************\n")
        print("****************************************************************\n")
        oper()
        choose(operations)

operations=oper()
choose(operations)