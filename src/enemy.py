import pygame as py
import random as r


#Later on mayber we can incorporate an ML model but 
#like that is work for later

class enemyAtStart:
    enemy_pos = py.Vector2(r.random()*1281, r.random()*721) 
    enemy_speed = 200  # Pixels per second I think
    def __init__(self, screen):
        self.sc = screen
    def moveThisEnemy(self, dt, player_pos):
        enemy_speed = 200  # Pixels per second I think
        direction = player_pos - enemy_pos
        if direction.length() > 0:
            enemy_pos += direction.normalize() * enemy_speed * dt
        self.rectAntag = py.draw.rect(self.sc, "blue", (enemy_pos.x, enemy_pos.y, 20, 20))