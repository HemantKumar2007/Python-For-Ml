## Q1. Get user input and display it
#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#city = input("Enter your city: ")
#print(f"Hello {name}, you are {age} years old and you live in {city}.")
#
## Q2. print the data type of the following variables: num1 = 12, num2 = 12.1, is_student = True
#num1 = 12
#num2 = 12.1
#is_student = True
#print(f"num1 is of type {type(num1)}")
#print(f"num2 is of type {type(num2)}")
#print(f"is_student is of type {type(is_student)}")
#
##Q3. basic arithmetic operations
#a= 12
#b = 14
#print( a+ b)
#print(a-b)
#print(a*b)
#print(a/b)
#
#
##Q4. swap two numbers without using a third variable
#c = 10
#d = 3 
#c,d = d,c
#print(c,d)
#
## Q5. convert a string to an integer and add 5 to it
#a = int("24")
#a = a + 5
#print(a)
#
## Q6. print the area of a rectangle using user input for length and width
#length = input("Enter the length of the rectangle: ")
#width = input("Enter the width of the rectangle: ")
#print(f"The area of the rectangle is: {int(length) * int(width)}")#
#
## Q7. 
#ml = "Machine Learning"
#print(ml[0:7])
#print(ml[8:17])
#print(len(ml))
#print("first char is:", ml[0])
#print("Last char is:" , ml[-1])
#
## Q8.
#n = "HEMANT KUMAR"
#print(n[::-1])

## Q9.
#fv = "hemant singh union"
#count = 0
#for vowel in fv:
#    if vowel in "aeiou":
#        count += 1
#print(count) 

# 10.
l = [1,2,3,4,5,6]
print(max(l))
print(min(l))
print(sum(l))
print(l[0])
print(l[3])
print(l[5])
l.append(7)
print(l)
l.remove(2)
print(l)
l[5] = 2
print(l)

# Q11.
l = [1,2,2,3,3,4]
unique  = list(set(l))
print(unique)
print(l[0])

# 12.
t = ('hemant',19,'gurugram','btech cse aiml')
print(len(t))
print(t[2])

#13. 
marks = [1,2,3,4,5]
total = sum(marks)
avg =  (total/len(marks))
print(avg)