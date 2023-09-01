import socket
import threading
import rsa

connection_type = input("Press (1) to host a server, (2) to connect to a server: ")

if connection_type == "1":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("100.64.15.30", 2000))
    server_socket.listen(1)
    print("Server started, waiting for connection...")

    client_socket, _ = server_socket.accept()
    print("Client connected.")

elif connection_type == "2":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("100.64.15.30", 2000))
    print("Connected to server.")