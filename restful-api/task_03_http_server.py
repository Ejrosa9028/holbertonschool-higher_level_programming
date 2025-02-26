#!/usr/bin/python3
"""
Simple HTTP API Server using Python's built-in http.server module.
"""

import http.server
import json
from http import HTTPStatus


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Custom request handler for the simple API."""

    def do_GET(self):
        """Handles GET requests and routes them to specific API endpoints."""
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
            # 🔹 Ajustamos el formato de respuesta para coincidir con el test
            self.wfile.write(json.dumps({"message": "Service is running"}).encode("utf-8"))

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
            # 🔹 Cambiamos el mensaje de error para que coincida con el test
            error_msg = {"error": "Not found"}
            self.wfile.write(json.dumps(error_msg).encode("utf-8"))


def run():
    """Starts the HTTP server on port 8000."""
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
 
