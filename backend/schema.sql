CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price NUMERIC,
    quantity INTEGER
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    product_name TEXT,
    quantity INTEGER,
    status TEXT,
    date TIMESTAMP
);
