import pandas as pd
pd.set_option('display.precision', 2)
df = pd.read_csv('MergedCustomers.csv')
print('Original Data: ')
print(df)

#Grouping by region
print('\nTotal transaction amount by region: ')
print(df.groupby('Region')['TransactionAmount'].sum())
print('\nAverage Transaction by Region: ')
print(df.groupby('Region')['TransactionAmount'].mean())
print('\nNumber of Customers per Region: ')
print(df.groupby('Region')['CustomerID'].count())

#Grouping by name 
print('\nTotal transactions per person: ')
print(df.groupby('Name')['TransactionAmount'].count())

#Flagging customers
print('\nOutlining customers with 1 transaction: ')
trxn_count = df.groupby('Name')['TransactionAmount'].count()
df['SingleTransaction'] = df['Name'].map(trxn_count==1)
print(df)

df.to_csv('Grouped_Summary.csv', index=False)