import socket

# Step 1: socket() → create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect() → connect to server
host = '127.0.0.1'
port = 5003
client_socket.connect((host, port))

# Step 3: send() → send file name
file_path = input("Enter file path to upload: ")
file_name = file_path.split("/")[-1]  # extract file name
client_socket.send(file_name.encode())

# Step 4: send() → send file data
with open(file_path, "rb") as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)

print("File uploaded successfully!")

# Step 5: close() → close connection
client_socket.close()