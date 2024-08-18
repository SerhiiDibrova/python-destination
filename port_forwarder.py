import socket
import select
import threading

def dynamic_forward_port(listen_chain, new_connection_chain, debug_settings):
    server_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_handler.bind(listen_chain)
    server_handler.listen(1)

    if debug_settings:
        print(f"Listening on {listen_chain}")

    while True:
        readable, writable, errored = select.select([server_handler], [], [], 0)
        for sock in readable:
            client_socket, address = server_handler.accept()
            if debug_settings:
                print(f"Accepted connection from {address}")
            handler_thread = threading.Thread(target=dynamic_forward_port_handler, args=(client_socket, new_connection_chain, debug_settings))
            handler_thread.start()

def ip_c4_to_text(ip_c4):
    return ".".join(map(str, ip_c4))

def dynamic_forward_port_handler(client_socket, new_connection_chain, debug_settings):
    forward_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    forward_socket.connect(new_connection_chain)

    if debug_settings:
        print(f"Connected to {new_connection_chain}")

    while True:
        readable, writable, errored = select.select([client_socket, forward_socket], [], [], 0)
        for sock in readable:
            if sock == client_socket:
                data = client_socket.recv(1024)
                if not data:
                    break
                forward_socket.sendall(data)
            else:
                data = forward_socket.recv(1024)
                if not data:
                    break
                client_socket.sendall(data)

def forward_port(listen_chain, new_connection_chain):
    server_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_handler.bind(listen_chain)
    server_handler.listen(1)

    while True:
        readable, writable, errored = select.select([server_handler], [], [], 0)
        for sock in readable:
            client_socket, address = server_handler.accept()
            handler_thread = threading.Thread(target=forward_port_handler, args=(client_socket, new_connection_chain))
            handler_thread.start()

def forward_port_handler(client_socket, new_connection_chain):
    forward_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    forward_socket.connect(new_connection_chain)

    while True:
        readable, writable, errored = select.select([client_socket, forward_socket], [], [], 0)
        for sock in readable:
            if sock == client_socket:
                data = client_socket.recv(1024)
                if not data:
                    break
                forward_socket.sendall(data)
            else:
                data = forward_socket.recv(1024)
                if not data:
                    break
                client_socket.sendall(data)

def vwait():
    while True:
        pass