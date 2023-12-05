'''
#pro to print diff vowels present in the given word and count of vowels
name="we are learning python programming language"
a=name.count("a")
b=name.count("e")
c=name.count("i")
d=name.count("o")
e=name.count("u")
sum=0
list=[a,b,c,d,e]
for j in list:
    sum=sum+j
print("Total vowels in the given word are:",sum,"and those are :-")
for i in name:
    if i in "aeiou":
        print("",i,"",end="")
print()

#pr to enter the name and % of marks in a dict and display info on the screen
students=(1)
n = int(input("Enter No of Students:"))
result = {}
for _ in range(students):
 roll_no = int(input("Roll No: "))
std_name = input("Student Name: ")
marks = int(input("Marks: "))
result[roll_no] = [std_name, marks]
print(result)

#removing duplicate elements from list 

l= [1, 5, 3, 6, 3, 5, 6, 1,7,7,8,9]
print("The original list is : " + str(l))
 
r= []
for i in l:
    if i not in r:
        r.append(i)
print("The list after removing duplicates : " + str(r))'''
