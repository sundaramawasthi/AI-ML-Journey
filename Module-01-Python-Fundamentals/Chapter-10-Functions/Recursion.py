# ==========================================================
#      PYTHON PROGRAMMING
#                Topic: Recursion
# ==========================================================

# In this lesson, you will learn:
#
# ✅ What is Recursion?
# ✅ Base Case
# ✅ Recursive Case
# ✅ Factorial using Recursion
# ✅ Sum of Natural Numbers
# ✅ Print Numbers using Recursion
# ✅ Print List Elements using Recursion


# ==========================================================
#              WHAT IS RECURSION?
# ==========================================================

# Recursion is a technique in which
# a function calls itself repeatedly
# to solve a problem.

# Every recursive function must have:
#
# 1. Base Case
#    → Stops the recursion.
#
# 2. Recursive Case
#    → Calls the function again.

# Without a Base Case,
# the function will call itself forever
# and cause a RecursionError.


# ==========================================================
#      EXAMPLE 1 : PRINT NUMBERS
# ==========================================================

# Print numbers from n to 1.

number = int(input("Enter a Number: "))

def show(n):

    # Base Case
    if n == 0:
        return

    # Print current number
    print(n)

    # Recursive Call
    show(n - 1)

show(number)

# Example:
#
# Input: 5
#
# Output:
# 5
# 4
# 3
# 2
# 1


# ==========================================================
#      EXAMPLE 2 : FACTORIAL
# ==========================================================

# Formula:
#
# 5! = 5 × 4 × 3 × 2 × 1
#
# Recursive Formula:
#
# fact(n) = n × fact(n-1)

number = int(input("Enter a Number: "))

def factorial(n):

    # Base Case
    if n == 0 or n == 1:
        return 1

    # Recursive Case
    return n * factorial(n - 1)

print("Factorial =", factorial(number))


# ==========================================================
#    EXAMPLE 3 : SUM OF FIRST N NATURAL NUMBERS
# ==========================================================

# Formula:
#
# sum(n) = n + sum(n-1)

number = int(input("Enter a Number: "))

def natural_sum(n):

    # Base Case
    if n == 0:
        return 0

    # Recursive Case
    return n + natural_sum(n - 1)

print("Sum =", natural_sum(number))


# ==========================================================
#     EXAMPLE 4 : PRINT ALL LIST ELEMENTS
# ==========================================================

# Print every element of a list
# using Recursion.

def print_list(items, index=0):

    # Base Case
    if index == len(items):
        return

    # Print current element
    print(items[index])

    # Recursive Call
    print_list(items, index + 1)

fruits = ["Mango", "Apple", "Litchi", "Banana"]

print_list(fruits)


# ==========================================================
#         HOW RECURSION WORKS?
# ==========================================================

# Example:
#
# factorial(4)
#
# factorial(4)
# ↓
# 4 × factorial(3)
# ↓
# 4 × 3 × factorial(2)
# ↓
# 4 × 3 × 2 × factorial(1)
# ↓
# 4 × 3 × 2 × 1
# ↓
# 24


# ==========================================================
#      RECURSION vs LOOP
# ==========================================================

# Loop
#
# • Uses for or while
# • Faster
# • Uses less memory

# Recursion
#
# • Function calls itself
# • Easier for recursive problems
# • Uses more memory because of
#   function calls


# ==========================================================
#          PRACTICE QUESTIONS
# ==========================================================

# Q1 Print numbers from 1 to n using recursion.

# Q2 Print numbers from n to 1 using recursion.

# Q3 Find the factorial of a number.

# Q4 Find the sum of the first n natural numbers.

# Q5 Calculate the power of a number using recursion.

# Q6 Find the Fibonacci series using recursion.

# Q7 Print every element of a list using recursion.


# ==========================================================
#              DAY 7 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ What is Recursion?
# ✅ Base Case
# ✅ Recursive Case
# ✅ Printing Numbers
# ✅ Factorial
# ✅ Sum of Natural Numbers
# ✅ Printing List Elements
#
# 🎉 Congratulations!
# You have successfully completed
# the Recursion chapter.
