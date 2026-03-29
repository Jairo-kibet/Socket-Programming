import socket

# Step 1: socket()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind()
host = '127.0.0.1'
port = 5000
server_socket.bind((host, port))

# Step 3: listen()
server_socket.listen(5)
print("Server is listening...")

# Step 4: accept()
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# Step 5: recv()
data = conn.recv(1024).decode()
print("Client says:", data)

# Step 6: send()
reply = "Hello from server!"
conn.send(reply.encode())

# Step 7: close()
conn.close()
server_socket.close()