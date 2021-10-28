import random

class Enemy:
    def __init__(self):
        #self.image = sprite
        self.x = 820
        self.velocidadeX = random.randint(3,6)
    def moveX(self):
        self.x -=  self.velocidadeX
        if self.x <= -20:
            self.x = random.randint(50,250) + 820
        return self.x