




# class MyClass:
#     def __init__(self, value):
#         self.value = value
#         print(self.value)
 
#     @classmethod
#     def get_max_value(self):
#         value=map(int,self.value.split(","))
        
    

# obj = MyClass("9")
# obj.get_max_value()




# class MyClass:
#     def __init__(self, value):
#         self.value = value
#         print(self.value)
    
#     def max(self):
#         value=map(int,self.value.split(','))
# b=MyClass("1,2")
# print(b.max())     

# #
# class myclass:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         print(self.x)
#         print(self.y)
        
#     @classmethod
#     def create_from_str(cls,string):
#         x,y=map(int,string.split(","))
#         return cls(x,y)
    
# obj=myclass("4","3")
# print(obj.create_from_str("2,4"))

class myClass:
    def __init__(self,a):
        self.a=a
        print(self.a)
        #self.b=b
    def my(self):
        a=map(int,self.a.split(","))
        self.a=a

    def cls(self): 
        print(self.a)   
        #return self(a,b)
    
obj=myClass("23.68")
obj.my()
obj.cls()
#













#class myclass:
#     clss_var="how are you"
#     @classmethod
#     def dffe(cls):
#         print(" hi hello",cls.clss_var)

# myclass.dffe()



