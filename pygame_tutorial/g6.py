import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

largura = 640
altura = 480


x:int = largura/2
y:int = altura/2

x_azul = randint(40, 600)
y_azul = randint(50, 430)

fonte = pygame.font.SysFont('Arial', 40, True, True)


tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('game')

relogio = pygame.time.Clock()
pontos = 0 

while True:
    # tempo do jogo, por frames
    relogio.tick(30)
    # loop do jogo 
    # preencher a tela quanto objeto se movimenta
    tela.fill('black')
    
    # texto na tela
    mensagem = f'pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    
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
    ret_verde = pygame.draw.rect(tela, (0, 200, 0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40,50))

    if ret_verde.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1

    tela.blit(texto_formatado, (400, 40))
    pygame.display.update()