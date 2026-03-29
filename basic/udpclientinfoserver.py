import socket

HOST = '127.0.0.1'
PORT = 5004

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"UDP Server listening on {HOST}:{PORT}...\n")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode()

        # Display client IP and port
        print(f"Received from IP: {client_address[0]}, Port: {client_address[1]} -> {message}")

        # Reply to client
        server_socket.sendto(f"Server received: {message}".encode(), client_address)