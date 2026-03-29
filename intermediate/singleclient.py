import socket

# Step 1: socket() → create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect() → connect to server
host = '127.0.0.1'
port = 5000
client_socket.connect((host, port))

# Step 3: send() & recv() → interactive chat loop
while True:
    # send message to server
    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break

    # receive reply from server
    reply = client_socket.recv(1024).decode()
    print("Server:", reply)
    if reply.lower() == "exit":
        break

# Step 4: close() → close connection
client_socket.close()