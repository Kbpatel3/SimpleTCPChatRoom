import socket
import threading
import rsa

# Generate public and private keys
public_key, private_key = rsa.newkeys(1024)

# Public key of the other client (server or client)
public_client_key = None


# Ask user if they want to host a server or connect to a server
connection_type = input("Press (1) to host a server, (2) to connect to a server: ")

# If user wants to host a server
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

# If user wants to connect to a server
elif connection_type == "2":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("100.64.15.30", 2000))
    print("Connected to server.")

    # Receive server's public key
    public_client_key = rsa.PublicKey.load_pkcs1(client_socket.recv(1024))

    # Send public key to server
    client_socket.send(public_key.save_pkcs1('PEM'))

# If user enters invalid input
else:
    print("Invalid input.")
    exit()


def send_message(client):
    """
    Send message to client
    :param client: The client socket
    :return: None
    """
    # While the client is connected to the server (or vice versa) send messages
    while True:
        message = input("")
        # Encrypt message with client's public key
        client.send(rsa.encrypt(message.encode(), public_client_key))
        print("You: " + message)


def receive_message(client):
    """
    Receive message from client
    :param client: The client socket
    :return: None
    """
    # While the client is connected to the server (or vice versa) receive messages
    while True:
        # Decrypt message with private key (only the client/server can decrypt the message)
        print("Client: " + rsa.decrypt(client.recv(1024), private_key).decode())


# Start threads to send and receive messages
threading.Thread(target=send_message, args=(client_socket,)).start()
threading.Thread(target=receive_message, args=(client_socket,)).start()
