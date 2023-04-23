# ============================================================================================================
# countplot to show the count of items ordered for each product_main_category

plt.figure(figsize=(15,7))
sns.countplot(data=ECom_Data, x='product_main_category');
plt.title("Product Category Type")
plt.xlabel("Product Main Category")
plt.ylabel("Count of Product Category")
plt.xticks(rotation = 90);
# ===========================================================================================================
# To find the product_main_category(s) for which maximum and minimum orders were placed
# Adjusting the scale to get clear comparison in the datasets

plt.figure(figsize=(15,7))
sns.countplot(data=ECom_Data, x='product_main_category');
plt.title("Product Category Type")
plt.xlabel("Product Main Category")
plt.ylabel("Count of Product Category")
plt.xticks(rotation = 90)
plt.yscale('log')
plt.show()

# ===========================================================================================================
# Boxplot for Retail Price in the datasets
plt.figure(figsize=(15,7))
sns.boxplot(data=ECom_Data, x='retail_price')
plt.title('Boxplot for Retail Price')
plt.xlabel("Retail Price");

# ===========================================================================================================
# scatterplot for retail_price (x-axis) and discounted_price (y-axis)
plt.figure(figsize=(15,7))
sns.scatterplot(data=ECom_Data, x='retail_price', y='discounted_price');
plt.title("Retail Price Vs Discounted Price")
plt.xlabel("Retail Price")
plt.ylabel("Discounted Price")
plt.show();

# ==============================================================================================================
# Pairplot for newly created 4 columns
plt.figure(figsize=(15,7))
sns.pairplot(brand_data[['Total no of orders','Total Retail Price','Total Discounted Price','Total Brand Revenue per Brand']]);
plt.show();

# ===========================================================================================================
## Creating Lineplot using Months and Revenue columns from the ECom_Data Series
plt.figure(figsize=(20,10))
sns.lineplot(data=ECom_Data, x='Months', y='revenue', hue='Region', markers='o', errorbar=None );
plt.title("Monthly Revenue for Regions")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.legend()
plt.xlim(0,14);