import socket
from socket_options import configure_socket_options

def set_up_channel(chan_client):
    listen_socket_options = {}
    
    if 'L_option' in globals():
        listen_socket_options['L_option'] = L_option
    
    if 'D_option' in globals():
        listen_socket_options['D_option'] = D_option
    
    channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    configure_socket_options(channel, listen_socket_options)
    
    return channel