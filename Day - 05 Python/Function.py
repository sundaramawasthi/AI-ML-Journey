 # ==========================================================
#            DAY 6 - PYTHON PROGRAMMING
#                 Topic: Functions
# ==========================================================

# In this lesson, you will learn:
#
# ✅ What is a Function?
# ✅ Why do we use Functions?
# ✅ Built-in Functions
# ✅ User-defined Functions
# ✅ Parameters and Arguments
# ✅ return Statement
# ✅ Practice Programs


# ==========================================================
#              WHAT IS A FUNCTION?
# ==========================================================

# A Function is a block of reusable code
# that performs a specific task.

# Instead of writing the same code
# again and again,
# we write it once inside a function
# and call it whenever needed.


# ==========================================================
#             TYPES OF FUNCTIONS
# ==========================================================

# 1. Built-in Functions
#
# Functions already provided by Python.
#
# Examples:
#
# print()
# input()
# len()
# type()
# range()

# 2. User-defined Functions
#
# Functions created by the programmer.


# ==========================================================
#          FUNCTION SYNTAX
# ==========================================================

# def function_name(parameters):
#     Code
#     return value

# Function Call
#
# function_name(arguments)


# ==========================================================
#      PARAMETERS vs ARGUMENTS
# ==========================================================

# Parameters
# Variables written while defining a function.

# Arguments
# Actual values passed while calling a function.


# ==========================================================
#      EXAMPLE 1 : ADD TWO NUMBERS
# ==========================================================

def add_numbers(a, b):

    total = a + b

    return total


result = add_numbers(4, 5)

print("Sum =", result)

# Here:
#
# a and b → Parameters
#
# 4 and 5 → Arguments


# ==========================================================
#       EXAMPLE 2 : MULTIPLICATION TABLE
# ==========================================================

def table(number):

    for i in range(1, 11):

        print(number, "x", i, "=", number * i)


number = int(input("Enter a Number: "))

table(number)


# ==========================================================
#      EXAMPLE 3 : AVERAGE OF 3 NUMBERS
# ==========================================================

def average(a, b, c):

    return (a + b + c) / 3


num1 = int(input("Enter First Number: "))

num2 = int(input("Enter Second Number: "))

num3 = int(input("Enter Third Number: "))

result = average(num1, num2, num3)

print("Average =", result)


# ==========================================================
#     EXAMPLE 4 : LENGTH OF A LIST
# ==========================================================

def list_length(my_list):

    return len(my_list)


numbers = list(map(int, input("Enter numbers: ").split()))

print("Length of List =", list_length(numbers))


# ==========================================================
#     EXAMPLE 5 : FACTORIAL OF A NUMBER
# ==========================================================

def factorial(number):

    fact = 1

    for i in range(1, number + 1):

        fact *= i

    return fact


number = int(input("Enter a Number: "))

print("Factorial =", factorial(number))


# ==========================================================
#    EXAMPLE 6 : USD TO INR CONVERSION
# ==========================================================

def usd_to_inr(usd):

    exchange_rate = 86

    return usd * exchange_rate


usd = float(input("Enter Amount in USD: "))

print("INR =", usd_to_inr(usd))


# ==========================================================
#      return vs print
# ==========================================================

# print()
#
# Displays output on the screen.

# return
#
# Sends the value back to the function call.


# ==========================================================
#          PRACTICE QUESTIONS
# ==========================================================

# Q1 Write a function to add two numbers.

# Q2 Write a function to subtract two numbers.

# Q3 Write a function to multiply two numbers.

# Q4 Write a function to divide two numbers.

# Q5 Write a function to print a multiplication table.

# Q6 Write a function to find the average of 3 numbers.

# Q7 Write a function to find the factorial of a number.

# Q8 Write a function to find the length of a list.

# Q9 Write a function to check whether a number is even or odd.

# Q10 Write a function to convert USD into INR.


# ==========================================================
#               DAY 6 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ Functions
# ✅ Built-in Functions
# ✅ User-defined Functions
# ✅ Parameters
# ✅ Arguments
# ✅ return Statement
# ✅ Function Calling
#
# 🎉 Congratulations!
# You have successfully completed
# the Functions chapter.
