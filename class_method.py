#pickling and unpickling
# import pickle 
 
# data = [ { 'a':'A', 'b':2, 'c':3.0 } ] 
# data_string = pickle.dumps(data) 
# print ('PICKLE:', data_string )       


# import pickle 
# import pprint 
# data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ] 
# print ('BEFORE:',) 
# pprint.pprint(data1) 

#dumps 
# data1_string = pickle.dumps(data1)

# #loads
# data2 = pickle.loads(data1_string) 
# print ('AFTER:',) 
# pprint.pprint(data2) 
 
# print ('SAME?:', (data1 is data2)) 
# print ('EQUAL?:', (data1 == data2))

import pickle
import pprint
object= ['m','a','h','e','s']
print("BEFORE")
pprint.pprint(object)

object_we= pickle.dumps(object)
object1 = pickle.loads(object_we)
print('After:')
pprint.pprint(object1)
print('SAME?:',(object is object1))
print('EQUAL?:',(object != object1))

class Student:
    sname="marvel"
    def __init__(mahi,person_name,person_section,person_rollno):
        mahi.name=person_name
        mahi.section=person_section
        mahi.rollno=person_rollno
    def display(self):
        print(self.sname,"----",self.name,"----",self.section,"----",self.rollno)

    
s=Student("mahi","a",21)
b=Student("khan","a",45)
c=Student("vamshi","B",98)
s.display()
b.display()
c.display()

#1.static var  2.non static var  3.local var
class student:
    def __init__(self):
        self.sn="mahi"
        self.sc="suryapet"
        print(" python is a powerfull language")
    def display(self):
        print(self.sn,"...........",self.sc)

student().display()

# class student:
#     def read(khan,sname,sid):
#         khan.sname='mahi'
#         khan.sid= 21
#         print('completed')
#     def display(khan):
#         print(khan.sname,"........",khan.sid,"......")  

# s=student()
# s.display()


# class rank:
#     def read(self,x,y):
#         self.sn=x
#         self.sid=y
#         print("yeahh")

#     def display(self):
#         print(self.sn,'---',self.sid,self.srank)
# s=rank()
# s.read("mahi","87","1")        
# s.display() 

class student:
    def read(self,x,y):
        self.name=x
        self.city=y
        print("it is python")
        
    def display(self):
        print(self.name,"...........",self.city)

s=student()
s.read("vamshi","hyd")
s.display()