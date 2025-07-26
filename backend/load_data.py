import psycopg2
import pandas as pd

# Connection config
conn = psycopg2.connect(
    dbname="ecommerce_db",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Load products
products_df = pd.read_csv('./data/products.csv')
print("PRODUCTS CSV COLUMNS:", products_df.columns.tolist())
for _, row in products_df.iterrows():
    cur.execute("""
        INSERT INTO products (product_name, category, price, quantity)
        VALUES (%s, %s, %s, %s)
    """, (row['name'], row['category'], row['retail_price'], 0))


# Load orders
orders_df = pd.read_csv('./data/orders.csv')
print("ORDERS CSV COLUMNS:", orders_df.columns.tolist())
for _, row in orders_df.iterrows():
    cur.execute("""
    INSERT INTO orders (product_name, quantity, status, date)
    VALUES (%s, %s, %s, %s)
""", (
    "Unknown Product",             # Since we don’t have product_name
    row['num_of_item'],            # Treat num_of_item as quantity
    row['status'],
    row['created_at']
))


conn.commit()
cur.close()
conn.close()

print("Data loaded successfully.")

