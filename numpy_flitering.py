import pandas as pd
import numpy as np 

#load the data and inspect 
df = pd.read_csv('ParisHousingClass.csv')
print(df.columns.tolist())
array = df.to_numpy()
print(f'Shape of array: {array.shape}')
print(f'Data type: {array.dtype}')
print(f'First 3 rows: \n{array[:3]}')

#data filtering
high_rooms = array[array[:, 1] > 4] #extract rows with more than 4 rooms
print(f'\nShape of rows with > 4 rooms: {high_rooms.shape}')
high_price_area = array[(array[:, 16] > 900000) & (array[:, 0] >= 2000)] #extract rows with> 900000 and area >=2000
print(f'\nShape of rows with > 900000 price and >= 2000 area: \n{high_price_area.shape}')
array[array[:, 16] < 300000, 16] = 300000 #replace <300000 values to 300000
avg_price = np.mean(array[array[:, 1] == 3, 16]) #calculate average price of 3-bedroom houses
print(f'\nAverage price of 3-bedroom houses: \n{avg_price}')