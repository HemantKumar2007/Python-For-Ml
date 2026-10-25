# Data Types
# 1. Numeric Data Types
# int, float, complex
# example:
x = 5 # int
y = 5.2 # float
z = 3 + 4j # complex
print(type(x)) 
print(type(y))
print(type(z))

#2. Sequence Data Types
# str, list, tuple
# example:
s = "Hello, World!" # str
l = [1, 2, 3] # list
t = (4, 5, 6) # tuple
print(type(s))
print(type(l))
print(type(t))

# slicing in python
# slicing is used to extract a portion of a sequence.
# example:
s = "Hello, World!"
print(s[0:5]) # Hello
print(s[7:12]) # World!
print(s[:5]) # Hello
print(s[7:12]) # World!
print(s[-6:-1]) # World
print(s[-6:]) # World!
print(s[:-6]) # Hello,
print(s[:]) # Hello, World!

s = "hemant"
print(s*12)

# Difference b/t list and array
# list can strore different data types, while array can only store same data type.
# example:
l = [1, 2, 3, "hello", 5.6] # list
print(l)
arr = [1, 2, 3, 4, 5] # array
print(arr)


# what is multable?
# mutable is a data type that can be changed after it is created.

# what is immutable?
# immutable is a data type that cannot be changed after it is created.

# what is tuple?
# tuple is an immutable data type that can store multiple values of different data types.

# range() function
# range() function is used to generate a sequence of numbers.
# example:
a = range(1,11)
print(a) # range(1, 11)
print(list(a)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# what is difference b/t bytes and bytearray?
# bytes is an immutable data type that can store a sequence of bytes.
# example:
b = b"hello"
#bytearray is a mutable data type that can store a sequence of bytes.
# example:
ba = bytearray(b"hello")

# set types
# set is a mutable data type that can store a collection of unique values.
# example:
s = {1, 2, 3, 4, 5 ,3, 2, 1}
# remove duplicates from set
print(s) # {1, 2, 3, 4, 5}

ch=set("hello")
print(ch) # {'h', 'e', 'l', 'o'}
# slicing in set is not possible because set is unordered.

s.update([5,8])
print(s) # {1, 2, 3, 4, 5, 8}

# what is dictionary?
# dictionary is a mutable data type that can store a collection of key-value pairs.
d = {"name": "John", "age": 30, "city": "New York"}
print(d) # {'name': 'John', 'age': 30, 'city': 'New York'}
print(d["name"]) # John
print(d["age"]) # 30

# what is none type?
# None type is a data type that represents the absence of a value.
n = None
print(n) # None

# what is literal?
# literal is a data type that represents a fixed value.
# example:
x = 5 # int literal
y = 5.2 # float literal
z = "hello" # string literal

# differnce b/t list and tuple.
# 