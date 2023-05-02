# %%
# importing the libraries
import numpy as np
import pandas as pd

# %%
"""
### 2.6 Pandas -  Series and DataFrames
"""

# %%
"""
**Pandas Series**
* Pandas Series is a one-dimensional labeled array/list capable of holding data of any type (integer, string, float, python objects, etc.). 
* The labels are collectively called index. 
* Pandas Series can be thought as a single column of an excel spreadsheet and each entry in a series corresponds to an individual row in the spreadsheet.
"""

# %%
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

# %%
"""
* We can see that the list and array have been converted to a Pandas Series object.
* We also see that the series has automatically got index labels. Let's see how these can be modified.
"""

# %%
# changing the index of a series
med_price_list_labeled = pd.Series(med_price_list, index = ['Omeprazole','Azithromycin','Metformin','Ibuprofen','Cetirizine'])
print(med_price_list_labeled)

# %%
"""
**Performing mathematical operations on Pandas Series**
"""

# %%
"""
* The price of each medicine was increased by $2.5. Let's add this to the existing price.
"""

# %%
# adding 2.5 to existing prices
med_price_list_labeled_updated = med_price_list_labeled + 2.5
med_price_list_labeled_updated

# %%
"""
* A new price list was released by vendors for each medicine. Let's find the difference between new price and the old price
"""

# %%
new_price_list = [77, 45.5, 100, 50, 80]
new_price_list_labeled = pd.Series(new_price_list, index = ['Omeprazole','Azithromycin','Metformin','Ibuprofen','Cetirizine'])
print(new_price_list_labeled)

# %%
print('Difference between new price and old price - ')
print(new_price_list_labeled - med_price_list_labeled_updated)

# %%
"""
**Pandas DataFrame**

Pandas DataFrame is a two-dimensional tabular data structure with labeled axes (rows and columns).
"""

# %%
"""
**Creating a Pandas DataFrame using a list**
"""

# %%
student = ['Mary', 'Peter', 'Susan', 'Toby', 'Vishal']
df1 = pd.DataFrame(student,columns=['Student'])
df1

# %%
"""
**Creating a Pandas DataFrame using a dictionary**
"""

# %%
# defining another list
grades = ['B-','A+','A-', 'B+', 'C']

# creating the dataframe using a dictionary
df2 = pd.DataFrame({'Student':student,'Grade':grades})
df2

# %%
"""
**Creating a Pandas DataFrame using Series**
"""

# %%
"""
The data for total energy consumption for the U.S. was collected from 2012 - 2018. Let's see how this data can be presented in form of data frame.
"""

# %%
year = pd.Series([2012,2013,2014,2015,2016,2017,2018])
energy_consumption = pd.Series([2152,2196,2217,2194,2172,2180,2258])

df3 = pd.DataFrame({'Year':year,'Energy_Consumption(Mtoe)':energy_consumption})
df3

# %%
"""
**Creating a Pandas DataFrame using random values**
"""

# %%
"""
For encryption purposes a web browser company wants to generate random values which have mean equal to 0 and variance equal to 1. They want 5 randomly generated numbers in 2 different trials.
"""

# %%
# we can create a new dataframe using random values 
df4 = pd.DataFrame(np.random.randn(5,2),columns = ['Trial 1', 'Trial 2'])
df4

# %%
"""
### 2.7 Pandas - Accessing and Modifying
"""

# %%
"""
**Accessing Series**
"""

# %%
"""
The revenue (in billion dollars) of different telecommunication operators in U.S. was collected for the year of 2020. The following lists consist of the names of the telecommunication operators and their respective revenue (in billion dollars).
"""

# %%
operators = ['AT&T', 'Verizon', 'T-Mobile US', 'US Cellular']
revenue = [171.76, 128.29, 68.4, 4.04]

#creating a Series from lists
telecom = pd.Series(revenue, index=operators)
telecom

# %%
"""
**Accessing Pandas Series using its index**
"""

# %%
# accessing the first element of series 
telecom[0]

# %%
#  accessing firt 3 elements of a series
telecom[:3]

# %%
# accessing the last two elements of a series
telecom[-2:]

# %%
# accessing multiple elements of a series
telecom[[0,2,3]]

