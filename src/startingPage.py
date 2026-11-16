import pygame as py

class startingPage:
    def __init__(self, sc, font):
        sc.fill("white")
        base_width, base_height = 200, 80
        current_width, current_height = base_width, base_height
        
        mouse_pos = py.mouse.get_pos()
        startRectangle = py.Rect(0, 0, 500, 200)
        startRectangle.center = (sc.get_width() // 2, sc.get_height() // 2)
        py.draw.rect(sc, "pink", startRectangle)
    
        if startRectangle.collidepoint(mouse_pos):
            color = "hotpink"
            # Smoothly approach target size (220x90)
            current_width += (220 - current_width) * 0.2
            current_height += (90 - current_height) * 0.2
        else:
            color = "pink"
            # Smoothly return to base size
            current_width += (base_width - current_width) * 0.2
            current_height += (base_height - current_height) * 0.2
        py.draw.rect(sc, color, startRectangle, border_radius=12)
        text_surface = font.render("Start Game", True, "black")
        text_rect = text_surface.get_rect(center=startRectangle.center)
        sc.blit(text_surface, text_rect)



