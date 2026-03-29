import socket
from multiprocessing import Process, Manager

HOST = '127.0.0.1'
PORT = 12345

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")
            client_socket.send(f"Server received: {message}".encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] {client_address}: {e}")
    finally:
        print(f"[DISCONNECTED] {client_address} disconnected.")
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        # Use multiprocessing.Process instead of fork
        process = Process(target=handle_client, args=(client_socket, client_address))
        process.daemon = True  # Optional: closes process when main program exits
        process.start()

if __name__ == "__main__":
    main()