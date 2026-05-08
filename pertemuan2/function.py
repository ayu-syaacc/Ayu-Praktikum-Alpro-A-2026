#Creating a Function
def my_function():
  print("Hello from a function")

#calling a Function
def my_function():
  print("Hello from a function")

my_function()

#ex 2
def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

#return values
#ex 1
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#ex 2
def get_greeting():
  return "Hello from a function"

print(get_greeting())

#arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#parameters vs Arguments
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

#Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Default Parameter Values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#ex 2
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

#Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

#ex 2
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

#Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#Passing Different Data Types
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#ex 2
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

#Return Values
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

#Returning Different Data Types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#ex 2
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

#Positional-Only Arguments
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

#ex 2
def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

#Keyword-Only Arguments
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

#ex 2
def my_function(name):
  print("Hello", name)

my_function("Emil")

#Combining Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

#*args and **kwargs
#Arbitrary Arguments - *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#Using *args with Regular Arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#Practical Example with *args
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#ex 2
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))

#Arbitrary Keyword Arguments - **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#Using **kwargs with Regular Arguments
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

#Combining *args and **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#Unpacking Arguments
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

#Scope
#local scope
def myfunc():
  x = 300
  print(x)

myfunc()

#Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#naming variabel
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#The global Keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#Nonlocal Keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

#The LEGB Rule
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

#function decorators
#basic decorator
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

#Multiple Decorator Calls
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

#Arguments in the Decorated Function
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#*args and **kwargs
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#Decorator With Arguments
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

#multiple decorators 
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

#Preserving Function Metadata
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

#ex 2
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

#ex 3
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

#Python Lambda
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#Lambda with Built-in Functions
#Using Lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#Using Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#Using Lambda with sorted()
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#recursion
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

#Base Case and Recursive Case
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))

#Fibonacci Sequence
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

#Recursion with Lists
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

#EX 2
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

#Recursion Depth Limit
import sys
print(sys.getrecursionlimit())

#generators
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

#The yield Keyword
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

#Generators Saves Memory
def large_sequence(n):
  for i in range(n):
    yield i
# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

#Using next() with Generators
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#Generator Expressions
# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

#Fibonacci Sequence Generator
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

#generator methods
#send() Method
def echo():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

#close() Method
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

