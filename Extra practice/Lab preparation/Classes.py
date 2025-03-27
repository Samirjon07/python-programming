class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
        
person1=Person("Samirjon",17)
print(person1.name) 
print(person1.age)
Person.introduce(person1)
        