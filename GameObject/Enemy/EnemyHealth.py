from GameObject.Enemy.Enemy import Enemy
import pygame

class EnemyHealth(Enemy):

    Image = pygame.image.load("assets/HealthAsteroid.png")
    
    def __init__(self, position, acceleration=1):
        super().__init__(
            position,
            acceleration
        )
