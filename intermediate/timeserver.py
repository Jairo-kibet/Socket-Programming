import socket
import datetime  # to get current system time

# Step 1: socket() → create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind() → assign IP and port
host = '127.0.0.1'
port = 5001
server_socket.bind((host, port))

# Step 3: listen() → start listening for clients
server_socket.listen(5)
print("Time server is running and waiting for clients...")

while True:
    # Step 4: accept() → accept client connection
    conn, addr = server_socket.accept()
    print("Connected to:", addr)
    
    # Step 5: recv() → wait for any client message/request
    request = conn.recv(1024).decode()
    if not request:
        conn.close()
        continue

    # Step 6: get current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Step 7: send() → send current time to client
    conn.send(current_time.encode())
    
    # Step 8: close() → close client connection
    conn.close()