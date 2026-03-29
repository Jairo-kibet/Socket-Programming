import socket
import json
import os

# Step 1: socket() → create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind() → assign IP and port
host = '127.0.0.1'
port = 5006
server_socket.bind((host, port))

# Step 3: listen() → start listening for clients
server_socket.listen(5)
print("Login Server with Registration is running...")

# Step 4: load or create credentials file
if os.path.exists("credentials.json"):
    with open("credentials.json", "r") as f:
        credentials = json.load(f)
else:
    credentials = {}

while True:
    # Step 5: accept() → accept client connection
    conn, addr = server_socket.accept()
    print("Connected to:", addr)

    # Step 6: recv() → receive action (register/login)
    action = conn.recv(1024).decode()

    # Step 7: recv() → receive username and password
    username = conn.recv(1024).decode()
    password = conn.recv(1024).decode()

    if action.lower() == "register":
        if username in credentials:
            response = "Registration Failed: Username already exists."
        else:
            credentials[username] = password
            # save to file
            with open("credentials.json", "w") as f:
                json.dump(credentials, f)
            response = "Registration Successful"
    
    elif action.lower() == "login":
        if username in credentials and credentials[username] == password:
            response = "Login Successful"
        else:
            response = "Login Failed"
    else:
        response = "Invalid Action"

    # Step 8: send() → send response
    conn.send(response.encode())

    # Step 9: close() → close client connection
    conn.close()
    print("Client disconnected.\n")