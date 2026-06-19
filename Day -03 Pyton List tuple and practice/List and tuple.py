#📘 Topic: Lists and Tuples in Python

#Today we will understand two very important data structures in Python:

#List
#Tuple

#These are used to store multiple values in a single variable.

#🟢 1. LIST in Python
#📌 What is a List?

#A list is a built-in data type in Python that can store a collection of values.

#⭐ Key Features:
#Lists are mutable → means we can change them after creation
#an store different data types together
#(integer, string, float, etc.)
#Ordered (indexing is possible)
#🔥 Example of List
property = [200, 300, 600, 700]
property[0] = "sundram"  # modifying list (mutable)

print("List of property is =", property)
print("Type of property is =", type(property))
print("Access index 1 =", property[1])
print("Length of list =", len(property))

#🧠 Explanation:
#property[0] = "sundram" → we changed value at index 0
#type() → tells the data type (list)
#property[1] → gives element at index 1
#len() → gives total number of elements



#✂️ 2. Slicing in List

#Slicing means getting a part of the list.

student = ["mohan", 67, "delhi"]

print("Whole list =", student)
print("Slicing [1:3] =", student[1:3])

#🧠 Explanation:
#Index starts from 0
#[1:3] means:
#start from index 1
#go till index 3 (but 3 is NOT included)

#So output will be:

[67, 'delhi']

#🛠️ 3. Methods in List
#➤ append()

#Used to add an element at the end of the list.

collection = ["name", "sundram", "age", 18, "place"]

collection.append("Delhi")

print(collection)

#🧠 Meaning:

#Adds "Delhi" at the last position.

#➤ sort()

#Used to arrange elements in ascending order.

num = [45, 67, 23, 90]

num.sort()
print(num)

#🧠 Output:
[23, 45, 67, 90]
#➤ reverse sort
num.sort(reverse=True)
print(num)
#🧠 Output:
[90, 67, 45, 23]
#➤ Sorting characters
alpha = ['a', 'd', 't', 'e', 'g', 't']

alpha.sort()
print(alpha)


#🧠 Output:

#Alphabetically sorted list.

#➤ reverse()

#Reverses the whole list (not sorting)

num = [45, 'y', 6]
num.reverse()
print(num)


#➤ insert()

#Used to insert element at specific position.

num.insert(0, 4)
#🧠 Meaning:

#Insert 4 at index 0

#➤ remove()

#Removes first occurrence of an element.

num.remove(45)
#➤ pop()

#Removes element from a specific index.

num.pop(2)

#🔵 4. TUPLE in Python
#📌 What is a Tuple?

#A tuple is similar to a list but:

#⭐ Key Difference:
#Tuples are immutable → cannot be changed after creation
#🔥 Example
tup = (2, 4, 6, 7, 5)

print("Element at index 2 =", tup[2])
print("Type =", type(tup[2]))

#✂️ Slicing in Tuple
print("Slicing [1:3] =", tup[1:3])
#🛠️ Methods in Tuple

#➤ index()

#Returns index of first occurrence of element.

print(tup.index(2))
#➤ count()

#Counts how many times an element appears.

print(tup.count(2))
"""
#📌 Final Summary
Feature	List	Tuple
Mutable	Yes	No
Syntax	[ ]	( )
Methods	Many	Limited
Performance	Slower	Faster
🎯 One-Line Concept
List = Flexible (changeable collection)
Tuple = Fixed (unchangeable collection)"""