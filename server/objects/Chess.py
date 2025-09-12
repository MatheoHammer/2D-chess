import random
from objects.Pieces import *
from objects.Client import Client

class Chess:
    def __init__(self, player1:Client, player2:Client):
        p1_white = random.randint(0,1)

        if (p1_white):
            self.white = player1
            self.black = player2
        else:
            self.white = player2
            self.black = player1

        self.white.start_game(self, "w")
        self.black.start_game(self, "b")

        self.turn = self.white
        self.not_turn = self.black

        self.board = self.create_default_position()
        self.game_running = False
    
    def get_valid_moves(self, color):
        valid_moves = []
        for row in self.board:
            for piece in row:
                if piece:
                    if piece.type == PAWN or piece.type == ROOK:
                        valid_moves.append(piece.get_valid_moves(self.board))
        
        return valid_moves

    def move(self, move):
        print(move)

        valid_moves = self.get_valid_moves(self.not_turn.piece_color)
        self.not_turn.socket.send(f"player has moved to {move}".encode())

        self.turn, self.not_turn = self.not_turn, self.turn
        self.turn.message_handler = self.move
        self.not_turn.message_handler = None

    def broadcast(self, message):
        message = message.encode()
        self.white.socket.send(message)
        self.black.socket.send(message)

    def create_default_position(self):
        row1_black = [Rook(0,0,"b")] + [None for _ in range(7)]
        pawn_row_black = [None for _ in range(8)]

        row1_white = [Rook(0,7,"w"), Knight(1,7,"w"), Bishop(2,7,"w"), Queen(3,7,"w"), King(4,7,"w"), Bishop(5,7,"w"), Knight(6,7,"w"), Rook(7,7,"w")]
        pawn_row_white = []
        for i in range(8):
            pawn_row_white .append(Pawn(i,6,"w"))

        board = [row1_black, pawn_row_black]
        for i in range(4):
            board.append([None for _ in range(8)])

        board.append(pawn_row_white)
        board.append(row1_white)

        return board
