import random
from Pieces import *
from Client import *

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

        self.board = self.create_default_position()

    def broadcast(self, message):
        self.white.socket.send(message)
        self.black.socket.send(message)

    def create_default_position(self):
        row1_black = [Rook(0,0,"b"), Knight(1,0,"b"), Bishop(2,0,"b"), Queen(3,0,"b"), King(4,0,"b"), Bishop(5,0,"b"), Knight(6,0,"b"), Rook(7,0,"b")]
        pawn_row_black = []
        for i in range(8):
            pawn_row_black.append(Pawn(i,1,"b"))

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
