import socket
from typing import List

def configure_channel(channel_id: int, socket_options: dict) -> None:
    listen_chain_args: List[str] = []
    
    if "L_option" in socket_options:
        listen_chain_args.append(socket_options["L_option"])
        
    if "D_option" in socket_options:
        listen_chain_args.append(socket_options["D_option"])
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", channel_id))
    
    for option in listen_chain_args:
        sock.setsockopt(socket.SOL_SOCKET, int(option), 1)
        
    sock.listen(5)