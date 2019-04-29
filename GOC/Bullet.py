import SpriteManager
from Sprite import Sprite

class Bullet(Sprite):
    xLength = 10
    yLength = 15
    c = color(255, 0 ,0)
    
    def __init__(self, x, y, vector, team):
        self.x = x
        self.y = y
        self.vector = vector
        self.team = team
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y        
        if self.x < 0 or self.x + self.xLength > width or self.y < 0 or self.y + self.yLength > height:
            SpriteManager.destroy(self)