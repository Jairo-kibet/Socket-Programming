import socket
import os

# Step 1: socket() → create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind() → assign IP and port
host = '127.0.0.1'
port = 5004
server_socket.bind((host, port))

# Step 3: listen() → start listening for clients
server_socket.listen(5)
print("Persistent File Download Server is running...")

while True:
    # Step 4: accept() → accept client connection
    conn, addr = server_socket.accept()
    print("Connected to:", addr)

    while True:
        # Step 5: recv() → receive requested file name
        file_name = conn.recv(1024).decode()
        if not file_name:
            break  # client disconnected
        if file_name.lower() == "exit":
            print("Client requested to exit.")
            break

        print(f"Client requested: {file_name}")

        # Step 6: check if file exists and send file data
        if os.path.exists(file_name):
            with open(file_name, "rb") as f:
                data = f.read(1024)
                while data:
                    conn.send(data)
                    data = f.read(1024)
            print(f"{file_name} sent successfully!")
        else:
            conn.send(b"ERROR: File not found")
            print(f"{file_name} not found!")

    # Step 7: close() → close client connection
    conn.close()
    print("Client disconnected. Waiting for next client...\n")