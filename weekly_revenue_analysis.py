import pandas as pd 
import numpy as np
df = pd.read_csv('index_1.csv')

#Loading the DataFrame into the array
selected = df['money']
array = selected.to_numpy()

#slicing the array into batches 
rows = (array.shape[0]//7)*7 
clean_array = array[:rows]

#reshaping the array 
reshaped = clean_array.reshape(-1, 7)
print(f'Reshaped: \n{reshaped}')

weekly_revenue = np.sum(reshaped,1)
daily_revenue = np.sum(reshaped,0)
print(f'\nTotal weeks: \n{reshaped.shape}')
print(f'\nRevenue First week; \n{np.sum(reshaped[0])}')
print(f'\nWeekly revenue: \n{weekly_revenue}')
print(f'\nDaily revenue pattern: \n{daily_revenue}')
