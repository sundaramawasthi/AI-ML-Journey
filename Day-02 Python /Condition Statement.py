 # ==========================================================
#            DAY 2 - PYTHON PROGRAMMING
#           Topic: Strings in Python
#
# In this lesson you will learn:
#
# ✅ What is a String?
# ✅ String Indexing
# ✅ Positive & Negative Indexing
# ✅ String Slicing
# ✅ Step Slicing
# ✅ Reverse String
# ✅ Escape Sequences
# ✅ String Immutability
# ✅ Membership Operators
# ✅ Built-in String Functions
# ==========================================================


# ==========================================================
#                WHAT IS A STRING?
# ==========================================================

# A String is a sequence of characters.

# Characters can be:
# • Letters
# • Numbers
# • Symbols
# • Spaces

text = "Python"

print(text)

# Output:
# Python


# ==========================================================
#          CREATING STRINGS
# ==========================================================

# String using single quotes

str1 = 'Python'

# String using double quotes

str2 = "Programming"

# Multi-line String

str3 = """Welcome
to
Python"""

print(str1)
print(str2)
print(str3)


# ==========================================================
#                 STRING INDEXING
# ==========================================================

# Every character has a position called an Index.

#            P   y   t   h   o   n
# Index      0   1   2   3   4   5

text = "Python"

print(text[0])

# Output:
# P

print(text[3])

# Output:
# h

print(text[5])

# Output:
# n


# ==========================================================
#             NEGATIVE INDEXING
# ==========================================================

# Python also counts from the end.

#             P   y   t   h   o   n
# Index      -6 -5  -4  -3  -2  -1

print(text[-1])

# Output:
# n

print(text[-2])

# Output:
# o

print(text[-6])

# Output:
# P


# ==========================================================
#            STRING LENGTH
# ==========================================================

print(len(text))

# Output:
# 6

# Highest Positive Index

print(len(text)-1)

# Output:
# 5


# ==========================================================
#                 STRING SLICING
# ==========================================================

# Syntax

# string[start:end]

# start → Included
# end → Excluded

text = "Python Programming"

print(text[0:6])

# Output:
# Python

print(text[7:18])

# Output:
# Programming

print(text[:6])

# Output:
# Python

print(text[7:])

# Output:
# Programming

print(text[:])

# Output:
# Python Programming


# ==========================================================
#          SLICING WITH STEP
# ==========================================================

# Syntax

# string[start:end:step]

text = "Python"

print(text[0:6:2])

# Output:
# Pto

# It skips one character every time.


print(text[::2])

# Output:
# Pto


print(text[1::2])

# Output:
# yhn


# ==========================================================
#            REVERSE A STRING
# ==========================================================

text = "Python"

print(text[::-1])

# Output:
# nohtyP

# Explanation

# Start from end
# Move backward one character


# ==========================================================
#             NEGATIVE SLICING
# ==========================================================

text = "Language"

print(text[-5:-2])

# Output:
# gua


# ==========================================================
#         INDEXING vs SLICING
# ==========================================================

# Indexing

print(text[2])

# Output:
# n

# Slicing

print(text[2:5])

# Output:
# ngu


# ==========================================================
#            STRING IMMUTABILITY
# ==========================================================

# Strings cannot be changed.

text = "Python"

# This is NOT allowed.

# text[0] = "J"

# It gives an error.

# Instead create a new string.

text = "J" + text[1:]

print(text)

# Output:
# Jython


# ==========================================================
#             ESCAPE SEQUENCES
# ==========================================================

print("Hello\nPython")

# \n means New Line

print("Hello\tPython")

# \t means Tab Space

print("He said \"Hello\"")

# \" prints double quote

print("C:\\Users\\Admin")

# \\ prints one backslash


# ==========================================================
#         MEMBERSHIP OPERATORS
# ==========================================================

text = "Python"

print("Py" in text)

# Output:
# True

print("Java" in text)

# Output:
# False

print("Java" not in text)

# Output:
# True


# ==========================================================
#          STRING FUNCTIONS
# ==========================================================

text = "python programming"

print(text.upper())

# PYTHON PROGRAMMING

print(text.lower())

# python programming

print(text.capitalize())

# Python programming

print(text.title())

# Python Programming

print(text.swapcase())

# PYTHON PROGRAMMING


# ==========================================================
#             startswith()
# ==========================================================

print(text.startswith("python"))

# True

print(text.startswith("Java"))

# False


# ==========================================================
#             endswith()
# ==========================================================

print(text.endswith("ming"))

# True

print(text.endswith("Java"))

# False


# ==========================================================
#               replace()
# ==========================================================

print(text.replace("python","Java"))

# Java programming


# ==========================================================
#                 find()
# ==========================================================

print(text.find("program"))

# 7

print(text.find("Java"))

# -1


# ==========================================================
#                count()
# ==========================================================

print(text.count("m"))

# 2


# ==========================================================
#            isalpha()
# ==========================================================

print("Python".isalpha())

# True

print("Python123".isalpha())

# False


# ==========================================================
#            isdigit()
# ==========================================================

print("12345".isdigit())

# True

print("12A".isdigit())

# False


# ==========================================================
#             isalnum()
# ==========================================================

print("Python123".isalnum())

# True

print("Python 123".isalnum())

# False


# ==========================================================
#            strip()
# ==========================================================

text = "   Python   "

print(text.strip())

# Python


# ==========================================================
#        COMMON BEGINNER MISTAKES
# ==========================================================

# Wrong

# text = "Python"
# text[0] = "J"

# ❌ Error

# Correct

text = "J" + text[1:]


# Wrong

# print(text[50])

# ❌ IndexError

# Always make sure the index exists.


# ==========================================================
#              MINI PRACTICE PROGRAMS
# ==========================================================

# Program 1
# Print first and last character.

name = "Sundram"

print(name[0])

print(name[-1])

# -------------------------------

# Program 2
# Reverse your name.

print(name[::-1])

# -------------------------------

# Program 3
# Print every second character.

print(name[::2])

# -------------------------------

# Program 4
# Count letter 'a'

print(name.count("a"))


# ==========================================================
#              PRACTICE QUESTIONS
# ==========================================================

# Q1 Print first character of your name.

# Q2 Print last character of your name.

# Q3 Reverse your name.

# Q4 Print every second character.

# Q5 Find length of your city name.

# Q6 Check if your name starts with "S".

# Q7 Check if your city ends with "i".

# Q8 Replace your city with another city.

# Q9 Count how many times "a" appears in your name.

# Q10 Convert your name into uppercase.


# ==========================================================
#                 DAY 2 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ What is a String?
# ✅ Creating Strings
# ✅ Positive Indexing
# ✅ Negative Indexing
# ✅ len()
# ✅ String Slicing
# ✅ Step Slicing
# ✅ Reverse String
# ✅ Escape Sequences
# ✅ String Immutability
# ✅ Membership Operators (in, not in)
# ✅ startswith()
# ✅ endswith()
# ✅ replace()
# ✅ find()
# ✅ count()
# ✅ upper()
# ✅ lower()
# ✅ capitalize()
# ✅ title()
# ✅ swapcase()
# ✅ strip()
# ✅ isalpha()
# ✅ isdigit()
# ✅ isalnum()

# 🎉 Congratulations!
# You have completed the complete String chapter of Day 2.
