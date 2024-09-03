import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
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
        response = f"Received POST request with body: {body.decode('utf-8')}"
        self.wfile.write(response.encode('utf-8'))

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = f"Received PUT request with body: {body.decode('utf-8')}"
        self.wfile.write(response.encode('utf-8'))

    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"DELETE request received")

def get_host():
    return socket.gethostbyname(socket.gethostname())

PORT = 5000

if __name__ == '__main__':
    try:
        httpd = HTTPServer((get_host(), PORT), MyHandler)
        print(time.asctime(), 'Server Starts - %s:%s' % (get_host(), PORT))
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print(time.asctime(), 'Server Stops - %s:%s' % (get_host(), PORT))
    except Exception as e:
        logging.error(f"An error occurred: {e}")