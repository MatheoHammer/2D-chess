import itertools
import pygame as pg
from objects.Connection import Connection
from config.constants import *
from objects.Pieces import *
from pvp import start_pvp

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

def create_board():
    colors = itertools.cycle((WHITE, BLACK))
    board = pg.Surface((BOARD_DIMENTION, BOARD_DIMENTION))

    for y in range(0, BOARD_DIMENTION, TILE_SIZE):
        for x in range(0, BOARD_DIMENTION, TILE_SIZE):
            rect = (x, y, TILE_SIZE, TILE_SIZE)
            pg.draw.rect(board, next(colors), rect)
        next(colors)

    return board 

def draw_pieces(pieces, surface):
    for y in range(8):
        for x in range(8):
            if (pieces[y][x]):
                pieces[y][x].draw(surface)

def draw_board(board, surface):
    surface.blit(board, (BOARD_OFFSET_X, BOARD_OFFSET_Y))

def handle_event(event, pieces, hovering_piece, running):
    if event.type == pg.QUIT:
        running = False

    elif event.type == pg.KEYDOWN: 
        if event.key == pg.K_ESCAPE:
            running = False
        elif event.key == pg.K_p:
            start_pvp()


    elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = pg.mouse.get_pos()
        for row in pieces:
            for piece in row:
                if piece and piece.is_hovered(mouse_pos) and not hovering_piece:
                    print("piece hovering")
                    piece.hovering = True
                    hovering_piece = piece

    elif event.type == pg.MOUSEBUTTONUP and event.button == 1 and hovering_piece:
        print("piece not hovering")
        hovering_piece.hovering = False
        hovering_piece = None
    
    return hovering_piece, running


def gameloop(color):
    pieces = create_default_position(color)
    board = create_board()

    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    running = True
    hovering_piece = None
    while running:
        for event in pg.event.get():
            hovering_piece, running = handle_event(event, pieces, hovering_piece, running)

        screen.fill((60, 70, 90))
        draw_board(board, screen)
        draw_pieces(pieces, screen)

        pg.display.flip()
        clock.tick(60)

def main():
    name = input("Name: ")

    connection = Connection(HOST, PORT)
    success = connection.connect(name)

    if not success:
        print("Could not connect to server")
        return

    connection.send(SEARCH_GAME)

    packet = connection.receive()

    if packet["type"] == GAME_FOUND:
        color = packet["payload"]
        print(f"Found game, color:{color}")
        gameloop(color)

    pg.quit()

if __name__ == "__main__":
    main()
