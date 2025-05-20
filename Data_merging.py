import pandas as pd
customer_df = pd.read_csv('CustomerInfo.csv')
transaction_df = pd.read_csv('Transactions.csv')
print('---Original Customer Info Data---')
print(customer_df)
print ('\n---Original Transaction Data---')
print(transaction_df)

#merging
inner_merge = pd.merge(customer_df, transaction_df, on= 'CustomerID', how='inner')
left_merge = pd.merge(customer_df, transaction_df, on= 'CustomerID', how='left')
print('\n---Inner Merging of Data---')
print(inner_merge)
print('\n---Left Merging of Data---')
print(left_merge)

left_merge.to_csv('MergedCustomers.csv', index=False)