# %%
"""
**Accessing Pandas Series using its labeled index**
"""

# %%
# accessing the revenue of AT&T
telecom['AT&T']

# %%
#  accessing firt 3 revenues of operators in the series
telecom[:'T-Mobile US']

# %%
# accessing multiple values
telecom[['AT&T','US Cellular','Verizon']]

# %%
"""
**Accessing DataFrames**
"""

# %%
"""
The data of the customers visiting 24/7 Stores from different locations was collected. The data includes Customer ID, location of store, gender of the customer,  type of product purchased, quantity of products purchased, total bill amount. Let's create the dataset and see how to access different entries of it.
"""

# %%
# creating the dataframe using dictionary
store_data = pd.DataFrame({'CustomerID': ['CustID00','CustID01','CustID02','CustID03','CustID04']
                           ,'location': ['Chicago', 'Boston', 'Seattle', 'San Francisco', 'Austin']
                           ,'gender': ['M','M','F','M','F']
                           ,'type': ['Electronics','Food&Beverages','Food&Beverages','Medicine','Beauty']
                           ,'quantity':[1,3,4,2,1],'total_bill':[100,75,125,50,80]})
store_data

# %%
# accessing first row of the dataframe
store_data[:1]

# %%
# accessing first column of the dataframe
store_data['location']

# %%
# accessing rows with the step size of 2
store_data[::2] 

# %%
# accessing the rows in reverse
store_data[::-2]

# %%
"""
**Using loc and iloc method**
"""

# %%
"""
**loc method**

* loc is a  method to access rows and columns on pandas objects. When using the loc method on a dataframe, we specify which rows and which columns we want by using the following format:

  * **dataframe.loc[row selection, column selection]**

* DataFrame.loc[] method is a method that takes **only index labels** and returns row or dataframe if the index label exists in the data frame.
"""

# %%
# accessing first index value using loc method (indexing starts from 0 in python)
store_data.loc[1]

# %%
"""
**Accessing selected rows and columns using loc method**
"""

# %%
# accessing 1st and 4th index values along with location and type columns 
store_data.loc[[1,4],['location','type']]

# %%
"""
**iloc method**

* The iloc indexer for Pandas Dataframe is used for **integer location-based** indexing/selection by position. When using the loc method on a dataframe, we specify which rows and which columns we want by using the following format:

  * **dataframe.iloc[row selection, column selection]**


"""

# %%
# accessing selected rows and columns using iloc method 
store_data.iloc[[1,4],[0,2]]

# %%
"""
**Difference between loc and iloc indexing methods**

* loc is label-based, which means that you have to specify rows and columns based on their row and column labels.
* iloc is integer position-based, so you have to specify rows and columns by their integer position values (0-based integer position).

"""

# %%
"""
If we use labels instead of index values in .iloc it will throw an error.
"""

# %%
# accessing selected rows and columns using iloc method 
store_data.iloc[[1,4],['location','type']]

# %%
"""
* As expected, .iloc has given error on using 'labels'.
"""

# %%


# %%
"""
We can modify entries of a dataframe using loc or iloc too
"""

# %%
print(store_data.loc[4,'type'])
store_data.loc[4,'type'] = 'Electronics'

# %%
store_data

# %%
store_data.iloc[4,3] = 'Beauty'
store_data

# %%
"""
**Condition based indexing**
"""

# %%
store_data['quantity']>1

# %%
"""
* Wherever the condition of greater than 1 is satisfied in quantity column, 'True' is returned. Let's retrieve the original values wherever the condition is satisfied.
"""

# %%
store_data.loc[store_data['quantity']>1]

# %%
"""
* Wherever the condition is satisfied we get the original values, and wherever the condition is not satisfied we do not get those records in the output.
"""

# %%
"""
**Column addition and removal from a Pandas DataFrame**
"""

# %%
"""
**Adding a new column in a DataFrame**
"""

# %%
store_data

# %%
# adding a new column in data frame store_data which is a rating (out of 5) given by customer based on their shopping experience
store_data['rating'] = [2,5,3,4,4]
store_data

# %%
"""
**Removing a column from a DataFrame**
"""

# %%
"""
* The CustomerID column is a unique identifier of each customer. This unique identifier will not help 24/7 Stores in getting useful insights about their customers. So, they have decided to remove this column from the data frame.
"""

