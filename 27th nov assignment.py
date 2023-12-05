'''numbers = {2, 3, 4, 5}
numbers.discard(3) 

print(numbers)
#2
n= {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(n)
n.discard(5)
print(n)

#3
myset = {'a', 1, "mahi", 2, 'b', 'abc', "maheshwari", 8} 
print(myset)
myset.discard("abc")
print(myset)

#5
my_set = set([12, 10, 13, 15, 8, 9])
 
 
while my_set:
    my_set.discard(max(my_set))
    print(my_set)


#1
s1 = {9, 1, 0}
s1.pop()
print(s1)

#2
s1 = {1, 2, 3, 4}
print("Before popping: ",s1)
s1.pop()
s1.pop()
s1.pop()
 
print("After 3 elements popped, s1:", s1)

#3
S = {}
 
#4 popping an element
print(S.pop())

print("Updated set is", S)

#1
my_set = set([12, 10, 13, 15, 8, 9])
 
for i in range(len(my_set)):
    my_set.remove(next(iter(my_set)))
    print(my_set)

#2
s=(1,2,3,4,5)
s.remove(2)
print(s)  '''


#write a pro to take tuple of numbers from keyboard and print Sum,avg
n = int(input("Enter number"))
sum = 0
# loop from 1 to n
for num in range(10):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)

