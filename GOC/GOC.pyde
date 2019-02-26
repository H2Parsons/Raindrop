import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
import SpriteManager


def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    
    #sprites.append(player)
    #sprites.append(Enemy(50, 50, enemyTeam))
    #sprites.append(Enemy(150, 150, enemyTeam))
    #sprites.append(Raindrop(25, random(0, 50), enemyTeam)) #1
    #sprites.append(Raindrop(75, random(0, 50), enemyTeam)) #2
    #sprites.append(Raindrop(125, random(0, 50), enemyTeam)) #3
    #sprites.append(Raindrop(175, random(0, 50), enemyTeam)) #4
    #sprites.append(Raindrop(225, random(0, 50), enemyTeam)) #5
    #sprites.append(Raindrop(275, random(0, 50), enemyTeam)) #6
    #sprites.append(Raindrop(325, random(0, 50), enemyTeam)) #7
    #sprites.append(Raindrop(375, random(0, 50), enemyTeam)) #8
    #sprites.append(Raindrop(425, random(0, 50), enemyTeam)) #9
    #sprites.append(Raindrop(475, random(0, 50), enemyTeam)) #10
    #sprites.append(JiggleBot(random(0, width), random(0, height), enemyTeam))
    #sprites.append(ScreenSaverBot(random(0, width), random(0, height), enemyTeam))
    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(random(0, width), random(0, height), 2))
    
def draw():
    global player, sprites
    background(255)    

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
