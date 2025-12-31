 # List
# String are imutable
# list are mutable
# # Built in data type that stores set of values
# can store element of different types (Integer, float, string, etc)


property =([200,300,600,700])
property[0] = "sundram"  #mutable list
print("List of property is = ",property)
print("Types of property is", type(property))
print("Can access the index also property[1] is = ",property[1])
print("length of the list is", len(property))


# Slicing in the list 

student = (["mohan",67,"delhi"])
print("Whole list is  = ",student)
# It not count the 3 index
print("slicing of the list is [1:3]= ",student[1:3] )



# Method in list 

# append method

collection = (["name", "sundram", "age", 18, "place"])

print("Our collection is = ",collection)

print("append the place name Delhi",collection.append("Delhi"))

print("our new list is = ",collection)


# sort() method

num = ([45,67,23,90])
print("Our list is = ",num)
print("sort number using sort method",num.sort)

print("New list is = ",num)


# Reverse sort

print("reverse the list using num.sort(reerse=True)",num.sort(reverse=True))
print("New list is = ",num)


# Char sort is also Posible 

alpha = (['a','d','t','e','g','t'])

print("Our list is = ",alpha)

print("sort the char using alphs.sort",alpha.sort())

print("New list is =",alpha)



# list.reverse() revverse the whole list
num=([45, 'y',6])
print("Our list is =",num)
num.reverse()
print("Reverse of the list is = ",num)


# list.inser( idx, element)

print("Our list is = ",num)
num.insert(0,4)
print("New list is. =",num)
