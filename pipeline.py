import sqlite3 
import pandas as pd 

df = pd.read_csv("sales.csv")

df.columns = df.columns.str.replace('', '_')

conn = sqlite3.connect("supermarket_data.db")
df.to_sql("sales_records", conn, if_exists="replace", index=False)

conn.close()

print("Pipeline Success! Your database 'supermarket.data.db' is ready.")