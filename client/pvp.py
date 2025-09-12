import pygame as pg
from objects.Connection import Connection
from config.constants import *
from objects.PvP_Pieces import *

def start_pvp(surface):
    clock = pg.time.Clock()
    player1 = Rook(100, 100, "b")
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                running = False  # exit back to main loop

        surface.fill(BACKGROUND_COLOR)
        player1.draw(surface)
        pg.display.flip()
        clock.tick(60)