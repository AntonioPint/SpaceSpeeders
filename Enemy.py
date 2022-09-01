from GameObject import GameObject
import pygame

class Enemy(GameObject):

    EnemyWidth = 75
    EnemyHeight = 75
    EnemyImage = pygame.image.load("assets/asteroid.png")

    def __init__(self, position):
        super().__init__(self.EnemyWidth, self.EnemyHeight, position)

    def getImage(self):
        return pygame.transform.scale(self.EnemyImage, (self.EnemyWidth, self.EnemyHeight))
