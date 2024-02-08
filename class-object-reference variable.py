#class-object-reference variable


#normal method:
class student:
    def read(self):
     print("it is python")

a=student()
a.read()


#
class student:
    def read(self):
     print("it is python")
    def write(self):
     print("this is prathibha")

a=student()
a.read()
a.write()

#
class student:
    def read(self,x,y):
        self.name=x
        self.city=y
        print("it is python")

a=student()
a.read("krish","hyderabad")


#
class student:
    def read(self,x,y):
        self.name=x
        self.city=y
        print("it is python")
        
    def display(self):
        print(self.name,"...........",self.city)

s=student()
s.read("dog","hyd")
s.display()




#constructer:_init_
class student:
    def _init_(self,x,y):
        self.name=x
        self.city=y
        print("it is python")
        print(self.name,"...........",self.city)

s=student("ravi","hyd")


#types of variables:
#1.static var  2.non static var  3.local var
#
class student:
    def _init_(self):
        self.sname="ravi"
        self.scity="vijaywada"
        print("it is python")
    def display(self):
        print(self.sname,"...........",self.scity)

student().display()



#static var
class employee:
    sname="coco"
    def __init__(self,emp_name,emp_id,emp_loc):
        self.name=emp_name
        self.id=emp_id
        self.loc=emp_loc
    def display(self):
        print(self.sname,"----",self.name,"----",self.id,"----",self.loc)

    

a=employee("vamshi","987","hyderabad")
b=employee("ram","023","benguluru")
c=employee("krish","873","chennai")

a.display()
b.display()
c.display()

#s=student()
#print(s.name)--object reference
#print(student.name)--class reference