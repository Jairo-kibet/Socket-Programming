import socket

# -----------------------------
# Server Configuration
# -----------------------------
HOST = '127.0.0.1'  # Server address (localhost)
PORT = 5001         # Port used by the echo server

# -----------------------------
# Create TCP Socket
# -----------------------------
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Attempt to connect to the server
    client_socket.connect((HOST, PORT))
    print(f"Connected to Echo Server at {HOST}:{PORT}")
    print("Type 'exit' to disconnect.\n")

    # -----------------------------
    # Communication Loop
    # -----------------------------
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            print("Disconnecting...")
            break

        # Send message to the server
        client_socket.send(message.encode())

        # Receive echoed message from server
        data = client_socket.recv(1024).decode()
        print(f"Echoed by Server: {data}")

except ConnectionRefusedError:
    print(f"Cannot connect to server at {HOST}:{PORT}. Make sure the server is running!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the socket
    client_socket.close()
    print("Connection closed.")