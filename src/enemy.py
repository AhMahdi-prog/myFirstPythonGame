import pygame as py
import random as r


#Later on mayber we can incorporate an ML model but 
#like that is work for later

class enemyAtStart:
    
    def __init__(self, screen):
        self.sc = screen
        self.enemy_pos = py.Vector2(r.random()*1281, r.random()*721) 
        self.enemy_speed = 200  # Pixels per second I think
    def moveThisEnemy(self, dt, player_pos):
        direction = player_pos - self.enemy_pos
        if direction.length() > 0:
            self.enemy_pos += direction.normalize() * self.enemy_speed * dt
        self.rectAntag = py.draw.rect(self.sc, "blue", (self.enemy_pos.x, self.enemy_pos.y, 20, 20))