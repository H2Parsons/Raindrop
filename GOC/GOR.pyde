import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
import SpriteManager
from ArmoredShooter import ArmoredShooter
from Star import Star
from random import randint

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    passiveTeam = 00
    NoTwinkle = 1
    YesTwinkle = 2
    TwinkleNo = 0
    player = Player(width / 2, height * 2/3, playerTeam)
    RogueColor = color(255)

    for i in range(0, height, 2):
        stroke(0)
        if TwinkleNo != 5:
            SpriteManager.spawn(Star(random(0, width), random(0, height), passiveTeam, NoTwinkle, 0, RogueColor))
            TwinkleNo += 1
        elif TwinkleNo == 5:
            SpriteManager.spawn(Star(random(0, width), random(0, height), passiveTeam, YesTwinkle, randint(1, 20), RogueColor))
            TwinkleNo = 0
            
    #SpriteManager.spawn(Star(250, 250, passiveTeam, YesTwinkle, 20, RogueColor))
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Enemy(20, 250, enemyTeam))
    SpriteManager.spawn(Enemy(150, 150, enemyTeam))
    
    #SpriteManager.spawn(Star(random(0, width), random(0, height), enemyTeam))
    #SpriteManager.spawn(Raindrop(25, random(0, 50), enemyTeam)) #1
    #SpriteManager.spawn(Raindrop(75, random(0, 50), enemyTeam)) #2
    #SpriteManager.spawn(Raindrop(125, random(0, 50), enemyTeam)) #3
    #SpriteManager.spawn(Raindrop(175, random(0, 50), enemyTeam)) #4
    #SpriteManager.spawn(Raindrop(225, random(0, 50), enemyTeam)) #5
    #SpriteManager.spawn(Raindrop(275, random(0, 50), enemyTeam)) #6
    #SpriteManager.spawn(Raindrop(325, random(0, 50), enemyTeam)) #7
    #SpriteManager.spawn(Raindrop(375, random(0, 50), enemyTeam)) #8
    #SpriteManager.spawn(Raindrop(425, random(0, 50), enemyTeam)) #9
    #SpriteManager.spawn(Raindrop(475, random(0, 50), enemyTeam)) #10
    #SpriteManager.spawn(JiggleBot(random(0, width), random(0, height), enemyTeam))
    #SpriteManager.spawn(ScreenSaverBot(random(0, width), random(0, height), enemyTeam))
    #SpriteManager.spawn(JiggleBot(random(0, width), random(0, height), 2))

    SpriteManager.spawn(ArmoredShooter(random(0, width), 50, enemyTeam))


def draw():
    background(0)
    #background(random(0, 255), random(0, 255), random(0, 255))
    SpriteManager.manage()
    RogueColor = color(random(0, 255), random(0, 255), random(0, 255))
    
def keyPressed():
    SpriteManager.player.keyDown()

def keyReleased():
    SpriteManager.player.keyUp()