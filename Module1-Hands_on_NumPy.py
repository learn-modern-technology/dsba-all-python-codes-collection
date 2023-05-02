# %%
# The first step of using numpy is to tell python to import it
import numpy as np

# %%
"""
### 2.1 NumPy Arrays
"""

# %%
"""
**NumPy Array**
* An array is a data structure that stores values of same data type.
* While python lists can contain values corresponding to different data types, arrays in python can only contain values corresponding to the same data type. 
* However python lists fail to deliver the performance required while computing large sets of numerical data. To address this issue we use NumPy arrays.
* We can create NumPy arrays by converting a list to an array.

"""

# %%
# defining a list of different car companies or string elements
arr_str = ['Mercedes', 'BMW', 'Audi', 'Ferrari', 'Tesla']

# defining a list of number of cylinders in car or numerical elements
arr_num = [5, 4, 6, 7, 3]

# %%
# connverting the list arr_str to a NumPy array
np_arr_str = np.array(arr_str)


# connverting the list arr_num to a NumPy array
np_arr_num = np.array(arr_num)

# checking the output
print('Numpy Array (arr_str): ',np_arr_str)
print('Numpy Array (arr_num): ',np_arr_num)

# %%
"""
The resuts look similar to a list but arr_str and arr_num have been converted to NumPy arrays. Let's check the data type to confirm this.
"""

# %%
# printing the data type of lists
print('Data type of arr_str: ',type(arr_str))
print('Data type of arr_num: ',type(arr_num))

# printing the data type after conversion of lists to array
print('Data type of np_arr_str: ',type(np_arr_str))
print('Data type of np_arr_num: ',type(np_arr_num))

# %%
"""
* The above output confirms that both the lists were successfully converted to arrays
"""

# %%
"""
**NumPy Matrix**
"""

# %%
"""
* A matrix is a two-dimensional data structure where elements are arranged into rows and columns.
* A matrix can be created by using list of lists
"""

# %%
# let's say we have information of different number of cylinders in a car and we want to display them in a matrix format
matrix = np.array([[1,2,1],[4,5,9],[1,8,9]])
print(matrix)

# %%
print('Data type of matrix: ',type(matrix))

# %%
"""
* We see that all the NumPy objects have data type as ndarray
"""

# %%
"""
### 2.2 NumPy Functions
"""

# %%
"""
**There are different ways to create NumPy arrays using the functions available in NumPy library**
"""

# %%
"""
**Using np.arange() function**
* The np.arange() function returns an array with evenly spaced elements as per the interval. The interval mentioned is half-opened i.e. start is included but stop is excluded.
* It has the following paramaters:
  * start : start of interval range. By default start = 0
  * stop  : end of interval range
  * step  : step size of interval. By default step size = 1
"""

# %%
arr2  = np.arange(start = 0, stop = 10) # 10 will be excluded from the output
print(arr2)

# or

arr2  = np.arange(0,10) 
print(arr2)

# %%
# adding a step size of 5 to create an array
arr3  = np.arange(start = 0, stop = 20, step = 5)
arr3

# %%
"""
**Using np.linspace() function**
* The np.linspace() function returns numbers which are evenly distributed with respect to interval. Here the start and stop both are included.            
*It has the following parameters:              
 * start: start of interval range. By default start = 0
 * stop: end of interval range
 * num : No. of samples to generate. By default num = 50
"""

# %%
matrix2 = np.linspace(0,5) # by default 50 evenly spaced values will be generated between 0 and 5
matrix2

# %%
"""
**How are these values getting generated?**

The step size or the difference between each element will be decided by the following formula:

**(stop - start) / (total elements - 1)**

So, in this case:
(5 - 0) / 49 = 0.10204082

The first value will be 0.10204082, the second value will be 0.10204082 + 0.10204082, the third value will be 0.10204082 + 0.10204082 +0.10204082, and so on.
"""

# %%
# generating 10 evenly spaced values between 10 and 20
matrix3 = np.linspace(10,20,10)
matrix3

# %%
"""
**Similarly we can create matrices using the functions available in NumPy library**
"""

# %%
"""
**Using np.zeros()**
 
* The np.zeros() is a function for creating a matrix and performing matrix operations in NumPy. 
* It returns a matrix filled with zeros of the given shape. 
* It has the following parameters:    
  * shape : Number of rows and columns in the output matrix.
  * dtype: data type of the elements in the matrix, by default the value is set to `float`.
"""

