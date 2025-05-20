#Forgot to save the file before uploading😆 so here the code
import pandas as pd
pd.set_option('display.precision', 2)
patients_df = pd.read_csv('Patients.csv')
print('Original DataFrame: ')
print(patients_df)

#Data exploration
print('\nDetecting missing values: ')
print(patients_df.isnull())
print('\nTotal Missing Values per Column: ')
print(patients_df.isnull().sum())
print('\nDisplay Rows with Missing Values: ')
print(patients_df[patients_df.isnull().any(axis=1)])

#Data cleaning
print('\nFeature Engineering on Age, Temperature and HeartRate columns: ')
mean_age = patients_df['Age'].mean()
mean_temperature = patients_df['Temperature'].mean()
mean_hr = patients_df['HeartRate'].mean()
patients_df.fillna({'Age': mean_age}, inplace=True)
patients_df.fillna({'Temperature': mean_temperature}, inplace=True)
patients_df.fillna({'HeartRate': mean_hr}, inplace=True)
print(patients_df)
print('\nDataFrame with Dropped rows with Missing Diagnosed values: ')
patients_df.dropna(subset=['Diagnosed'], inplace=True)
patients_df.reset_index(drop=True, inplace= True) #Resetting index
print(patients_df)

#Resaving
patients_df.to_csv('Patients_Cleaned.csv', index=False)
