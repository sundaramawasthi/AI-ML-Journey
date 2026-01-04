 # LOOP 
# Loop are used to repeat instructions.

count = 1
while count<=4 :
    print("hello")
    count +=1
print("loop Ended",count)

# WAP print number 1 to 100

num = 1 
print("number from 1 to 100")
while(num<=100):
    print(num)
    num+=1

#WAP print number. from 100 to 1

num = 100
print("From 100 to 1")
while(num>=1): # 100 is greater then 1 so it true Run
    print(num)
    num -=1

# WAP to print multiple table of a number n 

n = int(input("Enter the number that you want table of n "))

i =1
while(i<=10): 
    print(n*i) # it multiply the n*i then increase i each time till 10
    i+=1


# WAP to print the element of the following list using a loop

#[1,4,9,16,25,36,49,64]

num = int(input("Enter the num "))

while(num<=8):
  print("seriese is",num*num) #Seriese is square of each num
  num+=1


# Another method is

num  = [1,4,9,16,25,36,49,64]

idx= (int(input("Enter the idx value less then 0 ")))

while(idx < len(num)):
    print("seriese is",num[idx])
    idx+=1


# WAP to search the value in given seriese
num = [1,4,9,16,25,36,49,64]
search = int(input("Enter the num you want search: "))

idx = 0
while idx < len(num):
    if num[idx] == search:
        print("Found", search, "at idx", idx)
        break
    idx += 1
else:
    print("Not found")
   

# Break and Continue

# Break : used to terminate the loop when encounter

# Continue : terminates execution in the current iteration
# and continue execution of the loop with the next iteration.

# Break

i=1
while i<=5:
    print(i)
    if(i == 3):
        break
    i+=1
print("End of the loop")

# Continue

i=0
while i<=6:
    if(i ==4):
        i+=1
        continue #skip
    print(i)

# WAP to print only odd number

num = int(input("Enter num between 0 to 10"))

while(num<=10):
    if(num%2 == 0):
        num+=1
        continue #skip
    print("odd ",num)
    num+=1


#  FOR LOOP
#  loop are used for sequential travesal.For traeling list, string, tuples etc

num = [1,2,3,4,5]

for val in num:
    print(val)
else:
    print("End")


 # WAP to search string using for
name = "sundram"

for char in name:
    if(char == "d"):
        print(" found")
        break
    print(char)
else:
    print("End") # work that we want work till end of loop


# WAP a program to search the num using for loop

num = [1,4,6,8,9,2,4,0]
search = int(input("Enter the val u want search"))
idx =0
for val in num:
    if(val == search):
        print(val,"found" )
    idx+=1