 ### condition Statement

"""
Conditional Statements in Python

Conditional statements are used to make decisions in a program. They help the computer choose what to do based on a condition.

In simple words:

“If something is true, do this; otherwise do something else.”

1. if Statement

Used when you want to execute code only if a condition is true.

Syntax:
if condition:
    # code block
Example:
age = 18

if age >= 18:
    print("You are eligible to vote")
2. if-else Statement

Used when you have two choices: one for true, one for false.

Syntax:
if condition:
    # true block
else:
    # false block
Example:
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
3. if-elif-else Statement

Used when there are multiple conditions.

Syntax:
if condition1:
    # code
elif condition2:
    # code
else:
    # code
Example:
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
4. Nested if Statement

An if inside another if.

Example:
age = 20
citizenship = "India"

if age >= 18:
    if citizenship == "India":
        print("You can vote in India")
    else:
        print("You are not an Indian citizen")
else:
    print("Too young to vote")


"""



# if- elif-else (SYNTAX)

# Traffic light code


print("saw your traffic light ")

color = input("Enter Traffic light color ")

if(color=="red"):
    print("Red light stop")
elif(color=="green"):
    print("Green light Go")
elif(color == "orange"):
    print("ready to go")
else:
    print("Light is broken")




#2nd program student marks

marks= input(print("Enter you marks "))

if(marks == 90):
    print("Grade A")
elif(marks == 80 and marks >90):
    print("Grade B")
else:
    print("lower Grade ")


# If I have to wrote f statement in single line 
# Ternary operator
# <var> = < val1> if <condition>else <val2> 

food = input("wrote your food if it sweet or jalebi ")
print("sweet") if food == "jalebi" or food == "mango" else print("no taste")


# Clever if / Ternary Operator

#<var> = (false_val, true_al) [<condition>]

age = int(input("Enter your age "))
vote = ("12","18") [age<=18]
print("you can do vote")


sal=float(input("Enter your salary "))
total= sal*(0.1,0.2) [sal>40000]
print("good")


# Nested if

age = 34

if(age>=18):
    if(age>=80):
        print("can not drive ")
    else:
        print("can drive ")
