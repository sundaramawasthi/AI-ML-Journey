# ==========================================================
#          DAY 4 - PRACTICE QUESTIONS
#      Topic: Dictionary and Set in Python
# ==========================================================

# In this practice file, you will revise:
#
# ✅ Dictionary
# ✅ Nested Values
# ✅ Dictionary Methods
# ✅ Set
# ✅ Unique Values
# ✅ User Input


# ==========================================================
# QUESTION 1
# WAP to store the following word meanings
# in a Python Dictionary.
#
# table :
#     "A piece of furniture"
#     "A list of facts and figures"
#
# cat :
#     "A small animal"
# ==========================================================

dictionary = {

    "table": [

        "A piece of furniture",

        "A list of facts and figures"

    ],

    "cat": "A small animal"

}

print(dictionary)


# ==========================================================
# QUESTION 2
# You are given a list of subjects.
#
# Assume one classroom is required
# for one UNIQUE subject.
#
# Find the total number of classrooms
# required.
# ==========================================================

subjects = {

    "Python",

    "Java",

    "Java",

    "C++",

    "Python",

    "JavaScript"

}

print("Subjects =", subjects)

print("Total Classrooms Required =", len(subjects))

# Explanation:
#
# A Set automatically removes
# duplicate values.
#
# So only unique subjects remain.


# ==========================================================
# QUESTION 3
# WAP to enter the marks of
# three subjects from the user
# and store them in a Dictionary.
#
# Use:
# Subject Name -> Key
# Marks -> Value
# ==========================================================

marks = {}

computer = int(input("Enter Computer Marks: "))

marks["Computer"] = computer

math = int(input("Enter Math Marks: "))

marks["Math"] = math

python = int(input("Enter Python Marks: "))

marks["Python"] = python

print("Student Marks =", marks)


# ==========================================================
# QUESTION 4
# Can Python store 9 and 9.0
# as separate values inside a Set?
# ==========================================================

numbers = {9, 9.0}

print(numbers)

print("Length of Set =", len(numbers))

# Output:
#
# {9}
#
# Length = 1
#
# Explanation:
#
# Python considers
# 9 and 9.0 equal.
#
# Therefore,
# only one value is stored.


# ==========================================================
# QUESTION 5
# Store 9 and 9.0 separately
# using a Dictionary.
# ==========================================================

values = {

    "Integer": 9,

    "Float": 9.0

}

print(values)

# Output:
#
# {
#   'Integer': 9,
#   'Float': 9.0
# }
#
# Here,
# the Keys are different,
# so both values are stored.


# ==========================================================
# BONUS QUESTION 6
# Create a Dictionary containing
# your personal details.
# ==========================================================

student = {

    "Name": "Sundram",

    "Age": 22,

    "City": "Lucknow",

    "Course": "Python"

}

print(student)


# ==========================================================
# BONUS QUESTION 7
# Create two Sets and find
# their Union and Intersection.
# ==========================================================

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

print("Union =", set1.union(set2))

print("Intersection =", set1.intersection(set2))


# ==========================================================
#           PRACTICE SUMMARY
# ==========================================================

# After completing these questions,
# you should be able to:
#
# ✅ Create Dictionaries
# ✅ Store Lists inside Dictionaries
# ✅ Take User Input
# ✅ Update Dictionaries
# ✅ Create Sets
# ✅ Remove Duplicate Values
# ✅ Use len()
# ✅ Use union()
# ✅ Use intersection()
# ✅ Understand why 9 and 9.0
#    are treated as the same
#    value inside a Set.
#
# 🎉 Congratulations!
# You have completed the
# Dictionary and Set Practice Questions.


# ==========================================================
#           BONUS: INTERVIEW CONCEPT
# ==========================================================

# A common interview question is:
#
#   print({9, 9.0})
#
# Output:
#
#   {9}
#
# This happens because 9 == 9.0 is True in Python, and a
# Set only stores unique values -- so 9.0 is treated as a
# duplicate of 9 and dropped.
#
# If you want to store them separately, use different keys
# in a Dictionary instead (see Question 5 above), since
# Dictionary keys don't get merged by equality the way Set
# values do.
