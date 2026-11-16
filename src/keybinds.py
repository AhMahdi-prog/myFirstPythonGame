import pygame as py

class UniversalPovMove:
    def __init__(self):
        self.keys = py.key.get_pressed()
    
    def UniKeybinds(self, player_pos, dtime):
        
        self.keys = py.key.get_pressed()
        if self.keys[py.K_w] or self.keys[py.K_UP]:
            player_pos.y -= 300 * dtime
        if self.keys[py.K_s] or self.keys[py.K_DOWN]:
            player_pos.y += 300 * dtime
        if self.keys[py.K_a] or self.keys[py.K_LEFT]:
            player_pos.x -= 300 * dtime
        if self.keys[py.K_d] or self.keys[py.K_RIGHT]:
            player_pos.x += 300 * dtime
        
    def checkFirstPage(self):
        questioning1Rn = False
        if self.keys[py.K_0]:
            questioning1Rn = True
            return questioning1Rn
        else:
            return questioning1Rn