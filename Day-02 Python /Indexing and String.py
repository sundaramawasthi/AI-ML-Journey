 
# Indexing

Text = "Python"
print("Index 1",Text[1]) # index of python = [0],[1],[2],[3],[4],[5]
print("Total index in python is =",len(Text)-1)
print("Index in python start from 0")

# Slicing
# Accessing parts of a string

#SYNTAX - str[ starting_idx : Ending_idx]

Text = "your python course"
# we never include 5 it count 2,3,4 = ur 
print("Slicing of the str using index 2:5 it return = ", Text[2:5])
print("Slicing of the str using idx 7:9 it return =",Text[7:9])
print("Whenever we do slice like str[ :5] it return starting to 5 idx = ", str[:5])
print("slice like str[ 3:] it return  starting idx to last idx like = ", str[3:])
print("Full str =",Text)


# Negative Slicing

Text = "language"
# In negative slicing it skip last index i.e. -3 
print("Negative slicing in python is = ", Text[-5:-3])


#String Function

# str.endswith("") #This function check if the string end with given str or not.

Text= "check me"

print("Is check string last string is ck, if yes return true =",str.endswith("k"))

#str.capitalize() # function that capitalizes 1st char

print("capitalize 1st letter of string",Text.capitalize())


# str.replace() #Function replace the old value with new value

print("It replace c with k = ",Text.replace("c","k"))


#str.find() # function that find the index of given string 
print("Index of string me is ", Text.find("me"))


# str.count("") #Fuction count the occurrence of substr

print("str check c count is ", Text.count("c"))
