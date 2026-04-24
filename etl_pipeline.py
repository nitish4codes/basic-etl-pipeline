import pandas as pd
import sqlite3

# 1. Extract

df = pd.read_csv("googleplaystore.csv")

# 2. Transform (Cleaning logic for 10,000+ records)
df = df.drop_duplicates()

# Logic to remove '+' and ',' from Installs (e.g., '10,000+' -> 10000)
df['Installs'] = df['Installs'].str.replace('+', '', regex=False).str.replace(',', '', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce').fillna(0).astype(int)

# Function to convert Size (e.g., '19M' -> 19000000)
def convert_size(size):
    size = str(size)
    if 'M' in size:
        return float(size.replace('M', '')) * 1000000
    elif 'k' in size:
        return float(size.replace('k', '')) * 1000
    return 0

df['Size'] = df['Size'].apply(convert_size)

# 3. Load
# Save cleaned version to CSV
df.to_csv("cleaned_playstore_data.csv", index=False)

# Save to SQLite database
conn = sqlite3.connect("playstore_data.db")
df.to_sql("apps_table", conn, if_exists="replace", index=False)
conn.close()

print(f"ETL Complete: {len(df)} records processed!")
