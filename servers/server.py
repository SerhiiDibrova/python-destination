import json
from http.server import BaseHTTPRequestHandler, HTTPStatus
from recipes.urls import get_path


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(HTTPStatus.UNAUTHORIZED)
        self.send_header('WWW-Authenticate', 'Basic realm="Vubon Roy"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
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
            self.end_headers()
            return
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            data=data,
            authentication=self.headers.get('Authorization')
        )

        self.respond(status_code, response)

    def do_DELETE(self):
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            authentication=self.headers.get('Authorization')
        )
        self.respond(status_code, response)

    do_PUT = do_POST

    def handle_http(self, status_code, data=None):
        if not isinstance(status_code, int) or status_code < 100 or status_code > 599:
            raise ValueError("Invalid HTTP status code")
        
        self.send_response(status_code)
        if data is not None:
            self.send_header('Content-Type', 'application/json')
            content = json.dumps(data).encode('utf-8')
            self.wfile.write(content)

    def respond(self, status_code, data=None):
        try:
            self.handle_http(status_code, data)
        except ValueError as e:
            self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.end_headers()
            return