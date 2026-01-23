 # static Methods
# Method that don't use the sellf parameter(work at class level)

"""
class student:
@staticmethod #decrator
def college():
print("ABC College")

"""

class student:
    @staticmethod

    def college():
        print("College name is here")

# creating the object here
s1=student()
s1.college()

# Important concept 

# Abstraction 
#Hideing the implementation details of a class and only showing 
# the essential features to the user

# Encapsulation 
# Wrappng data and functions into a single unit(object)