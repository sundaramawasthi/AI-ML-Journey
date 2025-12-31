 ### condition Statement
# if- elif-else (SYNTAX)

# Traffic light code


print("saw your traffic light")

color = input("Enter Traffic light color")

if(color=="red"):
    print("Red light stop")
elif(color=="green"):
    print("Green light Go")
elif(color == "orange"):
    print("ready to go")
else:
    print("Light is broken")




#2nd program student marks

marks= input(print("Enter you marks"))

if(marks == 90):
    print("Grade A")
elif(marks == 80 and marks >90):
    print("Grade B")
else:
    print("lower Grade")


# If I have to wrote f statement in single line 
# Ternary operator
# <var> = < val1> if <condition>else <val2> 

food = input("wrote your food if it sweet or jalebi")
print("sweet") if food == "jalebi" or food == "mango" else print("no taste")


# Clever if / Ternary Operator

#<var> = (false_val, true_al) [<condition>]

age = int(input("Enter your age"))
vote = ("12","18") [age<=18]
print("you can do vote")

sal=float(input("Enter your salary"))
total= sal*(0.1,0.2) [sal>40000]
print("good")



age = 34

if(age>=18):
    if(age>=80):
        print("can not drive")
    else:
        print("can drive")
