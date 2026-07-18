# ==========================================================
#            DAY 9 - PYTHON PROGRAMMING
#         Topic: Modules and Packages
# ==========================================================

# In this lesson, you will learn:
#
# ✅ What is a Module?
# ✅ What is a Package?
# ✅ Different ways to import (import, as, from...import, import *)
# ✅ Built-in modules: math, random, datetime
# ✅ Creating and using your own custom module
# ✅ pip basics for third-party packages
# ✅ Practice Programs


# ==========================================================
#              WHAT IS A MODULE?
# ==========================================================

# A Module is simply a single .py file containing
# reusable code: functions, variables, and classes.

# You have already been writing modules this whole time -
# every lesson file in this repo IS a module, whether or
# not anyone ever imports it.


# ==========================================================
#              WHAT IS A PACKAGE?
# ==========================================================

# A Package is a FOLDER of related modules grouped together.

# NumPy, Pandas, and Matplotlib (from earlier chapters) are
# all packages you installed with pip and then imported.

# Package (folder)
#   ├── module_one.py
#   ├── module_two.py
#   └── __init__.py   (tells Python "treat this folder as a package")


# ==========================================================
#           WAYS TO IMPORT
# ==========================================================

import math

print("sqrt(16) =", math.sqrt(16))
print("pi =", math.pi)

# import x as y -> shorter alias, exactly like pd/np/plt in earlier chapters
import random as rnd

print("Random number 1-10 =", rnd.randint(1, 10))

# from x import y -> pull out just one name, use it directly (no prefix)
from datetime import datetime

print("Right now:", datetime.now())

# from x import * -> pulls EVERYTHING in.
# Convenient here, but avoid this in real projects: it's unclear which
# module a name came from, and it can silently overwrite your own variables.
from math import *

print("sqrt(25) via import * =", sqrt(25))


# ==========================================================
#           THE math MODULE
# ==========================================================

print("ceil(4.2) =", math.ceil(4.2))
print("floor(4.8) =", math.floor(4.8))
print("factorial(5) =", math.factorial(5))
print("pow(2, 3) =", math.pow(2, 3))


# ==========================================================
#           THE random MODULE
# ==========================================================

print("Random int 1-100 =", rnd.randint(1, 100))
print("Random choice =", rnd.choice(['apple', 'banana', 'cherry']))

numbers = [1, 2, 3, 4, 5]
rnd.shuffle(numbers)  # shuffles the list IN PLACE (no return value)
print("Shuffled list =", numbers)


# ==========================================================
#           THE datetime MODULE
# ==========================================================

today = datetime.now()

print("Today =", today)
print("Year:", today.year, "Month:", today.month, "Day:", today.day)

from datetime import timedelta

next_week = today + timedelta(days=7)
print("7 days from now =", next_week)


# ==========================================================
#      CREATING YOUR OWN CUSTOM MODULE
# ==========================================================

# "mymodule.py" sits in this same folder and defines
# greet(), add(), and PI_APPROX - see that file for the code.

import mymodule

print(mymodule.greet("Sundram"))
print("mymodule.add(4, 5) =", mymodule.add(4, 5))
print("mymodule.PI_APPROX =", mymodule.PI_APPROX)

# You can also import just one name from your own module,
# the same way you would from a built-in one.
from mymodule import add as module_add

print("module_add(10, 20) =", module_add(10, 20))


# ==========================================================
#           pip BASICS
# ==========================================================

# pip is Python's package installer - it downloads packages
# (like numpy, pandas, matplotlib) from PyPI (the Python Package Index).

# !pip install package_name          -> install the latest version
# !pip install package_name==1.2.3   -> install an exact version
# !pip list                          -> show everything installed
# !pip show package_name             -> show details about one package
# !pip freeze > requirements.txt     -> save exact installed versions
# !pip install -r requirements.txt   -> install everything from that file

# requirements.txt is how you share "which packages + versions" a
# project needs, so someone else's environment can match yours exactly.


# ==========================================================
#          PRACTICE QUESTIONS
# ==========================================================

# Q1 Import the math module and print the square root of 81.

# Q2 Import the random module and generate a random integer between 1 and 50.

# Q3 Import datetime and print today's date.

# Q4 Use math.factorial to find the factorial of 6.

# Q5 Use random.choice to pick a random item from a list of 5 fruits.

# Q6 Use timedelta to print the date 30 days from today.

# Q7 Write your own convert_temperature(c) function (Celsius to Fahrenheit)
#    the way you would inside a custom module, then call it.

# Q8 Import only the sqrt function from math using "from math import sqrt"
#    and use it directly without the math. prefix.

# Q9 Import the random module with the alias "rnd" and shuffle a list of numbers.

# Q10 Write down (as comments) the pip commands to install pandas
#     and to list all currently installed packages.


# ==========================================================
#               DAY 9 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ Modules vs Packages
# ✅ import, import as, from...import, import *
# ✅ math, random, and datetime modules
# ✅ Writing and importing your own custom module
# ✅ __name__ == "__main__"
# ✅ pip basics
#
# 🎉 Congratulations!
# You have successfully completed
# the Modules and Packages chapter.
