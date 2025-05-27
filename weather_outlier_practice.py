import pandas as pd
import numpy as np 
df = pd.read_csv('Weather Data.csv')

#exracting relevant features
selected = df.iloc[:, [1, 3, 6]]
array= selected.to_numpy()

#array percentile analysis
TempQ1 = np.percentile(array[:, 0], 25)
TempQ2 = np.percentile(array[:, 0], 50)
TempQ3 = np.percentile(array[:, 0], 75)
HumQ1 = np.percentile(array[:, 1], 25)
HumQ2 = np.percentile(array[:, 1], 50)
HumQ3 = np.percentile(array[:, 1], 75)
PressQ1 = np.percentile(array[:, 2], 25)
PressQ2 = np.percentile(array[:, 2], 50)
PressQ3 = np.percentile(array[:, 2], 75)
TempIQR = TempQ3 - TempQ1
HumIQR = HumQ3 - HumQ1
PressIQR = PressQ3 - PressQ1
print(f"Temperature's 25th, 50th, and 75th percentiles: \n{np.percentile(array[:, 0], [25, 50, 75])}")
print(f"Humidity's 25th, 50th, and 75th percentiles: \n{np.percentile(array[:, 1], [25, 50, 75])}")
print(f"Pressure's 25th, 50th, and 75th percentiles: \n{np.percentile(array[:, 2], [25, 50, 75])}")

#calculating interquartile range (IQR)
print(f"\nTemperature's IQR: \n{TempIQR}")
print(f"Humidity's IQR: \n{HumIQR}")
print(f"Pressure's IQR: \n{PressIQR}")

#identifying outliers for temperature
lower_bound = TempQ1 - 1.5*TempIQR
upper_bound = TempQ3 + 1.5*TempIQR
print(f'\nLower bound: {lower_bound}')
outliers = array[(array[:, 0] < lower_bound) | (array[:, 0] > upper_bound)]
print(f'\nOutliers: {outliers}')
