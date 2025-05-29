import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === Load and prepare data ===
df = pd.read_csv('WDI_Indicators_MainData.csv')

# Select relevant columns
selected = df[[
    "Time", 
    "Country Name", 
    "Current education expenditure, total (% of total expenditure in public institutions) [SE.XPD.CTOT.ZS]",
    "Current health expenditure (% of GDP) [SH.XPD.CHEX.GD.ZS]",
    "Educational attainment, at least Bachelor's or equivalent, population 25+, total (%) (cumulative) [SE.TER.CUAT.BA.ZS]",
    "Population, total [SP.POP.TOTL]",
    "Employment to population ratio, 15+, total (%) (modeled ILO estimate) [SL.EMP.TOTL.SP.ZS]"
]]

# Rename columns for clarity
selected.rename(columns={
    'Time': 'Year',
    'Current education expenditure, total (% of total expenditure in public institutions) [SE.XPD.CTOT.ZS]': 'Total_Education_Expenditure',
    'Current health expenditure (% of GDP) [SH.XPD.CHEX.GD.ZS]': 'Health_Expenditure',
    "Educational attainment, at least Bachelor's or equivalent, population 25+, total (%) (cumulative) [SE.TER.CUAT.BA.ZS]": "Ed_Attainment",
    'Population, total [SP.POP.TOTL]': 'Population',
    'Employment to population ratio, 15+, total (%) (modeled ILO estimate) [SL.EMP.TOTL.SP.ZS]': 'Emp_Pop_Ratio'
}, inplace=True)

# === Data cleaning ===
# Separate numeric and non-numeric parts
metadata = selected.iloc[:, :2]
numeric_array = selected.iloc[:, 2:].to_numpy()

# Fill missing values using median per column
for i in range(numeric_array.shape[1]):
    median_val = np.nanmedian(numeric_array[:, i])
    numeric_array[np.isnan(numeric_array[:, i]), i] = median_val

# Combine back cleaned array with metadata
cleaned = pd.concat([metadata.reset_index(drop=True), pd.DataFrame(numeric_array, columns=selected.columns[2:])], axis=1)

# === Part 1: Latest available year per country ===
latest_rows = cleaned.sort_values('Year').groupby('Country Name').tail(1)

# === Part 2: Country-wise average of selected indicators ===
country_averages = cleaned.groupby('Country Name')[[
    'Total_Education_Expenditure', 
    'Health_Expenditure', 
    'Ed_Attainment', 
    'Population', 
    'Emp_Pop_Ratio'
]].mean()

# === Part 3: Sort by average education expenditure ===
education_avg_sorted = country_averages['Total_Education_Expenditure'].sort_values(ascending=False)
print("\nTop 10 Countries by Average Education Expenditure:\n")
print(education_avg_sorted.head(10))

# === Part 4: Visualize population vs health expenditure ===
plt.figure(figsize=(10, 6))
plt.scatter(latest_rows['Population'], latest_rows['Health_Expenditure'], alpha=0.7)
plt.xlabel('Population')
plt.ylabel('Health Expenditure (% of GDP)')
plt.title('Health Spending vs Population (Latest Available Year)')
plt.grid(True)
plt.tight_layout()
plt.show()

# === Optional: Save to file ===
latest_rows.to_csv('Latest_Indicators_by_Country.csv', index=False)
country_averages.to_csv('Country_Averages.csv')