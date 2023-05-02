# ================================================================================================================
# Before jumping into the concept of looping, let's have a look at the range() function in Python.
# The range() method returns an immutable sequence of numbers between the given start integer to the stop integer.
#
# ================================================================================================================

print(list(range(0,36,4)))
# Output: [0, 4, 8, 12, 16, 20, 24, 28, 32]
# ================================================================================================================
# start the for loop
for i in range(5, 21, 5):
  # calculate the discount amount
  discount = price * (i / 100)
  # calculate the discounted price
  discounted_price = price - discount
  # print the discounted price
  print('The price after providing ', i, ' percent discount is $', discounted_price,sep='')
  print('The price after providing', i, 'percent discount is $', discounted_price)
  
#Output: The price after providing 5 percent discount is $855.0
#Output: The price after providing 5 percent discount is $ 855.0
#Output: The price after providing 10 percent discount is $810.0
#Output: The price after providing 10 percent discount is $ 810.0
#Output: The price after providing 15 percent discount is $765.0
#Output: The price after providing 15 percent discount is $ 765.0
#Output: The price after providing 20 percent discount is $720.0
#Output: The price after providing 20 percent discount is $ 720.0

# ===========================================================================================================
# store the price (in dollars) of the mobile in variable 'Price'.
Price = 900
# set the value of i to 5
i = 5
# start the while loop
while i <= 20:
  # calculate the discount amount
  discount = Price * (i / 100)
  # calculate the discounted price
  discounted_price = Price - discount
  # print the discounted price
  print('The price after providing ',i, ' percent discount is $', discounted_price,sep='')
  # increase the value of i by 5
  i += 5
  
# ===========================================================================================================
# One way of creating a discounted price list is by looping over the elements of price_list, subtracting the 
# discount from the price, and adding it one at a time to a new list discounted_price_list

discounted_price_list=[]
price_list = [900, 899, 600, 1000]
print('Price List:', price_list)

for x in price_list:
  discounted_price = x - (x*(5/100))
  discounted_price_list.append(discounted_price)

print(discounted_price_list)

#Output: Price List: [900, 899, 600, 1000]
#Output: [855.0, 854.05, 570.0, 950.0]

within_budget = []

for x in discounted_price_list:
  if x <= budget:
    within_budget.append('Yes')
  else:
    within_budget.append('No')

print(within_budget)

#Output: ['No', 'No', 'Yes', 'No']

# =============================================================================================================
# List Comprehensions

discounted_price_list = [x - (x*(5/100)) for x in price_list]
print(discounted_price_list)

# asking for customer's budget
budget = int(input('Enter your budget(in dollars): '))

# creating a list of Yes/No based on budget and discounted prices
within_budget = ['Yes' if x <= budget else 'No' for x in discounted_price_list]
print(within_budget)

#Output: Price List: [900, 899, 600, 1000]
#Output: [855.0, 854.05, 570.0, 950.0]
#Output: ['No', 'No', 'Yes', 'No']

# ==============================================================================================================
# 

# The if-else statement in Python can be used for decision-making
# Example: define the budget price
budget = int(input('Enter your budget(in dollars): '))
price = 500
# if-else statement
if price <= budget:
  print('Congrats! You can buy the Iphone')
else:
  print('Sorry! The mobile price is more than your budget')

#  A conditional statement to print the price based on the internal storage of the phone.  
Memory = int(input('Enter the memory: '))

if Memory == 32:
  print('The price of the phone is $600')
elif Memory == 64:
  print('The price of the phone is $700')
elif Memory ==128:
  print('The price of the phone is $900')
else:
  print('Please enter a valid memory requirement')