import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("data.csv")

# Transform (clean data)
df = df.dropna()

# Load (save cleaned data)
df.to_csv("cleaned_data.csv", index=False)

# Load into SQLite database
conn = sqlite3.connect("data.db")
df.to_sql("students", conn, if_exists="replace", index=False)

print("ETL Process Completed Successfully!")
