from config.constants import *

class Piece:
    def __init__(self, x, y, color, type_code):
        self.x = x
        self.y = y
        self.color = color
        self.type = type_code
    
    def get_possible_horizontal_moves(self, board):
        possible_moves = []
        x_offset_right = self.x
        x_offset_left = 7-self.x

        for x in range(x_offset_right, 0, -1):
            if not board[self.y][x]:
                possible_moves.append((x-self.x, 0))
            
            elif board[self.y][x].color == self.color:
                break
            
            else:
                possible_moves.append((x-self.x, 0))

        for x in range(self.x+1, x_offset_left+1, 1):
            if not board[self.y][x]:
                possible_moves.append((x-self.x, 0))
            
            elif board[self.y][x].color == self.color:
                break
            
            else:
                possible_moves.append((x-self.x, 0))
        
        return possible_moves

    def get_possible_vertical_moves(self, board):
        possible_moves = []
        y_offset_top = self.y
        y_offset_bottom = 7-self.y

        for y in range(y_offset_top, 0, -1):
            if not board[y][self.x]:
                possible_moves.append((0, y-self.y))
            
            elif board[y][self.x].color == self.color:
                break
            
            else:
                possible_moves.append((0, y-self.y))

        for y in range(self.y+1, y_offset_bottom+1, 1):
            if not board[y][self.x]:
                possible_moves.append((0, y-self.y))
            
            elif board[y][self.x].color == self.color:
                break
            
            else:
                possible_moves.append((0, y-self.y))
        
        return possible_moves


class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, PAWN)
    
    def get_valid_moves(self, board):
        if self.color == "b":
            possible_moves = [(0, 1), (0, 2)]
        else:
            possible_moves = [(0, -1), (0, -2)]
        
        valid_moves = {"original_pos":(self.x, self.y), "moves":[]}

        for move in possible_moves:
            if not board[self.y+move[1]][self.x+move[0]]:
                valid_moves["moves"].append(move)
        
        return valid_moves

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, ROOK)

    def get_valid_moves(self, board):
        valid_moves = {"original_pos":(self.x, self.y), "moves":[]}
        valid_moves["moves"] = self.get_possible_horizontal_moves(board)
        valid_moves["moves"] += self.get_possible_vertical_moves(board)
        
        return valid_moves
class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, QUEEN)

class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, KING)

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, KNIGHT)

class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, BISHOP)
