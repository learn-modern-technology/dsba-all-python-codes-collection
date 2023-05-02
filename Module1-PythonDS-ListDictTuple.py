# =================================================================================================================
# List  ->
# Let's create a variable that will store all the brand names given in the above table. 
# This can be achieved using the 'list' data struture in Python.
# Lists are used to store the data items inside square brackets [] where each data item is separated by a comma (,)
# =================================================================================================================
brand_list = ['Apple', 'Samsung', 'LG', 'Motorola']
ram_list = [4, 12, 8, 8]
storage_list = [128, 128, 64, 128, 256, 512, 1024, 2048, 4096]
price_list = [900, 899, 600, 1000, 800, 105, 329, 415]
print('RAM List:', ram_list)
print('Storage List:', storage_list)
print('Price List:', price_list)

# Output:   RAM List: [4, 12, 8, 8]
# Output:   Storage List: [128, 128, 64, 128, 256, 512, 1024, 2048, 4096]
# Output:   Price List: [900, 899, 600, 1000, 800, 105, 329, 415]

# ================================================================================================================
# len() is an in-built function in Python that provides the count of elements inside a list.

len(price_list)
# Output: 8

# ================================================================================================================
# min() and max() are in-built functions in Python that calculates the minimum and maximum values among the items in a list (or some other data types)

# minimum price
min_price = min(price_list)
print('The minimum price is $' + str(min_price))
# maximum price
max_price = max(price_list)
print('The maximum price is $' + str(max_price))

# ================================================================================================================
# We can also select a range of indices to access more than 1 item. This can be done by using a colon (:) between # the start and stop index

# first three items in price_list
print(price_list[0:3])

# last item in brand_list
print(brand_list[-1])
print(brand_list[len(brand_list)-1])

# ===============================================================================================================
# The append() method adds a single item to an existing list.

print(brand_list)
# Output: ['Apple', 'Samsung', 'LG',]

brand_list[3] = 'HTC'
# Output: ['Apple', 'Samsung', 'LG', 'HTC']

brand_list.append('Motorola')
# Output: ['Apple', 'Samsung', 'LG', 'HTC', 'Motorola']

brand_list[2:4]
# Output: ['LG', 'HTC']

# ===============================================================================================================
# Dictionary-> 
# Lists are great for storing data for a single attribute. But, we might want to add more information about the
# items in a variable. Suppose the store wants to store the attributes brand, ram, storage, and price in a single
# variable.

dict_attribute = {
    'Brand': 'Apple',
    'RAM (in GB)':16, 
    'Storage (in GB)':128, 
    'Price (in $)':800
    }
print(dict_attribute)

# Output: {'Brand': 'Apple', 'RAM (in GB)': 16, 'Storage (in GB)': 128, 'Price (in $)': 800}


# extract information from dictionary
print(dict_attribute['Price (in $)'])

# Dictionary items are ordered, changeable, and does not allow duplicates.
dict_attribute['Price (in $)'] = 1050
print(dict_attribute)

# Output: {'Brand': 'Apple', 'RAM (in GB)': 16, 'Storage (in GB)': 128, 'Price (in $)': 1050}

# ===============================================================================================================
# The values in a dictionary can also be a list to store information for more than one product

# create a list of brand
brand_list = ['Apple', 'Samsung', 'LG', 'HTC']
ram_list = [16, 12, 8, 8]
storage_list = [128, 128, 64, 128]
price_list = [900, 100, 200, 1000]
print('Brand List - ',brand_list)
print('RAM List - ',ram_list)
print('Storage List - ',storage_list)
print('Price List - ',price_list)

product_dict = {
    'Brand': brand_list,
    'RAM (in GB)': ram_list,
    'Memory (in GB)': storage_list,
    'Price (in $)': price_list
}

print(product_dict)

# Output: {'Brand': ['Apple', 'Samsung', 'LG', 'HTC'], 'RAM (in GB)': [16, 12, 8, 8], 'Memory (in GB)': [128, 128, 64, 128], 'Price (in $)': [900, 100, 200, 1000]}

# ================================================================================================================
# keys() and values() are methods of a dictionary to extract the lists of dictionary keys and dictionary values respectively.

# Prints the keys of the Dictionaries
print(product_dict.keys())

product_keys = product_dict.keys()
print(product_keys)

# Output: dict_keys(['Brand', 'RAM (in GB)', 'Memory (in GB)', 'Price (in $)'])

product_values = product_dict.values()
print(product_values)

# Output: dict_values([['Apple', 'Samsung', 'LG', 'HTC'], [16, 12, 8, 8], [128, 128, 64, 128], [900, 100, 200, 1000]])

product_dict['Brand'][0]
# Output: Apple

product_dict['Memory (in GB)'][0]
# Output: 128

# To update dictionary
dict_test={1:"USA", 2:"India", 3:"China"}
dict_test.update({3:"Japan"})
print(dict_test)
# Output: {1: 'USA', 2: 'India', 3: 'Japan'}

# ================================================================================================================
# Tuple ->
# Now that you have learned about lists, you know that data can be modified and altered in a list, 
# making it a mutable data structure. Sometimes, you might want to store data which should not be altered, 
# for example storage. The storage in a mobile phone is in terms of powers of 2, that is, 32 GB, 64 GB, 128 GB, 
# etc. You do not want to alter the number 32 and change it to 30

storage = (32,64,128,256,512,1024)
print(storage)

# Output: (32, 64, 128, 256, 512, 1024)


# try changing an item in a tuple
storage[1]=60
# TypeError: 'tuple' object does not support item assignment
