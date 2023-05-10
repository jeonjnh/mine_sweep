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
pygame.display.set_caption('Mine Sweeper')
FPSCLOCK = pygame.time.Clock()

#----Functions----#

# function count bomb
def num_of_bomb(field, x_pos, y_pos):
    count = 0
    for yoffset in range(-1,2): # y(-1,1)
        for xoffset in range(-1,2): #x(-1,1)
            xpos = x_pos + xoffset
            ypos = y_pos + yoffset
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == BOMB:
                count += 1
    return count

# function set bomb
def set_bomb(field):
    count = 0
    while count < NUMBER_OF_BOMS:
        xpos, ypos = randint(0, WIDTH-1), randint(0, HEIGHT-1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count += 1

# function tile open
def open_tile(field, x_pos, y_pos):
    global OPEN_COUNT
    if CHECKED[y_pos][x_pos]:
        return
    
    CHECKED[y_pos][x_pos] = True

    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos = x_pos + xoffset
            ypos = y_pos + yoffset
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and not(xpos == x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)

#----Main----#

def main():
    running = True

    smallfont = pygame.font.SysFont(None, 36)

    game_over = False
    field = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # set BOMB
    set_bomb(field)
    
    while running:
        FPSCLOCK.tick(15)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                xpos = floor(event.pos[0]/SIZE)
                ypos = floor(event.pos[1]/SIZE)
                if field[ypos][xpos] == BOMB:
                    game_over = True
                else:
                    open_tile(field,xpos,ypos)

        # draw
        SURFACE.fill((0,0,0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos*SIZE, ypos*SIZE, SIZE, SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE, (192,192,192), rect)
                elif tile == OPENED:
                    count = num_of_bomb(field, xpos,ypos)
                    if count > 0:
                        num_image = smallfont.render("{}".format(count), True, (255, 255, 0))
                        SURFACE.blit(num_image,(xpos*SIZE+10, ypos*SIZE+10))

        for index in range(0,WIDTH*SIZE, SIZE): # draw vertical line
            pygame.draw.line(SURFACE, (96,96,96), (index, 0), (index, HEIGHT*SIZE))
        
        for index in range(0,HEIGHT*SIZE, SIZE): # draw horizontal line
            pygame.draw.line(SURFACE, (96,96,96), (0, index), (WIDTH*SIZE, index))

        pygame.display.update()
        
    pygame.quit()


if __name__ == '__main__':
    main()