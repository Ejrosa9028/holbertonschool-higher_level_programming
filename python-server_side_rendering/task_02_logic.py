#!/usr/bin/env python3
"""
Task 2: Creating a Dynamic Template with Loops and Conditions in Flask
"""

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def display_items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items = data.get("items", [])  
    except Exception as e:
        items = []
        print(f"Error reading items.json: {e}")

    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)