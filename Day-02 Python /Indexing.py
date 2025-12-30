 
# Indexing

str = "Python"
print("Index 1",str[1]) # index of python = [0],[1],[2],[3],[4],[5]
print("Total index in python is =",len(str)-1)
print("Index in python start from 0")

# Slicing
# Accessing parts of a string

#SYNTAX - str[ starting_idx : Ending_idx]

str = "your python course"
# we never include 5 it count 2,3,4 = ur 
print("Slicing of the str using index 2:5 it return = ", str[2:5])
print("Slicing of the str using idx 7:9 it return =",str[7:9])
print("Whenever we do slice like str[ :5] it return starting to 5 idx = ", str[:5])
print("slice like str[ 3:] it return  starting idx to last idx like = ", str[3:])
print("Full str =",str)


# Negative Slicing

str = "language"
# In negative slicing it skip last index i.e. -3 
print("Negative slicing in python is = ", str[-5:-3])

