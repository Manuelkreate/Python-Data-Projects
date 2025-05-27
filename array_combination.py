import pandas as pd 
import numpy as np 

#Load both files 
df1 = pd.read_csv('Cleaned_LoanData.csv')
df2 = pd.read_csv('LoanData_Preprocessed_v1.2.csv')
a1 = df1.to_numpy() #convert df1 to array
selected = df2.iloc[:, [1, 2, 4]] #selecting 3 numeric columns
a2 = selected.to_numpy() #convert df2(selected numeric columns to array
print(f"Array 1's shape: {a1.shape}")
print(f"Array 2's shape: {a2.shape}")

#Combining them 
#due to a2 having a shape of (485, 3), print(np.hstack) will result into an error
#np.stack will also result into the same error as np.hstack for the same reason 
print(np.vstack((a1, a2))) #vertically stack or combine the two arrays and adds rows.
np.concatenate((a1,a2), axis=0) #equivalent of np.vstack