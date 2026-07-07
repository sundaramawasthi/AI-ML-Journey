# ==========================================================
#      MODULE 1 - CHAPTER 10: FUNCTIONS
#                Homework Solutions
# ==========================================================


# ==========================================================
# Q1 Write a function to add two numbers.
# ==========================================================

def add(a, b):
    return a + b

print(add(5, 3))


# ==========================================================
# Q2 Write a function to subtract two numbers.
# ==========================================================

def subtract(a, b):
    return a - b

print(subtract(5, 3))


# ==========================================================
# Q3 Write a function to multiply two numbers.
# ==========================================================

def multiply(a, b):
    return a * b

print(multiply(5, 3))


# ==========================================================
# Q4 Write a function to divide two numbers.
# ==========================================================

def divide(a, b):
    return a / b

print(divide(6, 3))


# ==========================================================
# Q5 Write a function to print a multiplication table.
# ==========================================================

def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

multiplication_table(5)


# ==========================================================
# Q6 Write a function to find the average of 3 numbers.
# ==========================================================

def average(a, b, c):
    return (a + b + c) / 3

print(average(10, 20, 30))


# ==========================================================
# Q7 Write a function to find the factorial of a number.
# ==========================================================

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))


# ==========================================================
# Q8 Write a function to find the length of a list.
# ==========================================================

def list_length(items):
    count = 0
    for item in items:
        count += 1
    return count

print(list_length([10, 20, 30, 40]))


# ==========================================================
# Q9 Write a function to check whether a number is even or odd.
# ==========================================================

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))


# ==========================================================
# Q10 Write a function to convert USD into INR.
# ==========================================================

def usd_to_inr(usd, rate=83):
    return usd * rate

print(usd_to_inr(10))