# %%
matrix4 = np.zeros([3,5])
matrix4

# %%
"""
**Using np.ones()**

* The np.ones() is another function for creating a matrix and performing matrix operations in NumPy. 
* It returns a matrix of given shape and type, filled with ones.
* It has the following parameters:  
  * shape : Number of rows and columns in the output matrix.
  * dtype: data type of the elements in the matrix, by default the value is set to `float`.
"""

# %%
matrix5 = np.ones([3,5])
matrix5

# %%
"""
**Using np.eye()**
* The np.eye() is a function for creating a matrix and performing matrix operations in NumPy. 
* It returns a matrix with ones on the diagonal and zeros elsewhere. 
* It has the following parameters:
  * n: Number of rows and columns in the output matrix 
  * dtype: data type of the elements in the matrix, by default the value is set to `float`.
"""

# %%
matrix6 = np.eye(5)
matrix6

# %%
"""
**We can also convert a one dimension array to a matrix. This can be done by using the np.reshape() function.**
"""

# %%
"""
* The shape of an array basically tells the number of elements and dimensions of the array. Reshaping a Numpy array simply means changing the shape of the given array. 
* By reshaping an array we can add or remove dimensions or change number of elements in each dimension. 
* In order to reshape a NumPy array, we use the reshape method with the given array. 
* **Syntax:** array.reshape(shape) 
  * shape: a tuple given as input, the values in tuple will be the new shape of the array.
"""

# %%
# defining an array with values 0 to 9
arr4 = np.arange(0,10) 
arr4

# %%
# reshaping the array arr4 to a 2 x 5 matrix
arr4_reshaped = arr4.reshape((2,5))
arr4_reshaped

# %%
arr4

# %%
# reshaping the array arr4 to a 2 x 6 matrix
arr4.reshape((2,6))

# %%
"""
* This did not work because we have 10 elements which we are trying to fit in a 2 X 6 shape which will require 12 elements.
"""

# %%
"""
**NumPy can also perform a large number of different mathematical operations and it provides different functions to do so.**

NumPy provides:
1. Trigonometric functions 
2. Exponents and Logarithmic functions
3. Functions for arithmetic operations between arrays and matrices
"""

# %%
"""
**Trigonometric functions**
"""

# %%
print('Sine Function:',np.sin(4))
print('Cosine Function:',np.cos(4))
print('Tan Function',np.tan(4))

# %%
"""
**Exponents and Logarithmic functions**
"""

# %%
"""
* Exponents
"""

# %%
np.exp(2)

# %%
arr5 = np.array([2,4,6])
np.exp(arr5)

# %%
"""
* Logarithms
"""

# %%
# by default NumPy takes the base of log as e
np.log(2)

# %%
np.log(arr5)

# %%
## log with base 10
np.log10(8) 

# %%
"""
**Arithmetic Operations on arrays**
"""

# %%
# arithmetic on lists

l1 = [1,2,3]
l2 = [4,5,6]
print(l1+l2)
# this does not behave as you would expect!


# %%
# we can +-*/ arrays together

# defining two arrays
arr7 = np.arange(1,6)
print('arr7:', arr7)

arr8 = np.arange(3,8)
print('arr8:', arr8)

# %%
print('Addition: ',arr7+arr8)
print('Subtraction: ',arr8-arr7)
print('Multiplication:' , arr7*arr8)
print('Division:', arr7/arr8)
print('Inverse:', 1/arr7)
print('Powers:', arr7**arr8) # in python, powers are achieved using **, NOT ^!!! ^ does something completely different!


# %%
"""
**Operations on Matrices**
"""

# %%
matrix7 = np.arange(1,10).reshape(3,3)
print(matrix7)

matrix8 = np.eye(3)
print(matrix8)

# %%
print('Addition: \n', matrix7+matrix8)
print('Subtraction: \n ', matrix7-matrix8)
print('Multiplication: \n', matrix7*matrix8)
print('Division: \n', matrix7/matrix8)

# %%
"""
* RuntimeWarning: Errors which occur during program execution(run-time) after successful compilation are called run-time errors. 
* One of the most common run-time error is division by zero also known as Division error. 
* Due to division by zero error, we are getting inf (infinity) values because 1/0 is not a defined operation.
"""

