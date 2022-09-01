from GameObject import GameObject
import pygame

class Shot(GameObject):

    ShotWidth = 10
    ShotHeight = 10
    ShotImage = pygame.image.load("assets/shot.png")

    def __init__(self, position):
        super().__init__(self.ShotWidth, self.ShotHeight, position)

    def getImage(self):
        return pygame.transform.scale(self.ShotImage, (self.ShotWidth, self.ShotHeight))
