#!/usr/bin/env python3
"""
Simple Flask API for managing user data.

This API provides endpoints to retrieve users, check status,
retrieve specific user details, and add new users.
"""

from flask import Flask, jsonify, request

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
    """
    Adds a new user to the system.

    Request:
        JSON: {
            "username": "string",
            "name": "string",
            "age": int,
            "city": "string"
        }

    Returns:
        JSON: Confirmation message and user details if successful,
              otherwise an error message.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON format"}), 400

    data = request.get_json()
    required_keys = {"username", "name", "age", "city"}

    if not all(key in data for key in required_keys):
        return jsonify({"error": "Missing required fields"}), 400

    username = data["username"].lower()

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data
    return jsonify({"message": "User added successfully", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
