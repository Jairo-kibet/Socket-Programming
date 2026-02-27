import socket

HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}. Type 'exit' to disconnect.\n")

    while True:
        message = input("You: ")
        if message.lower() == "exit":
            print("Disconnecting...")
            break

        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")

except ConnectionRefusedError:
    print(f"Cannot connect to server at {HOST}:{PORT}. Make sure the server is running!")

finally:
    client_socket.close()