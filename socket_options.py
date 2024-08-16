import socket
import argparse

SOCKS_PROTOCOL_REQUIRED = True

class SocketOptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Configure listen socket options')
        self.parser.add_argument('--remote-host', help='Remote host connection', required=True)
        self.parser.add_argument('--bind-port', type=int, help='Bind port for the connection')
        self.args = self.parser.parse_args()

    def configure_socket_options(self):
        if SOCKS_PROTOCOL_REQUIRED:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            if self.args.bind_port:
                self.socket.bind(('', self.args.bind_port))

            self.socket.listen(5)  # Listen for up to 5 connections

    def get_remote_host(self):
        return self.args.remote_host