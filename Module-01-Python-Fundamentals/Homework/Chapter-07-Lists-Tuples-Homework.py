# ==========================================================
#      MODULE 1 - CHAPTER 7: LISTS & TUPLES
#                Homework Solutions
# ==========================================================


# ==========================================================
# Q1 Create a list of five fruits.
# ==========================================================

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)


# ==========================================================
# Q2 Print the first and last element.
# ==========================================================

print(fruits[0])
print(fruits[-1])


# ==========================================================
# Q3 Change the second fruit.
# ==========================================================

fruits[1] = "Papaya"
print(fruits)


# ==========================================================
# Q4 Add a new fruit using append().
# ==========================================================

fruits.append("Pineapple")
print(fruits)


# ==========================================================
# Q5 Remove one fruit using remove().
# ==========================================================

fruits.remove("Mango")
print(fruits)


# ==========================================================
# Q6 Sort a list of numbers.
# ==========================================================

numbers = [23, 5, 42, 8, 15]
numbers.sort()
print(numbers)


# ==========================================================
# Q7 Reverse the list.
# ==========================================================

numbers.reverse()
print(numbers)


# ==========================================================
# Q8 Create a tuple of five numbers.
# ==========================================================

num_tuple = (10, 20, 30, 40, 50)
print(num_tuple)


# ==========================================================
# Q9 Print the third element of the tuple.
# ==========================================================

print(num_tuple[2])


# ==========================================================
# Q10 Find the index of an element using index().
# ==========================================================

print(num_tuple.index(30))


# ==========================================================
# Q11 Count how many times 5 appears in a tuple.
# ==========================================================

sample_tuple = (5, 2, 5, 8, 5, 9)
print(sample_tuple.count(5))


# ==========================================================
# Q12 What is the difference between List and Tuple?
# ==========================================================

# A List is mutable (its elements can be changed after
# creation) and is written with square brackets [ ].
# A Tuple is immutable (its elements cannot be changed
# after creation) and is written with round brackets ( ).

print("List is mutable, Tuple is immutable.")
