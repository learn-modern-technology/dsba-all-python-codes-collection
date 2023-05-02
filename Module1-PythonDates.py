import pandas as pd
import numpy as np

# ==============================================
# Pandas - Date-time Functions
# ==============================================

# reading the StockData
data=pd.read_csv("data\datesDemo\StockData.csv")

print('\nData after loading into DataFrame-\n')
print(data.head())

print('\nDatatypes of all the columns in the DataFrame-\n')
print(data.info())

data['date']  = pd.to_datetime(data['date'],dayfirst=True)

print('\nDatatypes of all the columns after change-\n')
print(data.info())

print('\nData after changing the datatype of Date-\n')
print(data.head())

print("\nDateFormat 1-\n",data['date'].dt.strftime('%m/%d/%Y').head(10))

print("\nDateFormat 2-\n",data['date'].dt.strftime('%m-%d-%Y').head(10))

print("\nExtract Year from Dates -\n",data['date'].dt.year.head(10))

print("\nExtract Months from Dates -\n",data['date'].dt.month.head(10))

print("\nExtract Days from Dates -\n",data['date'].dt.day.head(10))