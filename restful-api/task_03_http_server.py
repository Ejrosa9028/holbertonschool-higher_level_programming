#!/usr/bin/env python3
"""
Simple HTTP API Server using Python's built-in http.server module.

This module implements a basic API that serves different endpoints:
- "/"       : Returns a simple text message.
- "/data"   : Returns JSON data containing sample user information.
- "/status" : Returns a JSON status message.
- "/info"   : Returns API metadata.

If a request is made to an undefined endpoint, a 404 response is returned.
"""

import http.server
import json
from http import HTTPStatus


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom request handler for the simple API.

    This class extends BaseHTTPRequestHandler to handle GET requests and
    return JSON or text responses for different API endpoints.
    """

    def do_GET(self):
        """
        Handles GET requests and routes them to specific API endpoints.

        Supported endpoints:
        - "/"        : Returns a welcome message.
        - "/data"    : Returns a JSON object with sample user data.
        - "/status"  : Returns a JSON response confirming API availability.
        - "/info"    : Returns API metadata as a JSON response.

        If an unknown endpoint is accessed, it returns a 404 error response.
        """
        if self.path == "/":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            error_msg = {"error": "Endpoint not found"}  # Fixed key
            self.wfile.write(json.dumps(error_msg).encode("utf-8"))


def run():
    """
    Starts the HTTP server on port 8000.

    The server listens on all available network interfaces and processes
    incoming HTTP requests using the SimpleAPIHandler.
    """
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
