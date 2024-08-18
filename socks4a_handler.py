package socks4a_handler

class SOCKS4AHandler:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.socket = None

    def connect_to_remote_server(self, remote_address, remote_port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server_address, self.server_port))
        request = b'\x04\x01' + bytes([remote_port // 256, remote_port % 256]) + socket.inet_aton(remote_address) + b'\x00'
        self.socket.sendall(request)
        response = self.socket.recv(8)
        if response[0] != 0 or response[1] != 90:
            raise Exception('Failed to establish connection')

    def authenticate_client(self, username, password):
        request = b'\x04\x01' + bytes([0, 0]) + b'\x00' + len(username).to_bytes(1, 'big') + username.encode() + len(password).to_bytes(1, 'big') + password.encode()
        self.socket.sendall(request)
        response = self.socket.recv(8)
        if response[0] != 0 or response[1] != 90:
            raise Exception('Authentication failed')

    def close_connection(self):
        self.socket.close()