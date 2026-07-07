# ==========================================================
#      MODULE 1 - CHAPTER 8: DICTIONARIES & SETS
#                Homework Solutions
# ==========================================================


# ==========================================================
# Q1 Create a dictionary of a student.
# ==========================================================

student = {
    "name": "Sundram",
    "age": 21
}
print(student)


# ==========================================================
# Q2 Print all Keys.
# ==========================================================

print(student.keys())


# ==========================================================
# Q3 Print all Values.
# ==========================================================

print(student.values())


# ==========================================================
# Q4 Add your city.
# ==========================================================

student["city"] = "Delhi"
print(student)


# ==========================================================
# Q5 Update your age.
# ==========================================================

student["age"] = 22
print(student)


# ==========================================================
# Q6 Create a nested dictionary.
# ==========================================================

students = {
    "student1": {"name": "Sundram", "age": 21},
    "student2": {"name": "Riya", "age": 20}
}
print(students)


# ==========================================================
# Q7 Create a set of fruits.
# ==========================================================

fruits = {"Apple", "Banana", "Mango"}
print(fruits)


# ==========================================================
# Q8 Add one fruit.
# ==========================================================

fruits.add("Grapes")
print(fruits)


# ==========================================================
# Q9 Remove one fruit.
# ==========================================================

fruits.remove("Banana")
print(fruits)


# ==========================================================
# Q10 Find the union of two sets.
# ==========================================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))


# ==========================================================
# Q11 Find the intersection of two sets.
# ==========================================================

print(set_a.intersection(set_b))


# ==========================================================
# Q12 Explain the difference between Dictionary and Set.
# ==========================================================

# A Dictionary stores data as key-value pairs, e.g.
# {"name": "Sundram"}, and values are accessed by key.
# A Set stores only unique, unordered values with no keys,
# e.g. {1, 2, 3}.

print("Dictionary stores key-value pairs, Set stores unique unordered values.")
