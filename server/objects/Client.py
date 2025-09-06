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

        threading.Thread(target=self.listen).start()

    def start_game(self, game, piece_color):
        print(f"starting game for {piece_color}, name {self.name}")
        self.game = game
        self.in_game = True
        self.searching_match = False
        self.piece_color = piece_color

        self.socket.send(piece_color.encode())
        
        if piece_color == "w":
            self.message_handler = self.game.move
        else:
            self.message_handler = None

    def lobby_handler(self, message):
        if message == "search_match" and not self.in_game:
            self.searching_match = True

    def listen(self):
        while self.should_listen:
            try:
                print("listening to client")
                message = self.socket.recv(1024).decode()
                print(message + " sent from client")

                if not message:
                    break

                if self.message_handler:
                    self.message_handler(message)

            except ConnectionResetError:
                break

        self.socket.close()
