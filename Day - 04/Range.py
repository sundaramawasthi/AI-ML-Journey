# Range() 
# Range functions return a sequence of number, starting from 0 by default,
# and increment by 1 ( by default) and stop before specialize number
 # range( start ?,stop,step?)  # strp mean how much you want increment.


#staring,stop,step
for el in range(1,5,1):
    print(el) 

# stop
for el in range(10):
    print(el)

 #start and stop

for el in range(1,6):
    print(el)


#WAP print num from 1 to 100

for i in range(1,101):
    print("1 to 100 num",i)



for i in range(100,1,-1):
    print("1 to 100 num",i)


n = int(input("Enter Value of n"))

for i in range(1,11):
    print(n,"*",i,"=", n*i)



#  PASS STATEMENT 

# pass is a null statement that does nothing, it is used as placeholder for future code 

for el in range(10):
    pass
print("empty")



# WAp to find the sum of first n numbers(using while)

n=int(input("Enter the value of n"))
sum=0
i=0

while(i<=n):
    sum +=i
    i+=1
print("Sum = ",sum)


#WAP to find fact of the given num

fact = int(input("Enter the fact value"))

fact = 1
i =1

while(i<=n):
    fact*=i
    i+=1
print(fact)