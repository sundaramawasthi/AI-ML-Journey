# ==========================================================
#      MODULE 1 - CHAPTER 9: LOOPS
#                Homework Solutions
# ==========================================================


# ==========================================================
# Q1 Print 1 to 20
# ==========================================================

for i in range(1, 21):
    print(i)


# ==========================================================
# Q2 Print even numbers (1 to 20)
# ==========================================================

for i in range(2, 21, 2):
    print(i)


# ==========================================================
# Q3 Print odd numbers (1 to 20)
# ==========================================================

for i in range(1, 21, 2):
    print(i)


# ==========================================================
# Q4 Print a multiplication table
# ==========================================================

table_num = 7
for i in range(1, 11):
    print(table_num, "x", i, "=", table_num * i)


# ==========================================================
# Q5 Sum of first 10 numbers
# ==========================================================

total = 0
for i in range(1, 11):
    total += i
print(total)


# ==========================================================
# Q6 Factorial of a number
# ==========================================================

n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)


# ==========================================================
# Q7 Reverse counting (10 to 1)
# ==========================================================

for i in range(10, 0, -1):
    print(i)


# ==========================================================
# Q8 Print every character of a string
# ==========================================================

word = "Python"
for ch in word:
    print(ch)


# ==========================================================
# Q9 Search a number in a list
# ==========================================================

numbers = [4, 8, 15, 16, 23, 42]
search_num = 16

for value in numbers:
    if value == search_num:
        print(search_num, "found in the list")
        break
else:
    print(search_num, "not found in the list")


# ==========================================================
# Q10 Search a character in a string
# ==========================================================

text = "Sundram"
search_char = "d"

for ch in text:
    if ch == search_char:
        print(search_char, "found in", text)
        break
else:
    print(search_char, "not found in", text)


# ==========================================================
# Q11 Print squares of 1 to 10
# ==========================================================

for i in range(1, 11):
    print(i ** 2)


# ==========================================================
# Q12 Print cubes of 1 to 10
# ==========================================================

for i in range(1, 11):
    print(i ** 3)


# ==========================================================
# Q13 Print a string in reverse
# ==========================================================

word = "Python"
print(word[::-1])


# ==========================================================
# Q14 Count vowels in a string
# ==========================================================

sentence = "Learning Python is fun"
vowels = "aeiouAEIOU"
count = 0

for ch in sentence:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
