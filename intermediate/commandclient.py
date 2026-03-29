import socket

# Step 1: socket() → create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect() → connect to server
host = '127.0.0.1'
port = 5005
client_socket.connect((host, port))

while True:
    # Step 3: input → take command from user
    cmd = input("Enter command (or 'exit' to quit): ")
    client_socket.send(cmd.encode())  # send command

    if cmd.lower() == "exit":
        break

    # Step 4: recv() → receive execution result
    result = client_socket.recv(4096).decode()
    print(result)

# Step 5: close() → close connection
client_socket.close()