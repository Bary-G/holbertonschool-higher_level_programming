#!/usr/bin/env python3
"""
Module to set up a basic web server using the http.server module
"""
import http.server
import json


class server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.data == "/":
            self.send_response(200)
            self.send_header("Content-type:", "application/json")
            self.end_header()
            self.wfile.write("Hello, this is a simple API!")
        elif self.data == "/data":
            self.send_response(200)
            self.send_header("Content-type:", "application/json")
            self.end_header()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data))
        elif self.data == "/status":
            self.send_response(200)
            self.send_header("Content-type:", "application/json")
            self.end_header()
            self.wfile.write("OK")
        else:
            self.send_response(404)
            self.send_header("Content-type:", "application/json")
            self.end_header()
            self.wfile.write("Endpoint not found")

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Starting HTTP server on port 8000...")
    httpd.serve_forever()
