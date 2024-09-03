```python
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
            self.wfile.write(str(e).encode())

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"POST request received")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    def do_PUT(self):
        try:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"PUT request received")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    def do_DELETE(self):
        try:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"DELETE request received")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

def get_host():
    try:
        return socket.gethostname()
    except Exception as e:
        print("Error getting hostname:", str(e))
        return "localhost"

PORT = 5000

if __name__ == "__main__":
    try:
        httpd = HTTPServer((get_host(), PORT), MyHandler)
        print(time.asctime(), f"Server Starts - {get_host()}:{PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print(time.asctime(), f"Server Stops - {get_host()}:{PORT}")
    except Exception as e:
        print("Error starting server:", str(e))
```