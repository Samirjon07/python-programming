price=49
txt="The price is {} dollars"
print(txt.format(price))

quantity=3
itemno=567
price=49
myorder="I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))


myorder="I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity,itemno,price))


myorder="I want {quantity} pieces of item number {itemno} for {price:.2f} dollars."
print(myorder.format(quantity=quantity,itemno=itemno,price=price))


age=36
name="John"
txt="His name is {1}. {1} is {0} years old."
print(txt.format(age,name))