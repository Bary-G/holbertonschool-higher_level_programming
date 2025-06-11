#!/usr/bin/python3
import json
import http.server
import socketserver
"""
Module:
A Python script that runs functions.
"""


class MyHandler(http.server.BaseHTTPRequestHandler):
    def _send_response(self, response_data, status_code=200, content_type="application/json"):
        """
        Sends a simple text response back to the client.
        """
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        if isinstance(response_data, str):
            self.wfile.write(response_data.encode("UTF8"))
        else:
            self.wfile.write(json.dumps(response_data).encode("UTF8"))

    def do_GET(self):
        """
        Gets a simple dataset.
        """
        if self.path == "/":
            self._send_response("Hello, this is a simple API!", content_type="text/plain")
        elif self.path == "/data":
            self._send_response({"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/info":
            self._send_response({"version": "1.0", "description": "A simple API built with http.server"})
        else:
            self._send_response({"error": "Endpoint not found"}, status_code=404)


PORT = 8000
with socketserver.TCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
