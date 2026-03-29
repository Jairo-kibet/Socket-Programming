import socket

# Step 1: socket() → create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect() → connect to server
host = '127.0.0.1'
port = 5004
client_socket.connect((host, port))

# Step 3: send() → send file name to server
file_name = input("Enter the file name to download: ")
client_socket.send(file_name.encode())

# Step 4: recv() → receive file data and save
with open(f"downloaded_{file_name}", "wb") as f:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        if data.startswith(b"ERROR"):  # check if server returned error
            print(data.decode())
            break
        f.write(data)

print("File download complete!")

# Step 5: close() → close connection
client_socket.close()