import pandas as pd
#Loading and Normalising
customer_trx = pd.read_csv('CustomerTransactions.csv')
print('Original Data: ')
print(customer_trx)
customer_trx['Name'] = customer_trx['Name'].str.lower().str.strip()
customer_trx['Email'] = customer_trx['Email'].str.lower().str.strip()

#Displaying duplicates
print('\nDuplicates from entire Data: ')
print(customer_trx[customer_trx.duplicated()])
print('Number of Duplicates: ', customer_trx.duplicated().sum())

#Flagging duplicates
print('\nDuplicates by Name+Email: ')
print(customer_trx[customer_trx.duplicated(subset=['Name', 'Email'], keep=False)])
customer_trx['dup'] = customer_trx.duplicated(subset=['CustomerID', 'Email'], keep=False)
print('\nFlagged Entries: ')
print(customer_trx)

#Dropping the 'dup' Column
customer_trx = customer_trx.drop(columns=['dup'])

#Grouping and summing
customer_trx = customer_trx.groupby(['CustomerID', 'Email'], as_index=False)['TransactionAmount'].sum()
print('\nCombined Data: ')
print(customer_trx)
print('\nFinal Cleaned Data: ')
customer_trx.drop_duplicates(inplace=True)
print(customer_trx)

customer_trx.to_csv('CustomerTransactions_Cleaned.csv')