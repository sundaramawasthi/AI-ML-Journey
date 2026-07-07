# ==========================================================
#      MODULE 1 - CHAPTER 10: RECURSION
#                Homework Solutions
# ==========================================================


# ==========================================================
# Q1 Print numbers from 1 to n using recursion.
# ==========================================================

def print_1_to_n(n, i=1):
    if i > n:
        return
    print(i)
    print_1_to_n(n, i + 1)

print_1_to_n(5)


# ==========================================================
# Q2 Print numbers from n to 1 using recursion.
# ==========================================================

def print_n_to_1(n):
    if n < 1:
        return
    print(n)
    print_n_to_1(n - 1)

print_n_to_1(5)


# ==========================================================
# Q3 Find the factorial of a number.
# ==========================================================

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# ==========================================================
# Q4 Find the sum of the first n natural numbers.
# ==========================================================

def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

print(sum_natural(5))


# ==========================================================
# Q5 Calculate the power of a number using recursion.
# ==========================================================

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 5))


# ==========================================================
# Q6 Find the Fibonacci series using recursion.
# ==========================================================

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i), end=" ")
print()


# ==========================================================
# Q7 Print every element of a list using recursion.
# ==========================================================

def print_list(items, i=0):
    if i == len(items):
        return
    print(items[i])
    print_list(items, i + 1)

print_list([10, 20, 30, 40])
