class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname,self.lastname)
    
Object1=Person("Samirjon","Tursunov")
Object1.printname()

#create a child class:
class Student(Person):#hust in parentheses write parent name
    pass

Object2=Student("Mironshoh","Dustonov")
Object2.printname()

class Student(Person):
    def __init__(self,fname,lname):
        self.name=fname
        self.surname=lname
    def printname(self):
        print(self.name,self.surname)
        
Object2.printname()     
Object1.printname()   

#adding default graduation year
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

#adding Graduation year
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)