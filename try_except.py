#case-1
#if there is no error in try block statement-1,2,3,5 -Normal termination

#case-2
#if an excep raised at stat-2 and corresponding except block is matched -stat -1,4,5
#normal termination

#case -3
#if an excep raised at stat-2 and corresponding except block is not matched

#try exception
# try:
#     print(10/9)
#     print(10/8)
#     print(10/2)
# except ZeroDivisionError:
#     print(10/3)    
# print("hii mahi") 

#    #it is not going to next line to execute 


# try:
#     print('hi hello welcome')
#     print(10/0)
  #except ZeroDivisionError as m:
#     print(m)
# print('heheh')    


# try:  
#     a = [1, 2, 3]  
#     print (a[4])  
# except LookupError:  
#     print ("Index out of bound error.") 
# else:  
#     print ("Success") 


# def fun(a):
#     if a < 4:
 
#         b = a/(a-3)
#     print("Value of b = ", b)
# try:
#     fun(3)
#     fun(5/6)
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:
#     print("NameError Occurred and Handled")


# def mahi(a,b):
#     try :
#         e= ((a*b),(a-b))
#     except ZeroDivisionError as m:
#         print("got zero division errror") 
#     finally:print(e)
# mahi(23,7)
# mahi(20,70)  


# # try:
# #     print(1/0)
# #     print('mahi')
# # except ZeroDivisionError :
# #     print(10.2/0)
# # print('hello mahi')    

# try:
#     a=input("enter a number:")
#     b=input("enter a new number")
#     print(a/b)
# except TypeError:
#     print('mahi')

'''
def ss(a,b):
    try:
      ss=(a+b)
      print('kadjk')
    except TypeError:
     print('mahi') 
    ss(1,9) '''   









      

