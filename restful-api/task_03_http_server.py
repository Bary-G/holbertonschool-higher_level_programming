#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))
        
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            message = "OK"
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info = json.dumps(info)
            self.wfile.write(json_info.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            error_message = "Endpoint not found"
            self.wfile.write(error_message.encode("utf-8"))


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Starting HTTP server on port 8000...")
    httpd.serve_forever()
