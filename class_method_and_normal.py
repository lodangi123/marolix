#class method:

class myclass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(self.x)
        print(self.y)
        
    @classmethod
    def create_from_str(cls,string):
        x,y=map(int,string.split(","))
        return cls(x,y)
    
obj=myclass.create_from_str("6,8")



#normal method


class myclass:
    def __init__(self,abc):
        self.abc=abc
    
    def c(self):
        x,y=map(int,self.abc.split(","))
        self.x=x
        self.y=y
    def d(self):
        print(self.x)
        print(self.y)

     
obj=myclass("8,5")
obj.c()
obj.d()



#class method

class myclass:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)
        
    @classmethod
    def prathi(cls,string):
        a,b,c,d=map(int,string.split(","))
        return cls(a,b,c,d)
    
obj=myclass.prathi("3,6,77,8,")




# normal method

class myclass:
    def __init__(self,name):
        self.name=name
    
    def x(self):
        a,b,c,d=map(int,self.name.split(","))
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        
    def y(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)

     
obj=myclass("10,20,30,40")
obj.x()
obj.y()


# class method

class myclass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a)
        print(self.b)
        
    @classmethod
    def fan(cls,a,b):
        e=lambda a,b:a if a>b else b
        return e
    
obj=myclass.fan(8,7)