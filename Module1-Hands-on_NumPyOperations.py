# ===================
# NumPy Arrays
# ===================
# An array is a data structure that stores values of same data type.
# While python lists can contain values corresponding to different data types, arrays in python can only
# contain values corresponding to the same data type.
# However python lists fail to deliver the performance required while computing large sets of numerical data.
# To address this issue we use NumPy arrays.
# We can create NumPy arrays by converting a list to an array.
# ====================================================================================


# ipynb-py-convert Module1-BasicNumPyOperations.py Module1-BasicNumPyOperations.ipynb

# defining  list of different car companies or string elements
import numpy as np
brands_array = ['Mercedes', 'BMW', 'Audi', 'Ferrari', 'Tesla']
print("brands_array {}".format(brands_array))

# defining a list of no of cylinders
noofCylinder_array = [5, 4, 6, 7, 3]
print("noofCylinder_array {}".format(noofCylinder_array))

# converting the list arr_str to a NumPy array
np_brands_array = np.array(brands_array)
print("NumPy Array of Brands array is {}".format(np_brands_array))

# converting the list noofCylinder_array to a NumPy array
np_noofCylinder_array = np.array(noofCylinder_array)
print("NumPy Array of no of Cylinder is {}".format(np_noofCylinder_array))

print("The resuts look similar to a list but arr_str and arr_num have been converted to NumPy arrays. \
      Let's check the data type to confirm this.")

print("Data Type of brands_array is {}".format(type(brands_array)))
print("Data Type of noofCylinder_array is {}".format(type(noofCylinder_array)))
print("Data Type of np_brands_array is {}".format(type(np_brands_array)))
print("Data Type of np_noofCylinder_array is {}".format(type(np_noofCylinder_array)))

# ======================================================================================================
# Using np.arange() function
# ======================================================================================================
# 
# The np.arange() function returns an array with evenly spaced elements as per the interval. The interval mentioned is half-opened i.e. start is included but stop is excluded.
# It has the following paramaters:
#       start : start of interval range. By default start = 0
#       stop : end of interval range
#       step : step size of interval. By default step size = 1
# ====================================================================================
array1 = np.arange(stop = 7)
print("array1- ",array1)

array2 = np.arange(8,20)
print("array2- ",array2)

array3 = np.arange(8,20, 2)
print("array3- ",array3)

array4 = np.arange(start = 20, stop = 50, step = 5)
print("array4-",array4)

# =================================
# Using np.linspace() function
# ================================
# 
# The np.linspace() function returns numbers which are evenly distributed with respect to interval. Here the start and stop both are included.
# It has the following parameters:
#       start: start of interval range. By default start = 0
#       stop: end of interval range
#       num : No. of samples to generate. By default num = 50
# 
# ========================================
# How are these values getting generated?
# ========================================
# The step size or the difference between each element will be decided by the following formula:
# (stop - start) / (total elements - 1)
# So, in this case: (5 - 0) / 49 = 0.10204082
# The first value will be 0.10204082, the second value will be 0.10204082 + 0.10204082, 
# the third value will be 0.10204082 + 0.10204082 +0.10204082, and so on.
# =======================================================================================================
array5 = np.linspace(start = 10, stop = 20)
print("array5-", array5)
print("array5[19]- ",array5[19])

array6 = np.linspace(start = 20, stop=40)
print("array6-",array6)

array7 = np.linspace(20, 40, 10)
print("array7-",array7)
print("array7[4]-",array7[4])

# ========================================
# Arithmetic Operations on Arrays
# ========================================
l1 = [1,2,3]
l2 = [4,5,6]
# this is nothing but concatenation of two lists. It does not behave as you would expect!
print("l1+l2 = ",l1+l2)
print("l2+l1 = ",l2+l1)

# defining two arrays
var_array1 = np.arange(1,6)
print('Array 1:', var_array1)
var_array2 = np.arange(3,8)
print('Array 2:', var_array2)

