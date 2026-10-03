import pandas as pd
import matplotlib.pyplot as plt

# Load
df = pd.read_csv('sales.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Auto-find sales column
sales_col = next(c for c in ['Sales','Total','Amount','sales','total'] if c in df.columns)

# 1. Product analysis
product_sales = df.groupby('Product line')[sales_col].sum().sort_values(ascending=False)

# 2. City analysis
city_sales = df.groupby('City')[sales_col].sum().sort_values(ascending=False)

# 3. Monthly analysis
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))[sales_col].sum()

# --- Pretty Charts ---
plt.figure(figsize=(10,5))
product_sales.plot(kind='bar')
plt.title('Total Sales by Product Line')
plt.ylabel('Sales ($)')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('chart1_product.png')
plt.close()

plt.figure(figsize=(8,4))
city_sales.plot(kind='bar', color='orange')
plt.title('Total Sales by City')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('chart2_city.png')
plt.close()

plt.figure(figsize=(10,4))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('chart3_monthly.png')
plt.close()

print("Done! Insights:")
print(product_sales)
print("\nBest city:", city_sales.index[0])