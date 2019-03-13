from Sprite import Sprite

class Star(Sprite):
    
    speed = 1
    diameter = 4
    c = color(255)
        
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > height:
            self.y = 0
