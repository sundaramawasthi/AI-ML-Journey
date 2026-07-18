# ==========================================================
#      MODULE 2 - CHAPTER 15: LAMBDA FUNCTIONS
#                Homework Solutions
# ==========================================================

from functools import reduce


# ==========================================================
# Q1 Write a lambda that returns the square of a number.
# ==========================================================

square = lambda n: n ** 2
print(square(6))


# ==========================================================
# Q2 Use map() with a lambda to convert a list of Celsius
#    temperatures to Fahrenheit.
# ==========================================================

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))
print(fahrenheit)


# ==========================================================
# Q3 Use filter() with a lambda to keep only words longer than 3 letters.
# ==========================================================

words = ['ai', 'python', 'ml', 'data', 'go']
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)


# ==========================================================
# Q4 Use sorted() with a lambda key to sort a list of numbers
#    by their absolute value.
# ==========================================================

numbers = [-8, 3, -1, 5, -2]
sorted_by_abs = sorted(numbers, key=lambda n: abs(n))
print(sorted_by_abs)


# ==========================================================
# Q5 Use reduce() with a lambda to find the maximum number in
#    a list (without max()).
# ==========================================================

values = [12, 45, 7, 91, 34]
largest = reduce(lambda a, b: a if a > b else b, values)
print(largest)


# ==========================================================
# Q6 Write a lambda that checks whether a number is divisible
#    by both 3 and 5.
# ==========================================================

divisible_by_3_and_5 = lambda n: n % 3 == 0 and n % 5 == 0
print(divisible_by_3_and_5(30))
print(divisible_by_3_and_5(10))


# ==========================================================
# Q7 Use sorted() with a lambda key to sort a list of
#    dictionaries by an "age" field.
# ==========================================================

people = [
    {'name': 'Aarav', 'age': 22},
    {'name': 'Neha', 'age': 19},
    {'name': 'Kabir', 'age': 25}
]
sorted_by_age = sorted(people, key=lambda person: person['age'])
print(sorted_by_age)


# ==========================================================
# Q8 Use map() with a lambda to get the length of every string in a list.
# ==========================================================

names = ['Aarav', 'Neha', 'Kabir', 'Meera']
name_lengths = list(map(lambda name: len(name), names))
print(name_lengths)


# ==========================================================
# Q9 Use filter() with a lambda to remove all None values from a list.
# ==========================================================

mixed = [1, None, 2, None, 3, 4, None]
cleaned = list(filter(lambda x: x is not None, mixed))
print(cleaned)


# ==========================================================
# Q10 Write a lambda that takes two numbers and returns the larger one.
# ==========================================================

larger = lambda a, b: a if a > b else b
print(larger(15, 42))
