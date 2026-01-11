 
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