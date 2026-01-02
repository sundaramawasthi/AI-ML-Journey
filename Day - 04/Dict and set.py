 # Dictionary in Python

# Dictionaries are used to store data values in key:value pair

#They are unorderd, mutable and they are not allow the duplicate key

info = {"name" : "sundram",
        "cgpa": "10",
        "marks": [34,56,78,89],
        "address": "lucknow",
        "is_adult" : True}

print("Name in the dict is = ",info["name"])
print(type(info))

# add element in dict

info["name"] = "change"
print(info["name"])


# Nested dictionaries
    
student = {
    "name" : "sundram",
    "subject" : {
        "math":89,
        "che":90,
        }
}

print(student["subject"]["math"])

# Dictionary Method

# myDict.key() It return all key

print("Key of dict is ",student.keys()) # return key name and subject 

# To typecast in list 

print("Change to list",list(student.keys()))

# Total number of key

print("Length of dict is ",len(student))

# mydict.values() return the all values

print("value of dict student is ", student.values())

# imp: we can store list in dict and store dict in a list

# mydict.items() It return all (key, val) pair as tuple

print("It return the key value pair as tuple", student.items())



# we can not access the index in the items so we will convert it into list
""" 📦 List = Box

You can open it

You can take item number 0

You can count positions

👉 Indexing works

🪟 dict_items = Window

You can look through

You can walk through one by one

But there are no numbered positions 

👉 Indexing does NOT work """ 


print(list(student.keys()))
pair = list(student.keys())

print("Now it return the index item",pair[0][1])

# myDict.get(key) Return the key according to value

print(student.get("name")) # If key is wrong then return none

# MyDict.update(new dict) can update the dict

student.update({"City" : "Delhi"})
print("Updated dict is ",student)



# Set in python
# Set s the collection of the unordered items
# Each element in the set must be unique and immutable.
# we can't store list and dict in a set because it is mutable
# Repeated elements stored only once, so it resoled to {1,2}


collection = {1,2,3,4,4, "hello", "world"}
# Set ignore the dublicate value
print("Type of collection = ",collection)
print("Total number of item in collection is", len(collection))
print("type of set",type(collection))

# set Method 

#add method
collection.add(5)
print("add element in set 5 " )

print("update set ",collection)

# Remove method

print("remove element in set 5")
collection.remove(5)
print("update set are",collection)

# clear method

print(" Clean the set ")

collection.clear()

print("length of set after clear method is",len(collection))

collection = {3,4,6}

#pop() Pop the  random value

print(collection.pop())

# union(set2) combine the both set value and return new

collection ={1,2}
collection1 = {2,3,4}

print("set 1 is",collection)
print("set 2 is",collection1 )

print(" new set is",collection.union(collection1))

# intersection(set2) # combines common values and return new

print("common of these set is", collection.intersection(collection1))