class Test:
    a=140
    def __init__(self,a):
        self.a='hi ram how are you doing'
        Test.a='mahi'
        print(self.a)
        print(Test.a)
    
    def m1(self):
        self.a='hows going'
        Test.a='are'
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(self):
        self.a='you'
        Test.a='doing'
        print(self.a)
        print(Test.a)

    @staticmethod
    def m3():
        Test.a='rey'
        print(Test.a)

# print(Test.a)
# print(Test.__dict__)
t=Test('hi')
t.m1()
t.m2()
t.m3()
print(t.a)



from datetime import date
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
    @staticmethod
    def isAdult(age):
        return age > 18
 
 
person1 = Person('mahi', 23)
person2 = Person.fromBirthYear('mahi', 2000)
 
print(person1.age)
print(person2.age)
print(Person.isAdult(22))