# ==========================================================
#           DAY 3 - PRACTICE QUESTIONS
#        Topic: Strings, Conditions, Lists & Tuples
# ==========================================================

# In this practice file, you will revise:
#
# ✅ Strings
# ✅ String Functions
# ✅ if-else
# ✅ Logical Operators
# ✅ Lists
# ✅ Tuples
# ✅ List Methods


# ==========================================================
# QUESTION 1
# WAP to input the user's first name
# and print its length.
# ==========================================================

name = input("Enter your first name: ")

print("Your name is:", name)

print("Length of your name is:", len(name))


# ==========================================================
# QUESTION 2
# WAP to count the occurrence of '$'
# in a string.
# ==========================================================

text = input("Enter any string: ")

print("Number of '$' symbols =", text.count("$"))


# ==========================================================
# QUESTION 3
# WAP to check whether a number
# is even or odd.
# ==========================================================

number = int(input("Enter any number: "))

if number % 2 == 0:
    print(number, "is an Even Number.")

else:
    print(number, "is an Odd Number.")


# ==========================================================
# QUESTION 4
# WAP to find the greatest
# among three numbers.
# ==========================================================

num1 = int(input("Enter First Number: "))

num2 = int(input("Enter Second Number: "))

num3 = int(input("Enter Third Number: "))

if num1 >= num2 and num1 >= num3:

    print("Greatest Number =", num1)

elif num2 >= num1 and num2 >= num3:

    print("Greatest Number =", num2)

else:

    print("Greatest Number =", num3)


# ==========================================================
# QUESTION 5
# WAP to check whether a number
# is a multiple of 7.
# ==========================================================

number = int(input("Enter any number: "))

if number % 7 == 0:

    print(number, "is a multiple of 7.")

else:

    print(number, "is NOT a multiple of 7.")


# ==========================================================
# QUESTION 6
# WAP to ask the user to enter
# the names of their 3 favourite movies
# and store them in a list.
# ==========================================================

movie1 = input("Enter Movie 1: ")

movie2 = input("Enter Movie 2: ")

movie3 = input("Enter Movie 3: ")

movies = [movie1, movie2, movie3]

print("Favourite Movies =", movies)


# ==========================================================
# QUESTION 7
# WAP to check whether a list
# is a palindrome.
# ==========================================================

numbers = [1, 2, 3, 2, 1]

copy_numbers = numbers.copy()

copy_numbers.reverse()

if numbers == copy_numbers:

    print("The list is a Palindrome.")

else:

    print("The list is NOT a Palindrome.")


# ==========================================================
# QUESTION 8
# WAP to count the number of students
# who got Grade 'A'.
# ==========================================================

grades = ("C", "D", "E", "A", "F", "A", "G")

print("Number of students with Grade A =", grades.count("A"))


# ==========================================================
# QUESTION 9
# Store the grades in a list
# and sort them alphabetically.
# ==========================================================

grades = ["C", "D", "E", "A", "F", "A", "G"]

grades.sort()

print("Sorted Grades =", grades)


# ==========================================================
# QUESTION 10
# WAP to check whether a given word
# starts with the letter 'P'.
# ==========================================================

word = input("Enter any word: ")

if word.startswith("P"):

    print("The word starts with 'P'.")

else:

    print("The word does not start with 'P'.")


# ==========================================================
# QUESTION 11
# WAP to check whether a given word
# ends with the letter 'n'.
# ==========================================================

word = input("Enter any word: ")

if word.endswith("n"):

    print("The word ends with 'n'.")

else:

    print("The word does not end with 'n'.")


# ==========================================================
# QUESTION 12
# WAP to print the first and last
# character of a string.
# ==========================================================

text = input("Enter any string: ")

print("First Character =", text[0])

print("Last Character =", text[-1])


# ==========================================================
# QUESTION 13
# WAP to reverse a string.
# ==========================================================

text = input("Enter any string: ")

print("Reverse String =", text[::-1])


# ==========================================================
# QUESTION 14
# WAP to count the number of vowels
# in a string.
# ==========================================================

text = input("Enter any string: ")

count = 0

for ch in text.lower():

    if ch in "aeiou":

        count += 1

print("Total Vowels =", count)


# ==========================================================
# QUESTION 15
# WAP to create a list of 5 numbers
# and print the largest number.
# ==========================================================

numbers = [15, 42, 8, 97, 36]

print("Largest Number =", max(numbers))


# ==========================================================
#              DAY 3 PRACTICE SUMMARY
# ==========================================================

# After completing these questions,
# you should be able to:
#
# ✅ Take input from the user
# ✅ Work with Strings
# ✅ Use String Functions
# ✅ Use if-else statements
# ✅ Compare numbers
# ✅ Check Even/Odd
# ✅ Check Multiples
# ✅ Create Lists
# ✅ Modify Lists
# ✅ Check Palindrome
# ✅ Work with Tuples
# ✅ Count Tuple Elements
# ✅ Sort Lists
# ✅ Reverse Strings
# ✅ Find Largest Number
#
# 🎉 Congratulations!
# You have completed the Day 3 Practice Questions.
