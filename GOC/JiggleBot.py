from Sprite import Sprite

class JiggleBot(Sprite):
    
    speed = 2
    diameter = 25
    c = color(255, 200, 200)
        
    def move(self):
        self.x += random(-self.speed, self.speed)
        self.y += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)
