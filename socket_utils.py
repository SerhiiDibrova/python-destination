package socket_utils

import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def bind_socket(sock, local_addr, local_port):
    sock.bind((local_addr, local_port))

def set_socket_options(sock):
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

def forward_port(local_addr, local_port, remote_addr, remote_port):
    sock = create_socket()
    bind_socket(sock, local_addr, local_port)
    set_socket_options(sock)
    sock.listen(1)
    conn, addr = sock.accept()
    remote_sock = create_socket()
    remote_sock.connect((remote_addr, remote_port))
    while True:
        data = conn.recv(1024)
        if not data:
            break
        remote_sock.sendall(data)
    conn.close()
    remote_sock.close()