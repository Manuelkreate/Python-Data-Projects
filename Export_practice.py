import pandas as pd
pd.set_option('display.precision', 1)
df = pd.read_csv('Grouped_Summary.csv')

df.to_csv('CustomerData.csv', index=False)
df.to_excel('CustomerData.xlsx', index=False)
df.to_json('CustomerData.json', orient='records', indent=2)
df.to_csv('CustomerData.txt', sep='\t', index=False)