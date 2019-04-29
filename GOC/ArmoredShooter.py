import SpriteManager
from BigBullet import BigBullet
from Sprite import Sprite
from Shooter import Shooter

class ArmoredShooter(Sprite, Shooter):
    mark = 0
    wait = 3000
    speed = 3
    xLength = 50
    yLength = 50 
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
        rect(self.x, self.y, self.xLength, self.yLength)
        strokeWeight(1)
        #print(self.Armor)
        
    def fire(self, vector):
        if millis() - self.mark > self.wait:
            SpriteManager.spawn(BigBullet(self.x + self.xLength / 2 - 25, self.y + self.yLength, vector, self.team))
            self.mark = millis()
    
    def handleCollision(self):
        if self.Armor > 0:
            self.Armor -= 2
        else:
            SpriteManager.destroy(self)
            
    def isColliding(self, other):
        if ((self.x < other.x + other.xLength) 
        and (self.x + self.xLength > other.x)
        and (self.y < other.y + other.yLength)
        and (self.y + self.yLength > other.y)):
            return True
        else:
            return False