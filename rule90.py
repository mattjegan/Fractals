import pygame
from pygame.locals import *
import sys
import time
import random

WIDTH = 100
HEIGHT = 100

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), False, 32)
    pygame.display.set_caption("Rule 90")

    running = True

    #cells = initialCells()
    cells = emptyPlus()

    while running:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

        pxarray = pygame.PixelArray(screen)
        pxarray = drawRule90(pxarray, cells)

        cells = computeNew(cells)
        #time.sleep(0.5)

        pygame.display.update()

def emptyPlus():
    cells = []
    for cell in xrange(WIDTH*HEIGHT):
        cells.append(1)
    cells[0] = 0
    return cells

def initialCells():
    cells = []
    for cell in xrange(WIDTH*HEIGHT):
        state = random.randint(0, 1)
        cells.append(state)
    return cells

def drawRule90(pxarray, cells):
    curCell = 0
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            if cells[curCell] == 1:
                pxarray[y][x] = (255, 255, 255)
            else:
                pxarray[y][x] = (0, 0, 0)
            curCell += 1
    return pxarray

def computeNew(cells):
    table = []
    previous = cells[-1]
    for e, cell in enumerate(cells):
        next = cells[(e+1)%len(cells)]
        table.append(bool(previous) ^ bool(next))
        previous = cells[e]
    return table

if __name__ == "__main__": main()