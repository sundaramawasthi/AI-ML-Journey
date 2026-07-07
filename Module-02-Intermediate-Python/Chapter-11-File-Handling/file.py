# ==========================================================
#            DAY 8 - PYTHON PROGRAMMING
#              Topic: File Handling
# ==========================================================

# In this lesson, you will learn:
#
# ✅ What is File Handling?
# ✅ File Types
# ✅ open()
# ✅ read()
# ✅ readline()
# ✅ write()
# ✅ File Modes
# ✅ with Statement
# ✅ Delete a File
# ✅ Practice Programs


# ==========================================================
#           WHAT IS FILE HANDLING?
# ==========================================================

# File Handling is used to
# store data permanently inside a file.
#
# Without files,
# data is lost when the program ends.

# Examples:
#
# Student Records
# Notes
# Attendance
# Login Details


# ==========================================================
#              TYPES OF FILES
# ==========================================================

# 1. Text Files
#
# .txt
# .py
# .csv
# .log

# 2. Binary Files
#
# .jpg
# .png
# .mp3
# .mp4
# .pdf


# ==========================================================
#          OPENING A FILE
# ==========================================================

# Syntax
#
# open(file_name, mode)

# Example

file = open("sample.txt", "r")

# Always close the file
# after using it.

file.close()


# ==========================================================
#             FILE MODES
# ==========================================================

# "r"
# Read only.
#
# "w"
# Write.
# Creates a new file if it
# does not exist.
# Replaces old content.
#
# "a"
# Append.
# Adds data at the end.
#
# "x"
# Creates a new file.
# Gives an error if the file exists.
#
# "r+"
# Read and Write.


# ==========================================================
#             read()
# ==========================================================

# read() reads the complete file.

file = open("sample.txt", "r")

data = file.read()

print(data)

file.close()


# ==========================================================
#            readline()
# ==========================================================

# readline() reads one line
# at a time.

file = open("sample.txt", "r")

print(file.readline())

print(file.readline())

file.close()


# ==========================================================
#             readlines()
# ==========================================================

# readlines() returns
# all lines as a list.

file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# ==========================================================
#             write()
# ==========================================================

# "w" mode replaces
# old content.

file = open("sample.txt", "w")

file.write("Welcome to Python")

file.close()


# ==========================================================
#            append()
# ==========================================================

# "a" mode adds new data
# at the end of the file.

file = open("sample.txt", "a")

file.write("\nThis is a new line.")

file.close()


# ==========================================================
#        CREATE A NEW FILE
# ==========================================================

file = open("demo.txt", "w")

file.write("Python File Handling")

file.close()


# ==========================================================
#           with STATEMENT
# ==========================================================

# Best way to open files.
#
# It automatically closes
# the file.

with open("sample.txt", "r") as file:

    data = file.read()

    print(data)


# ==========================================================
#         DELETE A FILE
# ==========================================================

# import os
#
# os.remove("sample.txt")

# os is a built-in module
# used for file operations.


# ==========================================================
#     PROGRAM : SEARCH A WORD
# ==========================================================

word = "Python"

with open("sample.txt", "r") as file:

    data = file.read()

    if word in data:

        print("Word Found")

    else:

        print("Word Not Found")


# ==========================================================
#   PROGRAM : FIND THE LINE NUMBER
# ==========================================================

word = "Python"

line_number = 1

with open("sample.txt", "r") as file:

    for line in file:

        if word in line:

            print("Found at Line", line_number)

            break

        line_number += 1

    else:

        print("Word Not Found")


# ==========================================================
#    PROGRAM : COUNT EVEN NUMBERS
# ==========================================================

# This program expects demo.txt to contain
# comma-separated numbers, e.g:
#
# 1,2,3,4,5,6,7,8
#
# So we (re)write demo.txt with that content first,
# overwriting the "Python File Handling" text that was
# written into it earlier in this file.

with open("demo.txt", "w") as file:

    file.write("1,2,3,4,5,6,7,8")

count = 0

with open("demo.txt", "r") as file:

    data = file.read()

numbers = data.split(",")

for number in numbers:

    if int(number) % 2 == 0:

        count += 1

print("Total Even Numbers =", count)


# ==========================================================
#           PRACTICE QUESTIONS
# ==========================================================

# Q1 Read and print a file.

# Q2 Create a new file.

# Q3 Write your name into a file.

# Q4 Append your city name.

# Q5 Search a word in a file.

# Q6 Count the number of lines.

# Q7 Count the number of words.

# Q8 Count even numbers from a file.


# ==========================================================
#              DAY 8 SUMMARY
# ==========================================================

# Today you learned:
#
# ✅ File Handling
# ✅ open()
# ✅ read()
# ✅ readline()
# ✅ readlines()
# ✅ write()
# ✅ append()
# ✅ File Modes
# ✅ with Statement
# ✅ Delete a File
#
# 🎉 Congratulations!
# You have successfully completed
# the File Handling chapter.
