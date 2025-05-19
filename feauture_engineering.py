import pandas as pd
nutrition_df = pd.read_csv('Nutrition.csv')
print('Original Data: ')
print(nutrition_df)

df['IsHealthy'] = df['Calories']<200
df['PerBite'] = df['Calories']/5
