import socket


class ConnectionManager:
    def __init__(self):
        self.socket = None

    def set_up_channel(self, bind_port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("", bind_port))
        self.socket.listen(1)

    def read_identity_string_or_domain_name(self, connection):
        return connection.recv(1024).decode()

    def configure_channel(self, connection, identity_string_or_domain_name):
        connection.sendall(identity_string_or_domain_name.encode())

    def set_up_remote_host(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))