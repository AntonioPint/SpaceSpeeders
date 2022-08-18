import pygame

from GameObject import GameObject, GameObjectTypes
from OptionsReader import OptionsReader


class Character(GameObject):
    
    image = pygame.image.load("assets/spaceship.png")
    characterImage = None

    def __init__(self, position):
        super().__init__(
            int(OptionsReader().getValue("CharacterSizeX")),
            int(OptionsReader().getValue("CharacterSizeY")),
            position
        )
        self.characterImage = pygame.transform.scale(self.image, (self.width, self.height))
        self.objectType = GameObjectTypes.CHARACTER
        self.ACEL = 5

    def getCharacterImage(self):
        return self.characterImage

    def moveUp(self):
        self.movement += pygame.Vector2(0, -1)

    def moveDown(self):
        self.movement += pygame.Vector2(0, 1)

    def moveLeft(self):
        self.movement += pygame.Vector2(-1, 0)

    def moveRight(self):
        self.movement += pygame.Vector2(1, 0)

    def fire(self):
        print("fire")
