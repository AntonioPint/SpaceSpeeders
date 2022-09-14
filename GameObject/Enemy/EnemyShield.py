from GameObject.Enemy.Enemy import Enemy
import pygame

class EnemyShield(Enemy):

    Image = pygame.image.load("assets/ShieldAsteroid.png")
    
    def __init__(self, position, acceleration=1):
        super().__init__(
            position,
            acceleration
        )
        