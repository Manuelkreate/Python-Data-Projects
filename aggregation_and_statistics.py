import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('index_1.csv')
print(df.columns.to_list())

# Convert 'money' column to NumPy array
money_array = df['money'].to_numpy()

# Aggregations
total_revenue = np.sum(money_array)
avg_transaction = np.mean(money_array)
max_transaction = np.max(money_array)
std_transaction = np.std(money_array)
median_transaction = np.median(money_array)
above_avg = money_array[money_array > avg_transaction]

print(f"Total revenue: {total_revenue}")
print(f"Average transaction: {avg_transaction}")
print(f"Max transaction: {max_transaction}")
print(f"Std deviation in spend: {std_transaction}")
print(f"Median transaction: {median_transaction}")

# Optional filters
print(f"Latte Order Values: {df[df['coffee_name'] == 'Latte']['money'].to_numpy()}")
print(f"Transactions above average: {above_avg}")
