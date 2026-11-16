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

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Code for game YAYAYAYAYYA!!!!!
    move = UniversalPovMove.UniKeybinds()
    
  
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000