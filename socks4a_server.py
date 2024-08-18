import socket
import select

class SOCKS4AServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.inputs = [self.server_socket]
        self.outputs = []
        self.forward_ports = {}

    def listen(self):
        while True:
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
            for sock in readable:
                if sock == self.server_socket:
                    client_socket, address = self.server_socket.accept()
                    self.inputs.append(client_socket)
                else:
                    data = sock.recv(1024)
                    if not data:
                        self.inputs.remove(sock)
                        sock.close()
                    else:
                        forward_port = self.forward_ports.get(sock)
                        if forward_port:
                            forward_port.sendall(data)

    def dynamic_forward_port(self, host, port):
        forward_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        forward_socket.connect((host, port))
        self.forward_ports[forward_socket] = forward_socket
        self.inputs.append(forward_socket)