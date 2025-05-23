import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('AMZN_stock_data.csv')

# Select relevant numeric columns for analysis
selected = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# Convert the selected DataFrame to a NumPy array
array = selected.to_numpy()

# Print basic diagnostics
print('Shape', array.shape)                   # Total rows and columns
print('Data type', array.dtype)               # Should be float64
print(f'First 5 rows: \n{array[:5]}')         # Preview first few rows

# Ensure row count is divisible by 7 (for full weeks)
rows = (array.shape[0] // 7) * 7              # Drop remainder rows
clean_array = array[:rows]                    # Trim excess rows if necessary

# Reshape to 3D array: (weeks, days per week, features)
reshaped = clean_array.reshape(-1, 7, 5)

# Inspect the reshaped array
print(f'\nReshaped: \n{reshaped}')            # Print entire reshaped structure
print(f'\nFirst Week Data: \n{reshaped[0]}')  # First week's data (7 rows x 5 features)
print(f'\nFirst week open values: \n{reshaped[0, :, 0]}')  # Extract "Open" column for first week

# Flatten array for ML or statistical use (converts 3D → 1D)
flat = reshaped.flatten()
print(f'Flattened "reshaped" shape: \n{flat.shape}')

# Transpose the original array (rows become columns)
transposed = array.T
print(f'\nTransposed shape: \n{transposed.shape}')         # Should be (5, total_days)
print(f'\nFirst row: \n{transposed[0]}')                   # All open prices across time
