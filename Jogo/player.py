class Player:
    def __init__(self,x, y):
        #selg.image = Sprite do personagem
        self.x = x
        self.y = y

    def jump(self,puloY):
        self.y -= puloY
        return self.y