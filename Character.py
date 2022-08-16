import pygame
import math
from GameObject import GameObject
from OptionsReader import OptionsReader


class Character(GameObject):
    # Constants
    ACELX = 6
    ACELY = 4

    image = pygame.image.load("assets\spaceship.png")
    characterImage = None

    def __init__(self, position):
        super().__init__(
            int(OptionsReader().getValue("CharacterSizeX")),
            int(OptionsReader().getValue("CharacterSizeY")),
            position
        )
        self.characterImage = pygame.transform.scale(self.image, (self.width, self.height))

    def getCharacterImage(self):
        return self.characterImage

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

    def getCenterRotate(self):
        return self.getPosition() + pygame.Vector2(30,30)

    def getCharacterPointingToPosition(self, targetPosition):
        (x, y) = self.getPosition()
        (targetX, targetY) = targetPosition

        angle = 270-math.atan2(targetY-y,targetX-x)*180/math.pi 
        result = pygame.transform.rotate(self.getCharacterImage(), angle)
        self.center = result.get_rect(center=self.getPosition())
        #FIXME:
        return result