# %%
store_data.drop('CustomerID',axis=1)

# %%
"""
* We sucessfully removed the 'CustomerID' from dataframe. But this change is not permanent in the dataframe, let's have a look at the store_data again.
"""

# %%
store_data

# %%
"""
* We see that store_data still has column 'CustomerID' in it. 
* To make permanent changes to a dataframe there are two methods will have to use a parameter `inplace` and set its value to `True`.
"""

# %%


# %%
store_data.drop('CustomerID',axis=1,inplace=True)
store_data

# %%
"""
* Now the column has been permanently removed from the dataframe.
"""

# %%
# we can also remove multiple columns simultaneously 
# it is always a good idea to store the new/updated data frames in new variables to avoid changes to the existing data frame

# creating a copy of the existing data frame
new_store_data = store_data.copy()
store_data

# %%
# dropping location and rating columns simultaneously
new_store_data.drop(['location','rating'],axis=1,inplace=True)
new_store_data

# %%
# lets check if store_data was impacted
store_data

# %%
"""
* There were no changes to data frame store_data.
"""

# %%
"""
* Deep copy stores copies of the object’s value.
* Shallow Copy stores the references of objects to the original memory address. 
"""

# %%
"""
**Removing rows from a dataframe**
"""

# %%
store_data.drop(1,axis=0)

# %%
store_data

# %%
"""
* Notice that we used **`axis=0`** to drop a row from a data frame, while we were using **`axis=1`** for dropping a column from the data frame.
* Also, to make permanent changes to the data frame we will have to use `inplace=True` parameter.
* We also see that the index are not correct now as first row has been removed. So, we will have to reset the index of the data frame. Let's see how this can be done.
"""

# %%
# creating a new dataframe
store_data_new  = store_data.drop(1,axis=0)
store_data_new

# %%
# resetting the index of data frame
store_data_new.reset_index()

# %%
"""
* We see that the index of the data frame is now resetted but the index has become a column in the data frame. We do not need the index to become a column so we can simply set the parameter **`drop=True`** in reset_index() function.
"""

# %%
# setting inplace = True to make the changes permanent
store_data_new.reset_index(drop=True,inplace=True)
store_data_new

# %%
"""
### 2.8 Pandas - Combining DataFrames
"""

# %%
"""
We will examine 3 methods for combining dataframes

1. concat
2. join
3. merge
"""

# %%
data_cust = pd.DataFrame({"customerID":['101','102','103','104'], 
                        'category': ['Medium','Medium','High','Low'],
                        'first_visit': ['yes','no','yes','yes'],
                        'sales': [123,52,214,663]},index=[0,1,2,3])

data_cust_new = pd.DataFrame({"customerID":['101','103','104','105'], 
                    'distance': [12,9,44,21],
                    'sales': [123,214,663,331]},index=[4,5,6,7])

# %%
data_cust

# %%
data_cust_new

# %%
pd.concat([data_cust,data_cust_new],axis=0)

# %%
pd.concat([data_cust,data_cust_new],axis=1)

# %%
"""
**Merge and Join**

* Merge combines dataframes using a column's values to identify common entries

* Join combines dataframes using the index to identify common entries
"""

# %%
pd.merge(data_cust,data_cust_new,how='outer',on='customerID') # outer merge is union of on

# %%
pd.merge(data_cust,data_cust_new,how='inner',on='customerID') # inner merge is intersection of on

# %%
pd.merge(data_cust,data_cust_new,how='right',on='customerID') 

# %%
data_quarters = pd.DataFrame({'Q1': [101,102,103],
                              'Q2': [201,202,203]},
                               index=['I0','I1','I2'])

data_quarters_new = pd.DataFrame({'Q3': [301,302,303],
                                  'Q4': [401,402,403]},
                               index=['I0','I2','I3'])

# %%
data_quarters

# %%
data_quarters_new

# %%
"""
* `join` behaves just like merge,  except instead of using the values of one of the columns to combine data frames, it uses the index labels
"""

# %%
data_quarters.join(data_quarters_new,how='right') # outer, inner, left, and right work the same as merge

# %%
"""
### 2.9 Pandas - Saving and Loading DataFrames
"""

