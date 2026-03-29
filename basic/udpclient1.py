import socket

# -----------------------------
# Server Configuration
# -----------------------------
SERVER_HOST = '127.0.0.1'  # Server IP (localhost)
SERVER_PORT = 5002         # UDP port used by server

# -----------------------------
# Create UDP Socket
# -----------------------------
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)  # Optional: timeout for server response (seconds)

print(f"UDP Client ready. Sending messages to {SERVER_HOST}:{SERVER_PORT}")
print("Type 'exit' to quit.\n")

try:
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            print("Exiting UDP client...")
            break

        # Send message as a datagram
        client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

        try:
            # Receive response from server
            data, server = client_socket.recvfrom(1024)
            print(f"Server: {data.decode()}")
        except socket.timeout:
            print("No response from server (timeout).")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    client_socket.close()
    print("UDP client closed.")