import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 12345

# Function to continuously receive messages from server
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if not message:
                print("[DISCONNECTED] Server closed the connection.")
                break
            print(f"[SERVER] {message}")
        except:
            break

# Main client function
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.setblocking(True)  # Use blocking mode; reception handled in thread
    print(f"[CONNECTED] Connected to server {HOST}:{PORT}")
    print("Type 'exit' to quit.")

    # Start thread to receive messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    thread.start()

    # Main loop to send messages
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