import socket

# Step 1: socket() → create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: connect() → connect to server
host = '127.0.0.1'
port = 5006
client_socket.connect((host, port))

# Step 3: input → choose action
action = input("Do you want to register or login? (register/login): ").strip().lower()
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

# Step 4: send() → send action, username, password
client_socket.send(action.encode())
client_socket.send(username.encode())
client_socket.send(password.encode())

# Step 5: recv() → receive response
response = client_socket.recv(1024).decode()
print("Server response:", response)

# Step 6: close() → close connection
client_socket.close()