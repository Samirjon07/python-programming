"""
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""

class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
BMW=Vehicle(5,10)
print(BMW.max_speed,BMW.mileage)