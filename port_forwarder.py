import socket
import threading

class PortForwarder:
    def __init__(self, remote_host, remote_port):
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', 0))
        self.local_port = self.server_socket.getsockname()[1]
        self.server_socket.listen(1)

    def forward_port(self, option):
        if option == '-L':
            t = threading.Thread(target=self.forward_local_to_remote)
            t.start()
        else:
            raise ValueError("Invalid option")

    def forward_local_to_remote(self):
        client_socket, _ = self.server_socket.accept()
        remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_socket.connect((self.remote_host, self.remote_port))
        threads = []
        threads.append(threading.Thread(target=self.forward_data, args=(client_socket, remote_socket)))
        threads.append(threading.Thread(target=self.forward_data, args=(remote_socket, client_socket)))
        for t in threads:
            t.start()

    def forward_data(self, source_socket, destination_socket):
        while True:
            data = source_socket.recv(1024)
            if not data:
                break
            destination_socket.sendall(data)