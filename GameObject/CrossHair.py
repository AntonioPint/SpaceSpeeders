import pygame

from GameObject.GameObject import GameObject

class CrossHair(GameObject):
    CrossHairWidth = 75
    CrossHairHeight = 75

    def __init__(self, position = (0,0)):
        super().__init__(
            self.CrossHairWidth,
            self.CrossHairHeight,
            position,
            0,
            pygame.image.load("assets/crosshair.png")
        )

    def moveChrossHair(self, mousePos):
        (x,y) = mousePos
        self.position = (x - self.width / 2, y - self.height / 2)
        return self.position
        