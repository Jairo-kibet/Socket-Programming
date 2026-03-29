import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    print(f"UDP Server listening on {SERVER_HOST}:{SERVER_PORT}...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received from {client_address}: {message}")
        # Echo back the message
        server_socket.sendto(f"Echo: {message}".encode(), client_address)