Complete Loops Chapter (Updated)
# ==========================================================
#                    LOOPS IN PYTHON
# ==========================================================

1. What is a Loop?
2. While Loop
3. Print 1 to 100
4. Print 100 to 1
5. Multiplication Table
6. Search using While Loop
7. Infinite Loop
8. break Statement
9. continue Statement
10. pass Statement
11. for Loop
12. Traverse String
13. Search Character
14. Search Number
15. range()
16. Reverse Range
17. Nested Loops
18. Difference Between While and For
19. Common Beginner Mistakes
20. Practice Questions
21. Solutions of Practice Questions
==========================================================
1. WHAT IS A LOOP?
==========================================================
# A Loop is used to execute the same block of code
# again and again until a condition becomes False.

# Without Loop

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# Using While Loop

count = 1

while count <= 5:

    print("Hello")

    count += 1
Explanation
Initially
count = 1
Condition
count <= 5
is True
So Python enters the loop.
Iteration 1
count = 1

Print Hello

count = count + 1

count becomes 2
Iteration 2
count = 2

Print Hello

count becomes 3
Iteration 3
count = 3

Print Hello

count becomes 4
Iteration 4
count = 4

Print Hello

count becomes 5
Iteration 5
count = 5

Print Hello

count becomes 6
Now condition
6 <= 5
is False.
The loop stops.
==========================================================
2. WHILE LOOP
==========================================================
Syntax
while condition:

    # Code
Explanation
while
Keyword used to create a loop.
condition
Python checks this condition every time.
If condition is True
↓
Run the loop.
If condition becomes False
↓
Stop the loop.
# Code
The statements that repeat.
Example
count = 1

while count <= 3:

    print(count)

    count += 1
Output
1
2
3
==========================================================
3. PRINT 1 TO 100
==========================================================
count = 1

while count <= 100:

    print(count)

    count += 1
Explanation
count starts from 1

Print number

Increase count by 1

Repeat until 100
==========================================================
4. PRINT 100 TO 1
==========================================================
count = 100

while count >= 1:

    print(count)

    count -= 1
Explanation
Start from 100

Decrease by 1

Stop after reaching 1
==========================================================
5. MULTIPLICATION TABLE
==========================================================
num = int(input("Enter Number : "))

count = 1

while count <= 10:

    print(num, "x", count, "=", num * count)

    count += 1
Explanation
num
Stores the number entered by the user.
count = 1
Starts the table from 1.
while count <= 10
Runs the loop 10 times.
print(...)
Prints one line of the multiplication table.
count += 1
Moves to the next multiplication.
==========================================================
6. SEARCH USING WHILE LOOP
==========================================================
numbers = [12, 45, 78, 23, 90]

target = 78

idx = 0

while idx < len(numbers):

    if numbers[idx] == target:

        print("Found at Index", idx)

        break

    idx += 1

else:

    print("Not Found")
Explanation
len(list)
Returns the total number of elements.
Example
numbers = [10,20,30]

print(len(numbers))
Output
3
idx
Short form of
Index
Index tells the position.
Example
Index

0 1 2

10 20 30
numbers[0] = 10

numbers[1] = 20

numbers[2] = 30
break
Immediately exits the loop.
Python stops checking remaining elements.
else with while
The else block runs only if the loop finishes normally.
If break executes,
↓
else does NOT execute.
==========================================================
7. INFINITE LOOP
==========================================================
while True:

    print("Hello")
Explanation
True is always True.
Since the condition never becomes False,
Python keeps running forever.
This is called an
Infinite Loop.
Stop it using
Ctrl + C
==========================================================
8. break
==========================================================
for i in range(1,11):

    if i == 6:

        break

    print(i)
Output
1
2
3
4
5
Explanation
break immediately exits the loop.
Everything after 5 is skipped.
==========================================================
9. continue
==========================================================
for i in range(1,6):

    if i == 3:

        continue

    print(i)
Output
1
2
4
5
Explanation
continue skips the current iteration
and moves to the next iteration.
==========================================================
10. pass Statement
==========================================================
for i in range(5):

    pass

print("Done")
Explanation
pass means

Do Nothing.
Python simply ignores it.
Useful when writing empty loops or functions.
==========================================================
11. FOR LOOP
==========================================================
Syntax
for variable in sequence:

    # Code
Explanation
variable
Stores one item at a time.
sequence
A collection of items.
Examples
List

Tuple

String

Range
Example
for i in range(5):

    print(i)
==========================================================
12. TRAVERSE STRING
==========================================================
name = "Sundram"

for ch in name:

    print(ch)
Output
S
u
n
d
r
a
m
==========================================================
13. SEARCH CHARACTER
==========================================================
name = "Sundram"

target = "d"

for ch in name:

    if ch == target:

        print("Character Found")

        break
==========================================================
14. SEARCH NUMBER
==========================================================
numbers = [5,10,15,20]

target = 15

for num in numbers:

    if num == target:

        print("Found")

        break
==========================================================
15. range()
==========================================================
range(stop)
for i in range(5):

    print(i)
Output
0
1
2
3
4
range(start, stop)
for i in range(2,8):

    print(i)
Output
2
3
4
5
6
7
range(start, stop, step)
for i in range(2,15,2):

    print(i)
Output
2
4
6
8
10
12
14
Explanation
Start = 2

Stop before 15

Increase by 2
==========================================================
16. REVERSE RANGE
==========================================================
for i in range(10,0,-1):

    print(i)
Output
10
9
8
7
6
5
4
3
2
1
Explanation
Step = -1

Means move backward.
==========================================================
17. NESTED LOOPS
==========================================================
for i in range(3):

    for j in range(4):

        print("*", end=" ")

    print()
Output
* * * *

* * * *

* * * *
Explanation
Outer Loop

↓

Rows

Inner Loop

↓

Columns
