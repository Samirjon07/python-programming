'''
Convert Decimal number to octal using print() output formatting
Given:

num = 8
Expected Output:

The octal number of decimal number 8 is 10
'''


number=int(input("\nEnter a decimal number: "))
print("\nThe octal equivalent of",number,"is",oct(number))#oct() will convert decimal number to octal: output will look like 0o10

#ANSWER:
print('%o' % number)#%o will convert decimal number to octal, % number will print the octal number
#%o is used in old-style string formatting in Python.


#Other options:
print('{:o}'.format(number))  #{:o} will convert decimal number to octal


print(f'{number:o}') #{number:o} will convert decimal number to octal
