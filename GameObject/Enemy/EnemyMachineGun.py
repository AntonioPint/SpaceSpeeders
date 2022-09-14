from GameObject.Enemy.Enemy import Enemy
import pygame

class EnemyMachineGun(Enemy):

    Image = pygame.image.load("assets/AmmoAsteroid.png")
    
    def __init__(self, position, acceleration=1):
        super().__init__(
            position,
            acceleration
        )
        