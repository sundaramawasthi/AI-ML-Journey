# ==========================================================
#                 WHAT IS A LOOP?
# ==========================================================

# A Loop is used to execute the same block of code
# again and again.

# Instead of writing

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# We can simply write

count = 1

while count <= 5:

    print("Hello")

    count += 1

# How this works, iteration by iteration:
#
# Iteration 1 -> count = 1 -> condition True  -> prints "Hello" -> count becomes 2
# Iteration 2 -> count = 2 -> condition True  -> prints "Hello" -> count becomes 3
# Iteration 3 -> count = 3 -> condition True  -> prints "Hello" -> count becomes 4
# Iteration 4 -> count = 4 -> condition True  -> prints "Hello" -> count becomes 5
# Iteration 5 -> count = 5 -> condition True  -> prints "Hello" -> count becomes 6
#
# The loop stops because count becomes 6, and 6 <= 5 is False.


# ==========================================================
#                    2. WHILE LOOP
# ==========================================================

# Syntax:
#
# while condition:
#     # code to repeat
#
# - "condition" is checked before every iteration.
# - As long as the condition is True, the code inside
#   the loop keeps running.
# - The loop stops the moment the condition becomes False.
# - Something inside the loop must eventually make the
#   condition False, otherwise the loop never ends.


# ==========================================================
#              3. PRINT 1 TO 100 (WHILE LOOP)
# ==========================================================

num = 1

while num <= 100:
    print(num)
    num += 1

# "num" starts at 1 and increases by 1 every time.
# The loop keeps running until num becomes 101,
# at which point 101 <= 100 is False and it stops.


# ==========================================================
#              4. PRINT 100 TO 1 (WHILE LOOP)
# ==========================================================

num = 100

while num >= 1:
    print(num)
    num -= 1

# This time "num" starts at 100 and decreases by 1
# every time, so the numbers print in reverse order.
# The loop stops once num becomes 0.


# ==========================================================
#                5. MULTIPLICATION TABLE
# ==========================================================

n = int(input("Enter a number to see its table: "))

i = 1                            # i is the multiplier, starts at 1
while i <= 10:                   # repeat for multipliers 1 to 10
    print(n, "x", i, "=", n * i) # print one row of the table
    i += 1                       # move to the next multiplier

# We loop "i" from 1 to 10 and multiply "n" by "i" each time
# to print all 10 rows of the table.


# ==========================================================
#             6. SEARCH USING WHILE LOOP
# ==========================================================

numbers = [12, 45, 3, 67, 89, 22]

target = int(input("Enter a number to search: "))

idx = 0                     # idx is the position we are currently checking
found = False                # tracks whether we found the target

while idx < len(numbers):    # len(list) gives the number of items in the list
    if numbers[idx] == target:
        found = True
        break                 # break immediately exits the loop once found
    idx += 1

if found:
    print(target, "found at index", idx)
else:
    print(target, "not found in the list")

# len(numbers) -> total number of elements in the list, used so we
#                 never check an index that doesn't exist.
# idx          -> the index we are currently checking, moves 1 step
#                 at a time from 0 up to len(numbers) - 1.
# break        -> stops the loop immediately once a match is found,
#                 instead of wasting time checking the rest.


# ==========================================================
#                   7. INFINITE LOOP
# ==========================================================

# while True: is a loop whose condition is always True,
# so it never becomes False on its own and never stops.
#
# while True:
#     print("Hello")
#
# The example above is left commented out on purpose because
# running it would print "Hello" forever and freeze the
# program. An infinite loop only stops through a "break"
# statement inside it, an external interrupt (Ctrl+C), or
# a "return"/"exit()" call.


# ==========================================================
#                      8. break
# ==========================================================

# break immediately exits the loop it is inside of,
# skipping any remaining iterations.

for i in range(1, 10):
    if i == 5:
        break             # stop the loop completely once i is 5
    print(i)

# Output: 1 2 3 4
# The loop never reaches 5, 6, 7, 8, 9 because break
# exits it as soon as i == 5.


# ==========================================================
#                     9. continue
# ==========================================================

# continue skips the rest of the current iteration and
# moves on to the next one, without exiting the loop.

for i in range(1, 10):
    if i % 2 == 0:
        continue          # skip printing even numbers
    print(i)

# Output: 1 3 5 7 9
# When i is even, continue skips the print() and jumps
# straight to the next value of i.


