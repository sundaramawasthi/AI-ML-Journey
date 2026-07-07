# ==========================================================
#                DAY 1 - PYTHON PROGRAMMING
#        Topic: Introduction, Variables & Data Types
# ==========================================================

# ----------------------------------------------------------
# WHAT IS PYTHON?
# ----------------------------------------------------------
# Python is one of the most popular programming languages.
# It is beginner-friendly because its syntax is simple and easy to read.
#
# Features of Python:
# 1. Easy to learn and write
# 2. Free and Open Source
# 3. High-Level Programming Language
# 4. Portable (Runs on Windows, Mac, Linux, etc.)
# 5. Used in AI, Machine Learning, Web Development,
#    Data Science, Cybersecurity, Automation, and more.

# ==========================================================
#                OUR FIRST PYTHON PROGRAM
# ==========================================================

# print() is a built-in Python function.
# It is used to display (print) output on the screen.

print("Namaste")

# Output:
# Namaste

print("Hello Viewer, here is your first Python program!")

# Output:
# Hello Viewer, here is your first Python program!

# ==========================================================
#           CHARACTER SET USED IN PYTHON
# ==========================================================

# Python can work with many different types of characters.
#
# It supports:
#
# Letters
#   A-Z
#   a-z
#
# Numbers (Digits)
#   0-9
#
# Special Symbols
#   + - * / % @ # $ etc.
#
# White Spaces
#   Space
#   Tab (\t)
#   New Line (\n)
#
# Unicode Characters
#   Hindi, Japanese, Emojis 😊, and many more.

# Example

print("Python", "Programming")

# When multiple values are passed inside print(),
# Python automatically adds one space between them.

# Output:
# Python Programming

# ==========================================================
#                PRINTING NUMBERS
# ==========================================================

# Python can print both text and numbers.

print("My lucky number is", 45)

# Output:
# My lucky number is 45

# ==========================================================
#             BASIC ARITHMETIC OPERATIONS
# ==========================================================

# Python can perform mathematical calculations.

print("Addition =", 4 + 5)

# 4 + 5 = 9

print("Subtraction =", 10 - 5)

# 10 - 5 = 5

print("Multiplication =", 4 * 5)

# 4 × 5 = 20

print("Division =", 5 / 2)

# Division always returns a decimal value.
# 5 / 2 = 2.5

print("Modulus =", 5 % 2)

# Modulus (%) returns the remainder.
# 5 ÷ 2
# Quotient = 2
# Remainder = 1

print("Exponent =", 2 ** 3)

# ** means "power"
# 2³ = 8

# ==========================================================
#                    VARIABLES
# ==========================================================

# Definition:
# A variable is a name given to a memory location
# where a value is stored.

# Think of a variable as a labeled box.
#
# Variable Name ---> Stored Value
#
# name -----------> "Sundram"
# age ------------> 50

# Syntax:
#
# variable_name = value

# Example

name = "Sundram"

# Here,
# name → Variable
# "Sundram" → Value stored inside the variable

age = 50

# age is a variable
# 50 is the value stored in memory

# We can use variables whenever needed.

print("My name is", name, "and my age is", age)

# Output:
# My name is Sundram and my age is 50

# ==========================================================
#                 type() FUNCTION
# ==========================================================

# type() is a built-in Python function.
# It tells us the data type of a variable.

print(type(name))

# Output:
# <class 'str'>

print(type(age))

# Output:
# <class 'int'>

# We can also print it with a message.

print("Type of name variable is:", type(name))
print("Type of age variable is:", type(age))

# ==========================================================
#                  DATA TYPES IN PYTHON
# ==========================================================

# Everything stored in Python has a data type.

# ----------------------------------------------------------
# 1. STRING (str)
# ----------------------------------------------------------

student_name = "Rahul"

# String means text.
# Strings are written inside single (' ')
# or double (" ") quotes.

print(student_name)
print(type(student_name))

# ----------------------------------------------------------
# 2. INTEGER (int)
# ----------------------------------------------------------

marks = 95

# Integer means whole numbers.

print(marks)
print(type(marks))

# ----------------------------------------------------------
# 3. FLOAT (float)
# ----------------------------------------------------------

percentage = 92.75

# Float means decimal numbers.

print(percentage)
print(type(percentage))

# ----------------------------------------------------------
# 4. BOOLEAN (bool)
# ----------------------------------------------------------

is_pass = True

# Boolean has only two values:
# True
# False

print(is_pass)
print(type(is_pass))

# ----------------------------------------------------------
# 5. NONE TYPE
# ----------------------------------------------------------

data = None

# None means "No value" or "Nothing".

print(data)
print(type(data))

# ==========================================================
#        PROGRAM TO FIND SUM OF TWO NUMBERS
# ==========================================================

# Store first number

number1 = 3

# Store second number

number2 = 5

# Add both numbers

sum_of_numbers = number1 + number2

# Display the result

print("Sum of two numbers is:", sum_of_numbers)

# Output:
# Sum of two numbers is: 8

# ==========================================================
#            IMPORTANT PYTHON OPERATORS
# ==========================================================

# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division
# %  Modulus (Remainder)
# ** Exponent (Power)
# // Floor Division

print(10 // 3)

# Output:
# 3
#
# Floor division removes the decimal part.

# ==========================================================
#           PYTHON IS AN IMPLICITLY TYPED LANGUAGE
# ==========================================================

# Python automatically detects the data type.
# We do NOT need to mention whether the variable
# is int, float, or string.

x = 10

# Python understands x is an integer.

y = 10.5

# Python understands y is a float.

z = "Python"

# Python understands z is a string.

print(type(x))
print(type(y))
print(type(z))

# This is called Dynamic Typing (Implicit Typing).

# ==========================================================
#                MULTI-LINE COMMENTS
# ==========================================================

# Python officially has only single-line comments (#).
#
# However, for writing long descriptions,
# programmers often use triple quotes.

"""
This is a multi-line string.

It is commonly used as:
1. Documentation (Docstrings)
2. Long explanations
3. Notes for developers

Although many beginners call it a multi-line comment,
technically it is a multi-line string.
"""

# ==========================================================
#                   DAY 1 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ What is Python
# ✅ Features of Python
# ✅ print() function
# ✅ Character Set
# ✅ Printing Text and Numbers
# ✅ Arithmetic Operators
# ✅ Variables
# ✅ type() Function
# ✅ Data Types
#     - String
#     - Integer
#     - Float
#     - Boolean
#     - None
# ✅ Sum of Two Numbers Program
# ✅ Dynamic (Implicit) Typing
# ✅ Multi-line Documentation

# Congratulations! 🎉
# You have successfully completed Day 1 of Python Programming.
