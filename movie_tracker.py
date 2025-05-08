import pandas as pd
#Pandas data cleaning
#Projet: Movie Review Tracker
pd.set_option("display.precision", 2)

#1. Initial data (with some issues for cleaning practice)
data = {
 "Title": ["Matrix", "Inception", None, "Joker", "Avengers", "Her", "Inception"], 
 "Genre": ["Action", "Action", "Comedy", "Drama", "Action", "Drama", "Action"],
 "ViewerAge": [22, 30, 19, 25, None, 21, 30],
 "Rating": [9, 8, 6, 9, 7, 8, 8]
}

#2. Create a DataFrame
df=pd.DataFrame(data)

#3. Initial Exploration
print('Original DataFrame:')
print(df)
print('\nDataFrame Info:')
print(df.info(data))
print('\nMissing values per column (Original):')
print(df.isnull().sum())
