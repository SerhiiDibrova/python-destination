import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def bind_socket(sock, local_address, local_port):
    sock.bind((local_address, local_port))

def set_socket_options(sock):
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def forward_port(local_address, local_port, remote_host, remote_port):
    sock = create_socket()
    bind_socket(sock, local_address, local_port)
    set_socket_options(sock)
    sock.connect((remote_host, remote_port))
    return sock