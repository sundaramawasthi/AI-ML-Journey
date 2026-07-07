# ==========================================================
#            DAY 3 - PYTHON PROGRAMMING
#          Topic: Lists and Tuples in Python
# ==========================================================

# In this lesson, you will learn:
#
# ✅ What is a List?
# ✅ Creating Lists
# ✅ Accessing List Elements
# ✅ Updating Lists
# ✅ List Slicing
# ✅ List Methods
# ✅ What is a Tuple?
# ✅ Tuple Indexing
# ✅ Tuple Slicing
# ✅ Tuple Methods
# ✅ Difference Between List and Tuple


# ==========================================================
#              WHAT IS A LIST?
# ==========================================================

# A List is a built-in data type in Python
# used to store multiple values inside a
# single variable.

# Example:
#
# Instead of creating many variables,
#
# marks1 = 90
# marks2 = 85
# marks3 = 78
#
# We can store them inside one list.

marks = [90, 85, 78]

print(marks)

# Output:
# [90, 85, 78]


# ==========================================================
#            FEATURES OF A LIST
# ==========================================================

# ✅ Ordered
# Elements have indexes.

# ✅ Mutable
# We can change elements after creation.

# ✅ Stores Multiple Data Types
# Integer, Float, String, Boolean, etc.

# ✅ Allows Duplicate Values

# Example

student = ["Sundram", 22, 89.5, True]

print(student)

# Output:
# ['Sundram', 22, 89.5, True]


# ==========================================================
#             CREATING A LIST
# ==========================================================

property_list = [200, 300, 600, 700]

print(property_list)

print(type(property_list))

# Output:
# <class 'list'>


# ==========================================================
#           ACCESSING LIST ELEMENTS
# ==========================================================

# Indexing starts from 0.

# Index:
#
# 200  300  600  700
#  0    1    2    3

print(property_list[0])

# Output:
# 200

print(property_list[2])

# Output:
# 600

print(property_list[-1])

# Output:
# 700


# ==========================================================
#             MODIFYING A LIST
# ==========================================================

# Lists are Mutable.
#
# That means we can change values.

property_list[0] = "Sundram"

print(property_list)

# Output:
# ['Sundram', 300, 600, 700]


# ==========================================================
#              LENGTH OF A LIST
# ==========================================================

print(len(property_list))

# Output:
# 4

# len() returns the total number of elements.


# ==========================================================
#              LIST SLICING
# ==========================================================

student = ["Mohan", 67, "Delhi", True]

print(student)

# Syntax:
#
# list[start:end]

print(student[1:3])

# Output:
# [67, 'Delhi']

# Explanation:
#
# Start = 1 (Included)
#
# End = 3 (Excluded)


print(student[:2])

# Output:
# ['Mohan', 67]


print(student[2:])

# Output:
# ['Delhi', True]


print(student[:])

# Output:
# Entire List


# ==========================================================
#             LIST METHODS
# ==========================================================

# Python provides many useful methods
# for working with lists.


# ==========================================================
#               append()
# ==========================================================

# append() adds an element at the end.

cities = ["Lucknow", "Delhi"]

cities.append("Mumbai")

print(cities)

# Output:
# ['Lucknow', 'Delhi', 'Mumbai']


# ==========================================================
#                insert()
# ==========================================================

# insert(index, value)

cities.insert(1, "Kanpur")

print(cities)

# Output:
# ['Lucknow', 'Kanpur', 'Delhi', 'Mumbai']


# ==========================================================
#                extend()
# ==========================================================

# extend() joins two lists.

list1 = [1, 2]

list2 = [3, 4]

list1.extend(list2)

print(list1)

# Output:
# [1, 2, 3, 4]


# ==========================================================
#                 sort()
# ==========================================================

numbers = [45, 67, 23, 90]

numbers.sort()

print(numbers)

# Output:
# [23, 45, 67, 90]

# sort() arranges elements
# in ascending order.


# ==========================================================
#          SORT IN DESCENDING ORDER
# ==========================================================

numbers.sort(reverse=True)

print(numbers)

# Output:
# [90, 67, 45, 23]


# ==========================================================
#          SORTING STRINGS
# ==========================================================

letters = ["a", "d", "t", "e", "g"]

letters.sort()

print(letters)

# Output:
# ['a', 'd', 'e', 'g', 't']


# ==========================================================
#               reverse()
# ==========================================================

# reverse() only reverses
# the current order.

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

# Output:
# [40, 30, 20, 10]

# Note:
#
# reverse() does NOT sort.


# ==========================================================
#                remove()
# ==========================================================

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)

# Output:
# [10, 30, 20]

# remove() deletes only
# the FIRST occurrence.


# ==========================================================
#                  pop()
# ==========================================================

numbers = [10, 20, 30, 40]

