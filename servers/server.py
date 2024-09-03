import json
from http.server import BaseHTTPRequestHandler, HTTPStatus
from urllib.parse import urlparse
from recipes.urls import get_path


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_AUTH(self):
        self.send_response(HTTPStatus.UNAUTHORIZED)
        self.send_header('WWW-Authenticate', 'Basic realm="Vubon Roy"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        status_code, response = get_path(
            path=parsed_path.path,
            request_type=self.command,
            authentication=self.headers.get('Authorization')
        )
        self.respond(status_code, response)

    def do_POST(self):
        try:
            data_string = self.rfile.read(int(self.headers['Content-Length']))
            data = json.loads(data_string)
        except (json.JSONDecodeError, KeyError) as e:
            return self.handle_http(HTTPStatus.BAD_REQUEST, {'error': str(e)})
        
        parsed_path = urlparse(self.path)
        status_code, response = get_path(
            path=parsed_path.path,
            request_type=self.command,
            data=data,
            authentication=self.headers.get('Authorization')
        )

        self.respond(status_code, response)

    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        status_code, response = get_path(
            path=parsed_path.path,
            request_type=self.command,
            authentication=self.headers.get('Authorization')
        )
        self.respond(status_code, response)

    do_PUT = do_POST

    def handle_http(self, status_code, data):
        try:
            self.send_response(status_code)
            if data is not None:
                self.send_header('Content-Type', 'application/json')
                content = json.dumps(data).encode('utf-8')
                self.wfile.write(content)
            else:
                self.end_headers()
        except Exception as e:
            return self.handle_http(HTTPStatus.INTERNAL_SERVER_ERROR, {'error': str(e)})

    def respond(self, status_code, data=None):
        try:
            response = self.handle_http(status_code, data)
            if response is not None and data is not None:
                self.wfile.write(response)
        except Exception as e:
            self.handle_http(HTTPStatus.INTERNAL_SERVER_ERROR, {'error': str(e)})