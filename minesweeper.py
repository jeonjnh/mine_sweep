# Mine Sweeper Game
import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

#----Variables----#
WIDTH = 20              # 20개 가로타일
HEIGHT = 15             # 15개 세로타일
SIZE = 50               # 타일 사이즈
NUMBER_OF_BOMS = 20
EMPTY = 0
BOMB = 1
OPENED = 2
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])
FPSCLOCK = pygame.time.Clock()

#----Functions----#

# function count bomb

# function tile open


#----Main----#

def main():
    running = True

    field = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    while running:
        FPSCLOCK.tick(15)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break

        # draw
        SURFACE.fill((0,0,0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos*SIZE, ypos*SIZE, SIZE, SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE, (192,192,192), rect)

        for index in range(0,WIDTH*SIZE, SIZE): # draw vertical line
            pygame.draw.line(SURFACE, (96,96,96), (index, 0), (index, HEIGHT*SIZE))
        
        for index in range(0,HEIGHT*SIZE, SIZE): # draw horizontal line
            pygame.draw.line(SURFACE, (96,96,96), (0, index), (WIDTH*SIZE, index))

        pygame.display.update()
        
    pygame.quit()


if __name__ == '__main__':
    main()