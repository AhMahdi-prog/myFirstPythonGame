import pygame as py

class personAtStart: 
    def __init__(self, sc):
        self.playerPos = py.Vector2(sc.get_width() / 2, sc.get_height() / 2  + 200)
        
    def moveCircle(self, screen):
        circle = py.draw.circle(screen, "red", self.player_pos, 40)
        