import pandas as pd
import numpy as np

#Load the data and detect missing values
df = pd.read_csv('LoanData_Raw_v1.0.csv')
print(df.isnull().sum())

# Select only numeric columns with missing values
selected = df.iloc[:, [0, 1, 4]] #select age, Ed, income
array = selected.to_numpy()

#Detect and count missing values
print(np.isnan(array)) #detect missing values
print(np.isnan(array).sum()) #count missing values

#Data cleaning
mean_age = np.nanmean(array[:, 0])
mean_ed = np.nanmean(array[:, 1])
mean_inc = np.nanmean(array[:, 2])
array[np.isnan(array[:, 0]), 0] = mean_age
array[np.isnan(array[:, 1]), 1] = mean_ed
array[np.isnan(array[:, 2]), 2] = mean_inc

#Check missing values after cleaning
print('\nChecking for missing values after cleaning')
print(np.isnan(array).sum())
print('\nCleaned data analysis')
print(array.dtype)
print(array.shape)
print(array[:5])