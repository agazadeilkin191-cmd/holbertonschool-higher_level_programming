import sqlite3
import os

def create_database():
    # 1. Əgər fayl artıq varsa və korlanıbsa, onu silirik
    if os.path.exists('products.db'):
        os.remove('products.db')
        
    # 2. Yeni bazanı yaradırıq
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # 3. Cədvəli yaradırıq
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # 4. Məlumatları daxil edirik
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Database created successfully.")

if __name__ == '__main__':
    create_database()
