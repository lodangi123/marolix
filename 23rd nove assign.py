t=(10,20,30,40,50,60)#valid
t=10,#valid
t=12,30,00#valid
t=10# not valid
t=(10)#valid
t=(30,)#valid
t=()#valid

#list comprehesive
n= [y for y in range(100) if y % 2 == 0 if y % 5 == 0 ]
print(n)

#write  a program to display unique vowels present in the given words
ch=input("enter ur desired character")
if ch in "aeiou":
  print("given character is vowel")
else:
  print("given charcter is not vowel")

#square root of range from 1 to 20
a=[1,2,3,4,5,6,7,8,9,0]
for i in a:
  print(i*2)