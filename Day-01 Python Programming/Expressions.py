 # Let assigne an variable

a=3
b=5
txt  ="@"

print("The rule is we can execute string and number together by use of * ", 2*txt*3)
# 2 * txt mean wrote @ 2 times and * 3 mean multiply 2 times into 3 so it will wrote 6 times.
# Output is @@@@@@

# 2nd expression is 

print(txt+txt * a)



# here string and string can operate with +
# here output is A= 3 then @ then it multiply with 5 it mean we repeat 3@ to 5 times 

# Numeric Values can operate with all arithmatics operators

A =2
B=4
C=4

print("A+B*C = ", A+B*C)

# Airthematic expression with integer and float will result in float

A=5
B=4.0

C=A*B

print("A*B = ", A*B)

# In divisinal operator the result in float

print("A/B =", A/B)

#Integer Division with float and integer will given int display with float

C=A//B

print("C= A//B ",C)

#same as integer division , Floor  - Function in math that given closest integer Example -0.1 -> 0, 5.2->5.

# Operator precedence not>and>or

#assignment operators

num=10
num=num+5 # num+=5 (same), num**=5, num-=5, num%=5
print("Num = ",num)

# Relational operator

num1 = 50
num2 = 40

print(a==b)
print(a>b)
print(a<b)


# Logical operator
a = True
b = False

print("and operator", a and b)
print(" or operator", a or b)