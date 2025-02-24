#!/usr/bin/env python3
"""
Test Suite for task_03_http_server.py

This script tests the API to ensure it responds correctly to requests.
"""

import unittest
import requests
import json

BASE_URL = "http://localhost:8000"  # Adjust if using a different port


class TestSimpleAPIServer(unittest.TestCase):
    """Test cases for the HTTP server"""

    def test_root_endpoint(self):
        """Test if root (/) returns the correct message"""
        response = requests.get(f"{BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, this is a simple API!")

    def test_data_endpoint(self):
        """Test if /data returns the correct JSON response"""
        response = requests.get(f"{BASE_URL}/data")
        self.assertEqual(response.status_code, 200)

        expected_data = {"name": "John", "age": 30, "city": "New York"}
        self.assertEqual(response.json(), expected_data)

    def test_status_endpoint(self):
        """Test if /status returns the expected response"""
        response = requests.get(f"{BASE_URL}/status")
        self.assertEqual(response.status_code, 200)

        expected_data = {"status": "OK"}  # Ensure case sensitivity matches API
        self.assertEqual(response.json(), expected_data)

    def test_info_endpoint(self):
        """Test if /info returns API metadata"""
        response = requests.get(f"{BASE_URL}/info")
        self.assertEqual(response.status_code, 200)

        expected_data = {
            "version": "1.0",
            "description": "A simple API built with http.server",
        }
        self.assertEqual(response.json(), expected_data)

    def test_invalid_endpoint(self):
        """Test if an undefined endpoint returns a 404 with correct message"""
        response = requests.get(f"{BASE_URL}/undefined")
        self.assertEqual(response.status_code, 404)

        expected_data = {"error": "Endpoint not found"}
        self.assertEqual(response.json(), expected_data)


if __name__ == "__main__":
    unittest.main()