import select
import socket
import threading

class SOCKSProxy:
    def __init__(self, remote_host, remote_port):
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.socks_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socks_socket.connect((remote_host, remote_port))
        self.connections = [self.socks_socket]
        self.lock = threading.Lock()

    def connect(self):
        return self.socks_socket

    def dynamic_forward_port(self, item):
        with self.lock:
            local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            local_socket.bind(('', 0))
            local_socket.listen(1)
            local_port = local_socket.getsockname()[1]
            forward_thread = threading.Thread(target=self.forward_data, args=(local_socket, item))
            forward_thread.daemon = True
            forward_thread.start()
            return local_port

    def forward_data(self, local_socket, item):
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.connect((self.remote_host, self.remote_port))
        self.connections.append(local_socket)
        self.connections.append(remote_socket)
        while True:
            readable, writable, errored = select.select(self.connections, [], [])
            for sock in readable:
                if sock is local_socket:
                    data = local_socket.recv(4096)
                    if not data:
                        break
                    remote_socket.sendall(data)
                elif sock is remote_socket:
                    data = remote_socket.recv(4096)
                    if not data:
                        break
                    local_socket.sendall(data)
        self.connections.remove(local_socket)
        self.connections.remove(remote_socket)