import socket

# Step 1: socket() → create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect() → connect to server
host = '127.0.0.1'
port = 5002
client_socket.connect((host, port))

while True:
    # Step 3: input → take arithmetic expression from user
    expr = input("Enter expression (or 'exit' to quit): ")
    client_socket.send(expr.encode())  # send expression

    if expr.lower() == "exit":
        break

    # Step 4: recv() → receive result from server
    result = client_socket.recv(1024).decode()
    print(result)

# Step 5: close() → close connection
client_socket.close()