import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # server IP
PORT = 12345        # server port

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[SERVER] {message}")
        except:
            print("[ERROR] Connection closed by server.")
            break

# Main client function
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[CONNECTED] Connected to server {HOST}:{PORT}")

    # Start a thread to listen for incoming messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
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