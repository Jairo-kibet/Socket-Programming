import socket

# Step 1: socket()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect()
host = '127.0.0.1'
port = 5000
client_socket.connect((host, port))

# Step 3: send()
message = "Hello from client!"
client_socket.send(message.encode())

# Step 4: recv()
reply = client_socket.recv(1024).decode()
print("Server replied:", reply)

# Step 5: close()
client_socket.close()