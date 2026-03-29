import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 12345        # port number

# Handle each client connection
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break  # client disconnected
            print(f"[{client_address}] {message}")
            client_socket.send(f"Server received: {message}".encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] {client_address} {e}")
    finally:
        print(f"[DISCONNECTED] {client_address} disconnected.")
        client_socket.close()

# Main server function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        # Create a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()