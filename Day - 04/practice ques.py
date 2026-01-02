 # WAP store following word meanings in a python dictionary

# table ; "a piece of furniture" , "list of facts and figures"
# cat : "a small animal"

collection = {
    "cat" :" a small animal",
    "table " : ["a piece of furniture ","list of fact and figures"]
}

print(collection)


# You are given a list of subjects for students. Assume one classroom is
# required for 1 subject. How many classrooms are needed by all studensts.
 

classroom = {"java","python", "script", "java,","C++"
}
print("Total subjects are",classroom)        
print("Total subject required",len(classroom))    


# WAP to enter marks of 3 subjects from the user and storee them in a dictionary
# Start with an empty dict and add one by one. Use subject name as key and marks
# as value

marks = {}

x = int(input("Enter computer marks:  "))
marks.update({"computer" : x })


x = int(input("Enter math marks:  "))
marks.update({"math" : x })

y = int(input("Enter python marks:  "))
marks.update({"python" : y })

print(" Our updated list is",marks)


# WAP Figure out a way to store 9 and 9.0 as separate values in the set

cgpa = {}

x = int(input("Enter int value in cgpa"))
cgpa.update({"cgpa" : x})
y = float(input("Enter value in float"))
cgpa.update({"cgpa2" : y})

print("Latest CGPA is",cgpa)