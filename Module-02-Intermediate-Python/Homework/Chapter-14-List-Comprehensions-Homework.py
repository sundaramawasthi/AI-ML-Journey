# ==========================================================
#      MODULE 2 - CHAPTER 14: LIST COMPREHENSIONS
#                Homework Solutions
# ==========================================================


# ==========================================================
# Q1 Create a list of cubes for numbers 1 to 10 using a comprehension.
# ==========================================================

cubes = [n ** 3 for n in range(1, 11)]
print(cubes)


# ==========================================================
# Q2 Create a list of only the odd numbers between 1 and 30.
# ==========================================================

odds = [n for n in range(1, 31) if n % 2 != 0]
print(odds)


# ==========================================================
# Q3 Convert a list of temperatures in Celsius to Fahrenheit using a comprehension.
# ==========================================================

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9 / 5) + 32 for c in celsius]
print(fahrenheit)


# ==========================================================
# Q4 Given a list of words, create a list of their lengths.
# ==========================================================

words = ['python', 'ai', 'machine', 'learning']
lengths = [len(word) for word in words]
print(lengths)


# ==========================================================
# Q5 Given a list of numbers, label each as "Positive", "Negative", or "Zero".
# ==========================================================

values = [-5, 0, 3, -1, 8, 0]
labels = ["Positive" if v > 0 else "Negative" if v < 0 else "Zero" for v in values]
print(labels)


# ==========================================================
# Q6 Flatten a 3x3 matrix (list of lists) into a single list.
# ==========================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [num for row in matrix for num in row]
print(flattened)


# ==========================================================
# Q7 Given a sentence, create a list of all words that start with a vowel.
# ==========================================================

sentence = "AI and machine learning are exciting areas of study"
vowel_words = [word for word in sentence.split() if word[0].lower() in 'aeiou']
print(vowel_words)


# ==========================================================
# Q8 Create a dictionary mapping each number 1-5 to whether it's prime (True/False).
# ==========================================================

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


prime_map = {n: is_prime(n) for n in range(1, 6)}
print(prime_map)


# ==========================================================
# Q9 Given a list of names, create a set of their first letters (no duplicates).
# ==========================================================

names = ['Aarav', 'Neha', 'Kabir', 'Anaya', 'Meera']
first_letters = {name[0] for name in names}
print(first_letters)


# ==========================================================
# Q10 Create a list of (number, square) tuples for numbers 1 to 5.
# ==========================================================

number_square_pairs = [(n, n ** 2) for n in range(1, 6)]
print(number_square_pairs)
