from Sprite import Sprite

class ScreenSaverBot(Sprite):
    
    xspeed = 5
    yspeed = 5
    diameter = 25
    c = color(0,255,255)
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.y < 0 or self.y > height:
            self.yspeed *= -1 
        if self.x < 0 or self.x > width:
            self.xspeed *= -1