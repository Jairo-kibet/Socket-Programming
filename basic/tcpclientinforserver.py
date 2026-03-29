import socket

# -----------------------------
# Server Configuration
# -----------------------------
HOST = '127.0.0.1'
PORT = 5004

# -----------------------------
# Create TCP Socket
# -----------------------------
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)  # Accept single client
    print(f"Server listening on {HOST}:{PORT}...\n")

    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    with client_socket:
        # Display client IP and port
        print(f"Client connected from IP: {client_address[0]}, Port: {client_address[1]}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                print("Client disconnected")
                break

            message = data.decode()
            print(f"Received from client: {message}")

            # Send reply
            reply = f"Server received: {message}"
            client_socket.sendall(reply.encode())