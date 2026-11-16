#Outside imports 
import pygame 
import random as r

#Imports from other files
from keybinds import UniversalPovMove
from enemy import enemyAtStart
from startingPage import startingPage
from styleStuff import style
from person import personAtStart

# pygame setup
pygame.init()
sw, sh = 1280, 720
screen = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()
running = True
dt = 0

#Init stuff
styling = style.__init__()
you = personAtStart.__init__(screen)
enemyBigBlue = enemyAtStart.__init__(screen)
starting_page = startingPage.__init__(screen, styling.getFont())


while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Code for game YAYAYAYAYYA!!!!!
    startingPage.updatePage()
    move = UniversalPovMove.UniKeybinds()
    you = personAtStart.moveCircle()
    enemyBigBlue = enemyAtStart.moveThisEnemy()
  
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000