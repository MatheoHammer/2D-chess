class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "pawn"
