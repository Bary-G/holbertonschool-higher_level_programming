#!/usr/bin/python3
"""
Module : A Python file that runs functions.
http : A library used for web functions.
server : A module used for basic web server.
json : A library used for web functions.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MyServer(BaseHTTPRequestHandler):
    """A basic HTML server"""
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=UTF8")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("UTF8"))
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=UTF8")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("UTF8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=UTF8")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info = json.dumps(info)
            self.wfile.write(json_info.encode("UTF8"))
        else:
            return self.send_response(404)


host = "localhost"
port = 8000
server = HTTPServer((host, port), MyServer)
print(f"Serveur HTTP lancé sur http://{host}:{port}")

server.serve_forever()
