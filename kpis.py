import pandas as pd
from read_data import read_data

df = read_data()

number_sells = df["ORDER_COUNT"].sum()
total_revenue = df["REVENUE"].sum()

sorted_df = df.sort_values(by="REVENUE", ascending=False)

selected = sorted_df.head(10)

names = selected["CUSTOMER_NAME"]
revenues = selected["REVENUE"]

data = {'customer':names, 'revenue':revenues}
bigs = pd.DataFrame(data)

print(number_sells)
print(total_revenue)
print(big5)
