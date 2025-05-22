import numpy as np 
arr = np.random.randint(1, 100, size= (5, 5)) #creating an array of random integers between 1 and 100
print('Generated Array: ')
print(arr)

#Slicing and filtering the array 
print('\nExtract of first row: ')
print(arr[0, :])
print('\nExtract of last column: ')
print(arr[:, -1])

def extract_center_block (arr, blocksize):
	rows, cols = arr.shape
	r_center, c_center = rows//2, cols//2
	half = blocksize//2
	return arr[r_center - half : r_center + half + 1, c_center - half : c_center + half + 1]
center_3x3 = extract_center_block(arr, 3)
print('\nExtract of the centre 3x3 matrix by function: ')
print(center_3x3)
print('\nExtract of the centre 3x3 matrix by hard coding: ')
print(arr[1:4, 1:4])
print('\nAll elements > 50: ')
print(arr[arr>50])

print('\nRelaced odd numbers with "-1": ')
odd = arr%2 == 1 #creating a Boolean for odd numbers
arr[odd] = -1 #assigning every odd number in the array a "-1"
print(arr)
