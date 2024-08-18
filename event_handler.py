package event_handler

class ClientConnectionEstablishedEventHandler:
    def client_connected(self, connection):
        connection.send("Welcome to the server!")

class ErrorEventHandler:
    def error_occurred(self, connection, error):
        print(f"Error occurred: {error}")
        connection.close()

class ClientDisconnectedEventHandler:
    def client_disconnected(self, connection):
        print(f"Client disconnected: {connection}")