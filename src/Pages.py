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
            self.current_width += (220 - self.current_width) * 0.2
            self.current_height += (90 - self.current_height) * 0.2
        else:
            color = "pink"
            self.current_width += (self.base_width - self.current_width) * 0.2
            self.current_height += (self.base_height - self.current_height) * 0.2
        py.draw.rect(self.sc, color, startRectangle, border_radius=12)
        text_surface = self.font.render("To Start Game Press 0", True, "black")
        text_rect = text_surface.get_rect(center=startRectangle.center)
        self.sc.blit(text_surface, text_rect)

class SecondPage:
    def __init__(self, screen):
        self.sc = screen
        self.sc.fill("white")
        #Second Page probably but I dont know what I should add here so like-><-
        leftRect = py.Rect(0,0,100, 500)
        rightRect = py.Rect(0,0,100,500)
        topRect = py.Rect(0,0,500,100)
        bottomRect = py.Rect(0,0, 500,100)
        leftRect.center = (self.sc.get_width() // 2 + 100, self.sc.get_height() // 2)
        rightRect.center = (self.sc.get_width() // 2 - 100, self.sc.get_height() // 2)
        topRect.center = (self.sc.get_width() // 2 , self.sc.get_height() // 2 - 100)
        bottomRect.center = (self.sc.get_width() // 2 , self.sc.get_height() // 2 + 100)
        py.draw.rect(self.sc, "black", leftRect, border_radius= 10)
        py.draw.rect(self.sc, "black", rightRect, border_radius= 10)
        py.draw.rect(self.sc, "black", bottomRect, border_radius= 10)
        py.draw.rect(self.sc, "black", topRect, border_radius= 10)
        


