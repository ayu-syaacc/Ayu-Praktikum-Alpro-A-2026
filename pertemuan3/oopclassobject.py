#create class
class MyClass:
  x = 5

#create object
p1 = MyClass()
print(p1.x)

#Delete Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)

#multiple objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#pass statement
class Person:
  pass