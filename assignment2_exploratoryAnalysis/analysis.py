import pandas as pd

data = pd.read_csv("data/Sales-Export_2019-2020.csv")

#clean the column names and fix the money column
data.columns = data.columns.str.strip()
data["order_value_EUR"] = data["order_value_EUR"].str.replace(",", "")
data["order_value_EUR"] = data["order_value_EUR"].astype(float)

#basic information
print(data.shape)
print(data.head())
print(data.dtypes)
print(data.isna().sum())

##check the numbers
print(data["order_value_EUR"].describe())
print(data["cost"].describe())