import pandas as pd

#preparing the dataset
df = pd.read_csv('Weather Data.csv')
df['Date/Time'] = pd.to_datetime(df['Date/Time']) #parse timetamp
df.set_index('Date/Time', inplace=True) #set as index

#Daily average temperature
daily_avg = df['Temp_C'].resample('D').mean()
print(f'Daily Average Temperature: \n{daily_avg}')

#Weekly max relative humidity
weekly_max = df['Rel Hum_%'].resample('W').max()
print(f'\nWeekly max relative humidity: \n{weekly_max}')

#Monthly average visibility
month_avg = df['Visibility_km'].resample('M').mean()
print(f'\nMonthly average visibility: \n{month_avg}')

#24-Hour rolling average temperature
rolling_avg = df['Temp_C'].rolling(window=24).mean()
df['Rolling_avg'] = rolling_avg
print(df.head())
