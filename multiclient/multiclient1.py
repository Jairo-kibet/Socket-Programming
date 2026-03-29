import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Server IP
PORT = 12345        # Server Port

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break  # Server closed connection
            print(f"[SERVER] {message}")
        except:
            print("[ERROR] Connection closed by server.")
            break

# Main client function
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[CONNECTED] Connected to server {HOST}:{PORT}")

    # Start a thread to receive messages from the server
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.daemon = True  # Allows the thread to close when main thread exits
    thread.start()

    # Main loop to send messages to the server
    try:
        while True:
            message = input()
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        print("\n[DISCONNECTED] Closing connection.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()