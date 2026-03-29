import socket

# Step 1: socket() → create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect() → connect to server
host = '127.0.0.1'
port = 5007
client_socket.connect((host, port))

print("Connected to Key-Value Store Server.")
print("Commands: INSERT key value | GET key | DELETE key | exit")

while True:
    # Step 3: input → take command from user
    cmd = input("Enter command: ")
    client_socket.send(cmd.encode())  # send command

    if cmd.lower() == "exit":
        break

    # Step 4: recv() → receive response from server
    response = client_socket.recv(1024).decode()
    print("Server:", response)

# Step 5: close() → close connection
client_socket.close()