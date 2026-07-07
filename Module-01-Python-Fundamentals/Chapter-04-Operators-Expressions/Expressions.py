# ==========================================================
#            DAY 2 - PYTHON OPERATORS
#     Topic: Arithmetic, Assignment, Relational,
#              and Logical Operators
# ==========================================================

# In this lesson, we will learn different types of operators.
#
# Operators are special symbols that perform operations on values.
#
# Example:
# 5 + 3
#
# Here:
# 5 and 3 are operands.
# + is an operator.

# ==========================================================
#                 STRING OPERATIONS
# ==========================================================

# Let's create some variables.

a = 3
b = 5
txt = "@"

# ----------------------------------------------------------
# String Repetition (*)
# ----------------------------------------------------------

# The * operator repeats a string.
#
# Syntax:
# string * number

print("Result:", 2 * txt * 3)

# Step-by-step:
#
# 2 * "@"
# = "@@"
#
# "@@" * 3
# = "@@@@@@"
#
# Output:
# @@@@@@

# You can think of it like:
#
# Repeat "@" 2 times
# Then repeat that result 3 times
#
# Total:
# 2 × 3 = 6
#
# Final Output:
# @@@@@@

# ----------------------------------------------------------
# String Concatenation (+)
# ----------------------------------------------------------

print(txt + txt * a)

# Step-by-step:
#
# txt = "@"
# a = 3
#
# txt * 3
# = "@@@"
#
# txt + "@@@"
# = "@@@@"
#
# Output:
# @@@@

# + joins two strings together.
# This is called Concatenation.

# ==========================================================
# IMPORTANT RULES OF STRING OPERATIONS
# ==========================================================

# Rule 1:
# String + String ✅

print("Hello" + " World")

# Output:
# Hello World

# Rule 2:
# String * Integer ✅

print("Python " * 3)

# Output:
# Python Python Python

# Rule 3:
# String + Number ❌ (Not Allowed)

# Uncommenting the below line will give an error.

# print("Age = " + 20)

# Correct way:

print("Age =", 20)

# ==========================================================
#           NUMERIC ARITHMETIC OPERATIONS
# ==========================================================

# Numeric values can use all arithmetic operators.

A = 2
B = 4
C = 4

print("A + B * C =", A + B * C)

# Step-by-step:
#
# Multiplication has higher priority.
#
# B * C
# = 4 * 4
# = 16
#
# Now,
#
# A + 16
# = 18
#
# Output:
# 18

# ==========================================================
#      INTEGER + FLOAT = FLOAT
# ==========================================================

A = 5
B = 4.0

C = A * B

print("A * B =", C)

# Since one value is float,
# the answer is also float.

# Output:
# 20.0

# ==========================================================
#                 DIVISION (/)
# ==========================================================

print("A / B =", A / B)

# The / operator ALWAYS returns a float value.
#
# Even if both numbers are integers.
#
# Example:
#
# 10 / 2
# Output:
# 5.0

# ==========================================================
#             FLOOR DIVISION (//)
# ==========================================================

C = A // B

print("A // B =", C)

# // is called Floor Division.
#
# It removes the decimal part and returns
# the nearest smaller whole number.
#
# Example:
#
# 9 // 2
# = 4
#
# because
#
# 9 / 2 = 4.5
#
# Removing decimal gives:
# 4

# Another Example

print(15 // 4)

# Output:
# 3

# ==========================================================
#                  FLOOR FUNCTION
# ==========================================================

# Floor means:
# "Greatest integer less than or equal to the number."

# Examples:
#
# Floor(5.9)
# = 5
#
# Floor(8.1)
# = 8
#
# Floor(-2.3)
# = -3
#
# Notice:
# For negative numbers,
# floor goes to the next smaller integer.

# ==========================================================
#             OPERATOR PRECEDENCE
# ==========================================================

# Python follows a priority order while solving expressions.

# Arithmetic Operator Priority

# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -

print((2 + 3) * 4)

# Output:
# 20

print(2 + 3 * 4)

# Output:
# 14

# Because multiplication happens first.

# ----------------------------------------------------------
# Logical Operator Precedence
# ----------------------------------------------------------

# Highest
# not
#
# then
# and
#
# Lowest
# or

# Example

print(not False or False and True)

# First:
# not False = True
#
# Then:
# False and True = False
#
# Finally:
# True or False
# = True

# ==========================================================
#             ASSIGNMENT OPERATORS
# ==========================================================

# Assignment operator stores a value in a variable.

num = 10

# Normal assignment

num = num + 5

print("num =", num)

# Output:
# 15

# Shortcut Operators

num = 10

num += 5

print("After += :", num)

# Output:
# 15

num -= 3

print("After -= :", num)

# Output:
# 12

num *= 2

print("After *= :", num)

# Output:
# 24

num /= 4

print("After /= :", num)

# Output:
# 6.0

num %= 5

print("After %= :", num)

# Output:
# 1.0

num **= 3

print("After **= :", num)

# Output:
# 1.0

# ==========================================================
#             RELATIONAL (COMPARISON) OPERATORS
# ==========================================================

# These operators compare two values.
#
# Result is always:
# True
# or
# False

num1 = 50
num2 = 40

print("num1 == num2 :", num1 == num2)

# == means Equal To

print("num1 > num2 :", num1 > num2)

# > means Greater Than

print("num1 < num2 :", num1 < num2)

# < means Less Than

print("num1 != num2 :", num1 != num2)

# != means Not Equal To

print("num1 >= num2 :", num1 >= num2)

# >= means Greater Than or Equal To

print("num1 <= num2 :", num1 <= num2)

# <= means Less Than or Equal To

# ==========================================================
#               LOGICAL OPERATORS
# ==========================================================

# Logical operators work with True and False.

a = True
b = False

# ----------------------------------------------------------
# AND Operator
# ----------------------------------------------------------

print("AND =", a and b)

# AND returns True only when BOTH values are True.

# True and True
# = True

# True and False
# = False

# False and True
# = False

# False and False
# = False

# ----------------------------------------------------------
# OR Operator
# ----------------------------------------------------------

print("OR =", a or b)

# OR returns True if at least one value is True.

# True or True
# = True

# True or False
# = True

# False or True
# = True

# False or False
# = False

# ----------------------------------------------------------
# NOT Operator
# ----------------------------------------------------------

print("NOT True =", not True)

# Output:
# False

print("NOT False =", not False)

# Output:
# True

# NOT reverses the Boolean value.

# ==========================================================
#                DAY 2 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ String Concatenation (+)
# ✅ String Repetition (*)
# ✅ Arithmetic Operators
# ✅ Integer and Float Operations
# ✅ Division (/)
# ✅ Floor Division (//)
# ✅ Floor Concept
# ✅ Operator Precedence
# ✅ Assignment Operators
#    =, +=, -=, *=, /=, %=, **=
# ✅ Relational Operators
#    ==, !=, >, <, >=, <=
# ✅ Logical Operators
#    and, or, not
#
# 🎉 Congratulations!
# You have successfully completed Day 2 of Python Programming.
