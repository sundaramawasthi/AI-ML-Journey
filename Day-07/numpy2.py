
#First need to install library
# Library mean lines of code that already written
#pip install numpy #Syntax

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

# Array Indexing and slicing

a=np.array([1,2,3,4,5,6,7,8,9,0])
print(a)

print(a[1:9:2]) # Step mean how much element we want to jump

print(a[0::3])

# Indexing in 2Dimention array

# Indexing on 2 Dimensional Array
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2)

# 2D Array: [rows, columns]                   # 2D Array takes 2 values - rows and columns for indexing
# 3D Array: [layers/height, rows, columns]    # 3D Array takes 3 values - height, rows and columns for indexing

print(arr2[0]) #first row print
print(arr2[1])# Secound row

print(arr2[0][0]) #First row and firts coloum
print(arr2[1][0]) # Secound row first coloum
print(arr2[1][2]) #Secound row last colum
print(arr2[0][2]) #Fist row last colum
print(arr2[:,1]) #It print the secound colum here



arr3 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr3)

# 3D Array: [layers/height, rows, columns]        # 3D Array takes 3 values - height, rows and columns for indexing

print(arr3[0]) #First row
print(arr3[1]) #2nd row
print(arr3[2]) #3rd row

print(arr3[0][2])
print(arr3[2][1])



print(arr3[:, 0]) # 1st col value
print(arr3[:, 1]) # 2nd col value
print(arr3[:, 2]) # 3rd col value



#here syntax is row colum slicing
print(arr3[::1,2])  #slicing on columns # here 2 tell how much jump we do, and next 2 tell the which row
print(arr3[::, 1:2]) #slicing on rows and columns

# Array reshaping and flattening
# Reshape Array: changing its dimensions (e.g., rows and columns) without altering the actual data
# Flatten Array: transforming a multi-dimensional array into a single-dimensional array

arr1 = np.array([1,2,3,4,5,6]) #5 row 1 coloum
print(arr1)

# Now for reshape

reshape = arr1.reshape((6,1)) #5 colum 1 row
print(reshape)

# again reshape
reshape2= arr1.reshape((2,3))
print(reshape2)

# to convert 2 dimention or multidimentional array into one dimention we use #flatten

print(reshape2.flatten())          # flattened array from higher (2D) dimensional (2,3) to (1,6) (1D)

#

# Array Stacking:  combining multiple arrays along a new axis, resulting in an array with a higher dimension than the input arrays
# Array Splitting:



# stacking
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b))) # vertical stacking - row wise          -> output array is 2D
print(np.hstack((a,b))) # horizontal stacking - column wise     -> output array is 1D



# splitting
c = np.array([[1,2,3], [4,5,6]])
print(c)



hsplit = np.hsplit(c,3) # horizontal split -> input and output array are same dimention

for s in hsplit:
    print(s)



vsplit = np.vsplit(c,2) # vertical split -> input and output array are same dimention

for s in vsplit:
    print(s)

#mathmatics operation in array

#Create an array

arr1= np.array([2,3,4,5])
print("Our array is =",arr1)


# Airthmatic operation
print("\n Our array after mathmatical operation\n")
print(arr1+10) # add a value in array (Here it add 10 in our whole array )
print(arr1-30) # subs a value in array
print(arr1*2) # multiply by a value in array
print(arr1/10) # divide by a value in array

# another array -

b = np.array([1,4,9])
print(b)

# Find square and sqaure root of whole array -

print(np.square(b)) # square of all array elements
print(np.sqrt(b))   # square root of all array elements

#Mathmatical opearation on multiple array

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a)
print(b)

#Airthmatic operation on multiple array

print(np.add(a,b))          # add two arrays
print(np.subtract(a,b))     # subtract two arrays
print(np.multiply(a,b))     # multiply two arrays
print(np.divide(a,b))       # divide two arrays



# Dot product: computes the inner product of the two vectors and sum the results, here we first multioly the product then do sum of it
print(np.dot(a,b)) # dot product



print(a.T) # Transpose: Returns an array with axes transposed, Transpose flip the element, it flip row element into colum and colum element into row

t = np.array([[1,7,3],
              [4,5,6]])

print(t)    # initial shape: 2,3
print(t.T)  # shape after transpose: 3,2

#Statical Function

a = np.array([[1,2,3], [4,5,6]])
print(a)

#For fidning the sum of all element, or finding mean median, min max

print(np.sum(a))    # sum of all elements of an array
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.min(a))
print(np.max(a))

#Array comparison

a = np.array([1,5,3])
b = np.array([4,5,6])
print(a)
print(b)

print(a == b) # comparing each elements of an array , compare element level
print(np.array_equal(a,b)) # comparing complete array that we given

#Broadcasting

# Broadcasting: is a mechanism that allows arithmetic operations to be performed on arrays of different shapes and sizes,
# it eliminates the need for explicit loops or reshaping operations, making code more concise, readable and efficient.

# Broadcasting Rules:
    # Compare shapes from right to left.
    # Dimensions must match or be 1.
    # If one array has fewer dimensions, pad its shape on the left with 1s.
    # Any dimension equal to 1 can stretch to match the other array.

#When we have higher and lower dimention array and we want to perform the operation then it compare this at element level and without affect data it perform operation
a = np.array([1,2,3,4])
b = np.array([5])
print(a+b)      # adding 1D with 0ne-element array to 1D with multi-element array, here it add arr[5] with all element of arr[a]

c = np.array([[1,2,3], [4,5,6]])
d = np.array([10,20,30])
print(c+d)      # adding 2D with 6-element array (2,3) to 1D with 6-element array

"""#### 12 Handling with nan value  #inf mean infinite value"""



data1 =  np.array([1,2, np.nan, 4, np.inf])
print(data1)

print(np.isnan(data1))  # check how many null value in our array, null value and returns boolean value

#if we want to replace null value with zero

print(np.nan_to_num(data1))    # replace non-finite values within an array with specified finite numbers

#Save and load array

arr = np.array([1,0,0,8])
print(arr)
np.save('my_array.npy', arr)

loaded_arr = np.load('my_array.npy')
print(loaded_arr)
