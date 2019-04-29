import SpriteManager

class Sprite:
    team = 2
    xLength = 50
    yLength = 25
    c = color(255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move():
        pass
        
    def display(self):
        fill(self.c)
        stroke(50)
        rect(self.x, self.y, self.xLength, self.yLength)
        
    def animate(self):
        self.move()
        self.display()
        
    ### 2C ###
    def isColliding(self, other):
        if ((self.x < other.x + other.xLength) 
        and (self.x + self.xLength > other.x)
        and (self.y < other.y + other.yLength)
        and (self.y + self.yLength > other.y)):
            return True
        else:
            return False
        
    def handleCollision(self):
        SpriteManager.destroy(self)