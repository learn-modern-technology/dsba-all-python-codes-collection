import pandas as pd
import numpy as np
# ========================================================================================================
# Pandas Series 
# ================
# Pandas Series is a one-dimensional labeled array/list capable of holding data of any 
# type (integer, string, float, python objects, etc.).
# The labels are collectively called index.
# Pandas Series can be thought as a single column of an excel spreadsheet and each entry in a series 
# corresponds to an individual row in the spreadsheet

# =======================================================================================================
# creating a list of price of different medicines
med_price_list = [55,25,75,40,90]

# converting the med_price_list to an array 
med_price_arr = np.array(med_price_list)

# converting the list and array into a Pandas Series object  
series_list = pd.Series(med_price_list)
series_arr = pd.Series(med_price_arr)

# printing the converted series object
print(series_list)
print(series_arr)

# changing the index of a series
med_price_list_labeled = pd.Series(med_price_list, index = ['Omeprazole','Azithromycin','Metformin',
                                                            'Ibuprofen','Cetirizine'])
print(med_price_list_labeled)

# adding 2.5 to existing prices
med_price_list_labeled_updated = med_price_list_labeled + 2.5
med_price_list_labeled_updated

# A new price list was released by vendors for each medicine. Let's find the difference 
# between new price and the old price
new_price_list = [77, 45.5, 100, 50, 80]
new_price_list_labeled = pd.Series(new_price_list, index = ['Omeprazole','Azithromycin','Metformin','Ibuprofen','Cetirizine'])
print(new_price_list_labeled)

print('Difference between new price and old price - ')
print(new_price_list_labeled - med_price_list_labeled_updated)

# ===============================
# Accessing Pandas Series
# ===============================

# The revenue (in billion dollars) of different telecommunication operators in U.S. was collected for the 
# year of 2020. The following lists consist of the names of the telecommunication operators and their 
# respective revenue (in billion dollars).
operators = ['AT&T', 'Verizon', 'T-Mobile US', 'US Cellular']
revenue = [171.76, 128.29, 68.4, 4.04]

#creating a Series from lists
telecom = pd.Series(revenue, index=operators)
print('\nCreating a Series from lists - ',telecom)

# accessing the first element of series 
print('\nAccessing the first element of series -',telecom[0])

#  accessing firt 3 elements of a series
print('\nAccessing the first 3 element of series ',telecom[:3])

# accessing the last two elements of a series
print('\nAccessing the last two elements of a series-',telecom[-2:])

# accessing multiple elements of a series
print('\nAccessing multiple elements of a series -',telecom[[0,2,3]])

# Accessing Pandas Series using its labeled index
# accessing the revenue of AT&T
print('\nAccessing Pandas Series using its labeled index - ',telecom['AT&T'])

#  accessing firt 3 revenues of operators in the series
print('\nAccessing firt 3 revenues of operators in the series -',telecom[:'T-Mobile US'])

# ===================================================================================================
# Pandas DataFrame
# ================
# Pandas DataFrame is a two-dimensional tabular data structure with labeled axes (rows and columns)
# ===================================================================================================

# Creating a Pandas DataFrame using a list
student = ['Mary', 'Peter', 'Susan', 'Toby', 'Vishal']
df1 = pd.DataFrame(student,columns=['Student'])
print('\nStudents DataFrame-\n',df1.head())

# defining another list
grades = ['B-','A+','A-', 'B+', 'C']

# creating the dataframe using a dictionary
df2 = pd.DataFrame({'Student':student,'Grade':grades})
print('\nStudents Grades DataFrame-\n',df2.head())

# Creating a Pandas DataFrame using Series
# The data for total energy consumption for the U.S. was collected from 2012 - 2018. 
# Let's see how this data can be presented in form of data frame.

year = pd.Series([2012,2013,2014,2015,2016,2017,2018])
energy_consumption = pd.Series([2152,2196,2217,2194,2172,2180,2258])

df3 = pd.DataFrame({'Year':year,'Energy_Consumption(Mtoe)':energy_consumption})
print('\nEnergy Consumption DataFrame-\n',df3.head())

