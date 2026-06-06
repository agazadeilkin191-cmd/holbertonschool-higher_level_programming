from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# Köhnə marşrutlarınız...
@app.route('/')
def home():
    return render_template('index.html')

# Yeni /items marşrutu
@app.route('/items')
def items():
    # JSON faylını oxuyuruq
    json_path = 'items.json'
    if os.path.exists(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    else:
        items_list = []
        
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
