import socket
from objects.Client import Client
from objects.Chess import Chess

HOST = "127.0.0.1"
PORT = 5000

clients = []
chess_games = []

def matchmake():
    print("matchmaking")
    player1 = None
    player2 = None

    for client in clients:
        if client.searching_match:
            player1 = client
            break

    for client in clients:
        if client.searching_match and not client == player1:
            player2 = client
            break

    if not player1 or not player2:
        return

    game = Chess(player1, player2)
    chess_games.append(game)

def handshake(client, address):
    try:
        client.settimeout(10)
        name = client.recv(1024).decode()
        print(name)
        client.settimeout(None)
    except socket.timeout:
        return False

    if not name:
        return False

    return Client(name, client, address)

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"Server started on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        print(f"New connection from {client_address}")

        client = handshake(client_socket, client_address)
        client_socket.send("success".encode())
        print("handshake complete")

        if (not client):
            client_socket.close()
            continue

        clients.append(client)

        matchmake()

if __name__ == "__main__":
    start_server(HOST, PORT)
