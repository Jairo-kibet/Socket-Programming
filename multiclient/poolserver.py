import socket
import threading
from queue import Queue

HOST = '127.0.0.1'
PORT = 12345
NUM_WORKERS = 4  # Fixed number of worker threads

# Queue to store incoming client connections
client_queue = Queue()

def handle_client(client_socket, client_address):
    """Function to handle client communication"""
    print(f"[CONNECTED] {client_address} connected.")
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

def worker():
    """Worker thread function"""
    while True:
        client_socket, client_address = client_queue.get()
        if client_socket is None:
            break  # Stop worker
        handle_client(client_socket, client_address)
        client_queue.task_done()

def main():
    # Start worker threads
    for _ in range(NUM_WORKERS):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    # Start server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        # Add client connection to the queue
        client_queue.put((client_socket, client_address))

if __name__ == "__main__":
    main()