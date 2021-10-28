import Game, pygame
from Game import *

size = (800,600)
screen = pygame.display.set_mode(size,0,32)
clock = pygame.time.Clock()

pygame.font.init()
myfont = pygame.font.SysFont('Arial',30)

playGame = myfont.render('Jogar', False, (255,255,255))
optionGame = myfont.render('Opcoes', False, (255,255,255))
quitGame = myfont.render('Sair', False, (255,255,255))
escolha = myfont.render('*', False, (0,0,0))

contador = 0

game = Game()
while True:
    screen.fill((100, 0, 255))
    screen.blit(playGame, (size[0] / 2 - 30, size[1] / 2 - 100))
    screen.blit(optionGame, (size[0] / 2 - 30, size[1] / 2 - 50))
    screen.blit(quitGame, (size[0] / 2 - 30, size[1] / 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_DOWN and contador == 0:
                contador = 1
            elif event.key == K_DOWN and contador == 1:
                contador = 2
            elif event.key == K_UP and contador == 1:
                contador = 0
            elif event.key == K_UP and contador == 2:
                contador = 1

            if event.key == K_SPACE and contador == 2:
                pygame.quit()
                sys.exit()
            if event.key == K_SPACE and contador == 0:
                game.startGame()

    if contador == 0:
        screen.blit(escolha, (size[0] / 2 - 50, size[1] / 2 - 95))
    elif contador == 1:
        screen.blit(escolha,(size[0] / 2 - 50,size[1] / 2 - 45))
    elif contador == 2:
        screen.blit(escolha,(size[0] / 2 - 50,size[1] / 2 + 5))

    pygame.display.update()
    clock.tick(60)
