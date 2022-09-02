from GameObject import GameObject
from Shot import Shot
import pygame


class Character(GameObject):

    image = pygame.image.load("assets/spaceship.png")
    characterImage = None
    Shots = []
    CharacterWidth = 80
    CharacterHeight = 80
    chrosshairPosition = (0,0)
    def __init__(self, position):
        super().__init__(
            self.CharacterWidth,
            self.CharacterHeight,
            position
        )
        self.characterImage = pygame.transform.scale(
            self.image, (self.width, self.height))
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

    def move(self):
        if self.movement == pygame.Vector2(0, 0):
            return

        VectorMovement = self.movement.normalize() * self.ACEL

        VectorMovementX = (VectorMovement[0], 0)
        VectorMovementY = (0, VectorMovement[1])

        self.position += pygame.Vector2(VectorMovementX)
        if self.isOutOfBounds():
            self.position -= VectorMovementX

        self.position += pygame.Vector2(VectorMovementY)
        if self.isOutOfBounds():
            self.position -= VectorMovementY
        
        # Stop  movement
        self.movement = pygame.Vector2(0, 0)

    def fire(self, pos):
        shot = Shot(pygame.Vector2(self.getPosition()))
        shot.ACEL = 15
        shot.movement = pos - pygame.Vector2(self.getPosition())
        self.Shots.append(shot)
