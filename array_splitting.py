import pandas as pd
import numpy as np 

#load data with 3 numeric columns
df = pd.read_csv('Cleaned_LoanData.csv')
array = df.to_numpy()
print(f'Original Shape: {array.shape}')

#Split array with different methods
np_split = np.split(array, 2)
print(f'\nSplit() shape:')
for i, sub_array in enumerate (np_split):
	print(sub_array.shape) #print shape of each subarray in split()
print(f'\nSample segment: \n{np_split[:1]}')

np_array_split = np.array_split(array, 6)
print('\narray_split() shape:')
for i, sub_array in enumerate (np_array_split):
	print(sub_array.shape) #print shape of each subarrays in array_split()
print(f'\nSample segment: \n{np_array_split[:1]}')

v_split = np.vsplit(array, 5)
print('\nvsplit() shape:')
for i,sub_array in enumerate (v_split):
	print(sub_array.shape) #print shape of each subarrays in vsplit()
print(f'\nSample segment: \n{v_split[:1]}')

h_split = np.hsplit(array, 3)
print('\nhsplit() shape:')
for i,sub_array in enumerate (h_split):
	print(sub_array.shape) #print shape of each subarray in hsplit()
print(f'\nSample segment: \n{h_split[:1]}')