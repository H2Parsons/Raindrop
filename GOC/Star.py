from Sprite import Sprite

class Star(Sprite):
    mark = 0
    wait = 700
    step = 58
    maxSteps = 60
    NoTwinkle = 1
    YesTwinkle = 2
    
    speed = 0.1
    diameter = 4
    c = color(255)
        
    def __init__(self, x, y, team, twinkle):
        self.x = x
        self.y = y
        self.team = team
        self.twinkle = twinkle
        
        
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > height:
            self.y = 0
            
    #def handleCollision(self):
        #pass
        
    #def display(self):
        #self.x = 150
        #self.y = 150
        #fill(250)
        #noStroke()
        #triangle(x, y - 10, x - 10, y, x, y + 10)
        #triangle(x, y - 10, x + 10, y, x, y + 10)    
        #strokeWeight(1)
        
    def display(self):
        noStroke()
        if millis() - self.mark > self.wait:
            self.step = 1 if self.step > self.maxSteps else self.step + 1
            #step = step < numSteps ? step + 1 : 1
            self.mark = millis()
            
        if self.twinkle == self.NoTwinkle:
            fill(self.c)
            triangle(self.x, self.y - 2, self.x - 1.5, self.y, self.x, self.y + 2)
            triangle(self.x, self.y - 2, self.x + 1.5, self.y, self.x, self.y + 2)
        elif self.twinkle == self.YesTwinkle:    
            if self.step <= 59:
                fill(self.c)
                triangle(self.x, self.y - 2, self.x - 1.5, self.y, self.x, self.y + 2)
                triangle(self.x, self.y - 2, self.x + 1.5, self.y, self.x, self.y + 2)
            elif self.step > 59:
                #fill(self.c)
                #triangle(self.x, self.y - 2, self.x - 1.5, self.y, self.x, self.y + 2)
                #triangle(self.x, self.y - 2, self.x + 1.5, self.y, self.x, self.y + 2)
                fill(255, 255, 0)
                triangle(self.x + 2, self.y - 4, self.x + 0.5, self.y - 2, self.x + 2, self.y + 0)
                triangle(self.x + 2, self.y - 4, self.x + 3.5, self.y - 2, self.x + 2, self.y + 0)
                #triangle(self.x + 1, self.y - 3, self.x - 0.5, self.y - 1, self.x + 1, self.y + 1)
                #triangle(self.x + 1, self.y - 3, self.x + 2.5, self.y - 1, self.x + 1, self.y + 1)    
        strokeWeight(1)

    
        