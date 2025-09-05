class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "pawn"

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "rook"

class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "queen"

class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "king"

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "knight"

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "bishop"