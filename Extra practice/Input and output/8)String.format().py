'''
Write a program to use string.format() method to format the following three variables as per the expected output

Given:

totalMoney = 1000
quantity = 3
price = 450
Expected Output:

I have 1000 dollars so I can buy 3 football for 450.00 dollars.
'''

totalMoney = 1000
quantity = 3
price = 450

print("\nI have {} dollars so I can buy {} football for {} dollars.".format(totalMoney, quantity, price))


'''ANSWER:

quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))

'''