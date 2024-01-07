# f=open("abc","w")
# f.write("hi mahi")
# f.write("hello mahi")
# f.close()

#Example 1: The open command will open the file in the read mode and the for loop will print each line present in the file.
# f=open("abc","r")
# for each in f:
#     print(each)

    
# #Example 2: In this example, we will extract a string that contains all characters in the file then we can use 
#     #file.read(). 
# f=open('abc','r')
# print(f.read())

# #Example 3: In this example, we will see how we can read a file using the with statement.
# with open('abc') as f:
#     data=f.read()
# print(data)    

# #USING SPLIT METHOD mode character wise
# file = open("abc", "r")
# print (file.read())


#Working in Write Mode
#Example 2: We can also use the written statement along with the  with() function.
#with open('abc','w')as f:
 #   f.write('hey there is flower')

# file = open("abc", "r")
# print (file.read())    

#  append() mode
file = open('abc', 'a')
file.write("ooo nice flower it is beautiful")
file.close()

#file = open("abc", "r")
#print (file.read()) 
f=open('abc','r')
print(f.tell())
print(f.read(5))