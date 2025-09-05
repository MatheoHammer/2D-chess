import socket
import threading

class Client:
    def __init__(self, name:str, socket:socket.socket, address):
        self.name = name
        self.socket = socket
        self.address = address
        self.searching_match = False
        self.should_listen = True
        self.in_game = False
        self.message_handler = self.lobby_handler

        self.listen()
        threading.Thread(target=self.listen, daemon=True).start()

    def start_game(self, game, piece_color):
        self.game = game
        self.message_handler = self.game_handler
        self.in_game = True
        self.searching_match = False
        self.piece_color = piece_color

    def lobby_handler(self, message):
        if message == "search_match" and not self.in_game:
            self.searching_match = True
    
    def game_handler(self, message):
        if message == "move":
            print("move")

    def listen(self):
        while self.should_listen:
            try:
                message = self.socket.recv(1024).decode()

                if not message:
                    break

                self.message_handler(message)

            except ConnectionResetError:
                break

        self.socket.close()
