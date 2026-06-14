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
# Example 

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.gear = False
    
    def start(self):
        self.acc = True
        self.brk = True
        self.gear = True
        print("car started")
car1 = car()
car1.start()
    

# Encapsulation 
# Wrappng data and functions into a single unit(object)

# Inheritance



# polimorphism



#Question 
# create an account class with 2 attribute balance and account no.
# create an method of debit credit and showing the balance

class account():
    def __init__(self,bal, acc):
        self.balance = bal
        self.account= acc
    
    # debit card
    def debit(self,amount):
        self.balance =- amount
        print("Your rs", amount, "is debited")
        print("you ammount",self.balance)

        # debit card
    def credit(self,amount):
        self.balance =+ amount
        print("Your rs", amount, "is creadited")
        print("your ammount", self.balance)
    
    def get_balance(self):
        return self.balance

    

    
acc1 = account(1000,100)
print(acc1.balance)
print(acc1.account)

acc1.debit(1200)
acc1.credit(324)