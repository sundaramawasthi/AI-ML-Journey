# WAP to input user's first name and print its length

name = input("write your name ")
print("length of your name is",len(name),"your name is ", name)


# WAP to find the occurrence of '$' in a string.

str = input("write your string ")
print("occurrence of '$' in the string is ", str.count("$"))

#WAP that tell today rain going to happen or not.

cloud = input("Enter the condition of cloud rainy or sun ")
air = input("Enter the Air condition flowing or stop ")

if(cloud == "rainy" and air == "flowing"):
    print("rain happen")
elif(cloud == "sun" and air == "stop"):
    print("rain not happen")
elif( cloud == "rainy" or air == "flowing"):
    print("May be rain happens")




# WAP to check if a number entered by the user is odd or even
num = int(input("Enter any number"))

if(num/2 == 0):
    print("Number is even")
else:
    print("Number is odd")


#WAP to find the greatest of 3 number entered by the user.

num1 = input("Enter 1st number")
num2= input("Enter 2nd number")
num3 = input("Enter 3rd number")

if(num1>num2 and num1>num3):
    print("greatest number is =",num1)
else:
    if(num2>num1 and num2>num3):
        print("greatest number is = ", num2)
    else:
        print("Greatest number is = ", num3)


#WAP to check f a number is aa multiple of 7 or not 

num = int(input("Enter any number "))

if(num/7 == 0):
    print("number is multiple of 7", num)
else:
    print("number is not a multiple of 7",num)