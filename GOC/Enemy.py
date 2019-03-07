import SpriteManager
from Sprite import Sprite
from Bullet import Bullet


class Enemy(Sprite):
    
    speed = 8
    diameter = 25
    
    c = color(0, 0, 255)

    
    def move(self):
        mark = 0
        wait = 1000
        Go = True
        
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
        
        mark = 0
        wait = 1000
        Go = True
        
        if(millis() - mark > wait):
            Go = not Go
            mark = millis()
        
            if(Go):
                
                fill(255, 0, 0)
                
            else:
                
                fill(0, 255, 0)
        
        ellipse(50, 50, 50, 50)
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def aim(self, target):
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        Component = (xComponent * xComponent) + (yComponent * yComponent)
        D = sqrt(Component)
        return PVector(4*xComponent/D, 4*yComponent/D) 
    
    def fire(self, vector):
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
            mark = 0
            wait = 1000
            go = True
            
            if(millis() - mark > wait):
                   go = not go
                   mark = millis()
                   
            if(go):
                fill(0)
            else:
                fill(255)
                
            ellipse(100, 100, 50, 50)
