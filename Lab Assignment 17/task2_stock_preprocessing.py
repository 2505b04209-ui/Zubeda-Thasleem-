# Lab 17 - Task 2: Financial Data Preprocessing (Stock Market) - FINAL WORKING VERSION
import pandas as pd
import numpy as np

# Generate realistic sample stock data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100)
n = len(dates)

# Create closing prices with some trend + noise
price = 150 + np.cumsum(np.random.randn(n) * 2) + np.sin(np.arange(n)/10)*10
price = np.round(price, 2)

# Create volume (large numbers) - keep as float for safety
volume = np.random.lognormal(mean=12, sigma=1, size=n)
volume = np.round(volume).astype(float)  # float, not int

# Make some missing values
price[20:25] = np.nan
volume[30:35] = np.nan

# Add two extreme outliers
price[50] = 500   # super high
price[80] = 10    # super low

df = pd.DataFrame({
    'date': dates,
    'closing_price': price,
    'volume': volume
})

df = df.sort_values('date').reset_index(drop=True)

print("Original Raw Data (first 10 rows):")
print(df.head(10))
print("\n" + "="*70 + "\n")

# 1. Handle missing values
df['closing_price'] = df['closing_price'].fillna(df['closing_price'].median())
df['volume'] = df['volume'].fillna(df['volume'].median())

# 2. Create lag features (returns)
df['prev_close'] = df['closing_price'].shift(1)
df['1_day_return'] = df['closing_price'].pct_change(1)   # safer than manual formula
df['7_day_return'] = df['closing_price'].pct_change(7)

# 3. Normalize volume using log scaling
df['volume_log'] = np.log1p(df['volume'])

# 4. Detect outliers using IQR method
Q1 = df['closing_price'].quantile(0.25)
Q3 = df['closing_price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['is_outlier'] = (df['closing_price'] < lower_bound) | (df['closing_price'] > upper_bound)

# Final clean dataset ready for forecasting
final_df = df[['date', 'closing_price', 'volume_log', 
               '1_day_return', '7_day_return', 'is_outlier']].copy()

# Save to CSV
final_df.to_csv('clean_stock_data.csv', index=False)

print("TASK 2 COMPLETED 100% SUCCESSFULLY!")
print(f"\nTotal rows: {len(final_df)}")
print(f"Outliers detected: {df['is_outlier'].sum()} (the 500 and 10 ones)")
print("\nFirst 10 rows of final clean data:")
print(final_df.head(10))
print("\nFile saved: clean_stock_data.csv")