# %%
"""
**Linear algebra matrix multiplication**
"""

# %%
matrix9 = np.arange(1,10).reshape(3,3)
print('First Matrix: \n',matrix9)

matrix10 = np.arange(11,20).reshape(3,3)
print('Second Matrix: \n',matrix10)
print('')
# taking linear algebra matrix multiplication (some may have heard this called the dot product)
print('Multiplication: \n', matrix9 @ matrix10)

# %%
"""
**Transpose of a matrix**
"""

# %%
print(matrix9)

# %%
# taking transpose of matrix
np.transpose(matrix9)

# %%
# another way of taking a transpose
matrix9.T

# %%
"""
**Function to find minimum and maximum values**
"""

# %%
print(matrix9)

# %%
print('Minimum value: ',np.min(matrix9))

# %%
print('Maximum value: ',np.max(matrix9))

# %%
"""
**Function to generate random samples**
"""

# %%
"""
**Using np.random.rand function**

* The np.random.rand returns a random NumPy array whose element(s) are drawn randomly from the normal distribution over [0,1). (including 0 but excluding 1). 
* **Syntax** - np.random.rand(d0,d1)
  * d0,d1 – It represents the dimension of the required array given as int, where d1 is optional. 
"""

# %%
# Generating random values in an array
rand_mat = np.random.rand(5)
print(rand_mat)

# %%
# * Generating random values in a matrix
rand_mat = np.random.rand(5,5) # uniform random variable
print(rand_mat)

# %%
"""
**Using np.random.randn function**

* The np.random.randn returns a random numpy array whose sample(s) are drawn randomly from the standard normal distribution (Mean as 0 and standard deviation as 1)

* **Syntax** - np.random.randn(d0,d1)
  * d0,d1 – It represents the dimension of the output, where d1 is optional.
"""

# %%
# Generating random values in an array
rand_mat2 = np.random.randn(5) 
print(rand_mat2)

# %%
# Generating random values in a matrix
rand_mat2 = np.random.randn(5,5) 
print(rand_mat2)

# %%
# Let's check the mean and standard deviation of rand_mat2
print('Mean:',np.mean(rand_mat2))
print('Standard Deviation:',np.std(rand_mat2))

# %%
"""
*  We observe that the mean is very close to 0 and standard deviation is very close to 1.
"""

# %%
"""
**Using np.random.randint function**

* The np.random.randint returns a random numpy array whose element(s) are drawn randomly from low (inclusive) to the high (exclusive) range. 

* **Syntax** - np.random.randint(low, high, size) 

  * low – It represents the lowest inclusive bound of the distribution from where the sample can be drawn.
  * high – It represents the upper exclusive bound of the distribution from where the sample can be drawn. 
  * size – It represents the shape of the output. 
"""

# %%
# Generating random values in an array
rand_mat3 = np.random.randint(1,5,10)
print(rand_mat3)

# %%
# Generating random values in a matrix
rand_mat3 = np.random.randint(1,10,[5,5])
print(rand_mat3)

# %%
"""
### 2.3 Accessing the entries of a Numpy Array
"""

# %%
# let's generate an array with 10 random values
rand_arr = np.random.randn(10)
print(rand_arr)

# %%
"""
* Accessing one element from an array
"""

# %%
# accessing the 6 th entry of rand_arr
print(rand_arr[6])

# %%
"""
* Accessing multiple elements from an array
"""

# %%
# we can access multiple entries at once using
print(rand_arr[4:9])

# %%
# we can also access multiple non-consecutive entries using np.arange
print('Index of values to access: ',np.arange(3,10,3))
print(rand_arr[np.arange(3,10,3)])

# %%
"""
**Accessing arrays using logical operations**
"""

# %%
print(rand_arr)

# %%
rand_arr>0

# %%
# accessing all the values of rand_arr which are greater than 0
print('Values greater than 0: ',rand_arr[rand_arr>0])

# accessing all the values of rand_arr which are less than 0
print('Values less than 0: ',rand_arr[rand_arr<0])

# %%
"""
**Accessing the entries of a Matrix**
"""

# %%
# let's generate an array with 10 random values
rand_mat = np.random.randn(5,5)
print(rand_mat)

# %%
# acessing the second row of the rand_mat
rand_mat[1]

