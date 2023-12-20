#recursive fun

def fac(x):
    if x==1:
        result=1
    else:
        result=x*fac(x-1)
    return result
print(fac(7))


def fac(x):
    if x==1:
        result=9
    else:
        result=x*fac(x-1)
    return result
print(fac(9))


def fac(x):
    if x==1:
        result=0
    else:
        result=x*fac(x-1)
    return result
print(fac(5))


def fac(x):
    if x==1:
        result=5
    else:
        result=x*fac(x-1)
    return result
print(fac(11))

def fac(x):
    if x==1:
        result=10
    else:
        result=x*fac(x-1)
    return result
print(fac(10))


#lamda function

a=lambda a,b:a+b
print(a(5,6))

a=lambda a,b:a if a%2==0 else b
print(a(4,8))

a=lambda l,b:l*b
print(a(3,9))

a=lambda a,b:a+b-a-b
print(a(7,6))

a=lambda a,b:a if a>b else b
print(a(2,19))


#filter()
l=["ram",12,3.76,8,2]
x=list(filter(lambda a:a,l))
print(x)


t=("ram",12,3.76,8,2)
x=list(filter(lambda a:a,l))
print(x)


l=[12,3.76,8,2]
x=list(filter(lambda a:a%2!=0,l))
print(x)


t=(12,3.76,8,2)
x=list(filter(lambda a:a*a,l))
print(x)


l=[12,3.76,8,2]
x=list(filter(lambda a:a>5,l))
print(x)



#map() 

t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a-b,t,l))
print(a)


t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a*a,t,l))
print(a)


t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a%2==0,t,l))
print(a)


t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a-b+a*b,t,l))
print(a)


t=(1,4,3,5,9,3,85,10,65)
l=[23.5,98,3,5,2,8]
a=list(map(lambda a,b:a>b,t,l))
print(a)


#reduce()


from functools import *
t=(1,4.5,36,38,6,2)
print(reduce(lambda a,b:a+b,t))


t=(1,4.5,36,38,6,2)
print(reduce(lambda a,b:a+b-a*b+a*a,t))

l=[1,4.5,36,38,6,2]
print(reduce(lambda a,b:a<b,t))

t=(1,4.5,36,38,6,2)
print(reduce(lambda a,b:a%2!=0,t))

a=[2,6,18,9,83,72,90]
print(reduce(lambda x,y:y==2,a))