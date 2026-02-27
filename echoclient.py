import socket

HOST = '127.0.0.1'
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    print(f"Connected to Echo Server at {HOST}:{PORT}. Type 'exit' to quit.\n")

    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break

        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Echoed by Server: {data}")

finally:
    client_socket.close()