import pandas as pd
import numpy as np

# Load weather dataset
df = pd.read_csv('Weather Data.csv')

# Select relevant numerical columns: Temp, Humidity, Wind, Visibility, Pressure
selected = df.iloc[:, [1, 3, 4, 5, 6]]
array = selected.to_numpy()

# Clean data: trim to complete days (24 hours)
rows = (array.shape[0] // 24) * 24
clean_array = array[:rows]

# Reshape into daily chunks: (days, 24 hours, 5 features)
reshaped = clean_array.reshape(-1, 24, 5)
print(f'Daily batch of data: \n{reshaped}')

# Analysis
average_temp = np.mean(reshaped[:, :, 0])                    # Avg temperature overall
average_wind = np.mean(reshaped[:, :, 3], axis=0)            # Hourly avg wind speed
max_wind = np.argmax(average_wind)                           # Hour with highest wind speed
std_press = np.std(reshaped[:, :, 4])                        # Pressure standard deviation

# Visibility flag: mark hours where visibility < 1km
df['flagged'] = df['Visibility_km'] < 1

# Output
print(f'\nAverage daily temperature: \n{average_temp}')
print(f'\nHour of day with highest wind speed: \n{max_wind}')
print(f'\nStandard deviation of pressure: \n{std_press}')
print(f'\nFlag of hours with visibility below 1km: \n{df["flagged"]}')
print(f'\nNew Shape: {reshaped.shape}')
