#!/usr/bin/env python3
"""
Simple Flask API for managing user data.

This API provides endpoints to retrieve users, check status,
retrieve specific user details, and add new users.
"""

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    """
    Returns a welcome message for the API.

    Returns:
        str: Welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def data():
    """
    Returns all users stored in the system.

    Returns:
        JSON: A dictionary containing all users.
    """
    return jsonify(users)


@app.route('/status')
def status():
    """
    Returns the API status.

    Returns:
        str: The string 'OK' to indicate API is running.
    """
    return 'OK'


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Retrieves the full user object for the given username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        JSON: User details if found, otherwise an error message.
    """
    user = users.get(username.lower())
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Handles adding a new user with JSON validation."""

    try:
        data = request.get_json(force=True)
    except (TypeError, json.JSONDecodeError):
        return jsonify({"error": "Invalid JSON format"}), 400

    required_keys = {"username", "name", "age", "city"}
    if not all(key in data for key in required_keys):
        return jsonify({"error": "Missing required fields"}), 400

    username = data["username"].lower()
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data
    return jsonify({"message": "User added successfully", "user": data}), 201


@app.errorhandler(404)
def not_found(error):
    """
    Custom 404 error handler for undefined routes.
    Returns a JSON error response instead of the default HTML page.
    """
    return jsonify({"error": "Endpoint not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
