from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql():
    products = []
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    for row in rows:
        products.append({'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]})
    conn.close()
    return products

@app.route('/products')
def get_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products = []
    
    # Mənbəyə görə məlumatı seç
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    # ID ilə filtrasiya
    if product_id:
        filtered = [p for p in products if p['id'] == int(product_id)]
        if not filtered:
            return render_template('product_display.html', error="Product not found")
        products = filtered

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
