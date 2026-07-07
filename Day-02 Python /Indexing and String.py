# ==========================================================
#            DAY 2 - PYTHON PROGRAMMING
#      Topic: String Indexing, Slicing,
#           and Built-in String Functions
# ==========================================================

# In this lesson, you will learn:
#
# ✅ String Indexing
# ✅ Positive Indexing
# ✅ Negative Indexing
# ✅ String Slicing
# ✅ Positive Slicing
# ✅ Negative Slicing
# ✅ Common String Functions


# ==========================================================
#                  WHAT IS A STRING?
# ==========================================================

# A string is a sequence of characters.
#
# Example:

text = "Python"

print(text)

# Output:
# Python

# Every character inside the string has
# its own position called an Index.


# ==========================================================
#                  WHAT IS INDEXING?
# ==========================================================

# Indexing is used to access
# a SINGLE character from a string.
#
# Python starts counting from 0.

# Example String
#
#             P   y   t   h   o   n
# Index       0   1   2   3   4   5

text = "Python"

# Access the first character.

print("First Character =", text[0])

# Output:
# P

# Access the second character.

print("Second Character =", text[1])

# Output:
# y

# Access the fourth character.

print("Fourth Character =", text[3])

# Output:
# h

# Total number of characters.

print("Length of String =", len(text))

# Highest positive index is always:
#
# len(string) - 1

print("Last Positive Index =", len(text) - 1)

# Output:
# 5


# ==========================================================
#              POSITIVE INDEXING
# ==========================================================

# Python counts from LEFT to RIGHT.
#
#             P   y   t   h   o   n
# Index       0   1   2   3   4   5

text = "Python"

print(text[0])

# Output:
# P

print(text[2])

# Output:
# t

print(text[5])

# Output:
# n


# ==========================================================
#              NEGATIVE INDEXING
# ==========================================================

# Python can also count from RIGHT to LEFT.
#
#               P   y   t   h   o   n
# Index        -6  -5  -4  -3  -2  -1

text = "Python"

print(text[-1])

# Output:
# n

print(text[-2])

# Output:
# o

print(text[-6])

# Output:
# P

# Negative indexing starts from the end
# of the string.


# ==========================================================
#           DIFFERENCE BETWEEN POSITIVE
#             AND NEGATIVE INDEXING
# ==========================================================

# Positive Index
#
# Starts from the beginning.
#
# 0 → First Character

# Negative Index
#
# Starts from the end.
#
# -1 → Last Character


# ==========================================================
#                  WHAT IS SLICING?
# ==========================================================

# Slicing is used to access
# MULTIPLE characters from a string.

# Syntax
#
# string[start : end]
#
# start → Included
# end → Excluded

text = "Your Python Course"

print(text)

# Output:
# Your Python Course


# ==========================================================
#              POSITIVE SLICING
# ==========================================================

# Example 1

print(text[2:5])

# Count:
#
# Y o u r
# 0 1 2 3
#
# Actually:
#
# Index:
#
# Y o u r _ P y t h o n ...
# 0 1 2 3 4 5 6 7 ...
#
# 2:5
#
# Includes:
# 2
# 3
# 4
#
# Excludes:
# 5
#
# Output:
# ur

# ----------------------------------------------------------

# Example 2

print(text[5:11])

# Output:
# Python

# ----------------------------------------------------------

# Example 3

print(text[0:4])

# Output:
# Your


# ==========================================================
#            SLICING FROM THE BEGINNING
# ==========================================================

# If the starting index is omitted,
# Python automatically starts from index 0.

print(text[:4])

# Same as:
#
# text[0:4]

# Output:
# Your


# ==========================================================
#             SLICING TO THE END
# ==========================================================

# If the ending index is omitted,
# Python automatically goes till
# the last character.

print(text[5:])

# Output:
# Python Course


# ==========================================================
#              COMPLETE STRING
# ==========================================================

