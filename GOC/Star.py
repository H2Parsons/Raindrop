from Sprite import Sprite

class Star(Sprite):
    mark = 0
    wait = 700
    step = 28
    maxSteps = 30
    NoTwinkle = 1
    YesTwinkle = 2
    Rogue = 20
    xSize = 1.5
    ySize = 2
    xStart = 1.5
    yStart = 2
    xGrowthSpeed = random(1, 3)
    yGrowthSpeed = random(1, 3)
    
    speed = 0.1
    c = color(255)
        
    def __init__(self, x, y, team, twinkle, effect, RogueColor):
        self.x = x
        self.y = y
        self.team = team
        self.twinkle = twinkle
        self.effect = effect
        self.RogueColor = RogueColor
        
    def animate(self):
        self.CheckEffect()
        
    def RogueDisplay(self):
        fill(self.RogueColor)
        stroke(self.RogueColor)
        self.RogueColor = color(random(0, 255), random(0, 255), random(0, 255))
        triangle(self.x, self.y - self.ySize, self.x - self.xSize, self.y, self.x, self.y + self.ySize)
        triangle(self.x, self.y - self.ySize, self.x + self.xSize, self.y, self.x, self.y + self.ySize)
        
    def CheckEffect(self):
        if self.effect == self.Rogue:
            self.DisplayRogueStar()
        else:
            self.display()
            self.move()
            
    def DisplayRogueStar(self):
        self.RogueDisplay()
        self.RogueMove()
        self.RogueSize()
        
    def RogueMove(self):
        self.y += 5
        if self.y < 0 or self.y > height:
            self.y = 0
            
    def RogueSize(self):
        self.xSize += self.xGrowthSpeed
        if millis() - self.mark > self.wait:
            self.xGrowthSpeed *= -1
            self.yGrowthSpeed *= -1
            self.mark = millis()
        self.ySize += self.yGrowthSpeed
    
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > height:
            self.y = 0
        
    def display(self):
        noStroke()
        if millis() - self.mark > self.wait:
            self.step = 1 if self.step > self.maxSteps else self.step + 1
            self.mark = millis()
            
        if self.twinkle == self.NoTwinkle:
            fill(self.c)
            triangle(self.x, self.y - 2, self.x - 1.5, self.y, self.x, self.y + 2)
            triangle(self.x, self.y - 2, self.x + 1.5, self.y, self.x, self.y + 2)
        elif self.twinkle == self.YesTwinkle:    
            if self.step <= 29:
                fill(self.c)
                triangle(self.x, self.y - 2, self.x - 1.5, self.y, self.x, self.y + 2)
                triangle(self.x, self.y - 2, self.x + 1.5, self.y, self.x, self.y + 2)
            elif self.step > 29:
                fill(255, 255, 0)
                triangle(self.x + 2, self.y - 4, self.x + 0.5, self.y - 2, self.x + 2, self.y + 0)
                triangle(self.x + 2, self.y - 4, self.x + 3.5, self.y - 2, self.x + 2, self.y + 0)
        strokeWeight(1)

    
        