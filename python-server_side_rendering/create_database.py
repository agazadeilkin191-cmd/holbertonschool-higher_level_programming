import sqlite3
import os

def create_database():
    # Faylın adını təyin edirik
    db_file = 'products.db'
    
    # Əgər fayl varsa, onu proqramın özünə sildiririk
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
        except PermissionError:
            print(f"Fayl istifadədədir, silinə bilmədi: {db_file}")
            return

    # İndi təzə və təmiz bazanı yaradırıq
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == '__main__':
    create_database()
