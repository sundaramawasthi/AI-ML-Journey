 # Type Conversion

#Type Conversion in Python
"""

Type Conversion means converting one data type into another data type automatically by Python.

This is also called Implicit Type Conversion."""
Example
a = 10      # int
b = 5.5     # float

result = a + b

print(result)
print(type(result))
Output
15.5
#<class 'float'>
""" 
Here Python automatically converts 10 (int) into 10.0 (float) before performing the addition.

Type Casting in Python

Type Casting means converting one data type into another manually using functions.

This is also called Explicit Type Conversion.

Common Type Casting Functions
Function	Description
int()	Converts value to Integer
float()	Converts value to Float
str()	Converts value to String
bool()	Converts value to Boolean
"""

var1= 2 #int
var2 = 4.45 #float

sum = var1+var2
# variable = int+ float

print(sum)


# Type Casting

var1 = "2" #string
var2 = 4.56 #Float
var3 = int("2") # int

sum= var2+var3 #float + int

print(type(var3))
print(sum)


#String

#String is data type that stores a swquence of character

# Concatenation

str1 = "Python"
str2 = "language"
finalStr = str1+str2
print("Concatenation of string is str1+str2 = ", finalStr)



# Find the length of string
print("Length of str = ",len(finalStr))

