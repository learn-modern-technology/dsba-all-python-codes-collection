# =========================================================================================================
# Difference and Intersect in python NumPy

import numpy as np
n1=np.array([10,20,30,40,50,60])
n2=np.array([50,60,70,80,90])
n1minusn2 = np.setdiff1d(n1,n2)
print(n1minusn2)
intersect = np.intersect1d(n1,n2)
print(intersect)

# ==========================================================================================================
# Initialize NumPy Matrix with Zero
n4 = np.zeros((6,5))
print(n4) 

# ==========================================================================================================
# Initialize NumPy Matrix with Non-Zero Value
n5 = np.full(shape=(2,6),fill_value=29)
print(n5)

# To list the integers from 0 to 19.
n6 = np.arange(10,20)
print(n6)

# To list the integers from 0 to 50 in an increment of 5
n7 = np.arange(10,50,5)   ## 5 is skip value
print(n7)

# ==========================================================================================================
# To get 5 random integers from 1 to 100
n8 = np.random.randint(10,100,5)
print(n8)

# ==========================================================================================================
# NumPy Mathematical Operations

import numpy as np
n1=np.array([10,20,30,40,50,60])
n2=np.array([50,60,70,80,90,95])
result_sum = np.sum([n1,n2])
print("result_sum",result_sum)          
#Output: result_sum 655

result_sum_axis0 = np.sum([n1,n2],axis=0)
print("result_sum_axis0",result_sum_axis0)
#Output: result_sum_axis0 [ 60  80 100 120 140 155]

result_sum_axis1 = np.sum([n1,n2],axis=1)
print("result_sum_axis1",result_sum_axis1)
#Output: result_sum_axis1 [210 445]

# =============================================================================================================
n1=np.array([10,20,30,40,50,60])
n2=np.array([50,60,70,80,90,95])
result_basic_sum = n1 + 1
result_basic_mul = n2 * 5
result_basic_sub = n2 - 5
result_basic_div = n1 / 10
print("result_basic_sum",result_basic_sum)
print("result_basic_sum",result_basic_mul)
print("result_basic_sum",result_basic_sub)
print("result_basic_sum",result_basic_div)

#Output: result_basic_sum [11 21 31 41 51 61]
#Output: result_basic_sum [250 300 350 400 450 475]
#Output: result_basic_sum [45 55 65 75 85 90]
#Output: result_basic_sum [1. 2. 3. 4. 5. 6.]

import numpy as np
n2=np.array([50,60,70,80,90,95])
result_mean = np.mean(n2)
result_median = np.median(n2)
result_std = np.std(n2)
print("result_mean",result_mean)
print("result_median",result_median)
print("result_std",result_std)

#Output: result_mean 74.16666666666667
#Output: result_median 75.0
#Output: result_std 15.920810978785667

# ================================================================================================================