import json
from http.server import BaseHTTPRequestHandler, HTTPStatus
from recipes.urls import get_path


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self) -> None:
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'application/json')
        if not self.headers_sent:
            self.end_headers()

    def handle_auth_error(self, error_message: str = "Unauthorized") -> None:
        self.send_response(HTTPStatus.UNAUTHORIZED)
        self.send_header('WWW-Authenticate', 'Basic realm="Vubon Roy"')
        self.send_header('Content-type', 'application/json')
        if not self.headers_sent:
            self.end_headers()
        content = json.dumps({'error': error_message})
        self.wfile.write(bytes(content, 'UTF-8'))

    def do_GET(self) -> None:
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            authentication=self.headers.get('Authorization')
        )
        if status_code == HTTPStatus.UNAUTHORIZED:
            return self.handle_auth_error()
        self.respond(status_code, response)

    def do_POST(self) -> None:
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        try:
            data = json.loads(data_string)
        except json.JSONDecodeError as e:
            return self.handle_json_decode_error(e)
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            data=data,
            authentication=self.headers.get('Authorization')
        )
        if status_code == HTTPStatus.UNAUTHORIZED:
            return self.handle_auth_error()
        self.respond(status_code, response)

    def do_DELETE(self) -> None:
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            authentication=self.headers.get('Authorization')
        )
        if status_code == HTTPStatus.UNAUTHORIZED:
            return self.handle_auth_error()
        self.respond(status_code, response)

    def do_PUT(self) -> None:
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        try:
            data = json.loads(data_string)
        except json.JSONDecodeError as e:
            return self.handle_json_decode_error(e)
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            data=data,
            authentication=self.headers.get('Authorization')
        )
        if status_code == HTTPStatus.UNAUTHORIZED:
            return self.handle_auth_error()
        self.respond(status_code, response)

    def handle_json_decode_error(self, error: json.JSONDecodeError) -> None:
        self.send_response(HTTPStatus.BAD_REQUEST)
        self.send_header('Content-Type', 'application/json')
        if not self.headers_sent:
            self.end_headers()
        content = json.dumps({'error': str(error)})
        self.wfile.write(bytes(content, 'UTF-8'))

    def respond(self, status_code: int, data: dict | None) -> None:
        self.send_response(status_code)
        if data is not None:
            self.send_header('Content-Type', 'application/json')
            content = json.dumps(data)
            if not self.headers_sent:
                self.end_headers()
            self.wfile.write(bytes(content, 'UTF-8'))
        else:
            if not self.headers_sent:
                self.end_headers()