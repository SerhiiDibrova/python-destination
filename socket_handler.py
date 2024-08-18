package socket_handler

import socket
import select

class SocketHandler:
    def __init__(self, chain_args):
        self.chain_args = chain_args
        self.sockets = []

    def create_socket(self):
        for arg in self.chain_args:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(arg)
            sock.listen(1)
            self.sockets.append(sock)

    def handle_socket_events(self):
        while True:
            readable, writable, errored = select.select(self.sockets, [], [], 0)
            for sock in readable:
                conn, addr = sock.accept()
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
                conn.close()