# For encryption purposes a web browser company wants to generate random values which have mean equal to 0 
# and variance equal to 1. They want 5 randomly generated numbers in 2 different trials.
# Creating a Pandas DataFrame using random values
df4 = pd.DataFrame(np.random.randn(5,2),columns = ['Trial 1', 'Trial 2'])
print('\n5 randomly generated numbers in DataFrame-\n',df4)

# =======================
# Accessing DataFrames
# ======================
# The data of the customers visiting 24/7 Stores from different locations was collected. 
# The data includes Customer ID, location of store, gender of the customer, type of product purchased, 
# quantity of products purchased, total bill amount. 
# Let's create the dataset and see how to access different entries of it.

# creating the dataframe using dictionary
store_data = pd.DataFrame({'CustomerID': ['CustID00','CustID01','CustID02','CustID03','CustID04']
                           ,'location': ['Chicago', 'Boston', 'Seattle', 'San Francisco', 'Austin']
                           ,'gender': ['M','M','F','M','F']
                           ,'type': ['Electronics','Food&Beverages','Food&Beverages','Medicine','Beauty']
                           ,'quantity':[1,3,4,2,1],'total_bill':[100,75,125,50,80]})
store_data
print('\nCustomer info in DataFrame-\n',store_data)

# accessing first row of the dataframe
store_data[:1]
print('\nAccessing first row of the DataFrame-\n',store_data[:1])

# accessing first column of the dataframe
print('\nAccessing first column of the DataFrame-\n',store_data['location'])

# accessing rows with the step size of 2
store_data[::2]
print('\nAccessing rows with the step size of 2 in a DataFrame-\n',store_data[::2])

# accessing the rows in reverse step
store_data[::-2]
print('\nAccessing rows in reverse step in a DataFrame-\n',store_data[::-2])

# =====================================================================================================

# ===============================
# Using loc and iloc method
# ===============================

# ===========
# loc method
# ===========
# loc is a method to access rows and columns on pandas objects. 
# When using the loc method on a dataframe, we specify which rows and which columns we want 
# by using the following format:
# dataframe.loc[row selection, column selection]

# DataFrame.loc[] method is a method that takes only index labels and returns row or dataframe 
# if the index label exists in the data frame.

# accessing first index value using loc method (indexing starts from 0 in python)
store_data.loc[1]
print('\nAccessing first index value using loc method in a DataFrame-\n',store_data.loc[1])


# Accessing selected rows and columns using loc method
print('\nAccessing selected rows and columns using loc method in a DataFrame-\n',store_data.loc[[1,4],['location','type']])

print(store_data.columns.values[:])


# =================
# iloc method
# =================

# The iloc indexer for Pandas Dataframe is used for integer location-based indexing/selection by position. 
# When using the loc method on a dataframe, we specify which rows and which columns we want by using the 
# following format:
# dataframe.iloc[row selection, column selection]

# accessing selected rows and columns using iloc method 
print('\nAccessing selected rows and columns using iloc method in a DataFrame-\n',store_data.iloc[[1,4],[0,2]])


# accessing all rows and columns using iloc method 
print('\nAccessing all rows and columns using iloc method in a DataFrame-\n',store_data.iloc[:,:])

# accessing select rows and all columns using iloc method 
print('\nAccessing selected rows and all columns using iloc method in a DataFrame-\n',store_data.iloc[1:4,:])

# accessing all rows and selected columns using iloc method 
print('\nAccessing all rows and selected columns usingi loc method in a DataFrame-\n',store_data.iloc[:,1:5])

# Modify entries of a dataframe using loc
store_data.loc[4,'type'] = 'Electronics'
print('\nAccessing all rows and columns using iloc method in a DataFrame-\n',store_data.iloc[:,:])

# Modify entries of a dataframe using iloc
store_data.iloc[4,3] = 'Beauty'
print('\nAccessing all rows and columns using iloc method in a DataFrame-\n',store_data.iloc[:,:])

