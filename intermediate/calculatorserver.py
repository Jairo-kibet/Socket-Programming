import socket

# Step 1: socket() → create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind() → assign IP and port
host = '127.0.0.1'
port = 5002
server_socket.bind((host, port))

# Step 3: listen() → start listening for clients
server_socket.listen(5)
print("Calculator server is running and waiting for clients...")

while True:
    # Step 4: accept() → accept client connection
    conn, addr = server_socket.accept()
    print("Connected to:", addr)

    while True:
        # Step 5: recv() → receive arithmetic expression from client
        expr = conn.recv(1024).decode()
        if not expr or expr.lower() == "exit":
            break

        print("Received expression:", expr)

        try:
            # Step 6: evaluate expression safely
            result = eval(expr)  # caution: in real apps, use a safer parser
            response = f"Result: {result}"
        except Exception as e:
            response = f"Error: {str(e)}"

        # Step 7: send() → send result back to client
        conn.send(response.encode())

    # Step 8: close() → close client connection
    conn.close()