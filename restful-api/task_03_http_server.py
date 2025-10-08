#!/usr/bin/python3
"""
Module : A Python file that runs functions.
http : A library used for web functions.
server : A module used for basic web server.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    """A basic HTML server"""
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        message = "Hello, this is a simple API!"
        self.wfile.write(message.encode("utf-8"))

host = "localhost"
port = 8000
server = HTTPServer((host, port), MyServer)
print(f"Serveur HTTP lancé sur http://{host}:{port}")

server.serve_forever()