# ===================================================================================================
# Condition based indexing
# Wherever the condition of greater than 1 is satisfied in quantity column, 'True' is returned. 
# Let's retrieve the original values wherever the condition is satisfied

# Wherever the condition is satisfied we get the original values, 
# and wherever the condition is not satisfied we do not get those records in the output.
print(store_data.loc[store_data['quantity']>1])

# =======================================================================================================

# Column addition and removal from a Pandas DataFrame

# ====================================
# Adding a new column in a DataFrame
# ====================================

# adding a new column in data frame store_data which is a rating (out of 5) given by customer based on their shopping experience
store_data['rating'] = [2,5,3,4,4]
print("\nDataFrame after adding a new column-\n", store_data.iloc[:,:])

# =====================================
# Removing a column from a DataFrame
# =====================================
store_data.drop('CustomerID',axis=1,inplace=True)
print("\nDataFrame after removing a column-\n", store_data.iloc[:,:])

# creating a copy of the existing data frame
new_store_data = store_data.copy()

# Removing more than one column
new_store_data.drop(['location','rating'],axis=1,inplace=True)
print("\nDataFrame after removing 2 columns-\n", new_store_data.iloc[:,:])

# Removing rows from DataFrame
new_store_data.drop(1,axis=0)
print("\nDataFrame after removing 1 row-\n", new_store_data.iloc[:,:])

# Notice that we used axis=0 to drop a row from a data frame, while we were using axis=1 
# for dropping a column from the data frame.

# Also, to make permanent changes to the data frame we will have to use inplace=True parameter.
# We also see that the index are not correct now as first row has been removed. 
# So, we will have to reset the index of the data frame. Let's see how this can be done.


# creating a new dataframe
store_data_new  = store_data.drop(1,axis=0)

# ===================================================
# Resetting Indexes
# ==================================================

# resetting the index of data frame
store_data_new.reset_index()

# We see that the index of the data frame is now resetted but the index has become a column in the data frame.
# We do not need the index to become a column so we can simply set the parameter drop=True in reset_index() 
# function

store_data_new.reset_index(drop=True,inplace=True)
store_data_new
print("\nDataFrame after resetting index-\n", store_data_new.iloc[:,:])

# =========================================================================================================
# Combining DataFrames - join, merge and concat
# =========================================================================================================
data1 = pd.DataFrame({'name': ['A', 'B', 'C', 'D'],
                      'math': [60,89,82,70],
                      'physics': [66,95,83,66],
                      'chemistry': [61,91,77,70]
                      })

data2 = pd.DataFrame({'name': ['E', 'F', 'G', 'H'],
                      'math': [66,95,83,66],
                      'physics': [60,89,82,70],
                      'chemistry': [90,81,78,90]
                      })

# By default, concat - concatenats vertically along the axis 0 and preserves all existing indices.
print('\nConcat of DataFrame-\n',pd.concat([data1, data2]))

# you can set the argument ignore_index=True. 
# Then, the resulting DataFrame index will be labeled with 0, …, n-1
print('\nConcat of DataFrame with ignore_index=True-\n',pd.concat([data1, data2],ignore_index=True))

# To concatenate DataFrames horizontally along the axis 1 , you can set the argument axis=1
print('\nConcat of DataFrame horizontally-\n',pd.concat([data1, data2],axis=1))

# Avoiding duplicate indices
try:
    print('\nConcat of DataFrame with Integrity Constraint Verification-\n'
          ,pd.concat([data1, data2],verify_integrity=True))
except ValueError as e:
    print('ValueError', e)
    

# Adding a hierarchical index with keys and names options
res = pd.concat([data1, data2],keys=['Year 1','Year 2'])
print('\nConcat of DataFrame by adding a hierarchical index with keys and names options-\n',res)

# To access a specific group of values, for example, Year 1:
print('\nConcatinated DataFrame - To access a specific group of value-\n',res.loc['Year 1'])

# Add name 'Class' to the outermost index we just created
res2 = pd.concat([data1, data2], keys=['Year 1', 'Year 2'], names=['Class', None])
print('\nConcatinated DataFrame-After adding name to the outermost index-\n',res2)

