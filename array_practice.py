import numpy as np 

#printing the shape, dimension, size and data type of each output alongside
#Creating a 1D array with numbers from 10 to 90 (step of 10)
one_d_array = np.arange(10,90,10)
print('1D array: ')
print(one_d_array)
print(f'Shape: {one_d_array.shape}')
print(f'Dimension: {one_d_array.ndim}')
print(f'Size: {one_d_array.size}')
print(f'Data type: {one_d_array.dtype}')

#Creating a 3x3 array filled with 3.14s
three_by_three_array = np.full((3, 3), 3.14)
print('\n3x3 array')
print(three_by_three_array)
print(f'Shape: {three_by_three_array.shape}')
print(f'Dimension: {three_by_three_array.ndim}')
print(f'Size: {three_by_three_array.size}')
print(f'Data type: {three_by_three_array.dtype}')

#creating a 5x5 identify matrix
id_mtrx = np.eye(5)
print('\n5x5 identity matrix')
print(id_mtrx)
print(f'Shape: {id_mtrx.shape}')
print(f'Dimension: {id_mtrx.ndim}')
print(f'Size: {id_mtrx.size}')
print(f'Data type: {id_mtrx.dtype}')

#Creating a 4x6 array of random numbers between 0-1
rndm = np.random.random((4,6))
print('\nRandom numbers (between 0-1) in a 4x6 array')
print(rndm)
print(f'Shape: {rndm.shape}')
print(f'Dimension: {rndm.ndim}')
print(f'Size: {rndm.size}')
print(f'Data type: {rndm.dtype}')
