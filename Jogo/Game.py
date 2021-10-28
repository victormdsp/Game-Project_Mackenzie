import sys, pygame
from pygame.locals import *
from player import Player
from enemy import Enemy

pygame.init()

class Game:
    def __init__(self):
        self.tempo = 0
        self.distancia = 0
        self.font = pygame.font.SysFont('Arial', 30)

    def startGame(self):
        size = (800,600)
        screen = pygame.display.set_mode(size, 0, 32)

        clock = pygame.time.Clock()

        playerPosition = [20, 480]
        pulo = 0

        player = Player(playerPosition[0], playerPosition[1])
        enemy = Enemy()

        #Variavel teste cenario
        x = 800

        while True:
            # Texto Distancia e Tempo
            textDistancia = self.font.render(str(self.distancia // 1), False, (255, 0, 0))
            textTimer = self.font.render(str(self.tempo // 60), False, (255, 0, 0))
            x -= 3

            if x <= -180:
                x = 820

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if pulo == 0:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            pulo = 1

            if pulo == 1:
                player.jump(5)
                if player.y <= 400:
                    pulo = 2

            elif pulo == 2 and player.y < 480:
                player.jump(-2)

            else:
                pulo = 0


            self.distancia += 0.1
            self.tempo += 1
            enemy.moveX()

            screen.fill((255, 255, 255))
            screen.blit(textDistancia, (0, 0))
            screen.blit(textTimer, (size[0] - 30, 0))
            pygame.draw.rect(screen, (0, 0, 255), (20, player.y, 20, 20))
            pygame.draw.rect(screen, (255, 0, 0), (enemy.x, 480, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (0, size[1] - 100, 800, size[0]), 0)
            pygame.draw.rect(screen, (255, 255, 255), (x, 540, 180, 20))
            pygame.display.update()

            clock.tick(60)