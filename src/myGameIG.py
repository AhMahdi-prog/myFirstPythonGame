#Outside imports 
import pygame 
import random as r

#Imports from other files
from keybinds import UniversalPovMove
from enemy import enemyAtStart
from Pages import startingPage
from styleStuff import style
from person import personAtStart
from Pages import SecondPage

# pygame setup
pygame.init()
sw, sh = 1280, 720
screen = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()
running = True
dt = 0

#Init stuff
styling = style()
you = personAtStart(screen)
enemyBigBlue = enemyAtStart(screen)
page = startingPage(screen, styling.getFont())
move = UniversalPovMove()

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Code for game YAYAYAYAYYA!!!!!
    if (move.checkFirstPage()):
        page = SecondPage(screen)
    else:
        page.updatePage()
        you.moveCircle(screen)
        move.UniKeybinds(you.getPOV(), dt)
        enemyBigBlue.moveThisEnemy(dt, you.getPOV())
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000