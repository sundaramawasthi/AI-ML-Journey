 # Python can be used to perform operations on a file.( read and write data)

"""

Types of file 

1. Text files : .txt, .docx, .log etc
2. Binary files : ,mp4, .mov, .png, .jpeg 

"""

#  OPEN READ AND CLOSE FILE

""" WE HAE TO OPEN A FILE BEFORE READING OR WRITING"""

#F =open("file_name","mode")
# mode = read or write ( We have two mode read or write)

f = open("/Users/shivamawasthi/Desktop/AI-ML-Journey/Day - 05 Python/sample.txt", "r") # we open file
data = f.read() # we can pass parameter also line number of character
print(data)
print(type(data))
f.close()

# readline() # read one line at a time.

f = open("/Users/shivamawasthi/Desktop/AI-ML-Journey/Day - 05 Python/sample.txt", "r") # we open file

line1 = f.readline() # Line 1 read
print(line1)

line2 = f.readline() # line 2 read
print(line2)

f.close()



# writing to a file

""" There is two method one is we open file in w mode another is 
we open file in a(add at the end ) mode """

f = open("/Users/shivamawasthi/Desktop/AI-ML-Journey/Day - 05 Python/sample.txt", "w") # we open filef = open("/Users/shivamawasthi/Desktop/AI-ML-Journey/Day - 05 Python/sample.txt", "r") # we open file
f.write("I am writing my file, Its mean my previous text is change")
f.close()


f = open("demo.txt","w") # like that we can create our file demo.txt
f.write("1,2,3,4,5,3") # the abc is write in file demo.txt itself
f.close()


# Combine reading and writing 
# r+ ( reading and writig)



# with syntax

#with open("demo.txt", "a") as f:
#    data = f.read()
#    print(data)


# Delete the file 
""" using the os module
module(like a code library) is a file written by another
programmer that generally has a function we can use.
"""

#import os # pre install module

#os.remove("file name")


# WAP to searh writing word in sample.txt

word = "writing"
with open("/Users/shivamawasthi/Desktop/AI-ML-Journey/Day - 05 Python/sample.txt", "r") as f:
          data = f.read()
          if(data.find(word)!=-1):
                 print("found")
          else:
                 print("Not found") 



# WAP to find which line of the file does the word
# writing occur first
"""
def check_for_line():
        word ="writing"
        data = True
        line_no = 1
        with open("/Users/shivamawasthi/Desktop/AI-ML-Journey/Day - 05 Python/sample.txt", "r") as f:
                while data:
                        f.readline()
                        if(word in data):
                                print(line_no)
                                return
                        line_no+=1

                return -1
        
check_for_line()
"""


# WAP to read a file and print even number in the givve file

count = 0

with open("demo.txt", "r") as f:
        data =f.read()

        nums = data.split(",")
        for val in nums:
                if(int(val)%2 == 0):
                        count+=1
print(count)

