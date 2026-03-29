import socket
import subprocess

# Step 1: socket() → create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind() → assign IP and port
host = '127.0.0.1'
port = 5005
server_socket.bind((host, port))

# Step 3: listen() → start listening for clients
server_socket.listen(5)
print("Remote Command Server is running...")

while True:
    # Step 4: accept() → accept client connection
    conn, addr = server_socket.accept()
    print("Connected to:", addr)

    while True:
        # Step 5: recv() → receive command from client
        cmd = conn.recv(1024).decode()
        if not cmd:
            break  # client disconnected
        if cmd.lower() == "exit":
            print("Client requested to exit.")
            break

        print(f"Executing command: {cmd}")

        # Step 6: execute command safely
        try:
            # Only allow safe commands (dir, ls, date, echo, etc.)
            allowed_commands = ["dir", "ls", "date", "echo"]
            if cmd.split()[0] in allowed_commands:
                result = subprocess.getoutput(cmd)
            else:
                result = "Error: Command not allowed!"
        except Exception as e:
            result = f"Execution error: {str(e)}"

        # Step 7: send() → send result back to client
        conn.send(result.encode())

    # Step 8: close() → close client connection
    conn.close()
    print("Client disconnected. Waiting for next client...\n")