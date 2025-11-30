#!/usr/bin/env python3
from flask import Flask, request, render_template
import json, csv, os, sqlite3

app = Flask(__name__)
    
@app.route("/products")
def products():
    source = request.args.get("source")
    productId = request.args.get("id")
    filename = ""
    if source == "json":
        filename = "products.json"
        filepath = os.path.join(app.root_path, filename)
        with open(filepath) as f:
            data = json.load(f)
    elif source == "csv":
        filename = "products.csv"
        filepath = os.path.join(app.root_path, filename)
        with open(filepath) as f:
            data = list(csv.DictReader(f))
    elif source == "sql":
        try:
            connection = sqlite3.connect(os.path.join(app.root_path, 'products.db'))
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            data = [
                {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
                for row in rows
            ]
            connection.close()
        except Exception as e:
            return render_template('product_display.html', error=str(e))
    else:
        return render_template("product_display.html", error="Wrong source")
    if productId:
        productId = int(productId)
        filtered = [product for product in data if int(product["id"]) == productId]
        if filtered:
            return render_template("product_display.html", products=filtered)
        else:
            return render_template("product_display.html", error="Product not found")
    return render_template('product_display.html', products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)