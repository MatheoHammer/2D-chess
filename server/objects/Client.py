import json
import socket
import threading

from config.constants import *

class Client:
    def __init__(self, name:str, socket:socket.socket, address):
        self.name = name
        self.socket = socket
        self.address = address
        self.searching_match = False
        self.should_listen = True
        self.in_game = False
        self.message_handler = self.lobby_handler

        threading.Thread(target=self.listener).start()

    def send(self, type, payload=None):
        packet = {"type":type, "payload":payload}
        packet = json.dumps(packet).encode()
        self.socket.send(packet)

    def receive(self):
        packet = self.socket.recv(1024).decode()
        packet = json.loads(packet)
        return packet

    def start_game(self, game, piece_color):
        print(f"starting game for {piece_color}, name {self.name}")
        self.game = game
        self.in_game = True
        self.searching_match = False
        self.piece_color = piece_color

        self.send(GAME_FOUND, piece_color)
        
        if piece_color == "w":
            self.message_handler = self.game.move
        else:
            self.message_handler = None

    def lobby_handler(self, type, payload):
        if type == SEARCH_GAME and not self.in_game:
            self.searching_match = True

    def listener(self):
        while self.should_listen:
            try:
                print("listening to client")
                packet = self.receive()
                print(packet)

                if not packet:
                    break

                if self.message_handler:
                    self.message_handler(packet["type"], packet["payload"])

            except ConnectionResetError:
                break

        self.socket.close()
