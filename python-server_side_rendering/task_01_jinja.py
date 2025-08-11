#!/usr/bin/env python3
"""
Task 01: Basic Flask App with Jinja templates and reusable components
"""

from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Run the Flask app on port 5000 with debug mode on
    app.run(debug=True, port=5000)