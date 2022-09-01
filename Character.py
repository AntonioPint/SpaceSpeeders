from GameObject import GameObject, GameObjectTypes
from Shot import Shot
import pygame

class Character(GameObject):
    
    image = pygame.image.load("assets/spaceship.png")
    characterImage = None
    Shots = []
    CharacterWidth = 80
    CharacterHeight = 80

    def __init__(self, position):
        super().__init__(
            self.CharacterWidth,
            self.CharacterHeight,
            position
        )
        self.characterImage = pygame.transform.scale(self.image, (self.width, self.height))
        self.objectType = GameObjectTypes.CHARACTER
        self.ACEL = 5

    def getImage(self):
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
        shot = Shot(pygame.Vector2(self.getPosition()))
        shot.objectType = GameObjectTypes.SHOT
        shot.ACEL = 15
        shot.movement = (pygame.Vector2(self.getChrosshairPosition())) - pygame.Vector2(self.getPosition())
        self.Shots.append(shot)

    def setChrosshairPosition(self, pos):
        self.chrosshairPosition = pos

    def getChrosshairPosition(self):
        return self.chrosshairPosition
