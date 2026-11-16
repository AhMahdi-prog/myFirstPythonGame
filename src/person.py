import pygame as py

class personAtStart: 
    def __init__(self, screen):
        self.sc = screen
        self.playerPos = py.Vector2(self.sc.get_width() / 2, self.sc.get_height() / 2  + 200)
        
    def moveCircle(self, screen):
        self.sc = screen
        circle = py.draw.circle(self.sc, "red", self.playerPos, 40)
    def getPOV(self):
        return self.playerPos
        