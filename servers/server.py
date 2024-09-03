import json
from http.server import BaseHTTPRequestHandler, HTTPStatus
from recipes.urls import get_path


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def handle_auth(self):
        self.send_response(HTTPStatus.UNAUTHORIZED)
        self.send_header('WWW-Authenticate', 'Basic realm="Vubon Roy"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        return True

    def do_GET(self):
        if not self.headers.get('Authorization'):
            self.handle_auth()
            return

        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            authentication=self.headers.get('Authorization')
        )
        self.respond(status_code, response)

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        try:
            data = json.loads(data_string)
        except json.JSONDecodeError as e:
            self.send_response(HTTPStatus.BAD_REQUEST)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            return

        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            data=data,
            authentication=self.headers.get('Authorization')
        )

        self.respond(status_code, response)

    def do_PUT(self):
        if not self.headers.get('Authorization'):
            self.handle_auth()
            return

        data_string = self.rfile.read(int(self.headers['Content-Length']))
        try:
            data = json.loads(data_string)
        except json.JSONDecodeError as e:
            self.send_response(HTTPStatus.BAD_REQUEST)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            return

        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            data=data,
            authentication=self.headers.get('Authorization')
        )

        self.respond(status_code, response)

    def do_DELETE(self):
        if not self.headers.get('Authorization'):
            self.handle_auth()
            return

        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            authentication=self.headers.get('Authorization')
        )
        self.respond(status_code, response)

    def handle_http(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        content = json.dumps(data).encode('utf-8')
        self.wfile.write(content)

    def respond(self, status_code, data=None):
        if data is not None:
            self.handle_http(status_code, data)
        else:
            self.send_response(status_code)
            self.end_headers()