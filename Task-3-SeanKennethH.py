# PROJECT 3: SQL DATA ANALYSIS (VS CODE VERSION)
# Uses your existing order dataset

import pandas as pd
import sqlite3

# --------------------------
# 1. Load YOUR dataset
# --------------------------
df = pd.read_excel("Dataset for Data Analytics.xlsx", engine="openpyxl")

# --------------------------
# 2. Create SQL Database (automatic)
# --------------------------
conn = sqlite3.connect("orders_db.sqlite")  # creates a small database file
df.to_sql("orders", conn, if_exists="replace", index=False)

# Function to run SQL and show results neatly
def sql(query):
    output = pd.read_sql(query, conn)
    print("\n" + "="*50)
    print(query)
    print("-"*50)
    print(output)

# --------------------------
# 3. RUN ALL REQUIRED SQL QUERIES FOR PROJECT 3
# --------------------------

# 1. Show all orders (first 10 rows)
sql("SELECT * FROM orders LIMIT 10;")

# 2. Filter: Only DELIVERED orders
sql("SELECT OrderID, Product, TotalPrice, OrderStatus FROM orders WHERE OrderStatus = 'Delivered';")

# 3. Filter: Orders over $2000
sql("SELECT OrderID, Product, TotalPrice FROM orders WHERE TotalPrice > 2000;")

# 4. Sort: Most expensive orders first
sql("SELECT OrderID, Product, TotalPrice FROM orders ORDER BY TotalPrice DESC LIMIT 10;")

# 5. GROUP BY: Count orders per Product
sql("SELECT Product, COUNT(OrderID) AS Total_Orders FROM orders GROUP BY Product;")

# 6. GROUP BY: Total Revenue per Product
sql("SELECT Product, SUM(TotalPrice) AS Total_Revenue FROM orders GROUP BY Product ORDER BY Total_Revenue DESC;")

# 7. GROUP BY: Average Order Value per Product
sql("SELECT Product, AVG(TotalPrice) AS Avg_Order_Value FROM orders GROUP BY Product;")

# 8. Total Revenue per Order Status
sql("SELECT OrderStatus, SUM(TotalPrice) AS Total_Revenue FROM orders GROUP BY OrderStatus;")

# 9. Yearly Revenue (2023, 2024, 2025)
sql("SELECT strftime('%Y', Date) AS Year, SUM(TotalPrice) AS Revenue FROM orders GROUP BY Year;")

# Close database
conn.close()
print("\n✅ Project 3 SQL Analysis Completed!")