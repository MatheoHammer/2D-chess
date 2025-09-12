import pygame
from config.constants import *

class Piece:
    def __init__(self, x, y, color, type_code):
        self.x = x
        self.y = y
        self.color = color
        self.type = type_code
        self.scale_x = 1
        self.scale_y = 1
        self.sprite = f"./sprites/{self.color}{self.type}.png"
        self.image_surface = pygame.image.load(self.sprite)

        self.image_surface = pygame.transform.scale(self.image_surface,(self.scale_x,self.scale_y))

        self.rect = self.image_surface.get_rect()

    def draw(self, surface):
        
        self.rect.topleft = (self.x, self.y)

        surface.blit(self.image_surface, self.rect)

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, PAWN)

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, ROOK)

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
