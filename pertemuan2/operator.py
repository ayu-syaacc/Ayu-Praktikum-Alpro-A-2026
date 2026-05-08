sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

#aritmatik
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#division
x = 12
y = 5

print(x / y)

#Assignment Operators
#the walrus operator (:=)
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#chaining comparison operators
x = 5
print(1<x<10)
print (1<x and x<10)

#Logical Operators
#ex 1:
x = 5

print(x > 0 and x < 10)

#ex 2:
x = 5

print(x < 5 or x > 10)

#ex 3:
x = 5

print(not(x > 3 and x < 10))

#identity Operators
#ex 1:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#ex 2:
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#Difference Between is and ==
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#Membership Operators
#ex 1:
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#ex 2:
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

#Membership in Strings
#ex 3:
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#Bitwise Operators
#ex 1:
print(6 & 3)

#ex 2:
print(6 | 3)

#ex 3:
print(6 ^ 3)

#Operator Precedence
#ex 1:
print((6 + 3) - (6 + 3))

#ex 2:
print(100 + 5 * 3)

#Left-to-Right Evaluation
#ex 3:
print(5 + 4 - 7 + 3)

