import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('coffee.db')
c = conn.cursor()

# Create table for contact form messages
c.execute('''
CREATE TABLE IF NOT EXISTS contact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
)
''')

# Create table for coffee orders
c.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    coffee_type TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

print("✅ Database and tables created successfully!")