# %%
# acessing third element of the second row
print(rand_mat[1][2])

#or 

print(rand_mat[1,2])

# %%
# accessing first two rows with second and third column 
print(rand_mat[0:2,1:3])

# %%
"""
**Accessing matrices using logical operations**
"""

# %%
print(rand_mat)

# %%
# accessing all the values of rand_mat which are greater than 0
print('Values greater than 0: \n ',rand_mat[rand_mat>0])

# accessing all the values of rand_mat which are less than 0
print('Values less than 0: \n',rand_mat[rand_mat<0])

# %%
"""
**Modifying the entries of an Array**
"""

# %%
print(rand_arr)


# %%
# let's change some values in an array!
# changing the values of index value 3 and index value 4 to 5
rand_arr[3:5] = 5
print(rand_arr)

# %%
# changing the values of index value 0 and index value 1 to 2 and 3 respectively
rand_arr[0:2] = [2,3]
print(rand_arr)

# %%
# modify entries using logical references
rand_arr[rand_arr>0] = 65
rand_arr

# %%
"""
**Modifying the entries of a Matrix**
"""

# %%
print(rand_mat3)

# %%
# changing the values of the 4th and 5th element of the second and third rows of the matrix to 0
print('Matrix before modification: \n',rand_mat3)
rand_mat3[1:3,3:5] = 0
print('Matrix after modification: \n',rand_mat3)

# %%
# extracting the first 2 rows and first 3 columns from the matrix
sub_mat = rand_mat[0:2,0:3]
print(sub_mat)

# %%
# changing all the values of the extracted matrix to 3
sub_mat[:] = 3
print(sub_mat)

# %%
# what happened to rand_mat when we change sub_mat?
rand_mat

# %%
# to prevent this behavior we need to use the .copy() method when we assign sub_mat
# this behavior is the source of MANY errors for early python users!!!

rand_mat = np.random.randn(5,5)
print(rand_mat)
sub_mat = rand_mat[0:2,0:3].copy()
sub_mat[:] = 3
print(sub_mat)
print(rand_mat)

# %%
"""
### 2.4 Saving and Loading a NumPy array
"""

# %%
"""
**Let's save some NumPy objects on the disk for use later!**
"""

# %%
from google.colab import drive
drive.mount('/content/drive')

# %%
# creating a random matrices
randint_matrix1 = np.random.randint(1,10,10).reshape(2,5)
print(randint_matrix1)
print('')
randint_matrix2 = np.random.randint(10,20,10).reshape(2,5)
print(randint_matrix2)

# %%
"""
**Using np.save() function**
"""

# %%
np.save('/content/drive/MyDrive/Python Course/saved_file_name',randint_matrix1)

# %%
"""
**Using np.savez() function**
"""

# %%
np.savez('/content/drive/MyDrive/Python Course/multiple_files',randint_matrix1=randint_matrix1,randint_matrix2=randint_matrix2)

# %%
"""
* The files will be saved in the directory where the Jupyter Notebook is located.
* With np.save() function, we can save an array/matrix to a NumPy .npy format.
* np.savez() function has an advantage over np.save() function because with np.savez(), we can store several arrays/matrices into a single file in uncompressed .npz format.
"""

# %%
# now let's load it
loaded_arr = np.load('/content/drive/MyDrive/Python Course/saved_file_name.npy')
loaded_multi = np.load('/content/drive/MyDrive/Python Course/multiple_files.npz')

print(loaded_arr)
print('')
print(loaded_multi)

# %%
"""
* We see that .npy file has been loaded but the .npz file is returning a memory location.
* Let's see how to load the values stored in .npz file.
"""

# %%
print('1st Matrix: \n',loaded_multi['randint_matrix1'])
print('2nd Matrix: \n',loaded_multi['randint_matrix2'])

new_matrix  = loaded_multi['randint_matrix1']
print('New Matrix: \n',new_matrix)

# %%
# we can also save/load text files...but only single variables
np.savetxt('/content/drive/MyDrive/Python Course/text_file_name.txt',randint_matrix1,delimiter=',')
rand_mat_txt = np.loadtxt('/content/drive/MyDrive/Python Course/text_file_name.txt',delimiter=',')
print(randint_matrix1)
print('')
print(rand_mat_txt)

# %%
