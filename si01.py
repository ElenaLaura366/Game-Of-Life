from typing import Union

import pygame
import numpy as np
from pygame import Surface, SurfaceType
from pygame.locals import *

col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)

def update(surface, cur, sz):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = col_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            col = col_alive

        col = col if cur[r, c] == 1 else col_background
        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))

    return nxt

def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    eater = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], ###ultima originala
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    eater1 = np.array([[1, 1, 0, 0], [1, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 1]]);
    #pos5 = (64, 70)
    #pos = (20, 95)
    pattern_rot1 = np.rot90(eater, k=-1)
    pattern_rot2 = np.flip(pattern_rot1, axis=-1)
    disturber1 = np.rot90(pattern, k=-1)
    #cells[pos[0]:pos[0] + disturber1.shape[0], pos[1]:pos[1] + disturber1.shape[1]] = disturber1
    pos1 = (4, 15)
    cells[pos1[0]:pos1[0] + pattern.shape[0], pos1[1]:pos1[1] + pattern.shape[1]] = pattern
    pos2 = (5, 61)
    pos3 = (20, 10)
    cells[pos3[0]:pos3[0] + pattern_rot2.shape[0], pos3[1]:pos3[1] + pattern_rot2.shape[1]] = pattern_rot2
    eater_flip = np.flip(pattern, axis=1)
    cells[pos2[0]:pos2[0] + eater_flip.shape[0], pos2[1]:pos2[1] + eater_flip.shape[1]] = eater_flip
    #eater1_flip = np.flip(eater1, axis=1)
    #cells[pos5[0]:pos5[0] + eater1_flip.shape[0], pos5[1]:pos5[1] + eater1_flip.shape[1]] = eater1_flip

    return cells

def main(dimx, dimy, cellsize):
    pygame.init()
    surface: Union[Surface, SurfaceType] = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    font = pygame.font.Font(None, 27)

    cells = init(dimx, dimy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

        surface.fill(col_grid)
        cells = update(surface, cells, cellsize)

        text = font.render("DISTURBER", True, (200, 200, 225))
        text6 = font.render("INPUT B", True, (200, 200, 225))
        text10 = font.render("OUTPUT: 0", True, (200, 200, 225))
        text1 = font.render("I", True, (200, 200, 225))
        text2 = font.render("N", True, (200, 200, 225))
        text3 = font.render("P", True, (200, 200, 225))
        text4 = font.render("U", True, (200, 200, 225))
        text5 = font.render("T", True, (200, 200, 225))
        text7 = font.render("A", True, (200, 200, 225))
        surface.blit(text, (10, 10))
        surface.blit(text6, (500, 10))
        surface.blit(text10, (400, 415))
        surface.blit(text1, (33, 150))
        surface.blit(text2, (30, 170))
        surface.blit(text3, (30, 190))
        surface.blit(text4, (30, 210))
        surface.blit(text5, (30, 230))
        surface.blit(text7, (30, 250))

        pygame.display.update()

if __name__ == "__main__":
    main(120, 90, 6)