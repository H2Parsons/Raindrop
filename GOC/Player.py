from SpriteManager import sprites
from Sprite import Sprite
from Bullet import Bullet

class Player(Sprite):
    
    # instance variables
    left = False
    right = False
    up = False
    down = False
    speed = 5
    diameter = 30
    
    cR = 0
    cG = 150
    cB = 255
    
    c = color(random(0, 255), random(0, 255), random(0, 255))

    
    def display(self):
        fill(self.c)
        stroke(50)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
        #if self.cR < 255:
        #    self.cR += 5
        #elif self.cR == 255:
        #    self.cR = 0
        #    
        #if self.cG < 255:
        #    self.cG += 5
        #elif self.cG == 255:
        #    self.cG = 0
        #    
        #if self.cB < 255:
        #    self.cB += 5
        #elif self.cB == 255:
        #    self.cB = 0
    
    def move(self):
        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed
        if self.up:
            self.y -= self.speed
        if self.down:
            self.y += self.speed
        self.x = constrain(self.x, self.diameter / 2, width - self.diameter / 2)
        self.y = constrain(self.y, self.diameter / 2, height - self.diameter / 2)
        
        #if self.cR < 255:
        #    self.cR += 5
        #elif self.cR == 255:
        #    self.cR = 0
        #    
        #if self.cG < 255:
        #    self.cG += 5
        #elif self.cG == 255:
        #    self.cG = 0
        #    
        #if self.cB < 255:
        #    self.cB += 5
        #elif self.cB == 255:
        #    self.cB = 0
        
    def keyDown(self):
        if key == 'f' or key == 'F':
            sprites.append(Bullet(self.x, self.y, PVector(0, -10), self.team))
    
        if keyCode == LEFT:
            self.left = True
        if keyCode == RIGHT:
            self.right = True
        if keyCode == UP:
            self.up = True
        if keyCode == DOWN:
            self.down = True
            
    def keyUp(self):
        if keyCode == LEFT:
            self.left = False
        if keyCode == RIGHT:
            self.right = False
        if keyCode == UP:
            self.up = False
        if keyCode == DOWN:
            self.down = False
            
    def handleCollision(self):
        pass
            
    