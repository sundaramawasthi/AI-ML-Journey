 # Function in python
# Block of statement that perform a specific task
'''
def func_name(parameter 1, parameter2): # function define
    # some work
    return Val 

func_name(arg1, arg2) # function call 

There is two type of function print in and user define function


There is two type of fuction
built in and user define function

'''

def sum(a,b):
    sum= a+b
    print("sum of a and b =",sum)
    return sum

sum(4,5) # we call function here

sum(10,45) # we call function


# WAP to make a function that take input from user and
#wrote an table for him.

def table():
    n = int(input("Enter the number you want table"))

    for i in range(1,11):
        tab = n*i
        print(n,"*",i,"=",tab)   
    return tab
table()




# WAP that calculate ag of 3 people

def avg():
    n1= int(input("Enter 1 number "))

    n2= int(input("Enter 2 number "))

    n3= int(input("Enter 3 number "))

    cal = (n1+n2+n3) /3

    # print(cal)
    return cal

result = avg()
print("avg = ",result)


#WAP to print the length of list

def lenlist ():
    lst = list(map(int, input("Enter your list: ").split()))

    return(lst)

lstt=lenlist()
length = (len(lstt))
print("length oflist is",length,"=",lstt)



# WAP to print fac

def fact():
    fct=1
    
    n=int(input("Enter the number you want fact "))

    for i in range(1,n+1):
        fct = fct*i
        
    return fct

factorial = fact()
print("Factorial is =",factorial)



# WAP to convert USD into INR 

def convert():
    inr = int(input("Enter your value in rs "))

    usd = 86*inr

    return usd
final= convert()
print(final)




