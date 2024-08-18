import random

class PortAllocator:
    def __init__(self):
        self.allocated_ports = set()

    def allocate_port(self):
        while True:
            port = random.randint(1024, 65535)
            if port not in self.allocated_ports:
                self.allocated_ports.add(port)
                return port

    def release_port(self, port):
        if port in self.allocated_ports:
            self.allocated_ports.remove(port)