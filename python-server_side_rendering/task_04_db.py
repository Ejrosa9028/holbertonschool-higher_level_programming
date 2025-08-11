from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Ruta para mostrar los productos
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error_message = None

    if source == 'json':
        try:
            with open('products.json') as f:
                products = json.load(f)
        except Exception as e:
            error_message = "Error reading JSON file."
    elif source == 'csv':
        try:
            with open('products.csv', newline='') as f:
                reader = csv.DictReader(f)
                products = list(reader)
        except Exception as e:
            error_message = "Error reading CSV file."
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            query = "SELECT id, name, category, price FROM Products"
            if product_id is not None:
                query += " WHERE id = ?"
                cursor.execute(query, (product_id,))
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            products = [dict(id=row[0], name=row[1], category=row[2], price=row[3]) for row in rows]
            conn.close()
        except Exception as e:
            error_message = "Error accessing the database."
    else:
        error_message = "Wrong source"

    if product_id is not None and not products:
        error_message = "Product not found"

    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 