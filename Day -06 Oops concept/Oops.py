 # Oops in python 

# To map with real world scenarios, we started using objects in code
# This is called object oriented programming. 

# Object - Mouse , keyboard etc.
# before objeect we create the class

""" Clas is a blueprint for creating objects"""
"""
# Creating Class

class Student:
    name = "Sundram Awasthi" # same for everyone
    age = 32
    number = 56


# Creating object(instance)

s1= Student()
print(s1.age)


#Class fr car
class car:
    color = "blue"
    model = 2.0

# Object of car

car1 =car()
print(car1.color)

"""

"""
init_function

Constructor classes have a function called _init_(),
which is always executed when the class is being
initiated

""" 


class Student:
   # same for everyone
    def __init__(self, fullname,marks):  #constructor always take one parameter (self)
        self.name = fullname # we can store different variable and data using self
        self.marks = marks
        print("adding new student in Data base")
        

    


# Creating object(instance)

s1= Student("sundram", 67) # paranthesis called the init function
print(s1.name,s1.marks)