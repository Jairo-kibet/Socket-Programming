import socket

# -----------------------------
# Server Configuration
# -----------------------------
HOST = '127.0.0.1'  # Localhost
PORT = 5000         # Port to listen on

# -----------------------------
# Create TCP Socket
# -----------------------------
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Bind to address and port
    server_socket.listen(1)           # Listen for 1 client connection
    print(f"Server listening on {HOST}:{PORT}...")

    # -----------------------------
    # Accept a Client Connection
    # -----------------------------
    client_socket, client_address = server_socket.accept()
    with client_socket:
        print(f"Connected by {client_address}")

        # -----------------------------
        # Communication Loop
        # -----------------------------
        while True:
            data = client_socket.recv(1024)  # Receive message from client
            if not data:
                # Client disconnected
                print("Client disconnected")
                break

            message = data.decode()
            print(f"Client says: {message}")

            # Send a reply back
            reply = f"Server received: {message}"
            client_socket.sendall(reply.encode())

# Server automatically closes here
print("Server shut down.")