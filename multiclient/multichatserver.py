import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

rooms = {}  # Dict: room_name -> list of client sockets
clients = {}  # Dict: client_socket -> (username, room_name)
lock = threading.Lock()

def broadcast(message, room_name, sender_socket=None):
    """Send message to all clients in the room, except sender"""
    with lock:
        for client in rooms.get(room_name, []):
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    rooms[room_name].remove(client)
                    del clients[client]

def handle_client(client_socket):
    client_socket.send("Enter your username: ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8').strip()
    
    # Ask client to join a room
    client_socket.send("Enter room to join: ".encode('utf-8'))
    room_name = client_socket.recv(1024).decode('utf-8').strip()

    with lock:
        if room_name not in rooms:
            rooms[room_name] = []
        rooms[room_name].append(client_socket)
        clients[client_socket] = (username, room_name)

    broadcast(f"[SERVER] {username} has joined {room_name}.", room_name, client_socket)
    client_socket.send(f"[INFO] You joined room '{room_name}'. Type 'leave' to exit or 'switch <room>' to join another room.\n".encode('utf-8'))
    print(f"[CONNECTED] {username} joined {room_name}")

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            message = message.strip()

            if message.lower() == 'leave':
                # Leave current room
                with lock:
                    rooms[room_name].remove(client_socket)
                    clients[client_socket] = (username, None)
                client_socket.send(f"[INFO] You left room '{room_name}'. Enter a new room to join: ".encode('utf-8'))
                broadcast(f"[SERVER] {username} left {room_name}.", room_name, client_socket)
                room_name = client_socket.recv(1024).decode('utf-8').strip()
                with lock:
                    if room_name not in rooms:
                        rooms[room_name] = []
                    rooms[room_name].append(client_socket)
                    clients[client_socket] = (username, room_name)
                client_socket.send(f"[INFO] You joined room '{room_name}'.\n".encode('utf-8'))
                broadcast(f"[SERVER] {username} has joined {room_name}.", room_name, client_socket)
            elif message.startswith("switch "):
                # Switch to another room
                new_room = message.split(maxsplit=1)[1].strip()
                with lock:
                    rooms[room_name].remove(client_socket)
                    if new_room not in rooms:
                        rooms[new_room] = []
                    rooms[new_room].append(client_socket)
                    clients[client_socket] = (username, new_room)
                broadcast(f"[SERVER] {username} left {room_name}.", room_name, client_socket)
                broadcast(f"[SERVER] {username} joined {new_room}.", new_room, client_socket)
                room_name = new_room
                client_socket.send(f"[INFO] You switched to room '{room_name}'.\n".encode('utf-8'))
            else:
                # Regular message
                full_message = f"[{username}] {message}"
                print(f"[{room_name}] {full_message}")
                broadcast(full_message, room_name, client_socket)
    except:
        pass
    finally:
        with lock:
            if room_name in rooms and client_socket in rooms[room_name]:
                rooms[room_name].remove(client_socket)
            if client_socket in clients:
                del clients[client_socket]
        client_socket.close()
        broadcast(f"[SERVER] {username} disconnected.", room_name)
        print(f"[DISCONNECTED] {username} disconnected from {room_name}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Multi-room chat server on {HOST}:{PORT}")

    while True:
        client_socket, _ = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket,), daemon=True)
        thread.start()

if __name__ == "__main__":
    main()