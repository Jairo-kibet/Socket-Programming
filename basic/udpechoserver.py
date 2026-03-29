import socket

# -----------------------------
# Server Configuration
# -----------------------------
HOST = '127.0.0.1'
PORT = 5003  # Use a different port from previous UDP server

# -----------------------------
# Create UDP Socket
# -----------------------------
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"UDP Echo Server listening on {HOST}:{PORT}...\n")

    while True:
        # Receive datagram from client
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received from {client_address}: {message}")

        # Echo the message back to the client
        server_socket.sendto(data, client_address)