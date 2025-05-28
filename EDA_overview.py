import pandas as pd

#load and inspect the data
df = pd.read_csv('WDI_Indicators_MainData.csv')

#basic info 
print(f'Shape: \n{df.shape}') #Rows, Columns
df.info() #Data types + non-null counts 
print(f'\nDescription: \n{df.describe()}') #summary stats for numerical columns (count, mean, std, etc.,)
print(f'\nColumn names: \n{df.columns}') #Column names
print(f'\nFirst 5 rows: \n{df.head(5)}') #First 5 rows 
print(f'\nLast 5 rows: \n{df.tail(5)}') #Last 5 rows 
print(f'\nSum of empty values per column: \n{df.isnull().sum()}')
print(f'\nNumber of fully duplicated rows: \n{df.duplicated().sum()}')

#aggregations
print(f"\nUnique countries: {df['Country Name'].nunique()}") #number of countries 
print(f"\nUnique years: {df['Time'].nunique()}") #number of years
print(df['Country Name'].value_counts().head(10)) #to count the number of appearances per each value
