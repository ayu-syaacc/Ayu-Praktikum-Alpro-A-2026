#Python Conditions and If statements
a = 33
b = 200
if b > a:
  print("b is greater than a")

#How If Statements Work
number = 15
if number > 0:
  print("The number is positive")

#Multiple Statements in If Block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#Using Variables in Conditions
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Multiple Elif Statements
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#When to Use Elif
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#the else Statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#else without elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Complete If-Elif-Else Chain
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#Else as Fallback
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")


#Shorthand If
a = 5
b = 2
if a > b: print("a is greater than b")

#Shorthand If-Else
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Assign a Value With If ... Else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#multiple Conditions in One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Practical Examples
#ex 1
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

#Python Logical Operators
#the and Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#The or Operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#The not Operator
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Combining Multiple Operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#Using Parentheses for Clarity
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")



#ex 2
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)



#NESTED IF
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#Multiple Levels of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

#Nested If vs Logical Operators
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

#pass statement
a = 33
b = 200

if b > a:
  pass

#pass in Development
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

#pass vs comment
score = 85

if score > 90:
  pass # This is excellent
print("Score processed")

#pass with Multiple Conditions
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

#pass in Other Contexts
def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet

