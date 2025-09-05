import itertools
import pygame as pg

pg.init()

BLACK = pg.Color('black')
WHITE = pg.Color('white')

screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()

def create_background():
    colors = itertools.cycle((WHITE, BLACK))
    tile_size = 40
    width, height = 8*tile_size, 8*tile_size
    background = pg.Surface((width, height))

    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            rect = (x, y, tile_size, tile_size)
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

        screen.fill((60, 70, 90))
        screen.blit(background, (100, 100))

        pg.display.flip()
        clock.tick(30)

    pg.quit()

if __name__ == "__main__":
    main()