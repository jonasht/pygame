import pygame
from pygame.locals import *
from sys import exit



pygame.init()

largura = 640
altura = 480


x:int = largura/2
y:int = 0


tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('game')

relogio = pygame.time.Clock()

while True:
    # loop do jogo 
    # tempo do jogo, por frames
    relogio.tick(30)
    # preencher a tela quanto objeto se movimenta
    tela.fill('black')
    
    # eventos dos botoes
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_q:
                print('fechando programa')
                pygame.quit()
                exit()

    # desenhando =-=-=-=
    pygame.draw.rect(tela, (0, 200, 0), (x, y, 40, 50))
    if y >= altura:
        y = 0
    y = y + 1

    pygame.display.update()