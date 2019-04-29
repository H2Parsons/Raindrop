import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
from Shooter import Shooter


class Enemy(Sprite, Shooter):
    mark = 0
    wait = 500
    speed = 8
    xLength = 25
    yLength = 25
    
    c = color(0, 0, 255)
    
    def move(self):
        mark = 0
        wait = 1000
        
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)