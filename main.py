import socket
import threading
import rsa

# Generate public and private keys
public_key, private_key = rsa.newkeys(1024)
public_client_key = None


connection_type = input("Press (1) to host a server, (2) to connect to a server: ")

if connection_type == "1":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("100.64.15.30", 2000))
    server_socket.listen(1)
    print("Server started, waiting for connection...")

    client_socket, _ = server_socket.accept()
    print("Client connected.")

    # Send public key to client
    client_socket.send(public_key.save_pkcs1('PEM'))

    # Receive client's public key
    public_client_key = rsa.PublicKey.load_pkcs1(client_socket.recv(1024))

elif connection_type == "2":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("100.64.15.30", 2000))
    print("Connected to server.")

    # Receive server's public key
    public_client_key = rsa.PublicKey.load_pkcs1(client_socket.recv(1024))

    # Send public key to server
    client_socket.send(public_key.save_pkcs1('PEM'))
else:
    print("Invalid input.")
    exit()


def send_message(client):
    while True:
        message = input("")
        client.send(rsa.encrypt(message.encode(), public_client_key))
        print("You: " + message)


def receive_message(client):
    while True:
        print("Client: " + rsa.decrypt(client.recv(1024), private_key).decode())


threading.Thread(target=send_message, args=(client_socket,)).start()
threading.Thread(target=receive_message, args=(client_socket,)).start()
