import pygame
import math
from GameObject import GameObject
from OptionsReader import OptionsReader


class Character(GameObject):
    # Constants
    ACELX = float(OptionsReader().getValue("CharacterAcelerationX"))
    ACELY = float(OptionsReader().getValue("CharacterAcelerationY"))

    image = pygame.image.load("assets\spaceship.png")

    def __init__(self, position):
        super().__init__(
            int(OptionsReader().getValue("CharacterSizeX")),
            int(OptionsReader().getValue("CharacterSizeY")),
            position
        )

    def getCharacterImage(self):
        return pygame.transform.scale(self.image, (self.width, self.height))

    def moveUp(self, args):
        def Up():
            self.position = self.position - pygame.Vector2(0, self.ACELY)
        self.move(Up)

    def moveDown(self, args):
        def Down():
            self.position = self.position + pygame.Vector2(0, self.ACELY)
        self.move(Down)

    def moveLeft(self, args):
        def Left():
            self.position = self.position - pygame.Vector2(self.ACELX, 0)
        self.move(Left)
        #self.image = pygame.image.load("assets\spaceshipLeft.png")

    def moveRight(self, args):
        def Right():
            self.position = self.position + pygame.Vector2(self.ACELX, 0)
        self.move(Right)
        #self.image = pygame.image.load("assets\spaceshipRight.png")

    def reset(self, args):
        pass
        #self.image = pygame.image.load("assets\spaceship.png")

    def fire(self, args):
        print("fire")

    def getCharacterPointingToPosition(self, targetPosition):
        (x, y) = self.getPosition()
        (targetX, targetY) = targetPosition

        angle = 360-math.atan2(targetY-y,targetX-x)*180/math.pi -90
        result = pygame.transform.rotate(self.getCharacterImage(), angle)
        self.center = result.get_rect(center=self.position)

        return result