# %%
"""
**Note**

In real-life scenario, we deal with much larger datasets that have thousands of rows and multiple columns. It will not be feasible for us to create datasets using multiple lists, especially if the number of columns and rows increases.

So, it is clear we need a more efficient way of handling the data simultaneously at the columns and row levels. In Python, we can import dataset from our local system, from links, or from databases and work on them directly instead of creating our own dataset.
"""

# %%
"""
**Loading a CSV file in Python**
"""

# %%
"""
**For Jupyter Notebook**
* When the data file and jupyter notebook are in the same folder.
"""

# %%
# Using pd.read_csv() function will work without any path if the notebook and dataset are in the folder

# data = pd.read_csv('StockData.csv')

# %%
"""
**For Google Colab with Google Drive**

First, we have to give google colab access to our google drive:
"""

# %%
from google.colab import drive
drive.mount('/content/drive')

# %%
"""
Once we have access we can load files from google drive using read_csv() function.
"""

# %%
path="/content/drive/MyDrive/Python Course/StockData.csv" 
data=pd.read_csv(path)

# %%
# head() function helps us to see the first 5 rows of the data
data.head()

# %%
"""
**Loading an excel file in Python**
"""

# %%
path_excel="/content/drive/MyDrive/Python Course/StockData.xlsx" 
data_excel = pd.read_excel(path_excel)

# %%
data_excel.head()

# %%
"""
**Saving a dataset in Python**
"""

# %%
"""
**Saving the dataset as a csv file**

To save a dataset as .csv file the syntax used is - 

**data.to_csv('name of the file.csv', index=False)**
"""

# %%


# %%
data.to_csv('/content/drive/MyDrive/Python Course/Saved_StockData.csv',index=False)

# %%
"""
* In jupyter notebook, the dataset will be saved in the folder where the jupyter notebook is located.
* We can also save the dataset to a desired folder by providing the path/location of the folder.
"""

# %%
"""
**Saving the dataset as an excel spreadsheet**

To save a dataset as .xlsx file the syntax used is - 

**data.to_excel('name of the file.xlsx',index=False)**
"""

# %%
data.to_excel('/content/drive/MyDrive/Python Course/Saved_StockData.xlsx',index=False)

# %%
"""
### 2.10 Pandas - Functions
"""

# %%


# %%
"""
**head() - to check the first 5 rows of the dataset**
"""

# %%
data.head()

# %%
"""
**tail() - to check the last 5 rows of the dataset**
"""

# %%
data.tail()

# %%
"""
**shape - to check the number of rows and columns in the dataset**
"""

# %%
data.shape

# %%
"""
* The dataset has 5036 rows and 3 columns. 
"""

# %%
"""
**info() - to check the data type of the columns**
"""

# %%
data.info()

# %%
"""
* The price column is numeric in nature while the stock and date columns are of object types.
"""

# %%
"""
**min() - to check the minimum value of a numeric column**
"""

# %%
data['price'].min()

# %%
"""
**max() - to check the maximum value of a numeric column**
"""

# %%
data['price'].max()

# %%
"""
**unique() - to check the number of unique values that are present in a column**
"""

# %%
data['stock'].unique()

# %%
"""
**value_counts() - to check the number of values that each unique quantity has in a column**
"""

# %%
data['stock'].value_counts()

# %%
"""
**value_counts(normalize=True) - using the `normalize` parameter and initializing it to True will return the relative frequencies of the unique values.** 
"""

# %%
data['stock'].value_counts(normalize=True)

# %%
"""
**Statistical Functions**
"""

# %%
"""
**mean() - to check the mean (average) value of the column**
"""

# %%
data['price'].mean()

# %%
"""
**median() - to check the median value of the column**
"""

# %%
data['price'].median()

# %%
"""
**mode() - to check the mode value of the column**
"""

# %%
data['stock'].mode()

# %%
"""
**To access a particular mode when the dataset has more than 1 mode**
"""

# %%
#to access the first mode 
data['price'].mode()[0]

# %%
"""
**Group By function**
* Pandas dataframe.groupby() function is used to split the data into groups based on some criteria.
"""

# %%
data.groupby(['stock'])['price'].mean()