# ==========================================================
#                 10. pass STATEMENT
# ==========================================================

# pass is a null statement that does nothing. It is used
# as a placeholder where Python syntactically requires a
# statement, but there is no code to write yet.

for i in range(5):
    pass

print("Done")

# The loop above runs 5 times and does nothing each time
# because of pass, then "Done" is printed once it finishes.


# ==========================================================
#                    11. for LOOP
# ==========================================================

# Syntax:
#
# for variable in sequence:
#     # code to repeat
#
# "sequence" can be anything you can iterate over:
#   - list    e.g. [1, 2, 3]
#   - tuple   e.g. (1, 2, 3)
#   - string  e.g. "Python"
#   - range   e.g. range(5)
#
# On each pass through the loop, "variable" takes the
# next value from "sequence" automatically -- there is
# no need to manually track an index like in a while loop.


# ==========================================================
#                12. TRAVERSE STRING
# ==========================================================

name = "Sundram"

for ch in name:
    print(ch)

# "ch" takes the value of one character of "name" on
# each iteration, until every character has been printed.


# ==========================================================
#               13. SEARCH CHARACTER
# ==========================================================

text = input("Enter a word: ")
search_char = input("Enter a character to search for: ")

for ch in text:
    if ch == search_char:
        print(search_char, "found in", text)
        break
else:
    # the "else" of a for-loop runs only if the loop
    # finished normally, i.e. "break" was never hit
    print(search_char, "not found in", text)


# ==========================================================
#                14. SEARCH NUMBER
# ==========================================================

num_list = [4, 8, 15, 16, 23, 42]
search_num = int(input("Enter a number to search for: "))

for value in num_list:
    if value == search_num:
        print(search_num, "found in the list")
        break
else:
    print(search_num, "not found in the list")


# ==========================================================
#                     15. range()
# ==========================================================

# range(stop)               -> 0, 1, 2, ..., stop - 1
# range(start, stop)        -> start, start + 1, ..., stop - 1
# range(start, stop, step)  -> start, start + step, ... (stops before stop)

for i in range(5):
    print(i)

# Output: 0 1 2 3 4

for i in range(2, 8):
    print(i)

# Output: 2 3 4 5 6 7

for i in range(2, 15, 2):
    print(i)

# Output: 2 4 6 8 10 12 14


# ==========================================================
#                  16. REVERSE RANGE
# ==========================================================

for i in range(10, 0, -1):
    print(i)

# A negative step (-1) makes range() count downward,
# starting at 10 and stopping just before 0.


# ==========================================================
#                  17. NESTED LOOPS
# ==========================================================

for i in range(3):          # outer loop -> controls the rows
    for j in range(4):      # inner loop -> controls the columns
        print("*", end=" ")
    print()

# The outer loop runs 3 times (3 rows).
# For every single run of the outer loop, the inner loop
# runs completely (4 columns), which is why nested loops
# are the foundation of pattern printing.


# ==========================================================
#           18. DIFFERENCE BETWEEN WHILE AND FOR
# ==========================================================

# While Loop                            | For Loop
# ---------------------------------------|---------------------------------------
# Runs until a condition becomes False   | Runs through a sequence (list/range)
# Used when the number of iterations     | Used when the number of iterations
# is NOT known in advance                | IS known in advance


# ==========================================================
#             19. COMMON BEGINNER MISTAKES
# ==========================================================

# Mistake 1: Forgetting to update the loop variable.
#   count = 1
#   while count <= 5:
#       print(count)
#       # forgot count += 1 here -> condition never
#       # becomes False -> infinite loop
#
# Mistake 2: Forgetting "break" when searching.
#   Without break, the loop keeps checking every
#   remaining element even after the target is already
#   found, instead of stopping right away.


# ==========================================================
#                20. PRACTICE QUESTIONS
# ==========================================================

# Q1  Print 1 to 20
# Q2  Print even numbers (1 to 20)
# Q3  Print odd numbers (1 to 20)
# Q4  Print a multiplication table
# Q5  Sum of first 10 numbers
# Q6  Factorial of a number
# Q7  Reverse counting (10 to 1)
# Q8  Print every character of a string
# Q9  Search a number in a list
# Q10 Search a character in a string
# Q11 Print squares of 1 to 10
# Q12 Print cubes of 1 to 10
# Q13 Print a string in reverse
# Q14 Count vowels in a string
