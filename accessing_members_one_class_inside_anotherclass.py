
class Student:
    def __init__(self,sname,sage,stenth,sinter,sdegree):
        self.sname=sname
        self.sage=sage
        self.stenth=stenth
        self.sinter=sinter
        self.sdegree=sdegree


    def studentDetails(self):
        print("sname=",self.sname) 
        print("sage=",self.sage)    
        print("stenth=",self.stenth)  
        print("sinter=",self.sinter) 
        print("sdegree=",self.sdegree)  

class Test:
    def display(self):
        self.studentDetails()


class Test1:
    def display1(self):
        self.studentDetails()

s=Student("madhu",24,60,68,72.0)

# s.studentDetails()
# t=Test()
# t1=Test1()
Test.display(s)
Test1.display1(s)







class Student:
    def __init__(self,sname,sage,stenth,sinter,sdegree):
        self.sname=sname
        self.sage=sage
        self.stenth=stenth
        self.sinter=sinter
        self.sdegree=sdegree


    def studentDetails(self):
        print("sname=",self.sname) 
        print("sage=",self.sage)    
        print("stenth=",self.stenth)  
        print("sinter=",self.sinter) 
        print("sdegree=",self.sdegree)  

class Test:
    def display(stu):
        stu.studentDetails()


class Test1:
    def display1(stu):
        stu.studentDetails()

s=Student("ravi",24,60,68,72.0)
s.studentDetails()
t=Test()

t1=Test1()







#Inner class

class outer:
    def __init__(self):
        print("outer class object creations")
    
    class Inner:
        def __init__(self):
            print("first inner class of creation")
        
        def m1(self):
            print(" first inner class method")


    class Inner1:
        def __init__(self):
           print("second inner class of creation")

        def m2(self):
            print("second inner method")   
o=outer()
i=o.Inner()
i.m1()
i1=o.Inner1()
i1.m2()