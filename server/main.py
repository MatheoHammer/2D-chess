import socket
import time
import threading
from objects.Client import Client
from objects.Chess import Chess
from config.constants import *

clients = []
chess_games = []

def matchmake():
    while True:
        time.sleep(3)
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
            continue

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

    threading.Thread(target=matchmake).start()

    print(f"Server started on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        print(f"New connection from {client_address}")

        client = handshake(client_socket, client_address)
        if (not client):
            client_socket.close()
            continue

        client.send(SUCCESS)
        print("handshake complete")

        clients.append(client)

if __name__ == "__main__":
    start_server(HOST, PORT)
