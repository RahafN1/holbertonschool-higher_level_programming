#!/usr/bin/python3
"""Flask application that displays product data from JSON or CSV files."""

import csv
import json

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(file_path):
    """Read and parse product data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of dictionaries representing the products.
    """
    with open(file_path, 'r') as json_file:
        return json.load(json_file)


def read_csv(file_path):
    """Read and parse product data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: A list of dictionaries representing the products, with
            'id' converted to int and 'price' converted to float.
    """
    products = []
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


@app.route('/products')
def products():
    """Display product data read from either a JSON or CSV file.

    Query Parameters:
        source (str): 'json' or 'csv'. Determines which file to read.
        id (int, optional): If provided, filters the results to only
            the product with this id.

    Returns:
        str: The rendered product_display.html template.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template(
            'product_display.html', error="Wrong source"
        )

    try:
        if source == 'json':
            data = read_json('products.json')
        else:
            data = read_csv('products.csv')
    except FileNotFoundError:
        return render_template(
            'product_display.html', error="Wrong source"
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found"
            )

        product = next(
            (item for item in data if item['id'] == product_id), None
        )

        if product is None:
            return render_template(
                'product_display.html', error="Product not found"
            )

        return render_template('product_display.html', products=[product])

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
