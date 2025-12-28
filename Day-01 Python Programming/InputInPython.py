 # Take input in python

#Input() Statement is used to accept values from user

#String Input

name = input("Enter your name: " )
print("Your name is ",name)

#Integer

age = input("Enter your age")
print("Your age is", age)

#Float

price = float(input("enter float alue"))
print("your float price value is",price)



# program take two number input and print true if number 1 is greater then number 2
num = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

if(num < num2):
    print("num 1 is less than num 2 , False")
else:
    print("num 1 is greater then num 2, True")