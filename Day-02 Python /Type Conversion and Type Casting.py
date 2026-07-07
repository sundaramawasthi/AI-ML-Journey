# ==========================================================
#            DAY 2 - PYTHON PROGRAMMING
#       Topic: Type Conversion, Type Casting,
#                 and Strings
# ==========================================================

# In this lesson, you will learn:
#
# ✅ Type Conversion (Implicit Conversion)
# ✅ Type Casting (Explicit Conversion)
# ✅ int(), float(), str(), bool()
# ✅ String Basics
# ✅ String Concatenation
# ✅ len() Function


# ==========================================================
#              WHAT IS TYPE CONVERSION?
# ==========================================================

# Type Conversion means converting one data type
# into another data type automatically by Python.
#
# Since Python performs the conversion itself,
# it is called:
#
# ✔ Implicit Type Conversion
# OR
# ✔ Automatic Type Conversion

# Example

a = 10       # Integer
b = 5.5      # Float

result = a + b

print(result)

print(type(result))

# Output:
# 15.5
# <class 'float'>

# ----------------------------------------------------------
# Explanation
# ----------------------------------------------------------

# Before performing the addition,
# Python automatically converts:
#
# 10
#
# into
#
# 10.0
#
# because one value is already a float.
#
# So Python actually performs:
#
# 10.0 + 5.5
#
# = 15.5
#
# Therefore,
# the final answer is also a float.


# ==========================================================
#             ANOTHER EXAMPLE
# ==========================================================

number1 = 15

number2 = 2.5

answer = number1 + number2

print(answer)

print(type(answer))

# Python automatically converts:
#
# 15
#
# into
#
# 15.0
#
# Then performs:
#
# 15.0 + 2.5


# ==========================================================
#              WHAT IS TYPE CASTING?
# ==========================================================

# Type Casting means converting one data type
# into another manually.
#
# Since the programmer performs the conversion,
# it is called:
#
# ✔ Explicit Type Conversion
# OR
# ✔ Type Casting

# Python provides built-in functions for this.


# ==========================================================
#          COMMON TYPE CASTING FUNCTIONS
# ==========================================================

# int()
# Converts a value into an Integer.

# float()
# Converts a value into a Float.

# str()
# Converts a value into a String.

# bool()
# Converts a value into a Boolean.


# ==========================================================
#               int() FUNCTION
# ==========================================================

number = "25"

print(type(number))

# number is currently a string.

number = int(number)

print(number)

print(type(number))

# Output:
#
# 25
# <class 'int'>


# ==========================================================
#              float() FUNCTION
# ==========================================================

marks = "89.5"

print(type(marks))

marks = float(marks)

print(marks)

print(type(marks))

# Output:
#
# 89.5
# <class 'float'>


# ==========================================================
#               str() FUNCTION
# ==========================================================

age = 22

print(type(age))

age = str(age)

print(age)

print(type(age))

# Output:
#
# "22"
# <class 'str'>


# ==========================================================
#              bool() FUNCTION
# ==========================================================

print(bool(1))

# Output:
# True

print(bool(0))

# Output:
# False

print(bool("Python"))

# Output:
# True

print(bool(""))

# Output:
# False


# ==========================================================
#         EXAMPLE OF IMPLICIT CONVERSION
# ==========================================================

var1 = 2          # Integer

var2 = 4.45       # Float

sum_of_numbers = var1 + var2

print(sum_of_numbers)

print(type(sum_of_numbers))

# Python automatically converts:
#
# 2
#
# into
#
# 2.0
#
# Then performs:
#
# 2.0 + 4.45


# ==========================================================
#         EXAMPLE OF EXPLICIT CONVERSION
# ==========================================================

var1 = "2"        # String

var2 = 4.56       # Float

# Convert string into integer.

var3 = int(var1)

print(type(var3))

sum_of_numbers = var2 + var3

print(sum_of_numbers)

# Step-by-step:
#
# var1 = "2"
#
# int("2")
#
# becomes
#
# 2
#
# Then
#
# 4.56 + 2
#
# = 6.56


# ==========================================================
#          INVALID TYPE CASTING EXAMPLE
# ==========================================================

# Suppose we have:

text = "Hello"

# This will give an error.

# number = int(text)

# Because "Hello" is not a valid number.

# Always make sure the string contains
# numeric values before converting it.


# ==========================================================
#                  WHAT IS A STRING?
# ==========================================================

# A String is a data type used to store text.
#
# A string is simply a sequence of characters.

language = "Python"

name = "Sundram"

message = "Welcome to Python Programming"

# All the above values are strings.

print(language)

print(name)

print(message)


# ==========================================================
#          STRING CONCATENATION (+)
# ==========================================================

# Concatenation means joining two or more strings.

str1 = "Python "

str2 = "Programming"

final_string = str1 + str2

print(final_string)

# Output:
#
# Python Programming

# The + operator joins strings together.


# ==========================================================
#      CONCATENATION WITH MULTIPLE STRINGS
# ==========================================================

first_name = "Sundram"

last_name = " Awasthi"

full_name = first_name + last_name

print(full_name)

# Output:
#
# Sundram Awasthi


# ==========================================================
#          STRING REPETITION (*)
# ==========================================================

print("Python " * 3)

# Output:
#
# Python Python Python

# The * operator repeats a string.


# ==========================================================
#             FIND LENGTH OF A STRING
# ==========================================================

# len() is a built-in Python function.
#
# It returns the total number of characters
# present inside a string.

text = "Python"

print(len(text))

# Output:
# 6

# Count:
#
# P = 1
# y = 2
# t = 3
# h = 4
# o = 5
# n = 6


# ==========================================================
#          LENGTH OF CONCATENATED STRING
# ==========================================================

str1 = "Python"

str2 = "Language"

final_string = str1 + str2

print(final_string)

print("Length =", len(final_string))

# Output:
#
# PythonLanguage
#
# Length = 14


# ==========================================================
#          PRACTICE QUESTIONS
# ==========================================================

# Question 1
#
# Convert "100" into an integer
# and print its type.

# ----------------------------------------------------------

# Question 2
#
# Convert 50 into a string
# and print its type.

# ----------------------------------------------------------

# Question 3
#
# Convert "45.8" into a float.

# ----------------------------------------------------------

# Question 4
#
# Create two strings:
#
# "Hello"
# "Python"
#
# Join them using +.

# ----------------------------------------------------------

# Question 5
#
# Print your name 5 times
# using the * operator.

# ----------------------------------------------------------

# Question 6
#
# Find the length of your full name
# using len().

# ----------------------------------------------------------

# Question 7
#
# Convert:
#
# "250"
#
# into an integer,
# then add 50 and print the answer.


# ==========================================================
#                 DAY 2 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ Type Conversion (Implicit Conversion)
# ✅ Type Casting (Explicit Conversion)
# ✅ int() Function
# ✅ float() Function
# ✅ str() Function
# ✅ bool() Function
# ✅ Automatic Conversion
# ✅ Manual Conversion
# ✅ String Basics
# ✅ String Concatenation (+)
# ✅ String Repetition (*)
# ✅ len() Function
# ✅ Practice Questions
#
# 🎉 Congratulations!
# You have successfully completed the
# Type Conversion, Type Casting, and String
# concepts of Day 2.
