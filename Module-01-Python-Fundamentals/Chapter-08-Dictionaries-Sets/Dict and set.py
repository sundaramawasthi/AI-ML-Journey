# ==========================================================
#           
#          Topic: Dictionaries and Sets
# ==========================================================

# In this lesson, you will learn:
#
# ✅ What is a Dictionary?
# ✅ Creating Dictionaries
# ✅ Accessing Dictionary Values
# ✅ Updating Dictionaries
# ✅ Nested Dictionaries
# ✅ Dictionary Methods
# ✅ What is a Set?
# ✅ Creating Sets
# ✅ Set Methods
# ✅ Set Operations


# ==========================================================
#               WHAT IS A DICTIONARY?
# ==========================================================

# A Dictionary is a built-in Python data type
# used to store data in the form of
# Key : Value pairs.
#
# Example:
#
# Name  -> Sundram
# Age   -> 22
# City  -> Lucknow
#
# Here,
# Name, Age and City are Keys.
#
# Sundram, 22 and Lucknow are Values.

# Dictionary Syntax

student = {
    "name": "Sundram",
    "cgpa": 10,
    "marks": [34, 56, 78, 89],
    "address": "Lucknow",
    "is_adult": True
}

print(student)

# Output:
# {
#   'name': 'Sundram',
#   'cgpa': 10,
#   ...
# }


# ==========================================================
#            FEATURES OF DICTIONARY
# ==========================================================

# ✅ Stores data as Key : Value
#
# ✅ Mutable
# (We can change values.)
#
# ✅ Keys must be unique.
#
# ✅ Values can be duplicated.
#
# ✅ Can store different data types.
#
# ✅ Can even store Lists and Dictionaries.


# ==========================================================
#          ACCESSING VALUES FROM DICTIONARY
# ==========================================================

# We access values using their Keys.

print(student["name"])

# Output:
# Sundram

print(student["cgpa"])

# Output:
# 10

print(student["marks"])

# Output:
# [34, 56, 78, 89]


# ==========================================================
#             CHECKING DATA TYPE
# ==========================================================

print(type(student))

# Output:
# <class 'dict'>


# ==========================================================
#          UPDATING A DICTIONARY
# ==========================================================

# Dictionaries are mutable.
# So we can change existing values.

student["name"] = "Rahul"

print(student)

# Output:
# name becomes Rahul


# ==========================================================
#         ADDING A NEW KEY-VALUE PAIR
# ==========================================================

student["city"] = "Delhi"

print(student)

# A new key "city"
# has been added.


# ==========================================================
#          NESTED DICTIONARY
# ==========================================================

# A dictionary can contain another dictionary.

student = {

    "name": "Sundram",

    "subjects": {

        "Math": 89,

        "Chemistry": 90,

        "Physics": 95

    }

}

print(student)

# Access nested values

print(student["subjects"]["Math"])

# Output:
# 89


# ==========================================================
#          DICTIONARY METHODS
# ==========================================================


# ==========================================================
#                keys()
# ==========================================================

# keys() returns all Keys.

print(student.keys())

# Output:
# dict_keys(['name', 'subjects'])

# Convert into a list.

print(list(student.keys()))

# Output:
# ['name', 'subjects']

# Count total keys.

print(len(student))

# Output:
# 2


# ==========================================================
#               values()
# ==========================================================

# values() returns all Values.

print(student.values())

# Output:
# dict_values([...])

# Convert into list.

print(list(student.values()))


# ==========================================================
#                items()
# ==========================================================

# items() returns every
# Key-Value pair as a tuple.

print(student.items())

# Output:
# dict_items([
# ('name','Sundram'),
# ('subjects',{...})
# ])

# Convert into a list.

pairs = list(student.items())

print(pairs)

# Output:
# [('name','Sundram'),
# ('subjects',{...})]

# Now indexing works.

print(pairs[0])

# Output:
# ('name', 'Sundram')

print(pairs[0][0])

# Output:
# name

print(pairs[0][1])

# Output:
# Sundram


# ==========================================================
#                  get()
# ==========================================================

