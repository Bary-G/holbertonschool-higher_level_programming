#!/usr/bin/env python3
from flask import Flask, request, render_template
import json, csv, os

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