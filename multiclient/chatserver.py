import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

clients = []  # List to store all connected client sockets
clients_lock = threading.Lock()  # Lock to synchronize access

def broadcast(message, sender_socket):
    """Send message to all clients except the sender"""
    with clients_lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    # Remove client if sending fails
                    clients.remove(client)

def handle_client(client_socket, client_address):
    """Handle communication with a single client"""
    print(f"[CONNECTED] {client_address} connected.")
    with clients_lock:
        clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")
            broadcast(f"[{client_address}] {message}", client_socket)
    except:
        pass
    finally:
        with clients_lock:
            clients.remove(client_socket)
        client_socket.close()
        print(f"[DISCONNECTED] {client_address} disconnected.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Chat server running on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True)
        thread.start()

if __name__ == "__main__":
    main()