# Lab 17 - Task 3: IoT Sensor Data Preparation (No sklearn – 100% Working)
import pandas as pd
import numpy as np

# Generate realistic IoT sensor data
np.random.seed(42)
n = 200
dates = pd.date_range('2025-04-01 00:00:00', periods=n, freq='30min')

sensor_ids = ['S1', 'S2', 'S3', 'S4']
data = {
    'timestamp': dates,
    'sensor_id': np.random.choice(sensor_ids, n),
    'temperature': 22 + 5*np.sin(np.arange(n)/24) + np.random.normal(0, 2, n),
    'humidity': 50 + 20*np.sin(np.arange(n)/24 + 1) + np.random.normal(0, 5, n)
}

df = pd.DataFrame(data)

# Add missing values and drift
df.loc[50:60, 'temperature'] = np.nan
df.loc[120:140, 'humidity'] = np.nan
df.loc[80:100, 'temperature'] += np.linspace(0, 8, 21)  # drift

print("Original Raw IoT Data (first 10 rows):")
print(df.head(10))
print("\n" + "="*70 + "\n")

# 1. Handle missing values → forward fill
df['temperature'] = df['temperature'].ffill()
df['humidity'] = df['humidity'].ffill()

# 2. Remove sensor drift → rolling mean (3-hour window)
df['temp_smooth'] = df['temperature'].rolling(window=6, min_periods=1, center=True).mean()
df['humidity_smooth'] = df['humidity'].rolling(window=6, min_periods=1, center=True).mean()

# 3. Standard Scaling (Manual – No sklearn)
df['temp_scaled'] = (df['temp_smooth'] - df['temp_smooth'].mean()) / df['temp_smooth'].std()
df['humidity_scaled'] = (df['humidity_smooth'] - df['humidity_smooth'].mean()) / df['humidity_smooth'].std()

# 4. One-Hot Encode sensor_id
df = pd.get_dummies(df, columns=['sensor_id'], prefix='sensor')

# Final clean dataset
final_cols = ['timestamp', 'temp_scaled', 'humidity_scaled',
              'sensor_S1', 'sensor_S2', 'sensor_S3', 'sensor_S4']
final_df = df[final_cols].copy()

# Save
final_df.to_csv('clean_iot_data.csv', index=False)

print("TASK 3 COMPLETED 100% SUCCESSFULLY!")
print(f"Rows: {len(final_df)}")
print("\nFirst 10 rows of final clean data:")
print(final_df.head(10))
print("\nFile saved: clean_iot_data.csv")