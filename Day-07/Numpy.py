#First need to install library
# Library mean lines of code that already written
#!pip install numpy #Syntax

# step 2
import numpy as np

# Check version
print(np.__version__)

# Creating arrays
# types of data structure and container where we can store same types multiple value.
# Same we do in list but in list we can store multiple Data type value but when we apply numerical operator then it become heavy, it not efficient so we use Numpy

List1 = [1,2,3,4]
print(List1)

#Covert List into array

arr_list1 = np.array(List1)
print(arr_list1)

# we can see the difference its one dimentional array

#Know the data types
print(type(arr_list1))

# 2Dimention list

list1 = [1,3,4,3]
list2 = [4,5,2,5]

arr_list = np.array([list1,list2]) # here we put square bracket because we have 2Dimention array

print(arr_list) #2Dimention array

list1 = [1,3,4,3]
list2 = [4,5,2,5]
list3 = [5,6,4,3]

arr_list = np.array([[list1,list2,list3]]) # here we put square bracket because we have 2Dimention array

print(arr_list) #2Dimention array

print("Dimention of array is = ",arr_list.ndim)# To know the dimention of array

# Till now we know how we create array using list and types of array
# NOW
# numpy array attributes

arr1 = np.array([[1,2,3],[4,3,6]]) # Here we create an 2Dimention array , we put 2 [[parenthsis]]
print(arr1)

# Some operation
print("shape", arr1.shape) # it show row and coloum
print("Size",arr1.size) # Total Element in the array
print("Dimention",arr1.ndim) # which dimention array is
print("type",arr1.dtype)

# 1 Dimention array

arr = np.array([1,2,3,4])
print(arr)

print("shape",arr.shape) #(4,1) (row, coloum)
print("size",arr.size) #4
print("Dimention",arr.ndim) #1
print("dType",arr.dtype) #



# array initializing method

# we going to create an array with zero element

# Zero_array

zero_arr = np.zeros((2,3)) # here we give value like which types of array we need here we say 2 row and 3 coloum
print(zero_arr)

#Like same we creating ones array

one_arr = np.ones((3,4)) # here we pass 3 row and 4 coloum
print(one_arr)

# Full array : all elements are same based on given value

full_arr = np.full((3,2), 5)
print(full_arr)



# Identity Matrix : diagonal elements are ones and all other elements are zeros

id_arr = np.eye(5)
print(id_arr)



# empty array It generate the random value
print(np.empty(6)) #Here we pass our value of array



# evenly spaced array : elements are evenly spaced based on step value
print(np.arange(2,15,3))



# specific number of eqaully spaced values between a range : elements are equally spaced based on step value
print(np.linspace(1,10,6))



# random values array - float
r_arr = np.random.rand(3,2)
print(r_arr)



# random values array - int
int_arr = np.random.randint(4,200,(3,4))
print(int_arr)

