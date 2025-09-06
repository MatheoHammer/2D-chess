import pygame as pg
pg.init()

def get_screen_dimentions():
    info = pg.display.Info()
    return info.current_w/2, info.current_h/2

BLACK = pg.Color('#623f33')
WHITE = pg.Color('#f7cd90')
WIDTH, HEIGHT = get_screen_dimentions()
TILE_SIZE = int(HEIGHT*0.7/8)
BOARD_DIMENTION=TILE_SIZE*8

PAWN = "p"
KNIGHT = "kn"
KING = "k"
QUEEN = "q"
BISHOP = "b"
ROOK = "r"

HOST = "127.0.0.1"
PORT = 5000
