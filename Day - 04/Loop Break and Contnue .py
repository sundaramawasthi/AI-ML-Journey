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

i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

print("End of the loop")


# Continue

i = 0
while i <= 6:
    if i == 4:
        i += 1
        continue  # Skip 4

    print(i)
    i += 1

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

# FOR LOOP
# A for loop is used to visit (traverse) each item of a sequence one by one.
# A sequence can be a list, string, tuple, etc.

num = [1, 2, 3, 4, 5]      # Create a list containing five numbers.

for val in num:            # Take one value from the list and store it in 'val'.
    print(val)             # Print the current value.

else:                      # This else runs after the loop finishes normally.
    print("End")           # Print "End".


Explanation - 
Step-by-Step Execution

Iteration 1

val = 1
print(val)

Output:

1

Iteration 2

val = 2
print(val)

Output:

2

Iteration 3

val = 3
print(val)

Output:

3

Iteration 4

val = 4
print(val)

Output:

4

Iteration 5

val = 5
print(val)

Output:

5

Now the list is finished, so the else block runs.

Output:

End
Final Output
1
2
3
4
5
End




# WAP to search a character using a for loop.

name = "sundram"              # Store the string.

for char in name:             # Take one character at a time.

    if(char == "d"):          # Check if the current character is 'd'.
        print("Found")        # Print Found.
        break                 # Stop the loop immediately.

    print(char)               # Print the character if it is not 'd'.

else:                         # Runs only if the loop finishes without break.
    print("End")




# WAP to search a number using a for loop.

num = [1, 4, 6, 8, 9, 2, 4, 0]        # List of numbers.

search = int(input("Enter the value you want to search: "))  # Take input.

idx = 0                               # Start index from 0.

for val in num:                       # Visit each number in the list.

    if(val == search):                # Check whether current value matches.
        print(val, "found at index", idx)   # Print the value and its index.

    idx += 1                          # Move to the next index.