# %%
"""
* Here the groupby function is used to split the data into the 4 stocks that are present in the dataset and then the mean price of each of the 4 stock is calculated.
"""

# %%
# similarly we can get the median price of each stock
data.groupby(['stock'])['price'].median()

# %%
"""
* Here the groupby function is used to split the data into the 4 stocks that are present in the dataset and then the median price of each of the 4 stock is calculated.
"""

# %%
"""
**Let's create a function to increase the price of the stock by 10%**
"""

# %%
def profit(s):
    return s + s*0.10 # increase of 10%

# %%
"""
**The Pandas apply() function lets you to manipulate columns and rows in a DataFrame.**
"""

# %%
data['price'].apply(profit)

# %%
"""
* We can now add this updated values in the dataset.
"""

# %%
data['new_price'] =data['price'].apply(profit)
data.head()

# %%
"""
**Pandas sort_values() function sorts a data frame in ascending or descending order of passed column.**
"""

# %%
data.sort_values(by='new_price',ascending=False) # by default ascending is set to True

# %%
"""
### 2.11 Pandas - Date-time Functions
"""

# %%
# reading the StockData
data=pd.read_csv("StockData.csv")

# %%
# checking the first 5 rows of the dataset
data.head()

# %%
# checking the data type of columns in the dataset
data.info()

# %%
"""
* We observe that the date column is of object type whereas it should be of date time data type.
"""

# %%
# converting the date column to datetime format
data['date']  = pd.to_datetime(data['date'],dayfirst=True)

# %%
data.info()

# %%
"""
* We observe that the date column has been converted to datetime format
"""

# %%
data.head()

# %%
"""
**The column 'date' is now in datetime format. Now we can change the format of the date to any other format** 
"""

# %%
data['date'].dt.strftime('%m/%d/%Y')

# %%
data['date'].dt.strftime('%m-%d-%y')

# %%
"""
**Extracting year from the date column**
"""

# %%
data['date'].dt.year

# %%
"""
Creating a new column and adding the extracted year values into the dataframe.
"""

# %%
data['year'] = data['date'].dt.year

# %%
"""
**Extracting month from the date column**
"""

# %%
data['date'].dt.month

# %%
"""
Creating a new column and adding the extracted month values into the dataframe.
"""

# %%
data['month'] = data['date'].dt.month

# %%
"""
**Extracting day from the date column**
"""

# %%
data['date'].dt.day

# %%
"""
Creating a new column and adding the extracted day values into the dataframe.
"""

# %%
data['day'] = data['date'].dt.day

# %%
data.head()

# %%
"""
* We can see that year, month, and day columns have been added in the dataset.
"""

# %%
# The datetime format is convenient for many tasks!
data['date'][1]-data['date'][0]

# %%
"""
###  Merge and Join the datasets using Python

###  “Merging” two datasets is the process of bringing two datasets together into one, and aligning the rows from each based on common attributes or columns
###  Let’s first understand the data sets used with the following explanation on each dataframe.

### user_usage — A first dataset containing users monthly mobile usage statistics
### user_device — A second dataset containing details of an individual “use” of the system, with dates and device information
### android_device — A third dataset with device and manufacturer data, which lists all Android devices and their model code
"""

# %%
user_usage = pd.read_csv("data\\mergeDemo\\user_usage.csv")
user_device = pd.read_csv("data\\mergeDemo\\user_device.csv")
android_device = pd.read_csv("data\\mergeDemo\\android_device.csv")

# %%
user_usage.head()

# %%
user_device.head()

# %%
android_device.head()

# %%
left_merge = pd.merge(user_usage, user_device, on='use_id', how='left')

# %%
left_merge.head()

# %%
left_merge.tail()

# %%
right_merge = pd.merge(user_usage, user_device, on='use_id', how='right')
right_merge.head()

# %%
right_merge.tail()

# %%
inner_merge = pd.merge(user_usage, user_device, on='use_id', how='inner')
inner_merge.head()

# %%
inner_merge.tail()

# %%
outer_merge = pd.merge(user_usage, user_device, on='use_id', how='outer')
outer_merge.head()

# %%
outer_merge.tail()

# %%
left_merge.shape

# %%
right_merge.shape

# %%
inner_merge.shape

# %%
outer_merge.shape