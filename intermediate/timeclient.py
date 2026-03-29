import socket

# Step 1: socket() → create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect() → connect to server
host = '127.0.0.1'
port = 5001
client_socket.connect((host, port))

# Step 3: send() → send a request message
client_socket.send(b"Request time")  # any message

# Step 4: recv() → receive current time from server
time_data = client_socket.recv(1024).decode()
print("Current Time from Server:", time_data)

# Step 5: close() → close connection
client_socket.close()
