# ==========================================================
#      MODULE 1 - CHAPTER 5: STRINGS
#                Homework Solutions
# ==========================================================


# ==========================================================
# Question 1
# Create a string "Programming".
# Print first character and last character.
# ==========================================================

word = "Programming"
print(word[0])
print(word[-1])


# ==========================================================
# Question 2
# Print the first five characters using slicing.
# ==========================================================

print(word[0:5])


# ==========================================================
# Question 3
# Print the last four characters using negative slicing.
# ==========================================================

print(word[-4:])


# ==========================================================
# Question 4
# Find the length of your name.
# ==========================================================

name = "Sundram"
print(len(name))


# ==========================================================
# Question 5
# Convert your name into uppercase.
# ==========================================================

print(name.upper())


# ==========================================================
# Question 6
# Replace your city name with another city.
# ==========================================================

city = "Delhi"
new_city = city.replace(city, "Mumbai")
print(new_city)


# ==========================================================
# Question 7
# Count how many times the letter "a" appears in your name.
# ==========================================================

print(name.count("a"))


# ==========================================================
# Question 8
# Check whether your name ends with the letter "n".
# ==========================================================

print(name.endswith("n"))
