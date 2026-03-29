import socket
import threading
import sys

HOST = '127.0.0.1'  # Server IP
PORT = 12345        # Server port

# Function to receive messages from server
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if not message:
                print("[DISCONNECTED] Server closed the connection.")
                break
            print(f"[SERVER] {message}")
        except:
            # Socket might have been closed
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[CONNECTED] Connected to server {HOST}:{PORT}")
    print("Type 'exit' to quit.")

    # Start a thread to receive messages asynchronously
    thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    thread.start()

    # Main loop: read user input and send messages
    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                print("[DISCONNECTED] Closing connection.")
                break
            client_socket.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        print("\n[DISCONNECTED] Closing connection.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()