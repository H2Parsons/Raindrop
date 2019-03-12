import SpriteManager
from Bullet import Bullet
from Sprite import Sprite
from Shooter import Shooter

class ArmoredShooter(Sprite, Shooter):
    mark = 0
    wait = 1000
    speed = 3
    diameter = 40    
    
    c = color(150)
    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
        
