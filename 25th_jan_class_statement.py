#Create a Vehicle class without any variables and methods

class Vehicle:
    pass
v1=Vehicle()

#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle:

 def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage
class Bus(Vehicle):
 pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

#Create a Class with instance attributes
class Student:
   school='MVR'
   def __init__(mahi, name, roolnum, phnnum, course):
    mahi.name=name
    mahi.roolnum=roolnum
    mahi.phnnum=phnnum
    mahi.course=course

student1=Student('mike', 38,988347623,'pytho') 
student2=Student('mon',43,9384782637,'CSS')
print(student1.name, 38,988347623,'pytho')
print(student2.name,43,9384782637,'CSS')    

     
     