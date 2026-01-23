 # Class and instance Attributes

# Class.attr - common for whole class

# Instance - different from each object

# Object attribute is more preference then college attribute

class Student:
    college_name = "your college" # class attribute
   # same for everyone
    def __init__(self, fullname,marks):  #constructor always take one parameter (self)
        self.name = fullname # we can store different variable and data using self
        self.marks = marks # Object attribute
        print("adding new student in Data base")
        

# Creating object(instance)

s1= Student("sundram", 67) # paranthesis called the init function
print(s1.name,s1.marks)

s2 =Student("karan", 76)
print(s2.marks,s2.name,Student.college_name)





# Methods
# Method are  function that belong to object

# class has two thing to store data(attributes) and method.


class team:
    company_name = "naiva" # Class attribute

    def __init__(self, name, position):
        self.name = name # Object attribute
        self.position = position

#Creating method in class 
    def welcome(self):
       print("welcome CEO",self.name)



# Creating Object

c1=team("sundram","CEO")
print(c1.company_name, c1.name, c1.position )


# Creating object for method

c1.welcome()



# WAC of student that take name and marks of 3 subjects as
# arguments in a constructor then create a method to the print the 
# average


class student:
    collegename = "chandigarh University"

    
    def __init__(self,name,marks, subject):
        self.name = name # object parameter
        self.marks = marks
        self.subject = subject


    def average(self):

        avg = sum(self.marks)/len(self.marks)

        print("hi name is",self.name, "avg of three marks. =",avg)

# Creating object
s1=student("sundram", [76,34,23], "chemistry")
print(s1.collegename)
print(s1.name,s1.marks,s1.subject)


s1.average()


# Change the attribute  value directly

s1.name = "awasthi"
s1.average()