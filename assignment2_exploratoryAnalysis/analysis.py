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

#total sales by country
print(data.groupby("country")["order_value_EUR"].sum())

#biggest and smallest orders
print(data[data[ "order_value_EUR"]==data["order_value_EUR"].max()])
print(data [data["order_value_EUR"]==data["order_value_EUR" ].min()]) 

#check if average order meets the goal
average_order = data["order_value_EUR"].mean()
if average_order >= 100000:
    print("average order is at least 100000")
else:
    print("average order is below 100000")

#quick summary
print("total orders:", len(data))
print("average order value:", average_order)
print("total revenue:", data["order_value_EUR"].sum())