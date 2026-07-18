# ==========================================================
#            DAY 11 - PYTHON PROGRAMMING
#         Topic: Lambda Functions
# ==========================================================

# In this lesson, you will learn:
#
# ✅ What is a Lambda Function?
# ✅ Lambda vs a normal function
# ✅ map() with lambda
# ✅ filter() with lambda
# ✅ sorted() with a lambda key
# ✅ reduce() with lambda
# ✅ When to use (and not use) lambda
# ✅ Practice Programs


# ==========================================================
#        WHAT IS A LAMBDA FUNCTION?
# ==========================================================

# A Lambda Function is a small, anonymous (nameless) function
# written in a single line.

# Syntax:
#
# lambda arguments: expression

# It can take any number of arguments, but only ONE expression -
# and that expression's result is automatically returned
# (there is no "return" keyword).


# ==========================================================
#      LAMBDA vs A NORMAL FUNCTION
# ==========================================================

# Normal function:
def add_normal(a, b):
    return a + b


# The exact same thing as a lambda:
add_lambda = lambda a, b: a + b

print("Normal function:", add_normal(4, 5))
print("Lambda function:", add_lambda(4, 5))

# Both work identically. The difference is style, not power:
# lambda is for short, throwaway logic - not a replacement for def.


# ==========================================================
#      map() WITH LAMBDA
# ==========================================================

# map(function, iterable) applies "function" to EVERY item and
# returns a map object, which we usually convert to a list.

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n ** 2, numbers))
print("Squares via map:", squares)

# Same result as this comprehension, from the previous chapter:
# squares = [n ** 2 for n in numbers]


# ==========================================================
#      filter() WITH LAMBDA
# ==========================================================

# filter(function, iterable) keeps only the items where
# "function" returns True.

evens = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers via filter:", evens)


# ==========================================================
#      sorted() WITH A LAMBDA key
# ==========================================================

# This is one of the most common real-world uses of lambda:
# telling sorted() WHAT to sort by.

students = [
    ('Aarav', 85),
    ('Neha', 91),
    ('Kabir', 76),
    ('Meera', 88)
]

# Sort by score (the second item in each tuple), highest first.
by_score = sorted(students, key=lambda student: student[1], reverse=True)
print("Sorted by score (highest first):", by_score)

# Sort by name (the first item in each tuple), alphabetically.
by_name = sorted(students, key=lambda student: student[0])
print("Sorted by name:", by_name)


# ==========================================================
#      reduce() WITH LAMBDA
# ==========================================================

# reduce() is not built-in like map/filter - it lives in functools.
# It repeatedly combines items down into a single value.

from functools import reduce

total = reduce(lambda a, b: a + b, numbers)
print("Sum via reduce:", total)

product = reduce(lambda a, b: a * b, numbers)
print("Product via reduce:", product)


# ==========================================================
#      WHEN TO USE LAMBDA (AND WHEN NOT TO)
# ==========================================================

# Use lambda when:
#   - the logic is short (fits on one line)
#   - it's only needed once, as an argument to map/filter/sorted/etc.

# Use a normal def when:
#   - the logic needs multiple lines, or a docstring
#   - you plan to reuse the function elsewhere
#   - a descriptive function name would make the code clearer

# In short: map/filter/sorted/key= -> lambda is a great fit.
# Anything more involved -> write a real function.


# ==========================================================
#          PRACTICE QUESTIONS
# ==========================================================

# Q1 Write a lambda that returns the square of a number.

# Q2 Use map() with a lambda to convert a list of Celsius temperatures to Fahrenheit.

# Q3 Use filter() with a lambda to keep only words longer than 3 letters.

# Q4 Use sorted() with a lambda key to sort a list of numbers by their absolute value.

# Q5 Use reduce() with a lambda to find the maximum number in a list (without max()).

# Q6 Write a lambda that checks whether a number is divisible by both 3 and 5.

# Q7 Use sorted() with a lambda key to sort a list of dictionaries by an "age" field.

# Q8 Use map() with a lambda to get the length of every string in a list.

# Q9 Use filter() with a lambda to remove all None values from a list.

# Q10 Write a lambda that takes two numbers and returns the larger one.


# ==========================================================
#               DAY 11 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ Lambda function syntax
# ✅ Lambda vs a normal function
# ✅ map() with lambda
# ✅ filter() with lambda
# ✅ sorted() with a lambda key
# ✅ reduce() with lambda
# ✅ When lambda is (and isn't) the right tool
#
# 🎉 Congratulations!
# You have successfully completed
# the Lambda Functions chapter.
#
# 🎉 This also completes Module 2: Intermediate Python!
