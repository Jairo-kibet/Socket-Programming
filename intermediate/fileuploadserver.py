import socket

# Step 1: socket() → create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind() → assign IP and port
host = '127.0.0.1'
port = 5003
server_socket.bind((host, port))

# Step 3: listen() → start listening for clients
server_socket.listen(5)
print("File server is running and waiting for clients...")

# Step 4: accept() → accept client connection
conn, addr = server_socket.accept()
print("Connected to:", addr)

# Step 5: receive file name
file_name = conn.recv(1024).decode()
print(f"Receiving file: {file_name}")

# Step 6: receive file data
with open(f"received_{file_name}", "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully!")

# Step 7: close() → close connection
conn.close()
server_socket.close()