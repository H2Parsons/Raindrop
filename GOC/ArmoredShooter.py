import SpriteManager
from BigBullet import BigBullet
from Sprite import Sprite
from Shooter import Shooter

class ArmoredShooter(Sprite, Shooter):
    mark = 0
    wait = 3000
    speed = 3
    diameter = 40 
    Armor = 10   
    
    c = color(150)
    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def display(self):
        fill(self.c)
        strokeWeight(self.Armor)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        strokeWeight(1)
        
    def fire(self, vector):
        if millis() - self.mark > self.wait:
            SpriteManager.spawn(BigBullet(self.x, self.y, vector, self.team))
            self.mark = millis()
    
    def handleCollision(self):
        if self.Armor > 0:
            self.Armor -= 2
        else:
            SpriteManager.destroy(self)
    
