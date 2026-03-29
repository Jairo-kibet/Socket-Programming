import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if not message:
                print("[DISCONNECTED] Server closed connection.")
                break
            print(message)
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    # Start receiving thread
    thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    thread.start()

    try:
        while True:
            msg = input()
            if msg.lower() == "exit":
                break
            client_socket.send(msg.encode('utf-8'))
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()