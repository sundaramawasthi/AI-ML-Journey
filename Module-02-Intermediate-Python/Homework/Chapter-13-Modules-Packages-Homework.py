# ==========================================================
#      MODULE 2 - CHAPTER 13: MODULES AND PACKAGES
#                Homework Solutions
# ==========================================================

import math
import random as rnd
from datetime import datetime, timedelta


# ==========================================================
# Q1 Import the math module and print the square root of 81.
# ==========================================================

print(math.sqrt(81))


# ==========================================================
# Q2 Import the random module and generate a random integer between 1 and 50.
# ==========================================================

print(rnd.randint(1, 50))


# ==========================================================
# Q3 Import datetime and print today's date.
# ==========================================================

print(datetime.now().date())


# ==========================================================
# Q4 Use math.factorial to find the factorial of 6.
# ==========================================================

print(math.factorial(6))


# ==========================================================
# Q5 Use random.choice to pick a random item from a list of 5 fruits.
# ==========================================================

fruits = ['apple', 'banana', 'mango', 'grape', 'orange']
print(rnd.choice(fruits))


# ==========================================================
# Q6 Use timedelta to print the date 30 days from today.
# ==========================================================

print(datetime.now() + timedelta(days=30))


# ==========================================================
# Q7 Write your own convert_temperature(c) function (Celsius to
#    Fahrenheit) the way you would inside a custom module, then call it.
# ==========================================================

def convert_temperature(c):
    return (c * 9 / 5) + 32


print(convert_temperature(25))


# ==========================================================
# Q8 Import only the sqrt function from math using "from math import sqrt"
#    and use it directly without the math. prefix.
# ==========================================================

from math import sqrt

print(sqrt(144))


# ==========================================================
# Q9 Import the random module with the alias "rnd" and shuffle a list of numbers.
# ==========================================================

numbers = [10, 20, 30, 40, 50]
rnd.shuffle(numbers)
print(numbers)


# ==========================================================
# Q10 Write down (as comments) the pip commands to install pandas
#     and to list all currently installed packages.
# ==========================================================

# !pip install pandas
# !pip list
