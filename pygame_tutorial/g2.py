import pygame
from pygame.locals import *
from sys import exit



pygame.init()

largura = 640
altura = 480



tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('game')
while True:
    # eventos dos botoes
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key:
                print('fechando programa')
                pygame.quit()
                exit()

    # desenhando =-=-=-=
    # retangulo  255, 0, 0 vermelho 
    pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50))

    # circulo
    pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40)
    
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)
    pygame.display.update()