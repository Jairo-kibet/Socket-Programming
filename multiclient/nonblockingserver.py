import socket
import select

HOST = '127.0.0.1'
PORT = 12345

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
server.setblocking(False)  # Set non-blocking mode

print(f"[LISTENING] Server listening on {HOST}:{PORT}")

# List of sockets to monitor for incoming data
sockets_list = [server]  
clients = {}  # Map socket to client address

while True:
    # Use select to get sockets ready for reading
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server:
            # New connection
            client_socket, client_address = server.accept()
            client_socket.setblocking(False)
            sockets_list.append(client_socket)
            clients[client_socket] = client_address
            print(f"[CONNECTED] {client_address} connected.")
        else:
            # Existing client sent a message
            try:
                message = notified_socket.recv(1024).decode('utf-8')
                if not message:
                    # Client disconnected
                    print(f"[DISCONNECTED] {clients[notified_socket]} disconnected.")
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    notified_socket.close()
                    continue

                print(f"[{clients[notified_socket]}] {message}")
                # Echo back to client
                notified_socket.send(f"Server received: {message}".encode('utf-8'))
            except:
                # Exception if client abruptly closed
                sockets_list.remove(notified_socket)
                print(f"[ERROR] {clients[notified_socket]} disconnected abruptly.")
                del clients[notified_socket]
                notified_socket.close()

    # Handle exceptional sockets
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        print(f"[ERROR] {clients[notified_socket]} had an error.")
        del clients[notified_socket]
        notified_socket.close()