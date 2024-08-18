package dynamic_forward_port_handler

import socket_manager
import socks4a_handler
import event_handler

class DynamicForwardPortHandler:
    def __init__(self, new_connection_chain_args, debug, chan_client, client_addr, client_port):
        self.new_connection_chain_args = new_connection_chain_args
        self.debug = debug
        self.chan_client = chan_client
        self.client_addr = client_addr
        self.client_port = client_port
        self.socket_manager = socket_manager.SocketManager()
        self.socks4a_handler = socks4a_handler.SOCKS4AHandler()
        self.event_handler = event_handler.EventHandler()

    def handle_client_connection(self):
        remote_socket = self.socks4a_handler.establish_remote_connection(self.client_addr, self.client_port)
        if remote_socket:
            self.socket_manager.add_socket(remote_socket)
            self.event_handler.add_event(remote_socket, self.handle_forward_port)

    def forward_port(self, socket):
        data = socket.recv(1024)
        if data:
            self.chan_client.send(data)
        else:
            self.socket_manager.remove_socket(socket)
            self.event_handler.remove_event(socket)

    def handle_client_disconnection(self):
        self.socket_manager.remove_socket(self.chan_client)
        self.event_handler.remove_event(self.chan_client)