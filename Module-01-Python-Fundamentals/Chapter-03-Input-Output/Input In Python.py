# ==========================================================
#             
#      Topic: Taking Input from the User (input())
# ==========================================================

# In the previous lesson, we learned how to print output.
#
# Now let's learn how to take input from the user.
#
# Input means:
# The user enters some data using the keyboard,
# and our Python program stores that data in a variable.

# ==========================================================
#                 input() FUNCTION
# ==========================================================

# input() is a built-in Python function.
#
# It is used to accept data (input) from the user.
#
# Syntax:
#
# variable_name = input("Message to display")

# Example

name = input("Enter your name: ")

print("Your name is:", name)

# Example Execution
#
# Enter your name: Sundram
#
# Output:
# Your name is: Sundram

# ==========================================================
# IMPORTANT:
# input() ALWAYS RETURNS A STRING
# ==========================================================

# Even if the user enters a number,
# Python stores it as a string by default.

age = input("Enter your age: ")

print("Your age is:", age)

print(type(age))

# Example
#
# Input:
# 22
#
# Output:
# Your age is: 22
# <class 'str'>
#
# Notice:
# Although 22 looks like a number,
# Python stores it as a string.

# ==========================================================
#        CONVERTING INPUT INTO AN INTEGER
# ==========================================================

# If we want to perform mathematical operations,
# we must convert the input into an integer.

age = int(input("Enter your age: "))

print("Your age is:", age)

print(type(age))

# Example
#
# Input:
# 22
#
# Output:
# Your age is: 22
# <class 'int'>

# int() converts a string into an integer.

# ==========================================================
#        CONVERTING INPUT INTO A FLOAT
# ==========================================================

# float() converts the input into a decimal number.

price = float(input("Enter the product price: "))

print("Price is:", price)

print(type(price))

# Example
#
# Input:
# 99.99
#
# Output:
# Price is: 99.99
# <class 'float'>

# ==========================================================
#             TYPE CONVERSION FUNCTIONS
# ==========================================================

# Python provides different functions
# to convert one data type into another.

# int()   → Converts to Integer
# float() → Converts to Float
# str()   → Converts to String
# bool()  → Converts to Boolean

# Examples

number = int("25")

decimal = float("25.5")

text = str(100)

print(number)
print(decimal)
print(text)

# ==========================================================
#      PROGRAM 1 - ADD TWO NUMBERS USING INPUT
# ==========================================================

# Take first number

num1 = int(input("Enter the first number: "))

# Take second number

num2 = int(input("Enter the second number: "))

# Add both numbers

sum_of_numbers = num1 + num2

# Display the result

print("Sum =", sum_of_numbers)

# Example
#
# Input:
# 10
# 20
#
# Output:
# Sum = 30

# ==========================================================
# PROGRAM 2 - CHECK WHETHER FIRST NUMBER IS GREATER
# ==========================================================

# Take first number

num1 = int(input("Enter the first number: "))

# Take second number

num2 = int(input("Enter the second number: "))

# Compare the numbers

if num1 > num2:
    print("True")
    print("The first number is greater than the second number.")

else:
    print("False")
    print("The first number is NOT greater than the second number.")

# Example
#
# Input:
# 15
# 10
#
# Output:
# True
# The first number is greater than the second number.

# ==========================================================
# PROGRAM 3 - FIND THE SQUARE OF A NUMBER
# ==========================================================

# Take a number from the user

num = int(input("Enter a number: "))

# Calculate its square

square = num * num

# Display the result

print("Square =", square)

# Example
#
# Input:
# 5
#
# Output:
# Square = 25

# ==========================================================
# PROGRAM 4 - CHECK WHETHER A PERSON IS ADULT
# ==========================================================

# Take age as input

age = int(input("Enter your age: "))

# Check the age

if age >= 18:
    print("Adult")

else:
    print("Minor")

# Example
#
# Input:
# 16
#
# Output:
# Minor

# ==========================================================
# PROGRAM 5 - CHECK PASS OR FAIL
# ==========================================================

# Take marks from the user

marks = int(input("Enter your marks: "))

# Check the result

if marks >= 40:
    print("Pass")

else:
    print("Fail")

# Example
#
# Input:
# 55
#
# Output:
# Pass

# ==========================================================
#              EXTRA PRACTICE PROGRAM
# ==========================================================

# Program:
# Find the area of a rectangle.

# Formula:
# Area = Length × Breadth

length = float(input("Enter the length: "))

breadth = float(input("Enter the breadth: "))

area = length * breadth

print("Area of Rectangle =", area)

# Example
#
# Input:
# Length = 5
# Breadth = 4
#
# Output:
# Area of Rectangle = 20.0

# ==========================================================
#              COMMON BEGINNER MISTAKES
# ==========================================================

# Mistake 1
#
# num = input("Enter a number:")
# print(num + 5)
#
# ❌ Error
#
# Because input() returns a string.

# Correct

num = int(input("Enter a number: "))

print(num + 5)

# ✔ Correct Output

# ----------------------------------------------------------

# Mistake 2
#
# Forgetting int()

# Wrong

# age = input("Enter age:")
#
# if age >= 18:
#     print("Adult")
#
# ❌ Error

# Correct

# age = int(input("Enter age:"))

# ==========================================================
#                 DAY 1 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ input() Function
# ✅ Taking String Input
# ✅ Taking Integer Input
# ✅ Taking Float Input
# ✅ Type Conversion
#     • int()
#     • float()
#     • str()
#     • bool()
# ✅ Sum of Two Numbers
# ✅ Comparing Two Numbers
# ✅ Finding Square of a Number
# ✅ Adult or Minor Program
# ✅ Pass or Fail Program
# ✅ Area of Rectangle Program
# ✅ Common Beginner Mistakes
#
# 🎉 Congratulations!
# You have now completed the Input section of Day 1 in Python Programming.
