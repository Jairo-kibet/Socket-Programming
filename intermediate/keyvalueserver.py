import socket

# Step 1: socket() → create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind() → assign IP and port
host = '127.0.0.1'
port = 5007
server_socket.bind((host, port))

# Step 3: listen() → start listening for clients
server_socket.listen(5)
print("Key-Value Store Server is running...")

# Step 4: create in-memory key-value store
store = {}

while True:
    # Step 5: accept() → accept client connection
    conn, addr = server_socket.accept()
    print("Connected to:", addr)

    while True:
        # Step 6: recv() → receive command from client
        data = conn.recv(1024).decode()
        if not data:
            break  # client disconnected
        if data.lower() == "exit":
            break

        # Expected command format: INSERT key value | GET key | DELETE key
        parts = data.strip().split(" ", 2)
        command = parts[0].upper()

        if command == "INSERT" and len(parts) == 3:
            key, value = parts[1], parts[2]
            store[key] = value
            response = f"Inserted: {key} => {value}"

        elif command == "GET" and len(parts) == 2:
            key = parts[1]
            response = store.get(key, "Error: Key not found")

        elif command == "DELETE" and len(parts) == 2:
            key = parts[1]
            if key in store:
                del store[key]
                response = f"Deleted: {key}"
            else:
                response = "Error: Key not found"

        else:
            response = "Invalid command. Use INSERT/GET/DELETE"

        # Step 7: send() → send response back to client
        conn.send(response.encode())

    # Step 8: close() → close client connection
    conn.close()
    print("Client disconnected.\n")