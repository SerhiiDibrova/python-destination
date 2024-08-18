package backend

import socket
import select

class SocketHandler:
    def __init__(self, sock):
        self.sock = sock

    def setup_events(self):
        return [self.sock], [], []

    def handle_data(self, data):
        raise NotImplementedError

    def forward_to_remote(self, data):
        raise NotImplementedError


class ProxyServer:
    def __init__(self, remote_addr, remote_port):
        self.remote_addr = remote_addr
        self.remote_port = remote_port

    def forward_port(self, client_sock):
        handler = SocketHandler(client_sock)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as remote_sock:
            try:
                remote_sock.connect((self.remote_addr, self.remote_port))
            except socket.error as e:
                print(f"Error connecting to remote server: {e}")
                return

            read_fds, _, _ = select.select([client_sock, remote_sock], [], [])

            while True:
                for sock in read_fds:
                    if sock == client_sock:
                        data = client_sock.recv(4096)
                        if not data:
                            break
                        handler.forward_to_remote(data)
                    elif sock == remote_sock:
                        data = remote_sock.recv(4096)
                        if not data:
                            break
                        handler.handle_data(data)

                read_fds, _, _ = select.select([client_sock, remote_sock], [], [])