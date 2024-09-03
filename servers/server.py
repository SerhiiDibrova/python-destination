```python
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
        if status_code == HTTPStatus.UNAUTHORIZED:
            self.do_AUTHHEAD()
        else:
            self.respond(status_code, response)

    def do_POST(self):
        try:
            data_string = self.rfile.read(int(self.headers['Content-Length']))
            data = json.loads(data_string)
        except (json.JSONDecodeError, ValueError) as e:
            status_code = HTTPStatus.BAD_REQUEST
            response = {'error': 'Invalid JSON'}
            self.respond(status_code, response)
            return

        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            data=data,
            authentication=self.headers.get('Authorization')
        )
        if status_code == HTTPStatus.UNAUTHORIZED:
            self.do_AUTHHEAD()
        else:
            self.respond(status_code, response)

    def do_DELETE(self):
        status_code, response = get_path(
            path=self.path,
            request_type=self.command,
            authentication=self.headers.get('Authorization')
        )
        if status_code == HTTPStatus.UNAUTHORIZED:
            self.do_AUTHHEAD()
        else:
            self.respond(status_code, response)

    do_PUT = do_POST

    def handle_http(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        content = json.dumps(data).encode('utf-8')
        return content

    def respond(self, status_code, data=None):
        response = self.handle_http(status_code, data)
        self.wfile.write(response)
```