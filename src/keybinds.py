import pygame as py

class UniversalPovMove:
    
    def UniKeybinds(self, player_pos, dtime):
        
        keys = py.key.get_pressed()
        if keys[py.K_w] or keys[py.K_UP]:
            player_pos.y -= 300 * dtime
        if keys[py.K_s] or keys[py.K_DOWN]:
            player_pos.y += 300 * dtime
        if keys[py.K_a] or keys[py.K_LEFT]:
            player_pos.x -= 300 * dtime
        if keys[py.K_d] or keys[py.K_RIGHT]:
            player_pos.x += 300 * dtime
            