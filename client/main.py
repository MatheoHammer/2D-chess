import itertools
import pygame as pg
import socket
from config.constants import *
from objects.Pieces import *

def create_default_position(color):
    if color == "w":
        dir = ("w", "b")
    else:
        dir = ("b", "w")

    opposite_row1 = [Rook(0,0,dir[1]), Knight(1,0,dir[1]), Bishop(2,0,dir[1]), Queen(3,0,dir[1]), King(4,0,dir[1]), Bishop(5,0,dir[1]), Knight(6,0,dir[1]), Rook(7,0,dir[1])]
    opposite_pawn_row = []
    for i in range(8):
        opposite_pawn_row.append(Pawn(i,1,dir[1]))

    home_row1 = [Rook(0,7,dir[0]), Knight(1,7,dir[0]), Bishop(2,7,dir[0]), Queen(3,7,dir[0]), King(4,7,dir[0]), Bishop(5,7,dir[0]), Knight(6,7,dir[0]), Rook(7,7,dir[0])]
    home_pawn_row = []
    for i in range(8):
        home_pawn_row.append(Pawn(i,6,dir[0]))

    board = [opposite_row1, opposite_pawn_row]
    for i in range(4):
        board.append([None for _ in range(8)])

    board.append(home_pawn_row)
    board.append(home_row1)

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

    name = input("Name: ")

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((HOST, PORT))

    connection.send(name.encode())

    handshake_status = connection.recv(1024).decode()

    if handshake_status == "falsey":
        return

    connection.send("search_match".encode())

    color = connection.recv(1024).decode()
    print(color)

    board = create_default_position(color)
    background = create_background()

    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    running = True
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
