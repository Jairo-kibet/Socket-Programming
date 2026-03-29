import socket  # socket
# create socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host = '127.0.0.1'
port = 5000
# bind()
server_socket.bind((host, port)) 
# listen()
server_socket.listen(1)  
print("Server is listening...")
# accept()
conn, addr = server_socket.accept()  
print(f"Connected to {addr}")

while True:
    data = conn.recv(1024).decode()  # recv()

    if not data:
        break

    if data.lower() == "exit":
        break

    print("Client:", data)
 # send()
    reply = input("Server: ")
    conn.send(reply.encode()) 
# close()
conn.close()  
server_socket.close()  