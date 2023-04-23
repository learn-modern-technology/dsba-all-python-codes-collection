# ============================================================================================================
# Function to get the price as an input, calculate the revenue based on Rule and return the calculated revenue
def calculate_revenue(final_price):
    if final_price > 600:
        return final_price*0.25
    elif final_price > 350 & final_price <=600:
        return final_price*0.15
    elif final_price > 100 & final_price <=350:
        return final_price*0.10
    else:
        return final_price*0.05

# ============================================================================================================
# To Create a column revenue using the function - calculate_revenue
ECom_Data['revenue'] = ECom_Data['discounted_price'].apply(calculate_revenue)

total_revenue = ECom_Data['discounted_price'].apply(calculate_revenue).sum()
total_revenue

# ============================================================================================================
# Created a new dataframe to include the Brand specific information
brand_data = pd.DataFrame({'Total no of orders':total_no_of_orders,
                          'Total Retail Price': total_retail_price,
                          'Total Discounted Price': total_discounted_price,
                          'Total Brand Revenue per Brand': total_brand_revenue_per_brand})

## Reseting the index and renaming the columns for clarity
brand_data.reset_index(inplace=True)
brand_data.rename(columns={'index':'Brand'}, inplace=True)
brand_data

# =============================================================================================================
# Since we need monthly revenue, first we will classify order_date column by creating a month column using below code
ECom_Data['Months']=pd.to_datetime(ECom_Data['Order_Date'],infer_datetime_format=True).dt.month
# ECom_Data['Year']=pd.to_datetime(ECom_Data['Order_Date'],infer_datetime_format=True).dt.year

# =============================================================================================================
# write the function
def display_iphone_attributes():
    '''
    This function displays
    the stored attributes of
    the Apple iPhone
    '''
    # store the price (in dollars) of the mobile in variable 'price'
    price = 900
    # store the RAM (in GB) of the mobile in variable 'ram'.
    ram = 4
    # store the internal storage (in GB) of the mobile in variable 'storage'.
    storage = 128
    # display the details
    print('The Apple iPhone has ', ram, ' GB RAM and ', storage, ' GB internal storage and it costs $', price, sep='')
    
# call the function
display_iphone_attributes()

# ==============================================================================================================
# write the function
def dis_price(discount):
    """
    This function takes the discount 
    percentage as input and 
    returns the discounted price of Apple iPhone
    """
    # store the price (in dollars) of the mobile in variable 'price'
    price = 900
    # calculate the price after discount
    discounted_price = price - price * (discount / 100)
    # return the discounted price
    return discounted_price

# call the function with discount = 10%
dp = dis_price(10)
dp

# ==============================================================================================================
# lambda functions
dis_price_lambda = lambda discount : 900 - ( 900 * (discount / 100) ) 

# call the function with discount = 10%
dis_price_lambda(10)