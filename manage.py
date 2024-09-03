import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, world!")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)

    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Resource deleted")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_CONNECT(self):
        self.send_response(405)  # Method Not Allowed
        self.end_headers()

    def do_PATCH(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)

def get_host():
    return socket.gethostname()

PORT = 5000

if __name__ == "__main__":
    httpd = HTTPServer((get_host(), PORT), MyHandler)
    print(time.asctime(), f"Server Starts - {get_host()}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print(time.asctime(), f"Server Stops - {get_host()}:{PORT}")