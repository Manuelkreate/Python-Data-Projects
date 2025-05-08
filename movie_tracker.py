import pandas as pd
pd.set_option("display.precision", 2)

data = {
	"Title": ["Matrix", "Inception", "Up", "Joker", "Avengers", "Her"], 
	"Genre": ["Action", "Action", "Comedy", "Drama", "Action", "Drama"],
  "ViewerAge": [22, 30, 19, 25, 27, 21],
  "Rating": [9, 8, 6, 9, 7, 8]
}
print("DataFrame Created from the Data")
df=pd.DataFrame(data)
print(df)

df["Liked"]=df["Rating"]>=7
print("\n")
print("A New Liked Column based on Rating (True if >=7)")
print(df)

print('\n')
print("Number of Reviews Grouped by Genre")
print(df.groupby("Genre")["Rating"].count())

print('\n')
print("Average Rating and Viewer Age Grouped by Genre")
print(df.groupby("Genre")[["Rating", "ViewerAge"]].mean())

print('\n')
print("Movies with Rating < 7")
print(df[df["Rating"]<7])

df.rename(columns={"Rating": "Score"}, inplace=True)
print("\n")
print("Renaming Rating into Score")
print(df)
