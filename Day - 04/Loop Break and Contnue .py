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

Then explain:

Iteration 1
count = 1

Iteration 2
count = 2

...

Iteration 5
count = 5

Loop stops because
count becomes 6.
2. While Loop

Explain syntax.

# Syntax

while condition:

    # Code

Then explain each part.

3. Print 1 to 100

Keep your example.

4. Print 100 to 1

Keep it.

5. Multiplication Table

Keep it but explain every line.

6. Search using While Loop

Keep it.

Also explain

len(list)

idx

break

else

because beginners don't understand them.

7. Infinite Loop

Very important.

while True:

    print("Hello")

Explain why it never stops.

8. break

Keep yours.

Also explain

break immediately exits the loop.
9. continue

Keep yours.

10. pass Statement

Very important.

for i in range(5):

    pass

print("Done")

Explain that pass means

Do nothing.
11. for Loop

Keep yours.

Explain

for variable in sequence:

Explain

sequence

↓

list

tuple

string

range
12. Traverse String
name = "Sundram"

for ch in name:

    print(ch)
13. Search Character

Keep yours.

14. Search Number

Keep yours.

15. range()

This is missing and is extremely important.

Explain:

range(stop)

range(start, stop)

range(start, stop, step)

Examples

for i in range(5):

    print(i)

Output

0
1
2
3
4
for i in range(2,8):

    print(i)
for i in range(2,15,2):

    print(i)

Explain

2

4

6

8

10

12

14
16. Reverse Range
for i in range(10,0,-1):

    print(i)
17. Nested Loops

Very important before pattern printing.

for i in range(3):

    for j in range(4):

        print("*",end=" ")

    print()

Explain

Outer loop

↓

Rows

Inner loop

↓

Columns
18. Difference between While and For

Make a table.

While	For
Runs until condition becomes False	Runs through a sequence
Used when iterations are unknown	Used when iterations are known
19. Common Beginner Mistakes

Like

Forgot count += 1

↓

Infinite Loop
Forgot break

↓

Loop never exits
20. Practice Questions

I'd add about 15.

Q1 Print 1 to 20

Q2 Print even numbers

Q3 Print odd numbers

Q4 Print multiplication table

Q5 Sum of first 10 numbers

Q6 Factorial

Q7 Reverse counting

Q8 Print every character

Q9 Search number

Q10 Search character

Q11 Print squares

Q12 Print cubes

Q13 Print reverse string

Q14 Count vowels

