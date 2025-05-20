import pandas as pd
nutrition_df = pd.read_csv('Nutrition.csv')
print('Original Data: ')
print(nutrition_df)

nutrition_df['IsHealthy'] = nutrition_df['Calories']<200
nutrition_df['PerBite'] = nutrition_df['Calories']/5
category_map = {'Snack':0, 'Dairy':1, 'Breakfast':2, 'Drink':3, 'Fruit':4, 'Lunch':5}
nutrition_df['CategoryCode'] = nutrition_df['Category'].map(category_map)
print('\nEngineered Data;')
print(nutrition_df)

nutrition_df.to_csv('Nutrition_Featured.csv', index=False)
