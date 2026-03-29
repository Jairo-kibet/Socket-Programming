import socket

# Step 1: Create socket (IPv4 + TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Define server address
host = "127.0.0.1"   # Server IP
port = 5000          # Server Port

try:
    # Step 3: Connect to server
    client_socket.connect((host, port))
    print("Connected to server")

    # Step 4: Send greeting message
    message = "Hello Server, this is the client!"
    client_socket.send(message.encode())
    print("Message sent")

    # Step 5: Receive response
    response = client_socket.recv(1024).decode()
    print("Server replied:", response)

except Exception as e:
    print("Error:", e)

finally:
    # Step 6: Close connection gracefully
    client_socket.close()
    print("Connection closed")