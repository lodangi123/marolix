'''#positional arguments

def add(a,b):
    print(a-b)
add(2,3)  

def name(name,name1,name2):
    print("hi",name,name1,name2)
name("mahi","raju","aman")

def fruits(a,m,o,b):
    print("these are fruits we have:",a,m,o,b)
fruits("apple","mango","orange","banana",) 

def numb(a,b,c,d):
    print("these are pass marks for 1st class students:",a,b,c,d)

numb(35,45,25,15)   

def add(a,b,c,d,):
    return a+b,c*d
print(add(10,20,20,13))

#keyword arg

def f(name,roll):
    print("hi",name,roll)
f("mahi",23)     

def f1(name1,name2,name3):
    print("this is youngest person:" + name3)
f1(name1="mahi",name2="vamshi",name3= "krish")

def salary(salary,amount_credited):
    print("this is the actual salary",salary,
          "and this month credited salary:", amount_credited,)
    
salary(40000,35000)    

def team(name, project, members=None):
    team.name= name
    team.project= project
    team.members= members
    print(name, "is working on an", project)
    
team("krish", "mahi's project")

def team(*members):
    for member in members:
        print(member)
        
team("Ayan", "Mari")

#default arguments
def f(name,money,add_money):
        print(money,name,add_money)
f(45000,"mahi",5000)  

def lappy(i,o,u="dell"):
        print("best laptop in the market is;", o)
lappy(i="lenovo",o="dell",u="dell")

def phone(a,b,c,d):
        print("best phone in the markt:",c)
phone("iphone","moto","mi","redmi")

def student(firstname, lastname ='lodangi', standard ='Fifth'):
     print(firstname, lastname, 'studies in', standard, 'Standard')
 
student('John')                     
student('John', 'gattamaneni', 'Seventh')      
student('John', 'Gattamaneni')                  
student('John', 'Seventh')

def appendItem(itemName, itemList = []):
    itemList.append(itemName)
    return itemList
print(appendItem('apple'))
print(appendItem('buscuit'))
print(appendItem('mango'))


#pro to print sum if given number in var len arg
def f(*a):
    print(a)
    print(type(a))

f()
f(1,2,5,6,)
f(23,55,60,80,90)
f("mahi","aman","bhagya:","ravi")  

#variable lenght argument
def f(a):
    print("arguments:",a)

f(10)    

def sum_all(*args):
    result = 0
    for num in args:
        result += num
    return result
 
print(sum_all(1, 2, 3, 4, 5))

def division(*n):
    result =3
    for i in n:
        result /=i
    return result
print(division(23,90,3))  

def mul(*a):
    result =2  
    for i in a:
      
        result *= i
    return result
print(mul(20,40,70))

def name(*m):
    print("these given names:", m)
    for i in m:
        print(i)

name("mahi","ravi","aman","vamshi")      

#keyword variable len arg
def n(**a):
    print(a)
    for i,n in a.items():
        print(i,"......",n)
n(list=10,name="mahi",petn="pinky",brothen="vamshi") 

def fn(**a):
    for i in a.items():
        print (i)
fn(name="mahi",ybrother="mahesh",brother="vamshi",number=7981556461)

def m(**argv):
    for arg in argv:
        print(arg,end=" ")
       # print(m"{key}:{value}")
 
m(hi="helo", weclcome='Welcome', to='to', hyd='mahi')

def arg(*a1,**a2):
    print("positional arg:",a1)
    print("keyword arg:",a2)
arg(2,3,4,sister="mahi",brother="vamshi")    

def print_arg(*a1,**a2):
    print("positinal arg:")
    for i in a1:
        print(i)

    print("keyword arg:")    
    for key, value in a2.items():
        print(f"{key}:{value}")
print_arg(1,2,3,sis="mahi",age=22)    '''        


#def f(arg1,arg2,arg3=4,arg4=8):
 #   print(arg1,arg2,arg3,arg4)

#f(3,5) #output: 3 5 4 8 it takes 3 as a arg1 and 5 as arg2
#f(10,20,30,40)#output: 10 20 30 40 
#f(11,6,arg4=1000)#output: is 11 6 4 1000
#f(arg4=6,arg1=7,arg2=9)#output: 7 9 4 6
##f(arg3=90,arg4=80,10,50)#output: positional argument follows keyword argument
#f(6,8,arg2=89)#errror:f() got multiple values for argument 'arg2'
#f(4,5,arg3=7,arg5=78) #TypeError: f() got an unexpected keyword argument 'arg5'
#f()#TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'''

a=10
def f():
    global a
    a=34
    print("f",a)

def f1():
    global a
    a=00
    b=20

    
    print("f1",a,b)    

f1()
f()  
f1() 
f() 
        






