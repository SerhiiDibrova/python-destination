package socket_manager

import socket

class TCPSocket(socket.socket):
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0):
        super().__init__(family, type, proto)

def create_socket(socket_type=socket.SOCK_STREAM, protocol=socket.IPPROTO_TCP):
    return TCPSocket(type=socket_type, proto=protocol)

def dynamic_forward_port_handler():
    # TO DO: implement dynamic forward port handler functionality
    pass