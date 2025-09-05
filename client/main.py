import itertools
import pygame as pg
from config.constants import *
from objects.Pieces import *

def create_default_position():
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

def draw_pieces(board, surface):
    for y in range(8):
        for x in range(8):
            if (board[y][x]):
                board[y][x].draw(surface)

def create_background():
    colors = itertools.cycle((WHITE, BLACK))
    background = pg.Surface((BOARD_DIMENTION, BOARD_DIMENTION))

    for y in range(0, BOARD_DIMENTION, TILE_SIZE):
        for x in range(0, BOARD_DIMENTION, TILE_SIZE):
            rect = (x, y, TILE_SIZE, TILE_SIZE)
            pg.draw.rect(background, next(colors), rect)
        next(colors)

    return background

def main():
    running = True

    background = create_background()

    board = create_default_position()
    print(board)


    screen = pg.display.set_mode((0, 0),pg.RESIZABLE)
    clock = pg.time.Clock()


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN: 
                if event.key ==pg.K_ESCAPE:
                    running = False

        screen.fill((60, 70, 90))
        draw_pieces(board, background)
        screen.blit(background, (WIDTH/2-HEIGHT*0.7/2, HEIGHT*0.15))

        pg.display.flip()
        clock.tick(30)

    pg.quit()

if __name__ == "__main__":
    main()
