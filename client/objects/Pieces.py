import pygame
from config.constants import *

class Piece:
    def __init__(self, x, y, color, type_code):
        self.x = x
        self.y = y
        self.hovering = False
        self.hover_x = 0
        self.hover_y = 0
        self.color = color
        self.type = type_code
        self.sprite = f"./sprites/{self.color}{self.type}.png"
        self.image_surface = pygame.image.load(self.sprite)

        self.image_dimention_diff = self.image_surface.get_height()/self.image_surface.get_width()

        self.image_surface = pygame.transform.scale(self.image_surface, (TILE_SIZE*0.5,TILE_SIZE*0.5 * self.image_dimention_diff))

        self.rect = self.image_surface.get_rect()

    def draw(self, surface):
        if self.hovering:
            return

        pos_x = self.x * TILE_SIZE + (TILE_SIZE - self.rect.width) // 2 + BOARD_OFFSET_X
        pos_y = self.y * TILE_SIZE + (TILE_SIZE - self.rect.height) // 2 + BOARD_OFFSET_Y

        self.rect.topleft = (pos_x, pos_y)

        surface.blit(self.image_surface, self.rect)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint((mouse_pos[0], mouse_pos[1]))


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
