import itertools
import pygame as pg


def get_screen_dimentions():
    info = pg.display.Info()
    return info.current_w, info.current_h

pg.init()

BLACK = pg.Color('#623f33')
WHITE = pg.Color('#f7cd90')
WIDTH, HEIGHT = get_screen_dimentions()
TILE_SIZE = int(HEIGHT*0.7/8)
BOARD_DIMENTION=TILE_SIZE*8

screen = pg.display.set_mode((0, 0),pg.RESIZABLE)
clock = pg.time.Clock()


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

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN: 
                if event.key ==pg.K_ESCAPE:
                    running = False

        screen.fill((60, 70, 90))
        screen.blit(background, (WIDTH/2-HEIGHT*0.7/2, HEIGHT*0.15))

        pg.display.flip()
        clock.tick(30)

    pg.quit()

if __name__ == "__main__":
    main()