# get() safely returns a value.

print(student.get("name"))

# Output:
# Sundram

# If key does not exist

print(student.get("phone"))

# Output:
# None

# Unlike student["phone"],
# get() does NOT produce an error.


# ==========================================================
#                update()
# ==========================================================

# update() adds new data
# or updates existing data.

student.update({"city": "Lucknow"})

print(student)

# Add multiple values.

student.update({

    "age": 22,

    "branch": "AI & ML"

})

print(student)


# ==========================================================
#        IMPORTANT CONCEPT
# ==========================================================

# Dictionary can store Lists.

student = {

    "marks": [78, 90, 88]

}

# Dictionary can store Dictionaries.

student = {

    "details": {

        "city": "Lucknow"

    }

}

# List can also store Dictionaries.

students = [

    {"name": "Aman"},

    {"name": "Rahul"}

]


# ==========================================================
#              WHAT IS A SET?
# ==========================================================

# A Set is an unordered collection
# of UNIQUE elements.

# Features:
#
# ✅ No Duplicate Values
#
# ✅ Mutable
#
# ✅ Unordered
#
# ✅ No Indexing

collection = {1, 2, 3, 4, 4, "Hello", "World"}

print(collection)

# Duplicate value 4
# appears only once.

print(type(collection))

print(len(collection))


# ==========================================================
#          EMPTY SET
# ==========================================================

# Wrong

empty = {}

print(type(empty))

# Output:
# dict

# Correct

empty_set = set()

print(type(empty_set))

# Output:
# set


# ==========================================================
#             SET METHODS
# ==========================================================


# ==========================================================
#               add()
# ==========================================================

collection = {1, 2, 3}

collection.add(5)

print(collection)

# Adds 5 into the set.


# ==========================================================
#              remove()
# ==========================================================

collection.remove(5)

print(collection)

# Removes 5.

# If element does not exist,
# remove() gives an error.


# ==========================================================
#              discard()
# ==========================================================

# discard() removes an element.

# But unlike remove(),
# it never gives an error.

collection.discard(10)


# ==========================================================
#               clear()
# ==========================================================

collection.clear()

print(collection)

# Output:
# set()


# ==========================================================
#                pop()
# ==========================================================

collection = {10, 20, 30}

print(collection.pop())

# Removes a RANDOM element.

print(collection)


# ==========================================================
#                union()
# ==========================================================

set1 = {1, 2}

set2 = {2, 3, 4}

print(set1.union(set2))

# Output:
# {1,2,3,4}

# Union combines all unique values.


# ==========================================================
#            intersection()
# ==========================================================

print(set1.intersection(set2))

# Output:
# {2}

# Only common elements.


# ==========================================================
#             DIFFERENCE
# ==========================================================

# Dictionary
#
# Stores Key : Value pairs.
#
# Example
#
# {
#   "name":"Sundram"
# }

# Set
#
# Stores only unique values.
#
# Example
#
# {1,2,3,4}


# ==========================================================
#             PRACTICE QUESTIONS
# ==========================================================

# Q1 Create a dictionary of a student.

# Q2 Print all Keys.

# Q3 Print all Values.

# Q4 Add your city.

# Q5 Update your age.

# Q6 Create a nested dictionary.

# Q7 Create a set of fruits.

# Q8 Add one fruit.

# Q9 Remove one fruit.

# Q10 Find the union of two sets.

# Q11 Find the intersection of two sets.

# Q12 Explain the difference
# between Dictionary and Set.


# ==========================================================
#              DAY 4 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ Dictionary
# ✅ Key-Value Pair
# ✅ Access Dictionary Values
# ✅ Nested Dictionary
# ✅ keys()
# ✅ values()
# ✅ items()
# ✅ get()
# ✅ update()
# ✅ Set
# ✅ add()
# ✅ remove()
# ✅ discard()
# ✅ clear()
# ✅ pop()
# ✅ union()
# ✅ intersection()
#
# 🎉 Congratulations!
# You have successfully completed
# Dictionaries and Sets in Python.
