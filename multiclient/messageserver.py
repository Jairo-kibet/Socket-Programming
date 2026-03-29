import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

clients = {}  # Dictionary to store client sockets and usernames
clients_lock = threading.Lock()

def broadcast(message, sender_socket):
    """Send message to all clients except sender"""
    with clients_lock:
        for client, username in clients.items():
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    # Remove disconnected clients
                    client.close()
                    del clients[client]

def handle_client(client_socket):
    """Handle messages from a single client"""
    # Ask client for a username
    client_socket.send("Enter your username: ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8').strip()
    with clients_lock:
        clients[client_socket] = username

    broadcast(f"[SERVER] {username} has joined the chat.", client_socket)
    print(f"[CONNECTED] {username} connected.")

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            full_message = f"[{username}] {message}"
            print(full_message)
            broadcast(full_message, client_socket)
    except:
        pass
    finally:
        with clients_lock:
            del clients[client_socket]
        client_socket.close()
        broadcast(f"[SERVER] {username} has left the chat.", None)
        print(f"[DISCONNECTED] {username} disconnected.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Broadcast server running on {HOST}:{PORT}")

    while True:
        client_socket, _ = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket,), daemon=True)
        thread.start()

if __name__ == "__main__":
    main()