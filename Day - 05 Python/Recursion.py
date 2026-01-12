 
# Recursion in python 

# when function call itself repeatedly
num = int(input("Enter the number "))
def show(a):

   if(a == 0):
      return
   print(a)
   show(a-1)

show(num)


#WAP a program to calculate fact using recurssion

num = int(input("Enter the fact value "))

def fact(n):
   if(n ==1 or n==0):
      return 1
   return fact(n-1)*n

f = fact(num)
print(f)



# WAP to calculate first n natural number

num = int(input("Enter the number "))

def natural(n):
   if(n == 1 or n==0):
      return 1
   return natural(n-1)+n

sum =natural(num)
print(sum)


# Write a recursive function to print all element in a list

def print_lst(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_lst(list,idx+1)

fruits = ["mango", "litchi"]
print_lst(fruits)