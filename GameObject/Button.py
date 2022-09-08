import pygame

class Button(object):
 
    mfontColor = None
    def __init__(self, text, pos, fontSize=30, fontColor="white",backgr="black", callBack=None):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", fontSize)
        self.mfontColor = fontColor
        self.callBack = callBack
        self.change_text(text, backgr)
        
 
    def change_text(self, text, backgr="black"):
        self.text = self.font.render(text, 1, pygame.Color(self.mfontColor))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(backgr)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
    
    def setBackgroundColor(self, color):
        self.backGroundColor = color

    def setText(self, text):
        self.text = text

    def isCollidingPoint(self, pos):
        (x,y) = pos
        return self.rect.collidepoint(x, y)
    
    # def click(self, event):
    #     x, y = pygame.mouse.get_pos()
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         if pygame.mouse.get_pressed()[0]:
    #             if self.rect.collidepoint(x, y):
    #                 self.change_text(self.feedback, backgr="red")
    
