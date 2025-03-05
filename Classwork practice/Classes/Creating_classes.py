#simple class 
class Car:
    speed=5 # property

#simple object
BMW=Car()
print(BMW)#it will print <__main__.Car object at 0x0000018E19025D00>

#to print the value:
print(BMW.speed)# it will print speed of 5


# init function is built in- it is used to assign values to object properties
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
Object1=Person("Samirjon",17)

print(Object1.name)
print(Object1.age)


#__str() is string representation of an object: The __str__() method returns a human-readable, or informal, string representation of an object. 
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def myfunc(self):
        print("Hello my name is "+self.name)


Object1=Person("Samirjon",17)

print("\n",Object1)#it will print Samirjon(17)

Object1.myfunc()

#change object properties:
Object1.age=18

#Delete object properties
del Object1.age
#Delete object itself
del Object1












"""
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
"""





