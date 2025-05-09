import pandas as pd
#Pandas Data Cleaning

pd.set_option('display.precision', 2)
#1. Initial Data (With some issues for cleaning practice)
data={
	'Title': ['Matrix', 'Inception', None, 'Joker', 'Avengers', 'Her', 'Inception'], #Added a None, and a duplicate
	'Genre': ['Action', 'Action', 'Comedy', 'Drama', 'Action', 'Drama', 'Action'],
	'ViewerAge': [22, 30, 19, 25, None, 21, 30], #Added a None
	'Rating': [9, 8, 6, 9, 7, 8, 8]
}

#2. Create DataFrame 
df=pd.DataFrame(data)

#3. Initial Exploration
print('\nOriginal DataFrame')
print(df)
print('\nDataFrame Info:')
print(df.info())
print('\nMissing values per column')
print(df.isnull().sum())

print('\n---Data Cleaning---')
#Handle missing values
#For Title: Fill any missing title with 'Unknown')
df['Title'].fillna('Unknown', inplace = True)
print('\nDataFrame after filling missing titles:')
print(df)

#For ViewerAge: Fill any missing age with mean age of the column
mean_age = df['ViewerAge'].mean()
df['ViewerAge'].fillna(mean_age, inplace = True)
print('\nDataFrame after filling missing Viewer Age with mean:')
print(df)

#Verify no more missing values in the column
print('\nMissing values after filling Title and Viewer Age ')
print(df[['Title', 'ViewerAge']].isnull().sum())

#5. Handle Duplicates
#Identify and print every duplicate rows (based on all columns)
print('\nIdentifying duplicate rows (True if duplicate):')
print(df.duplicated())
print(f'Number of duplicate rows: {df.duplicated().sum()}')

#Show the actual duplicate rows
print('\nDuplicate rows:')
print(df[df.duplicated(keep = False)]) #Keep=False shows all occurrences of duplicates

#Removing duplicate rows, keeping the first occurrence
df.drop_duplicates(inplace=True)
print('\nDataFrame after removing duplicates (keeping first):')
print(df)

#6. Verify cleaning 
print ('\n---Post-Cleaning Verification---')
print('\nCleaned DataFrame')
print(df)
print('\n Cleaned DataFrame Info:')
df.info()
print('\nMissing values per column (cleaned)')
print(df.isnull().sum())
print(f'\nNumber of duplicate rows after cleaning: {df.duplicated().sum()}')
