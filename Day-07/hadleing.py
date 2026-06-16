print("This is our first exceptional handeler program ") 
# It give us error because we not put double quotes at the end, so compiler understand it, our code is not execuate

a = int(input("Enter the value "))
print(a)

#Here in the program when we enter the value which is greater then a then it give us valid output, and when we enter 0 then it give us invalid valid, even though o is an valid int value but it show the error in other shell so here concept came exceptional handeling. we can also handle using if else, but problem is in efelse we have to thing the condtion of the if else before so it little bit difficult so the module given in the python that is exceptional handeling.

b=5 
c = b/a
print(c)

try:
  a=int(input("Enter the value "))#Suspicious code
  b=5
  c=b/a
  print("\n",c)
except:
  print("This is wrong")# Not suspicious code


list = [1,2,3,4,5]
for i in  list:
  print(i)

# Another block came that is finally, This will execuate always

try:
  a=int(input("Enter the value "))#Suspicious code
  b=5
  c=b/a
  print("\n",c)
except:
  print("This is wrong")# Not suspicious code
finally:
  print("This will execuate always") # Here we put that block of code that we have to execuate in any cost even if code fail use in network database


list = [1,2,3,4,5]
for i in  list:
  print(i)

  # ==========================================
# Day 12: Exception Handling in Python
# ==========================================

# ------------------------------------------
# 1. What is Exception Handling?
# ------------------------------------------
# Exception = Error that occurs during program execution.
# Exception Handling prevents the program from crashing.

print("===== Example 1: Basic try & except =====")

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("Invalid Input! Please enter a number.")


# ------------------------------------------
# 2. Handling Specific Exceptions
# ------------------------------------------

print("\n===== Example 2: Specific Exception =====")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter valid numbers!")


# ------------------------------------------
# 3. Multiple Exceptions
# ------------------------------------------

print("\n===== Example 3: Multiple Exceptions =====")

try:
    numbers = [10, 20, 30]

    index = int(input("Enter list index (0-2): "))
    print("Value =", numbers[index])

except IndexError:
    print("Index out of range!")

except ValueError:
    print("Please enter a valid integer!")


# ------------------------------------------
# 4. else Block
# ------------------------------------------
# else executes only when no exception occurs.

print("\n===== Example 4: else Block =====")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Division Successful")
    print("Result =", result)


# ------------------------------------------
# 5. finally Block
# ------------------------------------------
# finally always executes whether exception occurs or not.

print("\n===== Example 5: finally Block =====")

try:
    num = int(input("Enter a number: "))
    print("Number =", num)

except ValueError:
    print("Invalid Input!")

finally:
    print("This block always executes.")


# ------------------------------------------
# 6. else + finally Together
# ------------------------------------------

print("\n===== Example 6: else and finally Together =====")

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = x / y

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

else:
    print("Division Successful")
    print("Result =", result)

finally:
    print("Program execution completed.")


# ------------------------------------------
# 7. raise Statement
# ------------------------------------------
# raise is used to create custom exceptions.

print("\n===== Example 7: raise Statement =====")

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("You are eligible.")

except ValueError as e:
    print("Error:", e)


# ------------------------------------------
# 8. Custom Validation using raise
# ------------------------------------------

print("\n===== Example 8: Custom Validation =====")

password = input("Enter Password: ")

try:
    if len(password) < 8:
        raise Exception("Password must contain at least 8 characters.")

    print("Password Accepted")

except Exception as e:
    print("Error:", e)


# ------------------------------------------
# Summary
# ------------------------------------------

print("\n===== Summary =====")
print("1. try      -> Code that may cause error")
print("2. except   -> Handles the error")
print("3. else     -> Runs if no error occurs")
print("4. finally  -> Runs always")
print("5. raise    -> Creates custom exceptions")