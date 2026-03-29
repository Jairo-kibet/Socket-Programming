import socket  # socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket

host = '127.0.0.1'
port = 5000

client_socket.connect((host, port))  # connect()

while True:
    message = input("You: ")
    client_socket.send(message.encode())  # send()

    if message.lower() == "exit":
        break

    reply = client_socket.recv(1024).decode()  # recv()
    print("Server:", reply)

client_socket.close()  # close()