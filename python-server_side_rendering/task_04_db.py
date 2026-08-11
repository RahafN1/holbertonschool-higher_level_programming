#!/usr/bin/python3
"""Flask application that displays product data from JSON, CSV, or SQL."""

import csv
import json
import sqlite3

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


def read_sql(db_path, product_id=None):
    """Read product data from the SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.
        product_id (int, optional): If provided, only the product with
            this id is fetched.

    Returns:
        list: A list of dictionaries representing the products.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if product_id is not None:
        cursor.execute(
            'SELECT id, name, category, price FROM Products WHERE id = ?',
            (product_id,),
        )
    else:
        cursor.execute('SELECT id, name, category, price FROM Products')

    rows = cursor.fetchall()
    conn.close()

    return [
        {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
        for row in rows
    ]


@app.route('/products')
def products():
    """Display product data read from a JSON, CSV, or SQLite source.

    Query Parameters:
        source (str): 'json', 'csv', or 'sql'. Determines the data source.
        id (int, optional): If provided, filters the results to only
            the product with this id.

    Returns:
        str: The rendered product_display.html template.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
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

    try:
        if source == 'json':
            data = read_json('products.json')
            if product_id is not None:
                data = [item for item in data if item['id'] == product_id]
        elif source == 'csv':
            data = read_csv('products.csv')
            if product_id is not None:
                data = [item for item in data if item['id'] == product_id]
        else:
            data = read_sql('products.db', product_id)
    except FileNotFoundError:
        return render_template(
            'product_display.html', error="Wrong source"
        )
    except sqlite3.Error:
        return render_template(
            'product_display.html', error="Error fetching data from SQL"
        )

    if product_id is not None and not data:
        return render_template(
            'product_display.html', error="Product not found"
        )

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
