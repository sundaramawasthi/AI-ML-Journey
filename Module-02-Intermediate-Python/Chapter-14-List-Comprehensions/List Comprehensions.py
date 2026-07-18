# ==========================================================
#            DAY 10 - PYTHON PROGRAMMING
#         Topic: List Comprehensions
# ==========================================================

# In this lesson, you will learn:
#
# ✅ What is a List Comprehension?
# ✅ Basic Comprehensions
# ✅ Conditional Comprehensions (if / if-else)
# ✅ Nested Comprehensions
# ✅ Practical Applications
# ✅ Bonus: Dict and Set Comprehensions
# ✅ Practice Programs


# ==========================================================
#        WHAT IS A LIST COMPREHENSION?
# ==========================================================

# A List Comprehension is a short, one-line way to build a
# new list from an existing iterable (list, range, string, etc.)

# Basic syntax:
#
# [expression for item in iterable]

# It replaces this pattern:
#
# result = []
# for item in iterable:
#     result.append(expression)


# ==========================================================
#      EXAMPLE 1 : SQUARES OF NUMBERS 1-10
# ==========================================================

# The old way, using a loop:
squares_loop = []
for n in range(1, 11):
    squares_loop.append(n ** 2)
print("Loop version:", squares_loop)

# The comprehension way - same result, one line:
squares = [n ** 2 for n in range(1, 11)]
print("Comprehension version:", squares)


# ==========================================================
#      CONDITIONAL COMPREHENSION (filtering with if)
# ==========================================================

# [expression for item in iterable if condition]

# Only keep even numbers from 1 to 20.
evens = [n for n in range(1, 21) if n % 2 == 0]
print("Even numbers:", evens)

# Only keep words longer than 4 letters.
words = ['cat', 'python', 'ai', 'machine', 'learning', 'dog']
long_words = [w for w in words if len(w) > 4]
print("Words longer than 4 letters:", long_words)


# ==========================================================
#      if-else INSIDE A COMPREHENSION
# ==========================================================

# This is different from filtering: every item is KEPT, but the
# expression itself changes based on the condition.
#
# [expression_if_true if condition else expression_if_false for item in iterable]

labels = ["Even" if n % 2 == 0 else "Odd" for n in range(1, 11)]
print("Even/Odd labels:", labels)


# ==========================================================
#      NESTED LOOPS INSIDE A COMPREHENSION
# ==========================================================

# Useful for flattening a 2D list (a list of lists) into a 1D list.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# Reading order matters: it runs top-to-bottom exactly like nested
# for-loops would -> "for row in matrix" (outer) then "for num in row" (inner).


# ==========================================================
#      PRACTICAL APPLICATIONS
# ==========================================================

# Extract vowels from a sentence.
sentence = "Python is fun to learn"
vowels = [ch for ch in sentence if ch.lower() in 'aeiou']
print("Vowels found:", vowels)

# Convert a list of names to uppercase.
names = ['aarav', 'neha', 'kabir']
upper_names = [name.upper() for name in names]
print("Uppercase names:", upper_names)

# Square only the EVEN numbers, skip the odd ones.
squared_evens = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print("Squares of even numbers:", squared_evens)


# ==========================================================
#      BONUS: DICT AND SET COMPREHENSIONS
# ==========================================================

# Same idea, different brackets: {} instead of [].

# Dict comprehension -> {key_expr: value_expr for item in iterable}
squares_dict = {n: n ** 2 for n in range(1, 6)}
print("Number -> Square dict:", squares_dict)

# Set comprehension -> {expr for item in iterable} (removes duplicates automatically)
unique_lengths = {len(word) for word in words}
print("Unique word lengths:", unique_lengths)


# ==========================================================
#          PRACTICE QUESTIONS
# ==========================================================

# Q1 Create a list of cubes for numbers 1 to 10 using a comprehension.

# Q2 Create a list of only the odd numbers between 1 and 30.

# Q3 Convert a list of temperatures in Celsius to Fahrenheit using a comprehension.

# Q4 Given a list of words, create a list of their lengths.

# Q5 Given a list of numbers, label each as "Positive", "Negative", or "Zero".

# Q6 Flatten a 3x3 matrix (list of lists) into a single list.

# Q7 Given a sentence, create a list of all words that start with a vowel.

# Q8 Create a dictionary mapping each number 1-5 to whether it's prime (True/False).

# Q9 Given a list of names, create a set of their first letters (no duplicates).

# Q10 Create a list of (number, square) tuples for numbers 1 to 5.


# ==========================================================
#               DAY 10 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ List Comprehension syntax
# ✅ Filtering with if
# ✅ if-else inside a comprehension
# ✅ Nested loops inside a comprehension (flattening)
# ✅ Practical text and number transformations
# ✅ Dict and Set comprehensions
#
# 🎉 Congratulations!
# You have successfully completed
# the List Comprehensions chapter.
