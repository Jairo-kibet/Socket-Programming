import socket

# Step 1: socket() → create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind() → assign IP and port
host = '127.0.0.1'
port = 5000
server_socket.bind((host, port))

# Step 3: listen() → start listening for clients
server_socket.listen(1)
print("Server is running and waiting for a client...")

# Step 4: accept() → accept client connection
conn, addr = server_socket.accept()
print("Connected to:", addr)

# Step 5: recv() & send() → interactive chat loop
while True:
    # receive message from client
    message = conn.recv(1024).decode()
    if not message:
        break
    if message.lower() == "exit":
        print("Client left the chat.")
        break
    print("Client:", message)

    # send reply to client
    reply = input("Server: ")
    conn.send(reply.encode())
    if reply.lower() == "exit":
        break

# Step 6: close() → close connections
conn.close()
server_socket.close()