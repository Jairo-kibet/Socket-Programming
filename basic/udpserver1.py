import socket

# -----------------------------
# Server Configuration
# -----------------------------
SERVER_HOST = '127.0.0.1'  # Localhost
SERVER_PORT = 5002         # UDP port

# -----------------------------
# Create UDP Socket
# -----------------------------
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    print(f"UDP Server listening on {SERVER_HOST}:{SERVER_PORT}...\n")

    while True:
        # Receive datagram from client
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received from {client_address}: {message}")

        # Prepare response
        response = f"Server received: {message}"

        # Send response back to the same client
        server_socket.sendto(response.encode(), client_address)