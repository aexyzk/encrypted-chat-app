import socket
import threading

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to a specific address and port
server_address = ('172.22.106.223', 12345)
server_socket.bind(server_address)

# Wait for clients to connect
server_socket.listen()

# Store all client sockets
sockets = []

# Broadcasting messages to all connected clients
def broadcast(message):
    for client_socket in sockets:
        client_socket.send(message.encode())

# Handle individual client connections
def handle_client(client_socket):
    while True:
        # Receive messages from the client
        message = client_socket.recv(1024).decode()
        
        if not message:
            # If the client has disconnected, remove its socket from the list
            sockets.remove(client_socket)
            client_socket.close()
            break
            
        # Broadcast the received message to all other connected clients
        broadcast(message)
        
        print(message)

# Accept new client connections
def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        sockets.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()
        print(client_address)

# Start accepting connections in a new thread
threading.Thread(target=accept_connections).start()