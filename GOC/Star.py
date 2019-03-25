from Sprite import Sprite

class Star(Sprite):
    mark = 0
    wait = 700
    step = 1
    
    speed = 0.1
    diameter = 4
    c = color(255)
        
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > height:
            self.y = 0
            
    def handleCollision(self):
        pass
        
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
            #numSteps = 60
            #step = self.step < self.numSteps ? self.step + 1 : 1
            self.mark = millis()
            
        #if step < 40:
        fill(255)
        triangle(self.x, self.y - 2, self.x - 1.5, self.y, self.x, self.y + 2)
        triangle(self.x, self.y - 2, self.x + 1.5, self.y, self.x, self.y + 2)
        #else if step > 40:
         #   fill(self.c)
          #  triangle(self.x, self.y - 2, self.x - 1.5, self.y, self.x, self.y + 2)
           # triangle(self.x, self.y - 2, self.x + 1.5, self.y, self.x, self.y + 2)
            
        strokeWeight(1)

    
        