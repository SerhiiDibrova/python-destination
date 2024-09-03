import json
from http.server import BaseHTTPRequestHandler, HTTPStatus
from recipes.urls import get_path


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_GET(self):
        try:
            authentication = self.headers.get('Authorization')
            if not authentication:
                status_code = HTTPStatus.UNAUTHORIZED
                response = {'error': 'Missing Authorization header'}
                self.respond(status_code, response)
                return

            status_code, response = get_path(
                path=self.path,
                request_type=self.command,
                authentication=authentication
            )
        except Exception as e:
            status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response = {'error': 'Internal Server Error'}
            self.respond(status_code, response)
            return

        self.respond(status_code, response)

    def do_POST(self):
        try:
            data_string = self.rfile.read(int(self.headers['Content-Length']))
            data = json.loads(data_string)
        except (json.JSONDecodeError, KeyError) as e:
            status_code = HTTPStatus.BAD_REQUEST
            response = {'error': 'Invalid JSON data'}
            self.respond(status_code, response)
            return

        try:
            authentication = self.headers.get('Authorization')
            if not authentication:
                status_code = HTTPStatus.UNAUTHORIZED
                response = {'error': 'Missing Authorization header'}
                self.respond(status_code, response)
                return

            status_code, response = get_path(
                path=self.path,
                request_type=self.command,
                data=data,
                authentication=authentication
            )
        except Exception as e:
            status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response = {'error': 'Internal Server Error'}
            self.respond(status_code, response)
            return

        self.respond(status_code, response)

    def do_DELETE(self):
        try:
            authentication = self.headers.get('Authorization')
            if not authentication:
                status_code = HTTPStatus.UNAUTHORIZED
                response = {'error': 'Missing Authorization header'}
                self.respond(status_code, response)
                return

            status_code, response = get_path(
                path=self.path,
                request_type=self.command,
                authentication=authentication
            )
        except Exception as e:
            status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            response = {'error': 'Internal Server Error'}
            self.respond(status_code, response)
            return

        self.respond(status_code, response)

    def do_PUT(self):
        return self.do_POST()

    def handle_http(self, status_code, data=None):
        if data is not None:
            try:
                content = json.dumps(data)
            except TypeError as e:
                status_code = HTTPStatus.INTERNAL_SERVER_ERROR
                content = json.dumps({'error': 'Failed to serialize response'})
        else:
            content = ''

        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        if status_code == HTTPStatus.UNAUTHORIZED:
            self.send_header('WWW-Authenticate', 'Basic realm="Vubon Roy"')
        self.end_headers()
        self.wfile.write(content.encode())

    def respond(self, status_code, data=None):
        return self.handle_http(status_code, data)