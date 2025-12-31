# WAP to input user's first name and print its length

name = input("write your name ")
print("length of your name is",len(name),"your name is ", name)


# WAP to find the occurrence of '$' in a string.

str = input("write your string ")
print("occurrence of '$' in the string is ", str.count("$"))

#WAP that tell today rain going to happen or not.

cloud = input("Enter the condition of cloud rainy or sun")
air = input("Enter the Air condition flowing or stop")

if(cloud == "rainy" and air == "flowing"):
    print("rain happen")
elif(cloud == "sun" and air == "stop"):
    print("rain not happen")
elif( cloud == "rainy" or air == "flowing"):
    print("May be rain happen")