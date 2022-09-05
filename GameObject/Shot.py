from GameObject.GameObject import GameObject
import pygame

class Shot(GameObject):

    ShotWidth = 10
    ShotHeight = 10

    def __init__(self, position):
        super().__init__(self.ShotWidth, self.ShotHeight, position, 15, pygame.image.load("assets/shot.png"))

