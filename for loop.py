#1Print the first 10 natural numbers using for loop
'''n = 11
for i in range(1,n):
    print(i)'''


#2 Python program to print all the even numbers within the given range.
'''given_range = 10
for i in range(given_range):
    if i%2==0:    
       print(i)'''

#3Python program to calculate the sum of all numbers from 1 to a given numbe
'''given_number=10
sum=0
for i in range(1,given_number+1):
    sum+=i
print("sum of the given numbers are ",sum)'''

#4 Python program to calculate the sum of all the odd numbers within the given range.
'''given_range=10
sum=0
for i in range(given_range):
    if i%2!=0:
        sum+=i
        print(sum)'''
#5 Python program to print a multiplication table of a given number
'''n=3
for i in range(11):
    print(n,"x",i,"=",3*i)'''

#6 Python program to display numbers from a list using a for loop.
'''list=[1,3,4,5,6,7]
for i in list:
    print(i)'''

#7 Python program to count the total number of digits in a number.
'''given_number="102001987"
count=0
for i in given_number:
    count+=1
    print(count)'''

#8Python program to count the number of even and odd numbers from a series of numbers.
'''num_list=[1,3,5,7,22,33,44,80]
for i in num_list:
    if i%2==0:
        print(i,"is even number")
    else:
        print(i,"is odd number")'''

#9 print given names using for loop
'''n=['mahi,ravi,pavan,vamshi,vijay,krish']
for i in n:
    print(i)'''

#10 write a program to determine give number is positive or not
'''number=int(input("enter a  number"))
if(number>0):
  print("positive number")
else:
  print("negative number")'''



#12 write a python program using without function to validate mobile number is valid or not
'''mob_num="7981556462"
if(len(mob_num)==10):
  print("given number is valid")
elif(len(mob_num)>10):
  print("mobile number is exceeded above 10, invalid number")
else:
  print("ur mobile number might have entered less than 10 digits, kindly enter 10 digit")'''

#13write a program to determine among four students heights who is taller
'''s1=1.96
s2=1.89
s3=1.57
s4=1.99
if(s1>s2 and s1>s3 and s1>s4):
  print("s1 is taller than rest")
elif(s2>s1 and s2>s3 and s2>s4):
  print("s2 is taller")
elif(s3>s1 and s3>s2 and s3>s4):
  print("s3 is taller")
else:
  print("s4 is taller than rest")'''

#15 write a program to recognize given charcter is vowel or consonent or digit or special characters
'''ch=input("enter ur desired character")
if(ch in "aeiou"):
  print("given character is vowel")
else:
  print("given charcter is consonent")''' 

'''#16write a python program to calculate luggage weight according to couuntry rule
weight=int(input("enter ur luggage weight at airport"))
fare=3000
if(weight==25):
  print("u have no extra tax as it is 25 kg:only fare need to be paid",fare)
elif(weight>25 and weight <50):
  print("total fare to be paid:",fare+2000)
else:
  print("kindly remove ur extra luggage else ur onboard is cancelled")'''


#17 write a python program to generate roll numbers of this students
#belonging to ECE from 401 to 460
#for z in range(401,461):
 # print(z, end =" ")

#18 write a python program to print or display welcome message 10 times
'''for i in range(10):
  print("welcome to hyd")'''

#19 write a python program to print natural numbers from 1 to 20
#for i in range(1,20):
 # print(i,end=" ")

#20 write a program to display characters in name using for loop
'''name="python"
for i in name:
  print(i)'''



 





