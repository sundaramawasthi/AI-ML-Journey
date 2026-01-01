# WAP to input user's first name and print its length

name = input("write your name ")
print("length of your name is",len(name),"your name is ", name)


# WAP to find the occurrence of '$' in a string.

name = input("write your string ")
print("occurrence of '$' in the string is ", name.count("$"))

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

print("Even" if num%2 == 0 else "odd")




#WAP to find the greatest of 3 number entered by the user.

num1 = int(input("Enter 1st number"))
num2= int(input("Enter 2nd number"))
num3 = int(input("Enter 3rd number"))

if(num1>num2 and num1>num3):
    print("greatest number is =",num1)
else:
    if(num2>num1 and num2>num3):
        print("greatest number is = ", num2)
    else:
        print("Greatest number is = ", num3)


#WAP to check f a number is aa multiple of 7 or not 

num = int(input("Enter any number "))

if(num%7 == 0):
    print("number is multiple of 7", num)
else:
    print("number is not a multiple of 7",num)



#WAP to ask the user to enter names of their 3 fa moie and store them in a list.

movie1 = str ( input("Enter your 1st movie name "))
movie2 = str (input("Enter your 2nd  movie name "))
movie3 = str (input("Enter your 3rd  movie name "))

final = [movie1,movie2,movie3]

print("our new list is =",final)

# WAP to check if a list contains a palindrome of elements

list1 = [1,2,1]

# copy function use to copy the given list
copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("pailandrome")
else:
    print("Not pailandrome")



# WAP to count the number of students with the "A" grade in following tuple

grade = ["C","D","E","A","F","A","G"]

print("Number of A in the tup is ", grade.count("A"))

print(type(grade))

# WAP to store the above values in a list and sort them from A to D

grade.sort()
print(grade)




#WAP to ask the user to enter names of their 3 fa moie and store them in a list.

movie1 = str ( input("Enter your 1st movie name "))
movie2 = str (input("Enter your 2nd  movie name "))
movie3 = str (input("Enter your 3rd  movie name "))

final = [movie1,movie2,movie3]

print("our new list is =",final)

# WAP to check if a list contains a palindrome of elements

list1 = [1,2,1]

# copy function use to copy the given list
copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("pailandrome")
else:
    print("Not pailandrome")



# WAP to count the number of students with the "A" grade in following tuple

grade = ["C","D","E","A","F","A","G"]

print("Number of A in the tup is ", grade.count("A"))

print(type(grade))

# WAP to store the above values in a list and sort them from A to D

grade.sort()
print(grade)