numbers.pop(2)

print(numbers)

# Output:
# [10, 20, 40]

# pop(index) removes an element
# using its index.

# If no index is given,
# pop() removes the last element.

numbers.pop()

print(numbers)

# Output:
# [10, 20]


# ==========================================================
#                 clear()
# ==========================================================

numbers.clear()

print(numbers)

# Output:
# []


# ==========================================================
#                 copy()
# ==========================================================

list1 = [10, 20, 30]

list2 = list1.copy()

print(list2)

# Output:
# [10, 20, 30]


# ==========================================================
#           MEMBERSHIP OPERATORS
# ==========================================================

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)

# True

print("Orange" in fruits)

# False


# ==========================================================
#             LOOP THROUGH A LIST
# ==========================================================

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# Output:
# Apple
# Banana
# Mango


# ==========================================================
#               COMMON MISTAKES
# ==========================================================

# Wrong

# fruits[10]

# ❌ IndexError

# Always make sure the
# index exists.


# ==========================================================
#             WHAT IS A TUPLE?
# ==========================================================

# A Tuple is also used to store
# multiple values.

# But unlike lists...

# Tuples are Immutable.

# Immutable means
# they cannot be changed.

tup = (2, 4, 6, 7, 5)

print(tup)

print(type(tup))

# Output:
# <class 'tuple'>


# ==========================================================
#            ACCESSING TUPLE ELEMENTS
# ==========================================================

print(tup[2])

# Output:
# 6

print(tup[-1])

# Output:
# 5


# ==========================================================
#             TUPLE SLICING
# ==========================================================

print(tup[1:4])

# Output:
# (4, 6, 7)


# ==========================================================
#          TUPLE IS IMMUTABLE
# ==========================================================

# This is NOT allowed.

# tup[0] = 100

# ❌ Error

# Tuples cannot be modified.


# ==========================================================
#             TUPLE METHODS
# ==========================================================

numbers = (2, 4, 6, 2, 8)

# index()

print(numbers.index(6))

# Output:
# 2

# count()

print(numbers.count(2))

# Output:
# 2


# ==========================================================
#       SPECIAL CASE - SINGLE VALUE TUPLE
# ==========================================================

# Wrong

a = (5)

print(type(a))

# Output:
# <class 'int'>

# Correct

b = (5,)

print(type(b))

# Output:
# <class 'tuple'>

# The comma is compulsory.


# ==========================================================
#      DIFFERENCE BETWEEN LIST AND TUPLE
# ==========================================================

# LIST
#
# • Uses []
# • Mutable
# • Many methods
# • Slightly slower
# • Good when data changes

# TUPLE
#
# • Uses ()
# • Immutable
# • Few methods
# • Faster
# • Good when data should not change


# ==========================================================
#           MINI PRACTICE PROGRAMS
# ==========================================================

# Program 1
# Create a list of fruits.

fruits = ["Apple", "Banana", "Mango"]

print(fruits)

# ------------------------------

# Program 2
# Change Banana to Orange.

fruits[1] = "Orange"

print(fruits)

# ------------------------------

# Program 3
# Add Grapes.

fruits.append("Grapes")

print(fruits)

# ------------------------------

# Program 4
# Remove Apple.

fruits.remove("Apple")

print(fruits)

# ------------------------------

# Program 5
# Create a tuple.

colors = ("Red", "Green", "Blue")

print(colors)


# ==========================================================
#             PRACTICE QUESTIONS
# ==========================================================

# Q1 Create a list of five fruits.

# Q2 Print the first and last element.

# Q3 Change the second fruit.

# Q4 Add a new fruit using append().

# Q5 Remove one fruit using remove().

# Q6 Sort a list of numbers.

# Q7 Reverse the list.

# Q8 Create a tuple of five numbers.

# Q9 Print the third element of the tuple.

# Q10 Find the index of an element using index().

# Q11 Count how many times 5 appears in a tuple.

# Q12 What is the difference between List and Tuple?


# ==========================================================
#                 DAY 3 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ What is a List?
# ✅ Features of Lists
# ✅ Creating Lists
# ✅ Indexing
# ✅ Slicing
# ✅ Updating Lists
# ✅ append()
# ✅ insert()
# ✅ extend()
# ✅ sort()
# ✅ reverse()
# ✅ remove()
# ✅ pop()
# ✅ clear()
# ✅ copy()
# ✅ Membership Operators (in, not in)
# ✅ Looping through Lists
# ✅ What is a Tuple?
# ✅ Tuple Indexing
# ✅ Tuple Slicing
# ✅ Tuple Methods
#     • index()
#     • count()
# ✅ Single-Element Tuple
# ✅ Difference Between List and Tuple

# 🎉 Congratulations!
# You have successfully completed
# Lists and Tuples in Python.
