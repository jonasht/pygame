import pygame as pg
from pygame.locals import *
import sys


pg.init()
tela_largura = 640
tela_altura = 480

pg.display.set_caption('game')

tela = pg.display.set_mode((tela_largura, tela_altura))


while True:
    
    # botoes event 
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        if event.type == KEYDOWN:
            pass

    # loop update
    pg.display.update()