#!/usr/bin/python3
"""
A simple API built using Python's http.server module.

Supported endpoints:
    /        -> Plain text welcome message
    /data    -> Sample JSON dataset
    /status  -> Plain text API status ("OK")
    /info    -> JSON with API version and description

Any other path returns a 404 Not Found JSON error message.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handles GET requests for the simple API."""

    def do_GET(self):
        """Route the incoming GET request based on self.path."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(200, data)

        elif self.path == "/status":
            self._send_text(200, "OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self._send_json(200, info)

        else:
            self._send_json(404, {"error": "Endpoint not found"})

    def _send_text(self, status_code, message):
        """Send a plain text response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json(self, status_code, data):
        """Send a JSON response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server and keep it running."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
