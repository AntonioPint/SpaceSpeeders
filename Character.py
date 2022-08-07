from pygame import transform
from pygame import image
from pygame import Vector2
from GameObject import GameObject
from OptionsReader import OptionsReader

class Character(GameObject):
    # Constants
    ACELX = float(OptionsReader().getValue("CharacterAcelerationX"))
    ACELY = float(OptionsReader().getValue("CharacterAcelerationY"))

    def __init__(self, positionX, positionY):
        super().__init__(
            int(OptionsReader().getValue("CharacterSizeX")),
            int(OptionsReader().getValue("CharacterSizeY")),
            Vector2(positionX, positionY))

    def getCharacterImage(self):
        return transform.scale(image.load("assets\spaceship.png"), (self.width, self.height))

    def moveUp(self):
        def Up():
            self.position = self.position - Vector2(0, self.ACELY)
        self.move(Up)

    def moveDown(self):
        def Down():
            self.position = self.position + Vector2(0, self.ACELY)
        self.move(Down)

    def moveLeft(self):
        def Left():
            self.position = self.position - Vector2(self.ACELX, 0)
        self.move(Left)

    def moveRight(self):
        def Right():
            self.position = self.position + Vector2(self.ACELX, 0)
        self.move(Right)

    def fire(self):
        pass