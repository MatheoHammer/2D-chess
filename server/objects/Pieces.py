from config.constants import *

class Piece:
    def __init__(self, x, y, color, type_code):
        self.x = x
        self.y = y
        self.color = color
        self.type = type_code
        self.moved = False

    def get_diagonal_moves(self, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            nx, ny = self.x, self.y
            while True:
                nx += dx
                ny += dy

                # Out of bounds
                if not (0 <= nx < len(board[0]) and 0 <= ny < len(board)):
                    break

                target = board[ny][nx]
                if target is None:
                    moves.append((nx, ny))
                else:
                    if target.color != self.color:
                        moves.append((nx, ny))  # capture
                    break

        return moves
    
    def get_straight_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            nx, ny = self.x, self.y
            while True:
                nx += dx
                ny += dy

                # Out of bound
                if not (0 <= nx < len(board[0]) and 0 <= ny < len(board)):
                    break

                target = board[ny][nx]

                if target is None:
                    moves.append((nx, ny))
                else:
                    if target.color != self.color:
                        moves.append((nx, ny)) #capture
                    break

        return moves



class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, PAWN)

    def get_valid_moves(self, board):
        moves = []
        direction = -1 if self.color == "w" else 1

        nx, ny = self.x, self.y + direction
        if 0 <= ny < len(board) and board[ny][nx] is None:
            moves.append((nx, ny))

            # Two steps ahead
            if not self.moved:
                ny2 = ny + direction
                if board[ny2][nx] is None:
                    moves.append((nx, ny2))

        # Diagonal captures
        for dx in (-1, 1):
            nx, ny = self.x + dx, self.y + direction
            if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                target = board[ny][nx]
                if target is not None and target.color != self.color:
                    moves.append((nx, ny))

        return moves

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, ROOK)

    def get_valid_moves(self, board):
        return self.get_straight_moves(board)

class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, QUEEN)

    def get_valid_moves(self, board):
        return self.get_straight_moves(board) + self.get_diagonal_moves(board)

class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, KING)

    def get_valid_moves(self, board):
        moves = []
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]

        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy

            # Out of bounds
            if not (0 <= nx < len(board[0]) and 0 <= ny < len(board)):
                continue

            target = board[ny][nx]
            if target is None:
                moves.append((nx, ny))
            elif target.color != self.color:
                moves.append((nx, ny))

        return moves

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, KNIGHT)

    def get_valid_moves(self, board):
        moves = []
        directions = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy

            # Out of bounds
            if not (0 <= nx < len(board[0]) and 0 <= ny < len(board)):
                continue

            target = board[ny][nx]
            if target is None or target.color != self.color:
                moves.append((nx, ny))

        return moves

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, BISHOP)

    def get_valid_moves(self, board):
        return self.get_diagonal_moves(board)
