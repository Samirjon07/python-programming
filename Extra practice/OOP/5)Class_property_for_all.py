"""Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white."""




class Vehicle:
    Color="White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

Object1=Bus("School Volvo", 180, 12)
Object2=Car("Ford", 180, 12)
print(Object1.Color,Object1.name,Object1.max_speed,Object1.mileage)
print(Object2.Color,Object2.name,Object2.max_speed,Object2.mileage)