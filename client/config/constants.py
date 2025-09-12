import pygame as pg
pg.init()

def get_screen_dimentions():
    info = pg.display.Info()
    return info.current_w/2, info.current_h/2

#Colors
BLACK = pg.Color('#623f33')
WHITE = pg.Color('#f7cd90')
BACKGROUND_COLOR = (60, 70, 90)

#Global dimentions
WIDTH, HEIGHT = get_screen_dimentions()
TILE_SIZE = int(HEIGHT*0.7/8)
BOARD_DIMENTION=TILE_SIZE*8
BOARD_OFFSET_X = WIDTH/2-HEIGHT*0.7/2
BOARD_OFFSET_Y = HEIGHT*0.15

#Pieces
PAWN = "p"
KNIGHT = "kn"
KING = "k"
QUEEN = "q"
BISHOP = "b"
ROOK = "r"

#Server connection info
HOST = "127.0.0.1"
PORT = 5000

#Network packet types
SEARCH_GAME = "search_game"
GAME_FOUND = "game_found"
HANDSHAKE = "handshake"
SUCCESS = "success"
FAILED = "failed"
