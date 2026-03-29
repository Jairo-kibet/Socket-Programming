import socket

# -----------------------------
# Server Configuration
# -----------------------------
HOST = '127.0.0.1'  # Localhost
PORT = 5001         # Port for echo server

# -----------------------------
# Create TCP Socket
# -----------------------------
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)  # Accept a single client
    print(f"Echo Server listening on {HOST}:{PORT}...")

    # -----------------------------
    # Accept a Client Connection
    # -----------------------------
    client_socket, client_address = server_socket.accept()
    with client_socket:
        print(f"Connected by {client_address}")

        # -----------------------------
        # Echo Loop
        # -----------------------------
        while True:
            data = client_socket.recv(1024)
            if not data:
                print("Client disconnected")
                break

            message = data.decode()
            print(f"Received: {message}")

            # Echo the message back to client
            client_socket.sendall(data)