print('Addition: ',var_array1+var_array2)
print('Subtraction: ',var_array1-var_array2)
print('Multiplication:' , var_array1*var_array2)
# the first element of array 1 is divided by first element of array 2
print('Division(float):', var_array2/var_array1)
print('Division(floor):', var_array2//var_array1)
print('Remainder:', var_array2%var_array1)
print('Inverse:', 1/var_array1)
print('Powers:', var_array1**var_array2)

# ===================================================================================
#    Accessing the entries of a Numpy Array
# ===================================================================================
rand_num = np.random.randint(10,50)
print("rand_num - ",rand_num)
np_array1 = np.random.randint(10,100,20)
print("np_array1 -",np_array1)

print("First Element of the Array -", np_array1[0])

print("5th to 10th Element of the Array -", np_array1[4:10])

print("Last 5 Element of the Array -", np_array1[-5:])

print("First 5 Element of the Array -", np_array1[0:5])

print("Array Elements greater than 50 are -", np_array1[np_array1>50])

print("Array Elements less than 30 are -", np_array1[np_array1<30])

# ===================================================================================
#    Modifying the entries of a Numpy Array
# ===================================================================================
print("np_array1-", np_array1)
# let's change some values in an array!
# changing the values of index value 3 and index value 4 to 5
np_array1[3:5] = -50
print("np_array1",np_array1)

# changing the values of index value 0 and index value 1 to 2 and 3 respectively
np_array1[0:2] = [-20,-50]
print("np_array1",np_array1)

# modify entries using logical references
np_array1[np_array1>0] = 65
print("np_array1",np_array1)
# ========================================================================================================
# Difference and Intersect in python NumPy
# ========================================================================================================
n1 = np.array([10, 20, 30, 40, 50, 60])
n2 = np.array([50, 60, 70, 80, 90])
n1minusn2 = np.setdiff1d(n1, n2)
print("n1minusn2-",n1minusn2)
intersect = np.intersect1d(n1, n2)
print("intersect-",intersect)

# ==========================================================================================================
# Initialize NumPy Matrix with Zero
n4 = np.zeros((6, 5))
print(n4)

# ==========================================================================================================
# Initialize NumPy Matrix with Non-Zero Value
n5 = np.full(shape=(2, 6), fill_value=29)
print(n5)

# To list the integers from 0 to 19.
n6 = np.arange(10, 20)
print(n6)

# To list the integers from 0 to 50 in an increment of 5
n7 = np.arange(10, 50, 5)  # 5 is skip value
print(n7)

# ==========================================================================================================
# To get 5 random integers from 1 to 100
n8 = np.random.randint(10, 100, 5)
print(n8)

# ==========================================================================================================
# NumPy Mathematical Operations

n1 = np.array([10, 20, 30, 40, 50, 60])
n2 = np.array([50, 60, 70, 80, 90, 95])
result_sum = np.sum([n1, n2])
print("result_sum", result_sum)
# Output: result_sum 655

result_sum_axis0 = np.sum([n1, n2], axis=0)
print("result_sum_axis0", result_sum_axis0)
# Output: result_sum_axis0 [ 60  80 100 120 140 155]

result_sum_axis1 = np.sum([n1, n2], axis=1)
print("result_sum_axis1", result_sum_axis1)
# Output: result_sum_axis1 [210 445]

# =============================================================================================================
n1 = np.array([10, 20, 30, 40, 50, 60])
n2 = np.array([50, 60, 70, 80, 90, 95])
result_basic_sum = n1 + 1
result_basic_mul = n2 * 5
result_basic_sub = n2 - 5
result_basic_div = n1 / 10
print("result_basic_sum", result_basic_sum)
print("result_basic_sum", result_basic_mul)
print("result_basic_sum", result_basic_sub)
print("result_basic_sum", result_basic_div)

# Output: result_basic_sum [11 21 31 41 51 61]
# Output: result_basic_sum [250 300 350 400 450 475]
# Output: result_basic_sum [45 55 65 75 85 90]
# Output: result_basic_sum [1. 2. 3. 4. 5. 6.]

n2 = np.array([50, 60, 70, 80, 90, 95])
result_mean = np.mean(n2)
result_median = np.median(n2)
result_std = np.std(n2)
print("result_mean", result_mean)
print("result_median", result_median)
print("result_std", result_std)

# Output: result_mean 74.16666666666667
# Output: result_median 75.0
# Output: result_std 15.920810978785667

# ================================================================================================================
