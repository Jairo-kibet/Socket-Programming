import socket

# -----------------------------
# Server Configuration
# -----------------------------
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5003

# -----------------------------
# Create UDP Socket
# -----------------------------
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)  # Timeout if server does not respond

print(f"UDP Echo Client ready. Sending messages to {SERVER_HOST}:{SERVER_PORT}")
print("Type 'exit' to quit.\n")

try:
    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break

        # Send message to server
        client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

        try:
            # Receive echoed message from server
            data, server = client_socket.recvfrom(1024)
            print(f"Echoed by Server: {data.decode()}")
        except socket.timeout:
            print("No response from server (timeout).")

finally:
    client_socket.close()
    print("UDP Echo Client closed.")