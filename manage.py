import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello, world!")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {e}".encode('utf-8'))

    def do_POST(self):
        try:
            if 'Content-Length' in self.headers:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                self.send_response(200)
                self.end_headers()
                response = f"Received POST request with body: {body.decode('utf-8')}"
                self.wfile.write(response.encode('utf-8'))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Content-Length header is missing")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {e}".encode('utf-8'))

    def do_PUT(self):
        try:
            if 'Content-Length' in self.headers:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                self.send_response(200)
                self.end_headers()
                response = f"Received PUT request with body: {body.decode('utf-8')}"
                self.wfile.write(response.encode('utf-8'))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Content-Length header is missing")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {e}".encode('utf-8'))

    def do_DELETE(self):
        try:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Resource deleted")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {e}".encode('utf-8'))

def get_host():
    try:
        return socket.gethostname()
    except Exception as e:
        print(f"Error getting hostname: {e}")
        return "localhost"

PORT = 5000

if __name__ == "__main__":
    httpd = HTTPServer((get_host(), PORT), MyHandler)
    print(time.asctime(), f"Server Starts - {get_host()}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print(time.asctime(), f" Server Stops - {get_host()}:{PORT}")