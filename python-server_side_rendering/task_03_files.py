from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # CSV-də bütün dəyərlər string gəlir, çevirmə edək
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def get_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products = []
    
    # Mənbəni yoxla
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
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