# If both indexes are omitted,
# Python returns the entire string.

print(text[:])

# Output:
# Your Python Course


# ==========================================================
#              NEGATIVE SLICING
# ==========================================================

text = "Language"

print(text)

# Index:
#
# L  a  n  g  u  a  g  e
#-8 -7 -6 -5 -4 -3 -2 -1

print(text[-5:-2])

# Count:
#
# -5 → g
# -4 → u
# -3 → a
#
# -2 is excluded.
#
# Output:
# gua


# ==========================================================
#         INDEXING VS SLICING
# ==========================================================

# Indexing
#
# Accesses ONE character.

print(text[0])

# Output:
# L

# -----------------------------

# Slicing
#
# Accesses MULTIPLE characters.

print(text[0:4])

# Output:
# Lang


# ==========================================================
#            COMMON STRING FUNCTIONS
# ==========================================================

# Python provides many useful functions
# for working with strings.


# ==========================================================
#                 endswith()
# ==========================================================

# endswith() checks whether
# the string ends with a given value.

text = "check me"

print(text.endswith("me"))

# Output:
# True

print(text.endswith("Python"))

# Output:
# False


# ==========================================================
#               capitalize()
# ==========================================================

# capitalize() converts only the
# first character into uppercase.

text = "python programming"

print(text.capitalize())

# Output:
# Python programming

# Only the first letter becomes capital.


# ==========================================================
#                 replace()
# ==========================================================

# replace(old, new)
#
# Replaces the old value with a new value.

text = "python"

print(text.replace("p", "P"))

# Output:
# Python

print(text.replace("python", "Java"))

# Output:
# Java


# ==========================================================
#                   find()
# ==========================================================

# find() returns the index of
# the first occurrence of a substring.

text = "check me"

print(text.find("me"))

# Output:
# 6

# If the text is not found,
# it returns -1.

print(text.find("Python"))

# Output:
# -1


# ==========================================================
#                  count()
# ==========================================================

# count() returns how many times
# a substring appears in the string.

text = "programming"

print(text.count("m"))

# Output:
# 2

print(text.count("g"))

# Output:
# 2


# ==========================================================
#            EXTRA STRING FUNCTIONS
# ==========================================================

text = "python programming"

# Convert to uppercase.

print(text.upper())

# Output:
# PYTHON PROGRAMMING

# -----------------------------

# Convert to lowercase.

print(text.lower())

# Output:
# python programming

# -----------------------------

# Remove spaces from beginning and end.

text = "   Python   "

print(text.strip())

# Output:
# Python


# ==========================================================
#               PRACTICE QUESTIONS
# ==========================================================

# Question 1
#
# Create a string:
#
# "Programming"
#
# Print:
#
# First character
# Last character

# ----------------------------------------------------------

# Question 2
#
# Print the first five characters
# using slicing.

# ----------------------------------------------------------

# Question 3
#
# Print the last four characters
# using negative slicing.

# ----------------------------------------------------------

# Question 4
#
# Find the length of your name.

# ----------------------------------------------------------

# Question 5
#
# Convert your name into uppercase.

# ----------------------------------------------------------

# Question 6
#
# Replace your city name
# with another city.

# ----------------------------------------------------------

# Question 7
#
# Count how many times the letter
# "a" appears in your name.

# ----------------------------------------------------------

# Question 8
#
# Check whether your name ends
# with the letter "n".


# ==========================================================
#                DAY 2 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ String Indexing
# ✅ Positive Indexing
# ✅ Negative Indexing
# ✅ String Slicing
# ✅ Positive Slicing
# ✅ Negative Slicing
# ✅ endswith()
# ✅ capitalize()
# ✅ replace()
# ✅ find()
# ✅ count()
# ✅ upper()
# ✅ lower()
# ✅ strip()
#
# 🎉 Congratulations!
# You have successfully completed
# String Indexing, Slicing, and
# String Functions in Day 2.