# To reset an index and turn it into a data column, you can use reset_index()
print('\nConcatinated DataFrame-After resetting Index-\n',res2.reset_index(level=1))
print('\nConcatinated DataFrame-After resetting Index-\n',res2.reset_index(level=0))

# Columns matching and sorting
# The concat() function is able to concatenate DataFrames with the columns in a different order.
# By default, the resulting DataFrame would have the same sorting as the first DataFrame.
# If you prefer the resulting DataFrame to be sorted alphabetically, you can set the argument sort=True

print('\nConcat of DataFrame and Sorting after concatenation-\n',pd.concat([data1, data2],sort=True))
print('\nConcat of DataFrame and Sorting after concatenation and resetting index-\n',
      pd.concat([data1, data2],sort=True,keys=['Year 1','Year 2'], names=['Class', None]).reset_index(level=0))

# If you prefer a custom sort, here is how to do it:
custom_sort = ['math', 'chemistry', 'physics', 'name','Class']
res3 = pd.concat([data1, data2],sort=True,keys=['Year 1','Year 2'], names=['Class', None]).reset_index(level=0)
print('\nCustomed Sorted DataFrame-\n',res3[custom_sort])

# ========================================================================================================
# Loading and concatenating datasets from a bunch of CSV files 
#
# https://towardsdatascience.com/pandas-concat-tricks-you-should-know-to-speed-up-your-data-analysis-cd3d4fdfe6dd
#
# ========================================================================================================
import pathlib2 as pl2
ps = pl2.Path('data/concatDemo')

dfs = (
    pd.read_csv(p, encoding='utf8') for p in ps.glob('*.csv')
)

result = pd.concat(dfs)
print('\nLoading and concatenating datasets from a bunch of CSV files-\n')
print(result.head())
print('\nShape of dataset-',result.shape)

# ============================================
# Merge and Join the datasets using Python
# ============================================
# ========================================================================================================
# “Merging” two datasets is the process of bringing two datasets together into one, 
# and aligning the rows from each based on common attributes or columns
# Let’s first understand the data sets used with the following explanation on each dataframe.
# 
# user_usage — A first dataset containing users monthly mobile usage statistics
# user_device — A second dataset containing details of an individual “use” of the system, 
#               with dates and device information
# android_device — A third dataset with device and manufacturer data, which lists all Android devices 
#                  and their model code
# ========================================================================================================

user_usage = pd.read_csv("data\\mergeDemo\\user_usage.csv")
user_device = pd.read_csv("data\\mergeDemo\\user_device.csv")
android_device = pd.read_csv("data\\mergeDemo\\android_device.csv")

print("\nUser Usage -\n",user_usage.head())
print("\nUser Device -\n",user_device.head())
print("\nAndroid Device -\n",android_device.head())

# Merge user_usage and user_device using LEFT JOIN and Userid
left_merge = pd.merge(user_usage, user_device, on='use_id', how='left')
print(f"\nDataframe after Merging using Left Join-\n\n{left_merge.head()}")

# Merge user_usage and user_device using RIGHT JOIN and Userid
right_merge = pd.merge(user_usage, user_device, on='use_id', how='right')
print(f"\nDataframe after Merging using Right Join-\n\n{right_merge.head()}")
print(f"\nDataframe after Merging using Right Join-\n\n{right_merge.tail()}")

# Merge user_usage and user_device using INNER JOIN and Userid
inner_merge = pd.merge(user_usage, user_device, on='use_id', how='inner')
print(f"\nDataframe after Merging using Right Join-\n\n{inner_merge.head()}")
print(f"\nDataframe after Merging using Right Join-\n\n{inner_merge.tail()}")

# Merge user_usage and user_device using OUTER JOIN and Userid
outer_merge = pd.merge(user_usage, user_device, on='use_id', how='outer')
print(f"\nDataframe after Merging using OUTER Join-\n\n{outer_merge.head()}")
print(f"\nDataframe after Merging using OUTER Join-\n\n{outer_merge.tail()}")