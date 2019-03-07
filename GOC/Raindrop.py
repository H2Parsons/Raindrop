from Sprite import Sprite

class Raindrop(Sprite):
    
    speed = 5
    diameter = 25
    c = color(0,0,255)
        
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > height:
            self.y = 0
