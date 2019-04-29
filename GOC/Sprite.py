import SpriteManager

class Sprite:
    team = 2
    diameter = 50
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
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
        
    def isColliding(self, other):
        r1 = self.diameter / 2.0
        r2 = self.diameter / 2.0
        return r1 + r2 > dist(self.x, self.y, other.x, other.y)
    
    def handleCollision(self):
        #if(self.team != other.team):
        SpriteManager.destroy(self)