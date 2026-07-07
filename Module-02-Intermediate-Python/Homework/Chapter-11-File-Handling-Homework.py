# ==========================================================
#      MODULE 2 - CHAPTER 11: FILE HANDLING
#                Homework Solutions
# ==========================================================

# Create a starter file so Q1 has something to read from.

with open("homework_sample.txt", "w") as f:
    f.write("Python is a beginner friendly language.\n")
    f.write("Python is used in AI and Machine Learning.\n")
    f.write("Loops and Functions make programs powerful.\n")


# ==========================================================
# Q1 Read and print a file.
# ==========================================================

with open("homework_sample.txt", "r") as f:
    print(f.read())


# ==========================================================
# Q2 Create a new file.
# ==========================================================

with open("homework_new.txt", "w") as f:
    f.write("This is a newly created file.")


# ==========================================================
# Q3 Write your name into a file.
# ==========================================================

with open("homework_new.txt", "w") as f:
    f.write("Sundram")


# ==========================================================
# Q4 Append your city name.
# ==========================================================

with open("homework_new.txt", "a") as f:
    f.write("\nDelhi")

with open("homework_new.txt", "r") as f:
    print(f.read())


# ==========================================================
# Q5 Search a word in a file.
# ==========================================================

search_word = "Python"

with open("homework_sample.txt", "r") as f:
    data = f.read()

if search_word in data:
    print(search_word, "found in the file")
else:
    print(search_word, "not found in the file")


# ==========================================================
# Q6 Count the number of lines.
# ==========================================================

with open("homework_sample.txt", "r") as f:
    lines = f.readlines()

print("Total Lines =", len(lines))


# ==========================================================
# Q7 Count the number of words.
# ==========================================================

with open("homework_sample.txt", "r") as f:
    data = f.read()

words = data.split()
print("Total Words =", len(words))


# ==========================================================
# Q8 Count even numbers from a file.
# ==========================================================

with open("homework_numbers.txt", "w") as f:
    f.write("1,2,3,4,5,6,7,8,9,10")

with open("homework_numbers.txt", "r") as f:
    data = f.read()

numbers = data.split(",")
even_count = 0

for number in numbers:
    if int(number) % 2 == 0:
        even_count += 1

print("Total Even Numbers =", even_count)
