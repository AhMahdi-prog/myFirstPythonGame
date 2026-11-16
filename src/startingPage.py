import pygame as py

class startingPage:
    def __init__(self, sc, font):
        self.sc = sc
        self.font = font
        self.sc.fill("white")
        self.base_width, self.base_height = 200, 80
        self.current_width, self.current_height = self.base_width, self.base_height
    
    def updatePage(self):    
        mouse_pos = py.mouse.get_pos()
        startRectangle = py.Rect(0, 0, 500, 200)
        startRectangle.center = (self.sc.get_width() // 2, self.sc.get_height() // 2)
        py.draw.rect(self.sc, "pink", startRectangle)
    
        if startRectangle.collidepoint(mouse_pos):
            color = "hotpink"
            # Smoothly approach target size (220x90)
            current_width += (220 - current_width) * 0.2
            current_height += (90 - current_height) * 0.2
        else:
            color = "pink"
            # Smoothly return to base size
            current_width += (self.base_width - current_width) * 0.2
            current_height += (self.base_height - current_height) * 0.2
        py.draw.rect(self.sc, color, startRectangle, border_radius=12)
        text_surface = self.font.render("Start Game", True, "black")
        text_rect = text_surface.get_rect(center=startRectangle.center)
        self.sc.blit(text_surface, text_rect)



