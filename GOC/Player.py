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
    #diameter = 30
    xLength = 30
    yLength = 30
    
    c = color(random(0, 255), random(0, 255), random(0, 255))

    
    def display(self):
        fill(self.c)
        stroke(50)
        rect(self.x, self.y, self.xLength, self.yLength)
    
    def move(self):
        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed
        if self.up:
            self.y -= self.speed
        if self.down:
            self.y += self.speed
        self.x = constrain(self.x, 0, width - self.xLength)
        self.y = constrain(self.y, 0, height - self.yLength)
        
    def keyDown(self):
        if key == 'f' or key == 'F':
            sprites.append(Bullet(self.x + self.xLength / 2 - 5, self.y - 5, PVector(0, -10), self.team))
    
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