import threading
import socket
import time

server = socket.socket()
server.bind(('localhost', 12451))
server.listen(5)
con, addr = server.accept()

def send_data():
    while True:
        try:
            send = input(">>")
            con.sendall(send.encode())
            time.sleep(5)
        except ConnectionResetError:
            print("Connection reset by peer.")
            break
        except BrokenPipeError:
            print("Broken pipe error.")
            break

def recv_data():
    while True:
        try:
            data_recv = con.recv(1024)
            if not data_recv:
                print("Client disconnected.")
                break
            print(data_recv.decode())
            time.sleep(5)
        except ConnectionResetError:
            print("Connection reset by peer.")
            break
        except BrokenPipeError:
            print("Broken pipe error.")
            break

threading.Thread(target=send_data).start()
threading.Thread(target=recv_data).start()