import socket
import selectors

HOST = '0.0.0.0'
PORT = 12345

sel = selectors.DefaultSelector()  # Cross-platform selector

# Create and register the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()
server.setblocking(False)

print(f"[LISTENING] Event-driven server on {HOST}:{PORT}")
sel.register(server, selectors.EVENT_READ, data=None)

clients = {}  # Map client socket to address

def accept_connection(sock):
    client_socket, client_address = sock.accept()
    print(f"[CONNECTED] {client_address} connected.")
    client_socket.setblocking(False)
    sel.register(client_socket, selectors.EVENT_READ, data=client_address)
    clients[client_socket] = client_address

def handle_client(sock):
    try:
        data = sock.recv(1024)
        if data:
            message = data.decode('utf-8')
            print(f"[{clients[sock]}] {message}")
            sock.send(f"Server received: {message}".encode('utf-8'))
        else:
            # Client disconnected
            print(f"[DISCONNECTED] {clients[sock]} disconnected.")
            sel.unregister(sock)
            sock.close()
            del clients[sock]
    except:
        sel.unregister(sock)
        sock.close()
        del clients[sock]

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            sock = key.fileobj
            if key.data is None:
                accept_connection(sock)
            else:
                handle_client(sock)
finally:
    sel.close()
    server.close()