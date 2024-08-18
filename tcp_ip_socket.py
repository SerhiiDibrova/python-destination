import socket
import select

class TCPIPSocket:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = [self.socket]

    def bind(self, address, port):
        self.socket.bind((address, port))

    def listen(self):
        self.socket.listen(1)

    def accept(self):
        conn, addr = self.socket.accept()
        self.connections.append(conn)
        return conn, addr

    def event_driven_io(self):
        while True:
            readable, writable, errored = select.select(self.connections, [], [])
            for sock in readable:
                if sock is self.socket:
                    conn, addr = self.accept()
                    print(f"Connected by {addr}")
                else:
                    data = sock.recv(1024)
                    if not data:
                        break
                    print(f"Received from {sock.getpeername()}: {data.decode()}")

    def close(self):
        for conn in self.connections:
            conn.close()