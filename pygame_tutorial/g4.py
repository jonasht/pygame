import pygame
from pygame.locals import *
from sys import exit



pygame.init()

largura = 640
altura = 480


x:int = largura/2
y:int = altura/2


tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('game')

relogio = pygame.time.Clock()

while True:
    # tempo do jogo, por frames
    relogio.tick(30)
    # loop do jogo 
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
            # if event.key == K_a:
                # x = x - 20
            # if event.key == K_d:
                # x = x +20
            # if event.key == K_w:
                # y = y - 20
            # if event.key == K_s:
                # y = y + 20
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x +20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
        
    # desenhando =-=-=-=
    pygame.draw.rect(tela, (0, 200, 0), (x, y, 40, 50))

    pygame.display.update()